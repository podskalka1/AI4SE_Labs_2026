"""Evidence-grounded review with validated targets and explicit actionability."""
import json
from hashlib import sha256

from ..config import Settings, load_settings
from ..llm import LLMError, StructuredLLM
from ..models import CandidateRequirement, ReviewResult
from ..prompts import PRIORITY_SCALE, REVIEW_SYSTEM_PROMPT
from ..state import GraphState
from ..validation import unique, validate_candidates


def validate_review(result: ReviewResult, state: GraphState) -> None:
    unique((issue.issue_id for issue in result.issues), "review issue IDs")
    candidates = state["candidates"]
    documents = state["documents"]
    validate_candidates(result.missing_candidates, documents)
    originals = {candidate.candidate_id: candidate for candidate in candidates}
    for candidate in result.missing_candidates:
        if candidate.candidate_id in originals and originals[candidate.candidate_id] != candidate:
            raise ValueError("Review candidate ID collides with original candidate")
    candidate_ids = set(originals) | {c.candidate_id for c in result.missing_candidates}
    requirement_keys = {r.internal_key for r in state["requirements"]}
    sources = {document.document_id: document for document in documents}
    for issue in result.issues:
        unique(issue.affected_keys, "issue requirement targets")
        unique(issue.affected_candidate_ids, "issue candidate targets")
        if not set(issue.affected_keys) <= requirement_keys:
            raise ValueError("Review references unknown requirement key")
        if not set(issue.affected_candidate_ids) <= candidate_ids:
            raise ValueError("Review references unknown candidate ID")
        for reference in issue.references:
            if reference.document_id not in sources:
                raise ValueError("Review references unknown source document")
            reference.validate_against(sources[reference.document_id])
    for conflict in state.get("unresolved_conflicts", []):
        if not any(issue.category == "OS7" and set(conflict.requirement_keys) <= set(issue.affected_keys)
                   for issue in result.issues):
            raise ValueError("Review must explicitly assess each unresolved conflict")


def stable_review(result: ReviewResult, state: GraphState) -> ReviewResult:
    result = result.model_copy(deep=True)
    remapped = {}
    for candidate in result.missing_candidates:
        # Match the extractor's canonical record scheme (without trusting model IDs).
        content = candidate.model_dump(mode="json", exclude={"candidate_id"})
        content["references"] = [json.loads(ref) for ref in sorted(
            set(reference.model_dump_json() for reference in candidate.references))]
        digest = sha256(json.dumps(content, sort_keys=True, ensure_ascii=False,
                                  separators=(",", ":")).encode("utf-8")).hexdigest()
        new_id = "CAND-" + digest
        existing = next((c for c in state["candidates"] if c.candidate_id == candidate.candidate_id), None)
        if existing is not None:
            new_id = existing.candidate_id
        remapped[candidate.candidate_id] = new_id
        candidate.candidate_id = new_id
    for issue in result.issues:
        issue.affected_candidate_ids = [remapped.get(key, key) for key in issue.affected_candidate_ids]
        content = issue.model_dump(mode="json", exclude={"issue_id"})
        content["affected_keys"] = sorted(content["affected_keys"])
        content["affected_candidate_ids"] = sorted(content["affected_candidate_ids"])
        content["references"] = sorted(content["references"], key=lambda ref: json.dumps(ref, sort_keys=True))
        issue.issue_id = "ISSUE-" + sha256(json.dumps(content, sort_keys=True, ensure_ascii=False,
                                                    separators=(",", ":")).encode("utf-8")).hexdigest()
    validate_review(result, state)
    return result


def requirements_reviewer(state: GraphState, *, settings: Settings | None = None,
                          llm: StructuredLLM | None = None) -> GraphState:
    if any(field not in state for field in ("documents", "candidates", "requirements")):
        raise ValueError("Reviewer requires documents, candidates and requirements")
    validate_candidates(state["candidates"], state["documents"])
    settings = settings or load_settings()
    payload = {
        "documents": [{"document_id": d.document_id, "filename": d.filename,
                       "content": d.content, "metadata": d.metadata,
                       "evidence_basis": d.evidence_basis} for d in state["documents"]],
        "priority_scale": PRIORITY_SCALE,
        "candidates": [c.model_dump(mode="json") for c in state["candidates"]],
        "requirements": [r.model_dump(mode="json") for r in state["requirements"]],
        "dispositions": [d.model_dump(mode="json") for d in state.get("dispositions", [])],
        "blacklist": [b.model_dump(mode="json") for b in state.get("blacklist", [])],
        "glossary": [g.model_dump(mode="json") for g in state.get("glossary", [])],
        "unresolved_conflicts": [c.model_dump(mode="json") for c in state.get("unresolved_conflicts", [])],
        "previous_review": state["latest_review"].model_dump(mode="json") if state.get("latest_review") else None,
    }
    owned_client = llm is None
    llm = llm or StructuredLLM(settings)
    try:
        def validate(output: ReviewResult) -> None:
            validate_review(output, state)
            stable_review(output, state)  # Also reject collisions after deterministic IDs.

        result = llm.generate(model=settings.reviewer_model, system_prompt=REVIEW_SYSTEM_PROMPT,
                              user_prompt=json.dumps(payload, ensure_ascii=False), output_type=ReviewResult,
                              validate=validate, operation="Review")
        result = stable_review(result, state)
        return {"latest_review": result, "review_history": [*state.get("review_history", []), result]}
    except LLMError as exc:
        raise LLMError(f"Requirements reviewer: {exc}") from None
    finally:
        if owned_client:
            llm.close()
