"""Validated deterministic Markdown rendering; no model calls."""
import html
import os
import re
from pathlib import Path
from urllib.parse import quote

from pydantic import ValidationError

from ..models import (CandidateRequirement, CompletionStatus, RefinementResult,
                      ReviewResult, ReviewStatus, SourceDocument)
from ..output import atomic_write, validate_output_path
from ..prompts import PRIORITY_SCALE
from ..state import GraphState
from ..validation import validate_refinement
from .reviewer import validate_review


class FormatterError(ValueError):
    """Invalid final structure or failed output writing."""


def escape(value: str) -> str:
    value = html.escape(str(value), quote=False)
    value = re.sub(r"([\\`*_{}\[\]()#+.!|~])", r"\\\1", value)
    return value.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "<br>")


def validate_final_state(state: GraphState):
    required = ("input_directory", "documents", "candidates", "requirements", "blacklist",
                "dispositions", "glossary", "unresolved_conflicts", "latest_review",
                "revision_count", "max_revisions", "completion_status")
    if any(field not in state for field in required) or state["latest_review"] is None:
        raise FormatterError("Formatter requires complete reviewed pipeline state")
    # Re-parse dictionaries to catch invalid model_copy/update or in-place edits.
    documents = [SourceDocument.model_validate(d.model_dump(warnings=False)) for d in state["documents"]]
    candidates = [CandidateRequirement.model_validate(c.model_dump(warnings=False)) for c in state["candidates"]]
    result = RefinementResult.model_validate({field: [record.model_dump(warnings=False) for record in state[field]]
        for field in ("requirements", "blacklist", "dispositions", "glossary", "unresolved_conflicts")})
    validate_refinement(result, candidates, documents)
    review = ReviewResult.model_validate(state["latest_review"].model_dump(warnings=False))
    validate_review(review, {**state, "documents": documents, "candidates": candidates,
                             "requirements": result.requirements})
    count, maximum = state["revision_count"], state["max_revisions"]
    if (type(count) is not int or type(maximum) is not int or not 0 <= count <= maximum):
        raise FormatterError("Invalid revision counters")
    statuses = {
        ReviewStatus.ACCEPTED: (CompletionStatus.COMPLETE, "accepted"),
        ReviewStatus.ACCEPTED_WITH_UNRESOLVED: (CompletionStatus.COMPLETE_WITH_UNRESOLVED, "source_ambiguity"),
        ReviewStatus.NEEDS_REVISION: (CompletionStatus.INCOMPLETE_REVIEW, "revision_limit"),
    }
    expected, reason = statuses[review.status]
    if state["completion_status"] != expected or (review.status == ReviewStatus.NEEDS_REVISION and count < maximum):
        raise FormatterError("Completion status disagrees with review or revision budget")
    if state.get("termination_reason", reason) != reason:
        raise FormatterError("Termination reason disagrees with review status")
    for field, actionable in (("unresolved_source_issues", False), ("unresolved_quality_issues", True)):
        if field in state and state[field] != [issue for issue in review.issues if issue.actionable == actionable]:
            raise FormatterError("Unresolved issue lists disagree with latest review")
    if "review_history" in state:
        history = state["review_history"]
        if len(history) != count + 1 or history[-1] != review:
            raise FormatterError("Review history disagrees with revision count or latest review")
    return documents, candidates, result, review


def render_document(state: GraphState) -> tuple[str, dict[str, str]]:
    documents, candidates, result, review = validate_final_state(state)
    requirements = sorted(result.requirements, key=lambda r: r.internal_key)
    final_ids = {r.internal_key: f"REQ-{index:03d}" for index, r in enumerate(requirements, 1)}
    if len(set(final_ids.values())) != len(requirements):
        raise FormatterError("Final requirement identifiers are not unique")
    sources = {document.document_id: document for document in documents}
    root = Path(state["input_directory"]).resolve()
    output_parent = Path(state["output_path"]).resolve().parent if state.get("output_path") else root

    key_pattern = (re.compile(r"(?<![\w-])(?:" + "|".join(re.escape(key) for key in
                   sorted(final_ids, key=len, reverse=True)) + r")(?![\w-])") if final_ids else None)

    def prose(value: str) -> str:
        if key_pattern:
            value = key_pattern.sub(lambda match: final_ids[match.group()], value)
        return escape(value)

    def source_link(document_id: str) -> str:
        document = sources[document_id]
        try:
            relative = os.path.relpath(root / document.filename, output_parent).replace(os.sep, "/")
            link = quote(relative, safe="/.-_")
        except ValueError:  # Different Windows drive letters cannot use relative links.
            link = (root / document.filename).as_uri()
        return f"[{escape(document.filename)}](<{link}>)"

    def evidence(references) -> list[str]:
        lines = []
        for ref in sorted(references, key=lambda r: (sources[r.document_id].filename, r.start_line, r.end_line, r.excerpt)):
            lines += [f"Source: {source_link(ref.document_id)}; document ID: {escape(ref.document_id)}; "
                      f"normalized lines {ref.start_line}–{ref.end_line}.", ""]
            lines += ["> " + escape(line) for line in ref.excerpt.split("\n")]
            lines.append("")
        return lines

    lines = ["# Software Requirements Specification", "",
             "This document consolidates software requirements from the supplied corpus. "
             "Source locations refer to normalized extracted text, including normalized email bodies.", "",
             "## Document overview", "", f"- Input corpus: {escape(str(root))}",
             f"- Source documents: {len(documents)}", f"- Retained requirements: {len(requirements)}",
             f"- Discarded requirements: {len(result.blacklist)} "
             f"({sum(len(b.candidate_ids) for b in result.blacklist)} candidates)",
             f"- Review completion status: {state['completion_status']}",
             f"- Latest review: {review.status}",
             f"- Revision passes: {state['revision_count']} / {state['max_revisions']}", "",
             "## Priority scale", "", escape(PRIORITY_SCALE), "",
             "## Requirements", ""]
    if not requirements:
        lines += ["No retained requirements.", ""]
    for requirement in requirements:
        final_id = final_ids[requirement.internal_key]
        lines += [f"### {final_id} — {prose(requirement.name)}", "",
                  f"- Internal key: {escape(requirement.internal_key)}",
                  f"- Type: {requirement.kind.value}", f"- Priority: {requirement.priority.value}",
                  f"- Priority basis: {'inferred' if requirement.priority_inferred else 'explicitly specified'}",
                  f"- Priority rationale: {prose(requirement.priority_rationale)}",
                  "- Originating candidates: " + ", ".join(escape(key) for key in sorted(requirement.candidate_ids)), "",
                  prose(requirement.description), "", "Sources and evidence:", ""]
        lines += evidence(requirement.references)
    lines += ["## Glossary", ""]
    if result.glossary:
        lines += ["| Preferred term | Definition | Aliases |", "| --- | --- | --- |"]
        for entry in sorted(result.glossary, key=lambda g: (g.term.casefold(), g.term)):
            lines.append(f"| {escape(entry.term)} | {escape(entry.definition)} | "
                         f"{', '.join(escape(alias) for alias in sorted(entry.aliases)) or 'None'} |")
        lines.append("")
    else:
        lines += ["No glossary entries.", ""]
    lines += ["## Blacklist", "", "Merged duplicates are retained through lineage and are not rejections.", ""]
    for item in sorted(result.blacklist, key=lambda b: b.blacklist_id):
        lines += [f"### {escape(item.blacklist_id)}", "",
                  "- Original candidates: " + ", ".join(escape(c) for c in sorted(item.candidate_ids)),
                  "- Reason for rejection: " + prose(item.rejection_reason),
                  "- Related retained requirement: " + (final_ids[item.merged_into_key] if item.merged_into_key else "None"),
                  "", "Original statement:", "", escape(item.original_statement), ""]
        lines += evidence(item.references)
    if not result.blacklist:
        lines += ["No discarded requirements.", ""]
    lines += ["## Unresolved issues", ""]
    source_issues = [issue for issue in review.issues if not issue.actionable]
    quality_issues = [issue for issue in review.issues if issue.actionable]
    if not (source_issues or quality_issues or result.unresolved_conflicts or review.missing_candidates):
        lines += ["No unresolved issues remain.", ""]
    for title, issues in (("Source ambiguities requiring clarification", source_issues),
                          ("Quality defects remaining after the revision limit", quality_issues)):
        lines += [f"### {title}", ""]
        if not issues:
            lines += ["None.", ""]
        for issue in sorted(issues, key=lambda i: i.issue_id):
            targets = ", ".join(final_ids[key] for key in sorted(issue.affected_keys)) or "Corpus-wide"
            lines += [f"#### {escape(issue.issue_id)} ({issue.category})", "",
                      f"Requirements: {targets}", "",
                      "Candidates: " + (", ".join(escape(c) for c in sorted(issue.affected_candidate_ids)) or "None"), "",
                      prose(issue.explanation), "", "Requested action: " + prose(issue.requested_correction), ""]
            lines += evidence(issue.references)
    if result.unresolved_conflicts:
        lines += ["### Unresolved source conflicts", ""]
        for conflict in sorted(result.unresolved_conflicts, key=lambda c: c.conflict_id):
            lines += [f"- {escape(conflict.conflict_id)}: " + ", ".join(final_ids[key] for key in sorted(conflict.requirement_keys))
                      + ". " + prose(conflict.explanation), ""]
            lines += evidence(conflict.references)
    if review.missing_candidates:
        lines += ["### Coverage gaps remaining after the revision limit", ""]
        for candidate in sorted(review.missing_candidates, key=lambda c: c.candidate_id):
            lines += [f"- {escape(candidate.candidate_id)}: {escape(candidate.statement)}", ""]
            lines += evidence(candidate.references)
    lines += ["## Traceability summary", "", "| Requirement | Internal key | Candidates | Sources |", "| --- | --- | --- | --- |"]
    for requirement in requirements:
        source_ids = sorted({r.document_id for r in requirement.references}, key=lambda key: sources[key].filename)
        lines.append(f"| {final_ids[requirement.internal_key]} | {escape(requirement.internal_key)} | "
                     + ", ".join(escape(c) for c in sorted(requirement.candidate_ids)) + " | "
                     + ", ".join(source_link(key) for key in source_ids) + " |")
    lines += ["", "### Source inventory", ""]
    for document in sorted(documents, key=lambda d: d.filename):
        lines += [f"- {source_link(document.document_id)} — {escape(document.document_id)}"]
        for warning in document.warnings:
            lines += ["  - Loader warning: " + escape(warning)]
    lines.append("")
    return "\n".join(lines), final_ids


def document_formatter(state: GraphState) -> GraphState:
    try:
        target = (validate_output_path(state["input_directory"], state["output_path"],
                                       state.get("allow_output_in_corpus", False))
                  if state.get("output_path") else None)
        content, final_ids = render_document(state)
        if target is not None:
            atomic_write(target, content)
        return {"final_document": content, "final_requirement_ids": final_ids}
    except (ValidationError, KeyError) as exc:
        raise FormatterError("Document structural validation failed: invalid or missing fields") from None
    except (ValueError, OSError) as exc:
        raise FormatterError(f"Cannot generate requirements document: {exc}") from None
