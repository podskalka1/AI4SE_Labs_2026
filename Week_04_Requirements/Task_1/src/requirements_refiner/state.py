"""Replacement semantics for all fields: nodes return only changed fields.

No append reducers: revised requirements and latest findings replace stale values.
The future reviewer will explicitly return an updated review_history list.
"""
from typing import Literal, TypedDict

from .models import (
    CandidateDisposition, CandidateRequirement, CompletionStatus,
    DiscardedRequirement, GlossaryEntry, Requirement, ReviewResult, SourceDocument,
    UnresolvedConflict, ReviewIssue,
)


class GraphState(TypedDict, total=False):
    input_directory: str
    output_path: str
    allow_output_in_corpus: bool
    documents: list[SourceDocument]
    candidates: list[CandidateRequirement]
    requirements: list[Requirement]
    blacklist: list[DiscardedRequirement]
    dispositions: list[CandidateDisposition]
    glossary: list[GlossaryEntry]
    unresolved_conflicts: list[UnresolvedConflict]
    latest_review: ReviewResult | None
    review_history: list[ReviewResult]
    revision_count: int
    max_revisions: int
    completion_status: CompletionStatus
    termination_reason: Literal["accepted", "source_ambiguity", "revision_limit"] | None
    unresolved_source_issues: list[ReviewIssue]
    unresolved_quality_issues: list[ReviewIssue]
    final_document: str | None
    final_requirement_ids: dict[str, str]
