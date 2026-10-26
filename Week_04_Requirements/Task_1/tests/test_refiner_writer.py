import json
from copy import deepcopy
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from requirements_refiner.config import Settings
from requirements_refiner.llm import LLMError, StructuredLLM
from requirements_refiner.models import (
    CandidateRequirement, RefinementResult, Requirement, ReviewIssue, ReviewResult,
    SourceDocument, SourceReference,
)
from requirements_refiner.nodes.refiner import requirements_refiner
from requirements_refiner.nodes.writer import requirements_writer


@pytest.fixture
def state():
    documents = [SourceDocument(document_id="D1", filename="one.txt",
                               original_content="Support login.\nRequire passwords.",
                               content="Support login.\nRequire passwords."),
                 SourceDocument(document_id="D2", filename="two.txt",
                               original_content="Allow staff to log in.",
                               content="Allow staff to log in.")]
    candidates = []
    for identifier, doc, line, statement in [("C1", documents[0], 1, "Support login."),
                                            ("C2", documents[1], 1, "Allow staff to log in.")]:
        candidates.append(CandidateRequirement(
            candidate_id=identifier, statement=statement, kind="functional",
            references=[SourceReference(document_id=doc.document_id, start_line=line,
                                        end_line=line, excerpt=statement)]))
    return {"documents": documents, "candidates": candidates}


def requirement(state, ids, key="temporary", **fields):
    candidates = {c.candidate_id: c for c in state["candidates"]}
    return {"internal_key": key, "candidate_ids": ids, "name": "Staff login",
            "description": "The system shall allow staff to log in.", "kind": "functional",
            "priority": "P2", "priority_rationale": "Important daily operation",
            "priority_inferred": True,
            "references": [r.model_dump(mode="json") for c in ids for r in candidates[c].references],
            **fields}


def merged(state):
    return {"requirements": [requirement(state, ["C1", "C2"])], "blacklist": [],
            "dispositions": [
                {"candidate_id": "C1", "status": "retained", "requirement_key": "temporary"},
                {"candidate_id": "C2", "status": "merged", "requirement_key": "temporary"}],
            "glossary": [{"term": "staff", "definition": "Authorized library employees", "aliases": []}],
            "unresolved_conflicts": []}


def separate(state):
    result = merged(state)
    result["requirements"] = [requirement(state, ["C1"], "first"),
                              requirement(state, ["C2"], "second", priority="P1",
                                          priority_inferred=False,
                                          priority_rationale="Explicit mandatory source priority")]
    result["dispositions"] = [{"candidate_id": "C1", "status": "retained", "requirement_key": "first"},
                              {"candidate_id": "C2", "status": "retained", "requirement_key": "second"}]
    return result


def service(payload, *additional, attempts=1):
    client = Mock()
    def wrap(value):
        content = value if isinstance(value, str) else json.dumps(value)
        return SimpleNamespace(choices=[SimpleNamespace(finish_reason="stop",
                               message=SimpleNamespace(content=content, refusal=None))])
    client.chat.completions.create.side_effect = [wrap(value) for value in (payload, *additional)]
    return StructuredLLM(Settings(extraction_attempts=attempts), client=client), client


def refine(state, payload):
    llm, client = service(payload)
    return requirements_refiner(state, settings=llm.settings, llm=llm), client


def test_initial_merge_provenance_priorities_glossary_and_no_input_mutation(state):
    before = deepcopy(state)
    update, client = refine(state, merged(state))
    assert state == before
    assert set(update) == {"requirements", "blacklist", "dispositions", "glossary", "unresolved_conflicts"}
    req = update["requirements"][0]
    assert req.internal_key.startswith("REQ-")
    assert req.candidate_ids == ["C1", "C2"]
    assert {r.document_id for r in req.references} == {"D1", "D2"}
    assert req.priority == "P2" and req.priority_inferred
    assert update["blacklist"] == []
    assert {d.status for d in update["dispositions"]} == {"merged", "retained"}
    assert {d.requirement_key for d in update["dispositions"]} == {req.internal_key}
    assert update["glossary"][0].term == "staff"
    assert client.chat.completions.create.call_args.kwargs["model"] == "gpt-5.6-luna"
    assert json.loads(client.chat.completions.create.call_args.kwargs["messages"][1]["content"].split("\nJSON schema:")[0])["mode"] == "initial"


def test_unresolved_conflict_retains_both_and_explicit_priority(state):
    competing = "Prohibit staff login; priority P1 Critical."
    state["documents"][1].content = competing
    state["documents"][1].original_content = competing
    state["candidates"][1].statement = competing
    state["candidates"][1].references[0].excerpt = competing
    result = separate(state)
    result["requirements"][1]["description"] = "The system shall prohibit staff login."
    result["unresolved_conflicts"] = [{"conflict_id": "F1", "requirement_keys": ["first", "second"],
                                       "explanation": "Source policies are incompatible; stakeholder decision needed.",
                                       "references": [r for req in result["requirements"] for r in req["references"]]}]
    update, _ = refine(state, result)
    assert len(update["requirements"]) == 2
    assert not update["requirements"][1].priority_inferred
    assert update["requirements"][1].priority == "P1"
    assert set(update["unresolved_conflicts"][0].requirement_keys) == {r.internal_key for r in update["requirements"]}
    assert not update["blacklist"]


def rejected(state):
    result = separate(state)
    result["requirements"] = result["requirements"][:1]
    c = state["candidates"][1]
    result["blacklist"] = [{"blacklist_id": "B1", "candidate_ids": ["C2"],
                            "original_statement": c.statement,
                            "rejection_reason": "Explicit source decision rejects this alternative.",
                            "references": [r.model_dump(mode="json") for r in c.references],
                            "merged_into_key": "first"}]
    result["dispositions"][1] = {"candidate_id": "C2", "status": "discarded", "blacklist_id": "B1"}
    return result


def test_justified_rejection_preserves_blacklist_originals(state):
    update, _ = refine(state, rejected(state))
    assert update["blacklist"][0].original_statement == state["candidates"][1].statement
    assert update["blacklist"][0].references == state["candidates"][1].references
    assert update["blacklist"][0].merged_into_key == update["requirements"][0].internal_key
    assert update["dispositions"][1].blacklist_id == "B1"


@pytest.mark.parametrize("corruption", ["lost_source", "unknown_candidate", "duplicate_key",
    "missing_disposition", "duplicate_disposition", "wrong_destination", "unknown_document",
    "evidence_mismatch", "invalid_priority", "no_representative", "extra_candidate",
    "lost_membership", "invented_conflict_key", "duplicate_lineage"])
def test_refiner_rejects_cross_record_and_schema_failures(state, corruption):
    result = merged(state)
    req = result["requirements"][0]
    if corruption == "lost_source": req["references"].pop()
    elif corruption == "unknown_candidate": req["candidate_ids"].append("invented")
    elif corruption == "duplicate_key": result["requirements"].append(deepcopy(req))
    elif corruption == "missing_disposition": result["dispositions"].pop()
    elif corruption == "duplicate_disposition": result["dispositions"].append(deepcopy(result["dispositions"][0]))
    elif corruption == "wrong_destination": result["dispositions"][1]["requirement_key"] = "wrong"
    elif corruption == "unknown_document": req["references"][0]["document_id"] = "unknown"
    elif corruption == "evidence_mismatch": req["references"][0]["excerpt"] = "invented"
    elif corruption == "invalid_priority": req["priority"] = "P9"
    elif corruption == "no_representative": result["dispositions"][0]["status"] = "merged"
    elif corruption == "extra_candidate": result["dispositions"].append({"candidate_id": "unknown", "status": "retained", "requirement_key": "temporary"})
    elif corruption == "lost_membership": req["candidate_ids"] = ["C1"]; req["references"] = req["references"][:1]
    elif corruption == "duplicate_lineage": req["candidate_ids"].append("C1")
    else: result["unresolved_conflicts"] = [{"conflict_id": "F1", "requirement_keys": ["temporary", "invented"], "explanation": "Conflict", "references": req["references"]}]
    with pytest.raises(LLMError, match="Requirements refiner:.*1 attempts"):
        refine(state, result)


@pytest.mark.parametrize("corruption", ["bad_original", "bad_destination", "bad_related_key", "lost_source", "retained_in_blacklist"])
def test_blacklist_integrity(state, corruption):
    result = rejected(state)
    if corruption == "bad_original": result["blacklist"][0]["original_statement"] = "rewritten"
    elif corruption == "bad_destination": result["dispositions"][1]["blacklist_id"] = "unknown"
    elif corruption == "bad_related_key": result["blacklist"][0]["merged_into_key"] = "unknown"
    elif corruption == "lost_source": result["blacklist"][0]["references"] = result["requirements"][0]["references"]
    else: result["dispositions"][1] = {"candidate_id": "C2", "status": "retained", "requirement_key": "first"}
    with pytest.raises(LLMError):
        refine(state, result)


def test_revision_feedback_missing_candidate_and_stable_key(state):
    initial, _ = refine(state, merged(state))
    old_key = initial["requirements"][0].internal_key
    missing = CandidateRequirement(candidate_id="C3", statement="Require passwords.", kind="functional",
                                   references=[SourceReference(document_id="D1", start_line=2, end_line=2,
                                                               excerpt="Require passwords.")])
    review = ReviewResult(status="needs_revision", issues=[ReviewIssue(issue_id="I1", category="OS8",
                          explanation="Password behavior missing", requested_correction="Reconsider password behavior")],
                          missing_candidates=[missing])
    revised_state = {**state, **initial, "latest_review": review}
    expanded = {**state, "candidates": [*state["candidates"], missing]}
    result = merged(expanded)
    result["requirements"].append(requirement(expanded, ["C3"], "passwords"))
    result["dispositions"].append({"candidate_id": "C3", "status": "retained", "requirement_key": "passwords"})
    update, client = refine(revised_state, result)
    assert update["requirements"][0].internal_key == old_key
    assert len(update["candidates"]) == 3
    assert len(update["dispositions"]) == 3
    assert "previous_requirements" in client.chat.completions.create.call_args.kwargs["messages"][1]["content"]
    assert '"mode": "revision"' in client.chat.completions.create.call_args.kwargs["messages"][1]["content"]
    assert revised_state["requirements"] == initial["requirements"]


def test_revision_replaces_stale_blacklist_and_preserves_key_when_merging(state):
    initial, _ = refine(state, rejected(state))
    update, _ = refine({**state, **initial}, merged(state))
    assert update["blacklist"] == []
    assert update["requirements"][0].internal_key == initial["requirements"][0].internal_key


def test_revision_split_reuses_key_once_and_is_independent_of_model_keys(state):
    initial, _ = refine(state, merged(state))
    result = separate(state)
    first, _ = refine({**state, **initial}, result)
    result["requirements"][0]["internal_key"] = "z-renamed"
    result["requirements"][1]["internal_key"] = "a-renamed"
    result["dispositions"][0]["requirement_key"] = "z-renamed"
    result["dispositions"][1]["requirement_key"] = "a-renamed"
    second, _ = refine({**state, **initial}, result)
    assert [r.internal_key for r in first["requirements"]] == [r.internal_key for r in second["requirements"]]
    assert sum(r.internal_key == initial["requirements"][0].internal_key for r in first["requirements"]) == 1


def test_writer_only_updates_presentation_and_preserves_state(state):
    refined, _ = refine(state, merged(state))
    before = deepcopy(refined)
    key = refined["requirements"][0].internal_key
    llm, client = service({"requirements": [{"internal_key": key, "name": "Staff access",
                                           "description": "The system shall permit staff to log in. Staff can thereby access authorized functions."}]})
    update = requirements_writer(refined, settings=llm.settings, llm=llm)
    assert list(update) == ["requirements"]
    actual = update["requirements"][0].model_dump(exclude={"name", "description"})
    assert actual == refined["requirements"][0].model_dump(exclude={"name", "description"})
    assert refined == before
    assert update["requirements"][0].name == "Staff access"
    assert client.chat.completions.create.call_args.kwargs["model"] == "gpt-5.4-nano"


@pytest.mark.parametrize("corruption", ["missing", "invented", "duplicate", "priority", "lineage", "reference", "paragraph", "invalid_json"])
def test_writer_rejects_missing_invented_or_immutable_output(state, corruption):
    refined, _ = refine(state, merged(state))
    record = {"internal_key": refined["requirements"][0].internal_key,
              "name": "Staff access", "description": "The system shall support login."}
    result = {"requirements": [record]}
    if corruption == "missing": result["requirements"] = []
    elif corruption == "invented": record["internal_key"] = "invented"
    elif corruption == "duplicate": result["requirements"].append(deepcopy(record))
    elif corruption == "priority": record["priority"] = "P4"
    elif corruption == "lineage": record["candidate_ids"] = ["invented"]
    elif corruption == "reference": record["references"] = []
    elif corruption == "paragraph": record["description"] = "First\n\nSecond"
    else: result = "not JSON"
    llm, _ = service(result)
    with pytest.raises(LLMError, match="Requirements writer:.*1 attempts"):
        requirements_writer(refined, settings=llm.settings, llm=llm)


def test_refiner_retry_can_recover_and_is_bounded(state):
    llm, client = service("not JSON", merged(state), attempts=2)
    requirements_refiner(state, settings=llm.settings, llm=llm)
    assert client.chat.completions.create.call_count == 2


def test_refiner_retry_receives_specific_failed_constraint(state):
    invalid = merged(state)
    invalid["dispositions"].append(deepcopy(invalid["dispositions"][0]))
    llm, client = service(invalid, merged(state), attempts=2)
    requirements_refiner(state, settings=llm.settings, llm=llm)
    messages = client.chat.completions.create.call_args.kwargs["messages"]
    assert "Duplicate candidate dispositions" in messages[-1]["content"]
    assert messages[-2]["role"] == "assistant"
    assert json.loads(messages[-2]["content"])["dispositions"] == invalid["dispositions"]
    llm, client = service("not JSON", "not JSON", attempts=2)
    with pytest.raises(LLMError, match="2 attempts"):
        requirements_refiner(state, settings=llm.settings, llm=llm)
    assert client.chat.completions.create.call_count == 2


def test_bad_input_evidence_and_candidate_collisions_fail_before_api(state):
    llm, client = service(merged(state))
    bad = deepcopy(state)
    bad["candidates"][0].references[0].document_id = "unknown"
    with pytest.raises(ValueError, match="Unknown source"):
        requirements_refiner(bad, settings=llm.settings, llm=llm)
    other = state["candidates"][0].model_copy(update={"statement": "Different statement"})
    with pytest.raises(ValueError, match="collides"):
        requirements_refiner({**state, "latest_review": ReviewResult(status="needs_revision", issues=[], missing_candidates=[other])},
                             settings=llm.settings, llm=llm)
    client.chat.completions.create.assert_not_called()


def test_empty_stages_do_not_need_credentials():
    assert requirements_writer({"requirements": []}) == {"requirements": []}
    assert requirements_refiner({"candidates": []}, settings=Settings()) == {
        "requirements": [], "blacklist": [], "dispositions": [], "glossary": [], "unresolved_conflicts": []}
