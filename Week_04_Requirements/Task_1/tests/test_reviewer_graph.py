import json
from copy import deepcopy
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from pydantic import ValidationError

from requirements_refiner.config import Settings
from requirements_refiner.graph import build_graph, complete_review, graph_recursion_limit
from requirements_refiner.llm import LLMError, StructuredLLM
from requirements_refiner.models import (
    CandidateDisposition, CandidateRequirement, Requirement, ReviewResult,
    SourceDocument, SourceReference, UnresolvedConflict,
)
from requirements_refiner.nodes.reviewer import requirements_reviewer


def response(payload):
    return SimpleNamespace(choices=[SimpleNamespace(finish_reason="stop", message=SimpleNamespace(
        content=payload if isinstance(payload, str) else json.dumps(payload), refusal=None))])


@pytest.fixture
def state():
    doc = SourceDocument(document_id="D1", filename="input.txt", content="Support login.\nKeep backups.",
                         original_content="Support login.\nKeep backups.")
    ref = SourceReference(document_id="D1", start_line=1, end_line=1, excerpt="Support login.")
    candidate = CandidateRequirement(candidate_id="C1", statement="Support login.", kind="functional", references=[ref])
    req = Requirement(internal_key="R1", candidate_ids=["C1"], name="Login", description="The system shall support login.",
                      kind="functional", priority="P2", priority_rationale="Daily operation", priority_inferred=True,
                      references=[ref])
    return {"documents": [doc], "candidates": [candidate], "requirements": [req],
            "dispositions": [CandidateDisposition(candidate_id="C1", status="retained", requirement_key="R1")],
            "blacklist": [], "glossary": [], "unresolved_conflicts": [], "review_history": []}


def issue(state, category="OS3", actionable=True):
    return {"issue_id": "temporary", "category": category, "affected_keys": ["R1"],
            "affected_candidate_ids": ["C1"], "actionable": actionable,
            "explanation": "Problem found in requirement", "requested_correction": "Correct the identified defect",
            "references": [state["candidates"][0].references[0].model_dump(mode="json")]}


def review(state, payload, attempts=1):
    client = Mock()
    client.chat.completions.create.side_effect = [response(payload) for _ in range(attempts)]
    settings = Settings(extraction_attempts=attempts)
    llm = StructuredLLM(settings, client=client)
    return requirements_reviewer(state, settings=settings, llm=llm), client


def test_successful_review_evidence_payload_and_history(state):
    before = deepcopy(state)
    update, client = review(state, {"status": "accepted", "issues": [], "missing_candidates": []})
    assert set(update) == {"latest_review", "review_history"}
    assert update["latest_review"].status == "accepted"
    assert len(update["review_history"]) == 1
    assert state == before
    request = client.chat.completions.create.call_args.kwargs
    assert request["model"] == "gpt-6-luna"
    payload = json.loads(request["messages"][1]["content"].split("\nJSON schema:")[0])
    assert payload["documents"][0]["content"] == state["documents"][0].content
    assert set(payload) >= {"documents", "candidates", "requirements", "dispositions", "blacklist", "glossary", "previous_review", "priority_scale"}


@pytest.mark.parametrize("category,explanation", [
    ("OS3", "Semantic duplicate"), ("OS7", "Contradiction"),
    ("OS7", "Unsupported statement"), ("OS4", "Incorrect output source reference"),
    ("OS5", "Description inadequate"), ("OS6", "Questionable priority"),
    ("OS8", "Candidate omitted"), ("OS9", "Unjustified rejection")])
def test_quality_findings_have_valid_targets_and_stable_ids(state, category, explanation):
    finding = issue(state, category)
    finding["explanation"] = explanation
    first, _ = review(state, {"status": "needs_revision", "issues": [finding]})
    finding["issue_id"] = "different-model-generated-id"
    second, _ = review({**state, **first}, {"status": "needs_revision", "issues": [finding]})
    assert first["latest_review"].issues[0].issue_id.startswith("ISSUE-")
    assert first["latest_review"].issues[0].issue_id == second["latest_review"].issues[0].issue_id
    assert len(second["review_history"]) == 2


def test_incorrect_requirement_reference_can_be_reported_using_original_evidence(state):
    state["requirements"][0].references[0] = SourceReference(document_id="wrong", start_line=1, end_line=1, excerpt="Wrong")
    update, _ = review(state, {"status": "needs_revision", "issues": [issue(state, "OS4")]})
    assert update["latest_review"].issues[0].references[0].document_id == "D1"


def test_missing_corpus_requirement_gets_stable_candidate_id(state):
    missing = {"candidate_id": "new", "statement": "Keep backups.", "kind": "functional", "references": [
        {"document_id": "D1", "start_line": 2, "end_line": 2, "excerpt": "Keep backups."}]}
    finding = issue(state, "OS8")
    finding["affected_candidate_ids"] = ["new"]
    update, _ = review(state, {"status": "needs_revision", "issues": [finding], "missing_candidates": [missing]})
    candidate = update["latest_review"].missing_candidates[0]
    assert candidate.candidate_id.startswith("CAND-")
    assert update["latest_review"].issues[0].affected_candidate_ids == [candidate.candidate_id]


@pytest.mark.parametrize("corruption", ["requirement", "candidate", "source", "range", "excerpt", "duplicate_id", "category", "accepted_with_actionable", "revision_without_actionable", "missing_candidate_source", "invalid_json"])
def test_invalid_review_is_retried_and_rejected(state, corruption):
    finding = issue(state)
    payload = {"status": "needs_revision", "issues": [finding]}
    if corruption == "requirement": finding["affected_keys"] = ["unknown"]
    elif corruption == "candidate": finding["affected_candidate_ids"] = ["unknown"]
    elif corruption == "source": finding["references"][0]["document_id"] = "unknown"
    elif corruption == "range": finding["references"][0]["end_line"] = 100
    elif corruption == "excerpt": finding["references"][0]["excerpt"] = "wrong"
    elif corruption == "duplicate_id": payload["issues"].append(deepcopy(finding))
    elif corruption == "category": finding["category"] = "OS1"
    elif corruption == "accepted_with_actionable": payload["status"] = "accepted"
    elif corruption == "revision_without_actionable": finding["actionable"] = False
    elif corruption == "missing_candidate_source": payload["missing_candidates"] = [{"candidate_id": "new", "statement": "Missing", "kind": "functional", "references": [{"document_id": "unknown", "start_line": 1, "end_line": 1, "excerpt": "Missing"}]}]
    else: payload = "not JSON"
    with pytest.raises(LLMError, match="Requirements reviewer:.*2 attempts"):
        review(state, payload, attempts=2)


def test_unresolved_conflict_must_be_assessed(state):
    other = state["requirements"][0].model_copy(update={"internal_key": "R2"})
    state["requirements"].append(other)
    state["unresolved_conflicts"] = [UnresolvedConflict(conflict_id="F1", requirement_keys=["R1", "R2"],
        explanation="Sources disagree", references=state["candidates"][0].references)]
    with pytest.raises(LLMError):
        review(state, {"status": "accepted", "issues": []})
    finding = issue(state, "OS7", actionable=False)
    finding["affected_keys"] = ["R1", "R2"]
    update, _ = review(state, {"status": "accepted_with_unresolved", "issues": [finding]})
    assert not update["latest_review"].issues[0].actionable


class FakeAPI:
    """Mock SDK boundary; all actual node and LangGraph logic executes."""
    def __init__(self, reviews, reject_initial=False):
        self.reviews = reviews
        self.calls = []
        self.review_index = 0
        self.refinement_index = 0
        self.reject_initial = reject_initial
        self.client = Mock()
        self.client.chat.completions.create.side_effect = self.create

    def create(self, **request):
        model = request["model"]
        self.calls.append(model)
        payload = json.loads(request["messages"][1]["content"].split("\nJSON schema:")[0])
        if model == "gpt-5-mini":
            refs = [{"document_id": payload["document_id"], "start_line": line, "end_line": line,
                     "excerpt": text, "evidence_basis": "normalized_text"}
                    for line, text in [(1, "Support login."), (2, "Keep backups.")]]
            if getattr(self, "omit_backup", False):
                refs = refs[:1]
            return response({"candidates": [{"statement": ref["excerpt"], "kind": "functional",
                                              "references": [ref], "extraction_note": None} for ref in refs]})
        if model == "gpt-5.6-luna":
            requirements, dispositions, blacklist = [], [], []
            for index, candidate in enumerate(payload["candidates"]):
                if self.reject_initial and self.refinement_index == 0 and index == 1:
                    blacklist.append({"blacklist_id": "B1", "candidate_ids": [candidate["candidate_id"]],
                                      "original_statement": candidate["statement"], "rejection_reason": "Questionable exclusion",
                                      "references": candidate["references"], "merged_into_key": None})
                    dispositions.append({"candidate_id": candidate["candidate_id"], "status": "discarded", "blacklist_id": "B1"})
                else:
                    key = f"temp-{index}"
                    requirements.append({"internal_key": key, "candidate_ids": [candidate["candidate_id"]],
                        "name": "Feature", "description": "The system shall " + candidate["statement"], "kind": candidate["kind"],
                        "priority": "P2", "priority_rationale": "Daily operation", "priority_inferred": True,
                        "references": candidate["references"]})
                    dispositions.append({"candidate_id": candidate["candidate_id"], "status": "retained", "requirement_key": key})
            self.refinement_index += 1
            return response({"requirements": requirements, "dispositions": dispositions, "blacklist": blacklist,
                             "glossary": [{"term": "current", "definition": f"Pass {self.refinement_index}", "aliases": []}],
                             "unresolved_conflicts": []})
        if model == "gpt-5.4-nano":
            return response({"requirements": [{"internal_key": r["internal_key"], "name": "Feature",
                                                "description": r["description"]} for r in payload["requirements"]]})
        assert model == "gpt-6-luna"
        outcome = self.reviews[min(self.review_index, len(self.reviews) - 1)]
        self.review_index += 1
        findings = []
        if outcome != "accepted":
            findings = [{"issue_id": "model-issue", "category": "OS7" if outcome == "ambiguity" else "OS9",
                "actionable": outcome != "ambiguity", "affected_keys": [payload["requirements"][0]["internal_key"]],
                "affected_candidate_ids": [payload["candidates"][0]["candidate_id"]],
                "explanation": "Ambiguous source policy" if outcome == "ambiguity" else "Reconsider exclusion",
                "requested_correction": "Disclose ambiguity" if outcome == "ambiguity" else "Reconsider evidence",
                "references": payload["candidates"][0]["references"]}]
        missing = []
        if outcome == "missing":
            missing = [{"candidate_id": "discovered", "statement": "Keep backups.", "kind": "functional", "references": [
                {"document_id": payload["documents"][0]["document_id"], "start_line": 2, "end_line": 2,
                 "excerpt": "Keep backups.", "evidence_basis": "normalized_text"}], "extraction_note": None}]
            findings[0]["category"] = "OS8"
            findings[0]["affected_candidate_ids"] = ["discovered"]
        status = {"accepted": "accepted", "actionable": "needs_revision", "missing": "needs_revision", "ambiguity": "accepted_with_unresolved"}[outcome]
        return response({"status": status, "issues": findings, "missing_candidates": missing})


def graph_fixture(tmp_path, outcomes, max_revisions=3, reject_initial=False):
    (tmp_path / "input.txt").write_text("Support login.\nKeep backups.", encoding="utf-8")
    api = FakeAPI(outcomes, reject_initial)
    settings = Settings(max_revisions=max_revisions)
    llm = StructuredLLM(settings, client=api.client)
    return build_graph(settings, llm=llm), api


def test_graph_compiles_and_accepts_in_order(tmp_path):
    graph, api = graph_fixture(tmp_path, ["accepted"])
    events = list(graph.stream({"input_directory": str(tmp_path)}, stream_mode="updates"))
    assert [next(iter(event)) for event in events] == ["loader", "extractor", "refiner", "writer", "reviewer", "complete", "formatter"]
    assert events[-2]["complete"]["completion_status"] == "complete"
    assert "# Software Requirements Specification" in events[-1]["formatter"]["final_document"]
    assert api.calls == ["gpt-5-mini", "gpt-5.6-luna", "gpt-5.4-nano", "gpt-6-luna"]
    assert len(set(api.calls)) == 4


def test_feedback_replaces_state_and_preserves_history(tmp_path):
    graph, api = graph_fixture(tmp_path, ["actionable", "accepted"], reject_initial=True)
    result = graph.invoke({"input_directory": str(tmp_path)})
    assert result["revision_count"] == 1
    assert len(result["review_history"]) == 2
    assert result["review_history"][0].status == "needs_revision"
    assert result["latest_review"].status == "accepted"
    assert result["completion_status"] == "complete"
    assert result["blacklist"] == []
    assert len(result["requirements"]) == len(result["dispositions"]) == len(result["candidates"]) == 2
    assert result["glossary"][0].definition == "Pass 2"
    assert result["documents"][0].content == "Support login.\nKeep backups."
    assert result["unresolved_quality_issues"] == []
    assert api.calls == ["gpt-5-mini"] + ["gpt-5.6-luna", "gpt-5.4-nano", "gpt-6-luna"] * 2


@pytest.mark.parametrize("maximum", [0, 3, 7])
def test_exact_revision_limit_and_no_infinite_loop(tmp_path, maximum):
    graph, api = graph_fixture(tmp_path, ["actionable"], max_revisions=maximum)
    result = graph.invoke({"input_directory": str(tmp_path)})
    assert result["revision_count"] == maximum
    assert len(result["review_history"]) == api.review_index == maximum + 1
    assert result["completion_status"] == "incomplete_review"
    assert result["termination_reason"] == "revision_limit"
    assert len(result["unresolved_quality_issues"]) == 1
    assert result["unresolved_source_issues"] == []
    assert graph.config["recursion_limit"] == graph_recursion_limit(maximum)


def test_unresolvable_source_ambiguity_terminates_without_revision(tmp_path):
    graph, api = graph_fixture(tmp_path, ["ambiguity"])
    result = graph.invoke({"input_directory": str(tmp_path)})
    assert result["revision_count"] == 0
    assert api.review_index == 1
    assert result["completion_status"] == "complete_with_unresolved"
    assert result["termination_reason"] == "source_ambiguity"
    assert len(result["unresolved_source_issues"]) == 1
    assert result["unresolved_quality_issues"] == []


def test_graph_review_discovered_candidate_is_added_on_revision(tmp_path):
    graph, api = graph_fixture(tmp_path, ["missing", "accepted"])
    api.omit_backup = True
    result = graph.invoke({"input_directory": str(tmp_path)})
    assert result["revision_count"] == 1
    assert len(result["candidates"]) == 2
    assert len(result["requirements"]) == len(result["dispositions"]) == 2
    discovered = result["review_history"][0].missing_candidates[0]
    assert discovered in result["candidates"]
    assert result["completion_status"] == "complete"


def test_completion_preserves_both_unresolved_source_and_quality_findings(state):
    actionable = issue(state)
    ambiguity = issue(state, "OS7", actionable=False)
    ambiguity["issue_id"] = "ambiguity"
    result = ReviewResult.model_validate({"status": "needs_revision", "issues": [actionable, ambiguity]})
    update = complete_review({**state, "latest_review": result, "revision_count": 3, "max_revisions": 3})
    assert update["completion_status"] == "incomplete_review"
    assert len(update["unresolved_source_issues"]) == len(update["unresolved_quality_issues"]) == 1


def test_fresh_invocation_resets_old_review_state(tmp_path):
    graph, _ = graph_fixture(tmp_path, ["accepted"])
    result = graph.invoke({"input_directory": str(tmp_path), "revision_count": 3,
                           "max_revisions": 99, "review_history": [ReviewResult(status="accepted", issues=[])],
                           "completion_status": "incomplete_review"})
    assert result["revision_count"] == 0
    assert result["max_revisions"] == 3
    assert len(result["review_history"]) == 1


def test_graph_rejects_insufficient_model_diversity_without_credentials():
    with pytest.raises(ValueError, match="three distinct"):
        build_graph(Settings(extractor_model="same", refiner_model="same", writer_model="same", reviewer_model="same"))


def test_resume_at_refiner_preserves_review_history_and_remaining_budget(tmp_path):
    graph, api = graph_fixture(tmp_path, ["actionable", "accepted"])
    saved = None
    accumulated = {"input_directory": str(tmp_path)}
    stream = graph.stream(accumulated, stream_mode="updates")
    for event in stream:
        for name, values in event.items():
            accumulated.update(values)
            if name == "revise":
                saved = deepcopy(accumulated)
                break
        if saved is not None:
            break
    stream.close()
    before_calls = len(api.calls)
    settings = Settings(max_revisions=3)
    resumed = build_graph(settings, llm=StructuredLLM(settings, client=api.client), entry_point="refiner")
    result = resumed.invoke(saved)
    assert api.calls[before_calls:] == ["gpt-5.6-luna", "gpt-5.4-nano", "gpt-6-luna"]
    assert result["revision_count"] == 1
    assert len(result["review_history"]) == 2
    assert result["completion_status"] == "complete"


@pytest.mark.parametrize("entry,stop_after", [("extractor", "loader"), ("refiner", "extractor"),
    ("writer", "refiner"), ("reviewer", "writer"), ("complete", "reviewer"),
    ("formatter", "complete"), ("revise", "reviewer")])
def test_recovery_at_each_stage_preserves_complete_state(tmp_path, entry, stop_after):
    outcomes = ["actionable", "accepted"] if entry == "revise" else ["accepted"]
    graph, api = graph_fixture(tmp_path, outcomes)
    saved = {"input_directory": str(tmp_path)}
    stream = graph.stream(saved, stream_mode="updates")
    for event in stream:
        name, update = next(iter(event.items()))
        saved.update(update)
        if name == stop_after:
            break
    stream.close()
    from requirements_refiner.run_support import encode_state, decode_state
    saved = decode_state(json.loads(json.dumps(encode_state(saved))))
    settings = Settings()
    resumed = build_graph(settings, llm=StructuredLLM(settings, client=api.client), entry_point=entry)
    result = resumed.invoke(saved)
    assert result["completion_status"] == "complete"
    assert result["revision_count"] == (1 if entry == "revise" else 0)
    assert len(result["review_history"]) == result["revision_count"] + 1
    assert len(result["documents"]) == 1
    assert "# Software Requirements Specification" in result["final_document"]
