"""Deterministic integrity checks shared by refinement and writing."""
from collections import Counter

from .models import (CandidateRequirement, DispositionStatus, RefinementResult,
                     Requirement, SourceDocument, SourceReference, WritingResult)


def unique(values, label: str) -> None:
    values = list(values)
    if len(values) != len(set(values)):
        raise ValueError(f"Duplicate {label}")


def reference_keys(references: list[SourceReference]) -> set[str]:
    return {reference.model_dump_json() for reference in references}


def validate_candidates(candidates: list[CandidateRequirement],
                        documents: list[SourceDocument]) -> None:
    unique((candidate.candidate_id for candidate in candidates), "candidate IDs")
    unique((document.document_id for document in documents), "source document IDs")
    sources = {document.document_id: document for document in documents}
    for candidate in candidates:
        for reference in candidate.references:
            if reference.document_id not in sources:
                raise ValueError("Unknown source document")
            reference.validate_against(sources[reference.document_id])


def validate_refinement(result: RefinementResult, candidates: list[CandidateRequirement],
                        documents: list[SourceDocument]) -> None:
    validate_candidates(candidates, documents)
    originals = {candidate.candidate_id: candidate for candidate in candidates}
    unique((r.internal_key for r in result.requirements), "requirement keys")
    unique((b.blacklist_id for b in result.blacklist), "blacklist IDs")
    unique((d.candidate_id for d in result.dispositions), "candidate dispositions")
    unique((c.conflict_id for c in result.unresolved_conflicts), "conflict IDs")
    unique((entry.term.casefold() for entry in result.glossary), "glossary terms")
    ledger = {d.candidate_id: d for d in result.dispositions}
    if set(ledger) != set(originals):
        raise ValueError("Candidate disposition coverage must be exact")
    requirements = {r.internal_key: r for r in result.requirements}
    blacklist = {b.blacklist_id: b for b in result.blacklist}
    memberships: Counter = Counter()
    for record in [*result.requirements, *result.blacklist]:
        unique(record.candidate_ids, "candidate IDs in output record")
        if not set(record.candidate_ids) <= set(originals):
            raise ValueError("Output references unknown candidate IDs")
        memberships.update(record.candidate_ids)
        expected = set().union(*(reference_keys(originals[c].references)
                                 for c in record.candidate_ids))
        if reference_keys(record.references) != expected:
            raise ValueError("Output must preserve the complete original source reference union")
    if set(memberships) != set(originals) or any(count != 1 for count in memberships.values()):
        raise ValueError("Each candidate must belong to exactly one output record")
    for requirement in result.requirements:
        entries = [ledger[c] for c in requirement.candidate_ids]
        if any(d.status == DispositionStatus.DISCARDED or
               d.requirement_key != requirement.internal_key for d in entries):
            raise ValueError("Requirement lineage disagrees with disposition ledger")
        if sum(d.status == DispositionStatus.RETAINED for d in entries) != 1:
            raise ValueError("Each requirement needs exactly one retained representative")
    for rejected in result.blacklist:
        if any(ledger[c].status != DispositionStatus.DISCARDED or
               ledger[c].blacklist_id != rejected.blacklist_id for c in rejected.candidate_ids):
            raise ValueError("Blacklist lineage disagrees with disposition ledger")
        if rejected.original_statement != "\n\n".join(originals[c].statement for c in rejected.candidate_ids):
            raise ValueError("Blacklist must preserve original statements")
        if rejected.merged_into_key is not None and rejected.merged_into_key not in requirements:
            raise ValueError("Blacklist related requirement key is invalid")
    for disposition in result.dispositions:
        if disposition.status == DispositionStatus.DISCARDED:
            if disposition.blacklist_id not in blacklist:
                raise ValueError("Invalid blacklist destination")
        elif disposition.requirement_key not in requirements:
            raise ValueError("Invalid requirement destination")
    for conflict in result.unresolved_conflicts:
        unique(conflict.requirement_keys, "conflict requirement keys")
        if not set(conflict.requirement_keys) <= set(requirements):
            raise ValueError("Conflict refers to unknown requirements")
        conflict_evidence = set().union(*(reference_keys(requirements[key].references)
                                          for key in conflict.requirement_keys))
        if not reference_keys(conflict.references) <= conflict_evidence:
            raise ValueError("Conflict evidence must come from the competing requirements")


def validate_writing(result: WritingResult, requirements: list[Requirement]) -> None:
    unique((r.internal_key for r in requirements), "input requirement keys")
    unique((r.internal_key for r in result.requirements), "writer output keys")
    if {r.internal_key for r in result.requirements} != {r.internal_key for r in requirements}:
        raise ValueError("Writer must return exactly the input requirement keys")
