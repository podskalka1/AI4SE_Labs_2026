import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from openai.types.chat import ChatCompletion

from requirements_refiner.compact import Catalog, CompactLLM, RefinementPlan, co_locate_duplicates
from requirements_refiner.config import Settings
from requirements_refiner.models import RefinementResult, ReviewResult, WritingResult
from requirements_refiner.llm import LLMError
from requirements_refiner.nodes.refiner import requirements_refiner
from requirements_refiner.nodes.reviewer import validate_review
from requirements_refiner.run_support import (
    BudgetExceeded, MeteredRequests, decode_state, encode_state,
)
from test_refiner_writer import state, merged, refine


def completion(content):
    return ChatCompletion.model_validate({"id": "test", "object": "chat.completion", "created": 0,
        "model": "gpt-5.6-luna", "choices": [{"index": 0, "finish_reason": "stop",
            "message": {"role": "assistant", "content": json.dumps(content)}}],
        "usage": {"prompt_tokens": 100, "completion_tokens": 50, "total_tokens": 150}})


def test_meter_reserves_before_sending_and_replays_without_cost(tmp_path):
    client = Mock()
    client.chat.completions.create.return_value = completion({"ok": True})
    meter = MeteredRequests(client, tmp_path)
    kwargs = {"model": "gpt-5.6-luna", "messages": [{"role": "user", "content": "test"}], "max_completion_tokens": 100}
    first = meter(**kwargs)
    estimate = meter.charged_estimate
    assert meter(**{**kwargs, "max_completion_tokens": 200}) == first
    assert meter.charged_estimate == estimate
    assert meter.cache_hits == 1
    client.chat.completions.create.assert_called_once()
    restored = MeteredRequests(client, tmp_path)
    assert restored.charged_estimate == estimate


def test_budget_refuses_request_before_api(tmp_path):
    client = Mock()
    meter = MeteredRequests(client, tmp_path, ceiling_eur=0.000001)
    with pytest.raises(BudgetExceeded):
        meter(model="gpt-5-mini", messages=[], max_completion_tokens=24000)
    client.chat.completions.create.assert_not_called()


def test_uncertain_failure_keeps_reservation(tmp_path):
    client = Mock()
    client.chat.completions.create.side_effect = RuntimeError("connection failed")
    meter = MeteredRequests(client, tmp_path)
    with pytest.raises(RuntimeError):
        meter(model="gpt-5-mini", messages=[], max_completion_tokens=24000)
    assert meter.charged_estimate > 0
    assert json.loads((tmp_path / "usage.json").read_text())[0]["error_type"] == "RuntimeError"


def test_completed_retry_replaces_only_partial_replay_cache(tmp_path):
    client = Mock()
    partial = completion({"ok": False})
    partial.choices[0].finish_reason = "length"
    success = completion({"ok": True})
    client.chat.completions.create.side_effect = [partial, success]
    meter = MeteredRequests(client, tmp_path)
    args = {"model": "gpt-5.6-luna", "messages": [], "max_completion_tokens": 100}
    assert meter(**args).choices[0].finish_reason == "length"
    assert meter(**{**args, "max_completion_tokens": 200}) == success
    assert meter(**args) == success
    assert client.chat.completions.create.call_count == 2
    assert len(list((tmp_path / "attempts").glob("*.json"))) >= 2


def test_complete_state_roundtrip_including_scalar_counters_and_review(state):
    refined, _ = refine(state, merged(state))
    value = {**state, **refined, "revision_count": 2, "max_revisions": 3,
             "latest_review": ReviewResult(status="accepted", issues=[]),
             "review_history": [ReviewResult(status="accepted", issues=[])], "final_document": "text"}
    assert decode_state(json.loads(json.dumps(encode_state(value)))) == value


def test_compact_refiner_restores_complete_evidence_and_ledger(state):
    payload = {"candidates": [c.model_dump(mode="json") for c in state["candidates"]],
               "previous_requirements": [], "glossary": []}
    catalog = Catalog(payload)
    ids = [catalog.forward[c.candidate_id] for c in state["candidates"]]
    client = Mock()
    client.chat.completions.create.return_value = completion({"requirements": [{"key": "new-login",
        "candidate_ids": ids, "name": "Login", "description": "The system shall support staff login.",
        "kind": "functional", "priority": "P2", "priority_rationale": "Daily operation", "priority_inferred": True}],
        "rejected": [], "glossary": [], "conflicts": []})
    llm = CompactLLM(Settings(), client=client)
    result = llm.generate(model="gpt-5.6-luna", system_prompt="test", user_prompt=json.dumps(payload),
                          output_type=RefinementResult)
    assert len(result.dispositions) == 2
    assert {r.document_id for r in result.requirements[0].references} == {"D1", "D2"}
    assert {d.status for d in result.dispositions} == {"retained", "merged"}


def test_compact_writer_batches_without_provenance_echo(state):
    refined, _ = refine(state, merged(state))
    req = refined["requirements"][0]
    requirements = [req.model_copy(update={"internal_key": f"R{i}"}) for i in range(3)]
    payload = {"requirements": [r.model_dump(mode="json") for r in requirements], "glossary": []}
    client = Mock()
    def create(**kwargs):
        prompt = json.loads(kwargs["messages"][1]["content"].split("\nJSON schema:")[0])
        assert "references" not in prompt["requirements"][0]
        return completion({"requirements": [{"internal_key": r["internal_key"], "name": "Login",
                           "description": "The system shall support login."} for r in prompt["requirements"]]})
    client.chat.completions.create.side_effect = create
    llm = CompactLLM(Settings(), client=client)
    llm.writer_batch_size = 2
    result = llm.generate(model="gpt-5.4-nano", system_prompt="test", user_prompt=json.dumps(payload), output_type=WritingResult)
    assert [r.internal_key for r in result.requirements] == ["R0", "R1", "R2"]
    assert client.chat.completions.create.call_count == 2


def test_compact_refinement_does_not_bypass_candidate_coverage(state):
    client = Mock()
    client.chat.completions.create.return_value = completion({"requirements": [], "rejected": [], "glossary": [], "conflicts": []})
    settings = Settings(extraction_attempts=1)
    llm = CompactLLM(settings, client=client)
    with pytest.raises(LLMError, match="cross-record"):
        requirements_refiner(state, settings=settings, llm=llm)


def test_compact_review_grounds_new_evidence_without_transcription(state):
    refined, _ = refine(state, merged(state))
    original = {**state, **refined}
    payload = {field: [record.model_dump(mode="json") for record in records]
               for field, records in original.items()}
    catalog = Catalog(payload)
    client = Mock()
    client.chat.completions.create.return_value = completion({"status": "needs_revision", "issues": [{
        "category": "OS8", "affected_keys": [catalog.forward[refined["requirements"][0].internal_key]],
        "affected_candidate_ids": [], "actionable": True, "explanation": "Password requirement missing",
        "requested_correction": "Retain it", "evidence_ids": [], "source_selections": [{
            "document_id": catalog.forward["D1"], "start_line": 2, "end_line": 2}]}],
        "missing_candidates": [{"candidate_id": "new-password", "statement": "Require passwords.",
            "kind": "functional", "references": [{"document_id": catalog.forward["D1"], "start_line": 2, "end_line": 2}],
            "extraction_note": None}]})
    llm = CompactLLM(Settings(), client=client)
    result = llm.generate(model="gpt-6-luna", system_prompt="test", user_prompt=json.dumps(payload),
                          output_type=ReviewResult, validate=lambda result: validate_review(result, original))
    assert result.issues[0].references[0].excerpt == "Require passwords."
    assert result.missing_candidates[0].references[0].document_id == "D1"


def test_full_run_cli_dispatch_preserves_configuration(tmp_path, monkeypatch):
    from requirements_refiner import cli
    from requirements_refiner import full_run
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    output = tmp_path / "requirements.md"
    directory = tmp_path / "run"
    monkeypatch.setattr(cli, "load_settings", lambda path: Settings(api_key="fake"))
    execute = Mock(return_value=0)
    monkeypatch.setattr(full_run, "run", execute)
    assert cli.main([str(corpus), "--output", str(output), "--run-directory", str(directory), "--max-revisions", "1"]) == 0
    assert execute.call_args.args[0].max_revisions == 1
    assert execute.call_args.args[1:] == (corpus, output, directory, False)


def test_recovery_directory_cannot_pollute_corpus(tmp_path):
    from requirements_refiner.full_run import run
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    with pytest.raises(ValueError, match="outside the source corpus"):
        run(Settings(api_key="fake"), corpus, tmp_path / "req.md", corpus / "run")


def test_partition_rejects_unbounded_omnibus_batch():
    with pytest.raises(ValueError):
        RefinementPlan.model_validate({"batches": [{"topic": "Everything", "candidate_ids": [f"c{i:04d}" for i in range(1, 540)]}]})


def test_batched_refinement_preserves_all_candidates_and_namespaces_keys(state):
    original = state["candidates"][0]
    candidates = [original.model_copy(update={"candidate_id": f"C{i}"}) for i in range(37)]
    payload = {"candidates": [c.model_dump(mode="json") for c in candidates],
               "previous_requirements": [], "glossary": [],
               "review": {"issues": [], "missing_candidates": [candidates[-1].model_dump(mode="json")]}}
    client = Mock()
    def create(**kwargs):
        title = kwargs["response_format"]["json_schema"]["schema"]["title"]
        data = json.loads(kwargs["messages"][1]["content"].split("\nJSON schema:")[0])
        if title == "RefinementPlan":
            return completion({"batches": [{"topic": "First", "candidate_ids": [f"c{i:04d}" for i in range(1, 21)]},
                                            {"topic": "Second", "candidate_ids": [f"c{i:04d}" for i in range(21, 38)]}]})
        assert data["review"]["missing_candidates"] == []
        return completion({"requirements": [{"key": f"new-{i}", "candidate_ids": [c["candidate_id"]],
            "name": "Login", "description": "The system shall support login.", "kind": "functional",
            "priority": "P2", "priority_rationale": "Daily use", "priority_inferred": True}
            for i, c in enumerate(data["candidates"])], "rejected": [], "glossary": [], "conflicts": []})
    client.chat.completions.create.side_effect = create
    llm = CompactLLM(Settings(), client=client)
    result = llm.generate(model="gpt-5.6-luna", system_prompt="test", user_prompt=json.dumps(payload), output_type=RefinementResult)
    assert len(result.requirements) == len(result.dispositions) == 37
    assert len({r.internal_key for r in result.requirements}) == 37
    assert {d.candidate_id for d in result.dispositions} == {c.candidate_id for c in candidates}
    assert client.chat.completions.create.call_count == 3


def test_duplicate_feedback_targets_are_colocated_without_dropping_candidates(state):
    payload = {"candidates": [c.model_dump(mode="json") for c in state["candidates"]],
               "previous_requirements": [{"internal_key": "A", "candidate_ids": ["C1"]},
                                         {"internal_key": "B", "candidate_ids": ["C2"]}],
               "review": {"issues": [{"category": "OS3", "actionable": True,
                                      "affected_keys": ["A", "B"], "affected_candidate_ids": []}]}}
    catalog = Catalog(payload)
    plan = RefinementPlan.model_validate({"batches": [
        {"topic": "one", "candidate_ids": [catalog.forward["C1"]]},
        {"topic": "two", "candidate_ids": [catalog.forward["C2"]]}]})
    result = co_locate_duplicates(plan, payload, catalog)
    assert len(result.batches) == 1
    assert set(result.batches[0].candidate_ids) == {catalog.forward["C1"], catalog.forward["C2"]}


def test_compact_refinement_rejects_simultaneous_retention_and_rejection(state):
    payload = {"candidates": [c.model_dump(mode="json") for c in state["candidates"]], "previous_requirements": [], "glossary": []}
    client = Mock()
    client.chat.completions.create.return_value = completion({"requirements": [{"key": "new", "candidate_ids": ["c0001", "c0002"],
        "name": "Login", "description": "The system shall support login.", "kind": "functional", "priority": "P2",
        "priority_rationale": "Daily work", "priority_inferred": True}],
        "rejected": [{"candidate_ids": ["c0001"], "reason": "Current state", "related_key": None}], "glossary": [], "conflicts": []})
    from requirements_refiner.validation import validate_refinement
    llm = CompactLLM(Settings(extraction_attempts=1), client=client)
    with pytest.raises(LLMError):
        llm.generate(model="gpt-5.6-luna", system_prompt="test", user_prompt=json.dumps(payload), output_type=RefinementResult,
            validate=lambda result: validate_refinement(result, state["candidates"], state["documents"]))


def test_full_run_does_not_blindly_retry_truncation():
    from requirements_refiner.full_run import FullRunLLM
    client = Mock()
    value = completion({"candidates": []})
    value.choices[0].finish_reason = "length"
    client.chat.completions.create.return_value = value
    llm = FullRunLLM(Settings(), client, {})
    from requirements_refiner.nodes.extractor import ExtractionResult
    with pytest.raises(LLMError, match="Output limit reached"):
        llm.generate(model="gpt-5-mini", system_prompt="test", user_prompt=json.dumps({"document_id": "test"}), output_type=ExtractionResult)
    client.chat.completions.create.assert_called_once()
