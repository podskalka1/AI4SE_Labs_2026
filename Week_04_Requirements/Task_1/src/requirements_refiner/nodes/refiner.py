"""Initial/revision refinement with complete ledger and stable lineage keys."""
import json
from hashlib import sha256

from ..config import Settings, load_settings
from ..llm import LLMError, StructuredLLM
from ..models import RefinementResult, Requirement
from ..prompts import REFINEMENT_SYSTEM_PROMPT
from ..state import GraphState
from ..validation import unique, validate_candidates, validate_refinement


def stabilize_keys(result: RefinementResult, previous: list[Requirement]) -> RefinementResult:
    """Reuse exact-lineage keys first, then best overlap for merges or splits.

    Each previous key can survive in only one record. Semantic continuity remains
    the refiner's responsibility; overlap matching itself is deterministic.
    """
    result = result.model_copy(deep=True)
    unique((r.internal_key for r in previous), "previous requirement keys")
    pairs = []
    for new in result.requirements:
        for old in previous:
            overlap = len(set(new.candidate_ids) & set(old.candidate_ids))
            if overlap:
                pairs.append((set(new.candidate_ids) == set(old.candidate_ids), overlap,
                              old.internal_key, new.internal_key))
    mapping: dict[str, str] = {}
    used: set[str] = set()
    lineages = {r.internal_key: tuple(sorted(r.candidate_ids)) for r in result.requirements}
    for exact, overlap, old_key, new_key in sorted(
            pairs, key=lambda p: (-p[0], -p[1], p[2], lineages[p[3]])):
        if new_key not in mapping and old_key not in used:
            mapping[new_key] = old_key
            used.add(old_key)
    reserved = {r.internal_key for r in previous} | used
    for requirement in sorted(result.requirements, key=lambda r: sorted(r.candidate_ids)):
        if requirement.internal_key in mapping:
            continue
        seed = json.dumps(sorted(requirement.candidate_ids), separators=(",", ":"))
        key = "REQ-" + sha256(seed.encode("utf-8")).hexdigest()
        while key in reserved:
            key += "-new"
        mapping[requirement.internal_key] = key
        reserved.add(key)
    for requirement in result.requirements:
        requirement.internal_key = mapping[requirement.internal_key]
    for disposition in result.dispositions:
        if disposition.requirement_key is not None:
            disposition.requirement_key = mapping[disposition.requirement_key]
    for rejected in result.blacklist:
        if rejected.merged_into_key is not None:
            rejected.merged_into_key = mapping[rejected.merged_into_key]
    for conflict in result.unresolved_conflicts:
        conflict.requirement_keys = [mapping[key] for key in conflict.requirement_keys]
    return result


def requirements_refiner(state: GraphState, *, settings: Settings | None = None,
                         llm: StructuredLLM | None = None) -> GraphState:
    if "candidates" not in state:
        raise ValueError("Refiner state requires candidates")
    candidates = list(state["candidates"])
    unique((c.candidate_id for c in candidates), "candidate IDs")
    known = {c.candidate_id: c for c in candidates}
    review = state.get("latest_review")
    if review is not None:
        for candidate in review.missing_candidates:
            if candidate.candidate_id in known:
                if known[candidate.candidate_id] != candidate:
                    raise ValueError("Review candidate ID collides with a different candidate")
            else:
                candidates.append(candidate)
                known[candidate.candidate_id] = candidate
    documents = state.get("documents", [])
    validate_candidates(candidates, documents)
    previous = state.get("requirements", [])
    unique((r.internal_key for r in previous), "previous requirement keys")
    settings = settings or load_settings()
    if not candidates:
        return {"requirements": [], "blacklist": [], "dispositions": [],
                "glossary": [], "unresolved_conflicts": []}
    payload = {
        "mode": "revision" if previous or review is not None else "initial",
        "candidates": [c.model_dump(mode="json") for c in candidates],
        "previous_requirements": [r.model_dump(mode="json") for r in previous],
        "previous_blacklist": [b.model_dump(mode="json") for b in state.get("blacklist", [])],
        "glossary": [g.model_dump(mode="json") for g in state.get("glossary", [])],
        "unresolved_conflicts": [c.model_dump(mode="json") for c in state.get("unresolved_conflicts", [])],
        "review": review.model_dump(mode="json") if review else None,
    }
    owned_client = llm is None
    llm = llm or StructuredLLM(settings)
    try:
        result = llm.generate(
            model=settings.refiner_model, system_prompt=REFINEMENT_SYSTEM_PROMPT,
            user_prompt=json.dumps(payload, ensure_ascii=False), output_type=RefinementResult,
            validate=lambda output: validate_refinement(output, candidates, documents),
            operation="Refinement")
        result = stabilize_keys(result, previous)
        validate_refinement(result, candidates, documents)
        update: GraphState = {
            "requirements": result.requirements, "blacklist": result.blacklist,
            "dispositions": result.dispositions, "glossary": result.glossary,
            "unresolved_conflicts": result.unresolved_conflicts,
        }
        if candidates != state["candidates"]:
            update["candidates"] = candidates
        return update
    except LLMError as exc:
        raise LLMError(f"Requirements refiner: {exc}") from None
    finally:
        if owned_client:
            llm.close()
