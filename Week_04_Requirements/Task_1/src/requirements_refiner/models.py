"""Validated shared records. IDs are supplied once and preserved across revisions."""
from enum import StrEnum
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

Text = Annotated[str, Field(min_length=1, pattern=r"\S")]


class Record(BaseModel):
    model_config = ConfigDict(extra="forbid")


class RequirementType(StrEnum):
    FUNCTIONAL = "functional"
    NONFUNCTIONAL = "nonfunctional"


class Priority(StrEnum):
    CRITICAL = "P1"
    HIGH = "P2"
    MEDIUM = "P3"
    LOW = "P4"


class DispositionStatus(StrEnum):
    RETAINED = "retained"
    MERGED = "merged"
    DISCARDED = "discarded"


class ReviewStatus(StrEnum):
    ACCEPTED = "accepted"
    ACCEPTED_WITH_UNRESOLVED = "accepted_with_unresolved"
    NEEDS_REVISION = "needs_revision"


class CompletionStatus(StrEnum):
    PENDING = "pending"
    COMPLETE = "complete"
    UNRESOLVED = "unresolved"
    COMPLETE_WITH_UNRESOLVED = "complete_with_unresolved"
    INCOMPLETE_REVIEW = "incomplete_review"


class SourceDocument(Record):
    document_id: Text
    filename: Text  # POSIX path relative to the corpus root
    original_content: str
    content: str  # Canonical evidence text, LF newlines
    evidence_basis: Literal["normalized_text"] = "normalized_text"
    metadata: dict[str, str] = Field(default_factory=dict)
    warnings: list[str] = Field(default_factory=list)


class SourceReference(Record):
    document_id: Text
    start_line: int = Field(ge=1)
    end_line: int = Field(ge=1)
    excerpt: Text
    evidence_basis: Literal["normalized_text"] = "normalized_text"

    @model_validator(mode="after")
    def ordered_lines(self) -> "SourceReference":
        if self.end_line < self.start_line:
            raise ValueError("end_line must be >= start_line")
        return self

    def validate_against(self, document: SourceDocument) -> None:
        lines = document.content.splitlines()
        if self.document_id != document.document_id or self.end_line > len(lines):
            raise ValueError("Reference does not locate lines in this document")
        if self.excerpt != "\n".join(lines[self.start_line - 1:self.end_line]):
            raise ValueError("Evidence excerpt must exactly match normalized lines")


class CandidateRequirement(Record):
    candidate_id: Text
    statement: Text
    kind: RequirementType
    references: list[SourceReference] = Field(min_length=1)
    extraction_note: Text | None = None  # Explicitly mark uncertainty or inference


class Requirement(Record):
    internal_key: Text
    candidate_ids: list[Text] = Field(min_length=1)
    name: Text
    description: Text
    kind: RequirementType
    priority: Priority
    priority_rationale: Text
    priority_inferred: bool
    references: list[SourceReference] = Field(min_length=1)


class DiscardedRequirement(Record):
    blacklist_id: Text
    candidate_ids: list[Text] = Field(min_length=1)
    original_statement: Text
    rejection_reason: Text
    references: list[SourceReference] = Field(min_length=1)
    merged_into_key: Text | None = None


class CandidateDisposition(Record):
    candidate_id: Text
    status: DispositionStatus
    requirement_key: Text | None = None
    blacklist_id: Text | None = None

    @model_validator(mode="after")
    def valid_destination(self) -> "CandidateDisposition":
        discarded = self.status == DispositionStatus.DISCARDED
        if discarded and (self.blacklist_id is None or self.requirement_key is not None):
            raise ValueError("Discarded candidates require only a blacklist destination")
        if not discarded and (self.requirement_key is None or self.blacklist_id is not None):
            raise ValueError("Retained/merged candidates require only a requirement destination")
        return self


class GlossaryEntry(Record):
    term: Text
    definition: Text
    aliases: list[Text] = Field(default_factory=list)


class ReviewIssue(Record):
    issue_id: Text
    category: Literal["OS2", "OS3", "OS4", "OS5", "OS6", "OS7", "OS8", "OS9"]
    affected_keys: list[Text] = Field(default_factory=list)
    affected_candidate_ids: list[Text] = Field(default_factory=list)
    actionable: bool = True
    references: list[SourceReference] = Field(default_factory=list)
    explanation: Text
    requested_correction: Text


class ReviewResult(Record):
    status: ReviewStatus
    issues: list[ReviewIssue]
    missing_candidates: list[CandidateRequirement] = Field(default_factory=list)

    @model_validator(mode="after")
    def consistent_status(self) -> "ReviewResult":
        actionable = bool(self.missing_candidates) or any(issue.actionable for issue in self.issues)
        expected = (ReviewStatus.NEEDS_REVISION if actionable else
                    ReviewStatus.ACCEPTED_WITH_UNRESOLVED if self.issues else ReviewStatus.ACCEPTED)
        if self.status != expected:
            raise ValueError("Review status must agree with actionable and unresolved findings")
        return self


class UnresolvedConflict(Record):
    conflict_id: Text
    requirement_keys: list[Text] = Field(min_length=2)
    explanation: Text
    references: list[SourceReference] = Field(min_length=1)


class RefinementResult(Record):
    requirements: list[Requirement]
    blacklist: list[DiscardedRequirement]
    dispositions: list[CandidateDisposition]
    glossary: list[GlossaryEntry]
    unresolved_conflicts: list[UnresolvedConflict]


class WrittenRequirement(Record):
    internal_key: Text
    name: Annotated[str, Field(min_length=1, max_length=120, pattern=r"\S")]
    description: Text

    @model_validator(mode="after")
    def single_paragraph(self) -> "WrittenRequirement":
        if any(character in self.name + self.description for character in "\r\n"):
            raise ValueError("Writer names and explanations must each be a single paragraph")
        return self


class WritingResult(Record):
    requirements: list[WrittenRequirement]
