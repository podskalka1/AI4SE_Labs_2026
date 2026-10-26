"""Compact model-facing records; authoritative provenance is restored locally.

All existing node validators still run on the reconstructed ordinary models.
No evidence is omitted: a reference catalog is sent once instead of per record.
"""
import json
import re
from collections import Counter
from hashlib import sha256
from typing import Annotated, Literal

from pydantic import Field

from .llm import StructuredLLM
from .models import (
    CandidateDisposition, CandidateRequirement, DiscardedRequirement, GlossaryEntry,
    Priority, Record, RefinementResult, Requirement, RequirementType, ReviewIssue,
    ReviewResult, ReviewStatus, SourceReference, Text, UnresolvedConflict,
    WrittenRequirement, WritingResult,
)


CandidateAlias = Annotated[str, Field(pattern=r"^c[0-9]{4,}$")]


class CompactRequirement(Record):
    key: Text
    candidate_ids: list[CandidateAlias] = Field(min_length=1)
    name: Text
    description: Text
    kind: RequirementType
    priority: Priority
    priority_rationale: Text
    priority_inferred: bool


class CompactRejection(Record):
    candidate_ids: list[CandidateAlias] = Field(min_length=1)
    reason: Text
    related_key: Text | None = None


class CompactConflict(Record):
    requirement_keys: list[Text] = Field(min_length=2)
    explanation: Text
    evidence_ids: list[Text] = Field(min_length=1)


class CompactRefinement(Record):
    requirements: list[CompactRequirement]
    rejected: list[CompactRejection]
    glossary: list[GlossaryEntry]
    conflicts: list[CompactConflict]


class CandidateBatch(Record):
    topic: Text
    candidate_ids: list[Text] = Field(min_length=1, max_length=36)


class RefinementPlan(Record):
    batches: list[CandidateBatch]


class LineSelection(Record):
    document_id: Text
    start_line: int = Field(ge=1)
    end_line: int = Field(ge=1)


class CompactIssue(Record):
    category: Literal["OS2", "OS3", "OS4", "OS5", "OS6", "OS7", "OS8", "OS9"]
    affected_keys: list[Text]
    affected_candidate_ids: list[Text]
    actionable: bool
    explanation: Text
    requested_correction: Text
    evidence_ids: list[Text] = Field(default_factory=list)
    source_selections: list[LineSelection] = Field(default_factory=list)


class CompactMissing(Record):
    candidate_id: Text
    statement: Text
    kind: RequirementType
    references: list[LineSelection] = Field(min_length=1)
    extraction_note: Text | None = None


class CompactReview(Record):
    status: ReviewStatus
    issues: list[CompactIssue]
    missing_candidates: list[CompactMissing]


def digest(value) -> str:
    return sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


class Catalog:
    def __init__(self, payload: dict):
        self.forward: dict[str, str] = {}
        groups = {"c": [], "r": [], "d": []}
        for c in payload.get("candidates", []):
            groups["c"].append(c["candidate_id"])
        for r in payload.get("previous_requirements", payload.get("requirements", [])):
            groups["r"].append(r["internal_key"])
        self.references: dict[str, dict] = {}

        def collect(value):
            if isinstance(value, dict):
                if set(("document_id", "start_line", "end_line", "excerpt")) <= set(value):
                    self.references[json.dumps(value, sort_keys=True)] = value
                    groups["d"].append(value["document_id"])
                if "document_id" in value and "content" in value:
                    groups["d"].append(value["document_id"])
                for child in value.values():
                    collect(child)
            elif isinstance(value, list):
                for child in value:
                    collect(child)
        collect(payload)
        for prefix, ids in groups.items():
            for index, identifier in enumerate(sorted(set(ids)), 1):
                self.forward[identifier] = f"{prefix}{index:04d}"
        self.reverse = {v: k for k, v in self.forward.items()}
        self.evidence = {f"e{index:04d}": reference for index, (_, reference) in
                         enumerate(sorted(self.references.items()), 1)}
        self.ref_ids = {json.dumps(ref, sort_keys=True): key for key, ref in self.evidence.items()}

    def pack(self, value):
        if isinstance(value, str):
            return self.forward.get(value, value)
        if isinstance(value, list):
            return [self.pack(v) for v in value]
        if isinstance(value, dict):
            result = {}
            for key, child in value.items():
                if key == "references":
                    result["evidence_ids"] = [self.ref_ids[json.dumps(ref, sort_keys=True)] for ref in child]
                elif key != "original_statement":
                    result[key] = self.pack(child)
            return result
        return value

    def expand_text(self, value: str) -> str:
        if not self.reverse:
            return value
        pattern = r"(?<![\w])(?:" + "|".join(map(re.escape, self.reverse)) + r")(?![\w])"
        return re.sub(pattern, lambda match: self.reverse[match.group()], value)

    def ref(self, identifier: str) -> SourceReference:
        if identifier not in self.evidence:
            raise ValueError("Unknown evidence identifier")
        return SourceReference.model_validate(self.evidence[identifier])

    def prompt(self, payload: dict, include_catalog=True, include_excerpts=True) -> str:
        result = self.pack(payload)
        if include_catalog:
            result["evidence_catalog"] = {key: {field: self.pack(value) for field, value in ref.items()
                                               if include_excerpts or field != "excerpt"}
                                          for key, ref in self.evidence.items()}
        return json.dumps(result, ensure_ascii=False, separators=(",", ":"))


def co_locate_duplicates(plan: RefinementPlan, payload: dict, catalog: Catalog) -> RefinementPlan:
    """Co-locate explicit reviewer duplicate targets; never merge their meanings."""
    expected = {catalog.forward[c["candidate_id"]] for c in payload["candidates"]}
    parent = {key: key for key in expected}
    previous = {r["internal_key"]: r["candidate_ids"] for r in payload.get("previous_requirements", [])}
    def find(key):
        while parent[key] != key:
            parent[key] = parent[parent[key]]
            key = parent[key]
        return key
    for issue in (payload.get("review") or {}).get("issues", []):
        if issue["category"] != "OS3" or not issue["actionable"]:
            continue
        ids = set(issue.get("affected_candidate_ids", []))
        for key in issue.get("affected_keys", []):
            ids.update(previous.get(key, []))
        aliases = sorted(catalog.forward[key] for key in ids if key in catalog.forward and catalog.forward[key] in expected)
        if 1 < len(aliases) <= 36:
            for key in aliases[1:]:
                parent[find(key)] = find(aliases[0])
    components = {}
    for key in sorted(expected):
        components.setdefault(find(key), []).append(key)
    forced = [keys for keys in components.values() if 1 < len(keys) <= 36]
    if not forced:
        return plan
    batches = []
    for keys in sorted(forced, key=lambda keys: (-len(keys), keys)):
        if not batches or len(batches[-1].candidate_ids) + len(keys) > 36:
            batches.append(CandidateBatch(topic="Reviewer-requested duplicate corrections", candidate_ids=list(keys)))
        else:
            batches[-1].candidate_ids.extend(keys)
    moved = {key for keys in forced for key in keys}
    for batch in plan.batches:
        remaining = [key for key in batch.candidate_ids if key not in moved]
        if remaining:
            batches.append(CandidateBatch(topic=batch.topic, candidate_ids=remaining))
    return RefinementPlan(batches=batches)


class CompactLLM(StructuredLLM):
    """Optional compact adapter; ordinary nodes/state/validators stay unchanged."""
    writer_batch_size = 20

    def generate(self, *, model, system_prompt, user_prompt, output_type, validate=None,
                 operation="Extraction"):
        if output_type not in {RefinementResult, WritingResult, ReviewResult}:
            return super().generate(model=model, system_prompt=system_prompt,
                user_prompt=user_prompt, output_type=output_type, validate=validate, operation=operation)
        payload = json.loads(user_prompt)
        catalog = Catalog(payload)
        if output_type is RefinementResult:
            if len(payload["candidates"]) > 36:
                return self._refine_batched(model, system_prompt, payload, catalog, validate, operation)
            return self._refine(model, system_prompt, payload, catalog, validate, operation)
        if output_type is WritingResult:
            return self._write(model, system_prompt, payload, catalog, validate, operation)
        return self._review(model, system_prompt, payload, catalog, validate, operation)

    def _refine_batched(self, model, system, payload, catalog, validate, operation):
        """Model-planned topical batches, followed by the unchanged global reviewer."""
        from .validation import reference_keys, unique
        candidates = {c["candidate_id"]: c for c in payload["candidates"]}
        expected = {catalog.forward[key] for key in candidates}
        plan_payload = {"candidates": [{"id": catalog.forward[c["candidate_id"]],
            "statement": c["statement"], "kind": c["kind"]} for c in payload["candidates"]],
            "review_feedback": catalog.pack(payload.get("review")),
            "previous_groups": [{"key": catalog.forward.get(r["internal_key"], r["internal_key"]),
                                  "candidate_ids": [catalog.forward[c] for c in r["candidate_ids"]]}
                                 for r in payload.get("previous_requirements", [])]}

        def check_plan(plan):
            ids = [key for batch in plan.batches for key in batch.candidate_ids]
            counts = Counter(ids)
            missing, unknown = sorted(expected - set(ids)), sorted(set(ids) - expected)
            repeats = sorted(key for key, count in counts.items() if count != 1)
            if missing or unknown or repeats:
                raise ValueError(f"Partition must cover each candidate once; missing={missing[:12]}, unknown={unknown[:3]}, repeated={repeats[:3]}")
        previous_cap = self.settings.max_output_tokens
        self.settings.max_output_tokens = 16000
        try:
            plan = super().generate(model=model,
                system_prompt="""Partition ALL supplied software requirement candidates into topical processing batches.
Do not refine, merge, reject or summarize candidates in this planning step. Each
candidate ID must occur exactly once, as an individual ID (never ID ranges).
Each batch has at most 36 candidates. Co-locate semantic duplicates and competing
requirements where possible; use reviewer feedback to co-locate issues needing
joint correction. Different topics remain separate. A batch is NOT a requirement:
its contents will be refined into distinct, atomic requirements in the next step.
Return only the supplied JSON schema.""",
                user_prompt=json.dumps(plan_payload, ensure_ascii=False, separators=(",", ":")),
                output_type=RefinementPlan, validate=check_plan, operation="Refinement planning")
            plan = co_locate_duplicates(plan, payload, catalog)
            check_plan(plan)
            combined = RefinementResult(requirements=[], blacklist=[], dispositions=[], glossary=[], unresolved_conflicts=[])
            terms = {g["term"].casefold(): GlossaryEntry.model_validate(g) for g in payload.get("glossary", [])}
            for index, batch in enumerate(plan.batches, 1):
                ids = {catalog.reverse[key] for key in batch.candidate_ids}
                local = {**payload, "candidates": [candidates[key] for key in sorted(ids)],
                    "previous_requirements": [r for r in payload.get("previous_requirements", []) if set(r["candidate_ids"]) <= ids],
                    "previous_blacklist": [b for b in payload.get("previous_blacklist", []) if set(b["candidate_ids"]) <= ids],
                    "glossary": [g.model_dump(mode="json") for g in terms.values()],
                    "unresolved_conflicts": [], "batch_topic": batch.topic}
                # Missing candidates were incorporated before planning. Repeating
                # their global records in every batch invites duplicate assignment.
                feedback = payload.get("review") or {}
                previous_groups = {r["internal_key"]: set(r["candidate_ids"])
                                   for r in payload.get("previous_requirements", [])}
                projected = []
                for issue in feedback.get("issues", []):
                    target_ids = set(issue.get("affected_candidate_ids", []))
                    for key in issue.get("affected_keys", []):
                        target_ids.update(previous_groups.get(key, set()))
                    if target_ids and not target_ids.intersection(ids):
                        continue
                    projected.append({**{field: issue[field] for field in
                        ("category", "actionable", "explanation", "requested_correction")},
                        "affected_candidate_ids": sorted(target_ids.intersection(ids))})
                local["review"] = {"issues": projected, "missing_candidates": []}
                print(f"Refiner batch {index}/{len(plan.batches)}: {len(ids)} candidates; {batch.topic}", flush=True)

                def check_local(result):
                    unique((r.internal_key for r in result.requirements), "batch requirement keys")
                    memberships = Counter(c for record in [*result.requirements, *result.blacklist] for c in record.candidate_ids)
                    if set(memberships) != ids or any(count != 1 for count in memberships.values()):
                        aliases = {key: f"c{number:04d}" for number, key in enumerate(sorted(ids), 1)}
                        repeated = [aliases.get(key, key) for key, count in memberships.items() if count > 1]
                        missing = [aliases[key] for key in sorted(ids - set(memberships))]
                        raise ValueError(f"Each candidate must occur once ACROSS requirements and rejected, not in both. Duplicated={repeated[:10]}; missing={missing[:10]}. Choose retained OR rejected using evidence.")
                    lookup = {r.internal_key: r for r in result.requirements}
                    for conflict in result.unresolved_conflicts:
                        if not set(conflict.requirement_keys) <= set(lookup):
                            raise ValueError("Unknown conflict requirement in batch")
                        evidence = set().union(*(reference_keys(lookup[key].references) for key in conflict.requirement_keys))
                        if not reference_keys(conflict.references) <= evidence:
                            raise ValueError("Conflict evidence must belong to its competing requirements")
                self.settings.max_output_tokens = 24000
                part = self._refine(model, system + "\nThis is one bounded topic batch. Produce DISTINCT atomic, testable requirements; never an omnibus requirement merely describing the batch topic. No candidate ranges or raw hashes. Only the supplied batch candidates may be assigned. Reviewer-discovered candidates are already incorporated and allocated by the planner; never add them a second time. Do not infer that everything in this batch is a duplicate.",
                    local, Catalog(local), check_local, operation)
                local_previous_keys = {r["internal_key"] for r in local["previous_requirements"]}
                mapping = {r.internal_key: r.internal_key if r.internal_key in local_previous_keys
                           else f"batch{index}/{r.internal_key}" for r in part.requirements}
                for r in part.requirements:
                    r.internal_key = mapping[r.internal_key]
                for disposition in part.dispositions:
                    if disposition.requirement_key:
                        disposition.requirement_key = mapping[disposition.requirement_key]
                for rejected in part.blacklist:
                    if rejected.merged_into_key:
                        rejected.merged_into_key = mapping[rejected.merged_into_key]
                for conflict in part.unresolved_conflicts:
                    conflict.requirement_keys = [mapping[key] for key in conflict.requirement_keys]
                    conflict.conflict_id = f"batch{index}/" + conflict.conflict_id
                for term in part.glossary:
                    old = terms.get(term.term.casefold())
                    if old:
                        term.aliases = sorted(set(old.aliases + term.aliases))
                    terms[term.term.casefold()] = term
                combined.requirements.extend(part.requirements)
                combined.blacklist.extend(part.blacklist)
                combined.dispositions.extend(part.dispositions)
                combined.unresolved_conflicts.extend(part.unresolved_conflicts)
            combined.glossary = list(terms.values())
            if validate:
                validate(combined)
            return combined
        finally:
            self.settings.max_output_tokens = previous_cap

    def _refine(self, model, system, payload, catalog, validate, operation):
        candidates = {c["candidate_id"]: c for c in payload["candidates"]}

        def expand(result: CompactRefinement) -> RefinementResult:
            requirements, blacklist, dispositions = [], [], []
            keys = {r.key: catalog.reverse.get(r.key, r.key) for r in result.requirements}
            for draft in result.requirements:
                ids = [catalog.reverse.get(key, key) for key in draft.candidate_ids]
                if any(key not in candidates for key in ids):
                    raise ValueError("Unknown candidate identifier")
                refs = {json.dumps(ref, sort_keys=True): ref for key in ids for ref in candidates[key]["references"]}
                requirement = Requirement(internal_key=keys[draft.key], candidate_ids=ids,
                    name=catalog.expand_text(draft.name), description=catalog.expand_text(draft.description),
                    kind=draft.kind, priority=draft.priority, priority_rationale=draft.priority_rationale,
                    priority_inferred=draft.priority_inferred,
                    references=[SourceReference.model_validate(ref) for _, ref in sorted(refs.items())])
                requirements.append(requirement)
                representative = min(ids)
                dispositions.extend(CandidateDisposition(candidate_id=key,
                    status="retained" if key == representative else "merged",
                    requirement_key=requirement.internal_key) for key in ids)
            for draft in result.rejected:
                ids = [catalog.reverse.get(key, key) for key in draft.candidate_ids]
                if any(key not in candidates for key in ids):
                    raise ValueError("Unknown rejected candidate")
                related = keys.get(draft.related_key) if draft.related_key else None
                if draft.related_key and related is None:
                    raise ValueError("Unknown related requirement")
                refs = {json.dumps(ref, sort_keys=True): ref for key in ids for ref in candidates[key]["references"]}
                rejected = DiscardedRequirement(blacklist_id="BL-" + digest(sorted(ids)), candidate_ids=ids,
                    original_statement="\n\n".join(candidates[key]["statement"] for key in ids),
                    rejection_reason=catalog.expand_text(draft.reason), merged_into_key=related,
                    references=[SourceReference.model_validate(ref) for _, ref in sorted(refs.items())])
                blacklist.append(rejected)
                dispositions.extend(CandidateDisposition(candidate_id=key, status="discarded",
                                    blacklist_id=rejected.blacklist_id) for key in ids)
            conflicts = []
            for conflict in result.conflicts:
                if any(key not in keys for key in conflict.requirement_keys):
                    raise ValueError("Unknown competing requirement")
                targets = [keys[key] for key in conflict.requirement_keys]
                conflicts.append(UnresolvedConflict(conflict_id="CONFLICT-" + digest(targets),
                    requirement_keys=targets, explanation=catalog.expand_text(conflict.explanation),
                    references=[catalog.ref(key) for key in conflict.evidence_ids]))
            return RefinementResult(requirements=requirements, blacklist=blacklist,
                dispositions=dispositions, glossary=result.glossary, unresolved_conflicts=conflicts)

        def check(result):
            expanded = expand(result)
            if validate:
                validate(expanded)
        extra = """\nWIRE FORMAT OVERRIDE: Use the supplied compact schema. Alias c#### means a
candidate, r#### an existing requirement, d#### a document, and e#### exact evidence.
Requirement key can be an existing r#### or a unique new key. Every candidate must
belong to exactly one requirement group or rejected group, never both. Return all
groups, even unchanged ones during revision. Do NOT output dispositions, original
statements or source quotations: the application reconstructs the ledger and exact
union of candidate evidence deterministically. 'rejected' contains only genuine
rejections with reasons, not merged duplicates. 'conflicts' must select evidence_ids
belonging to their listed requirements. Preserve all meaning and original evidence.
Reviewer-requested new detail must be associated with its relevant original candidate;
do not assign one candidate to multiple groups. Unsupported wording can be corrected
without rejecting the supported intent. Use the glossary and full reviewer feedback.
"""
        result = super().generate(model=model, system_prompt=system + extra,
            user_prompt=catalog.prompt(payload), output_type=CompactRefinement,
            validate=check, operation=operation)
        return expand(result)

    def _write(self, model, system, payload, catalog, validate, operation):
        output = []
        for start in range(0, len(payload["requirements"]), self.writer_batch_size):
            batch = payload["requirements"][start:start + self.writer_batch_size]
            # The writer edits prose only; provenance/priority remain in authoritative state.
            compact = {"requirements": [{"internal_key": catalog.forward[r["internal_key"]],
                        "name": r["name"], "description": r["description"]} for r in batch],
                       "glossary": payload.get("glossary", []),
                       "unresolved_conflicts": catalog.pack(payload.get("unresolved_conflicts", []))}
            expected = {r["internal_key"] for r in batch}
            def check(result):
                actual = [catalog.reverse.get(r.internal_key, r.internal_key) for r in result.requirements]
                if len(actual) != len(set(actual)) or set(actual) != expected:
                    raise ValueError("Writer batch keys must match exactly")
            result = super().generate(model=model, system_prompt=system,
                user_prompt=json.dumps(compact, ensure_ascii=False, separators=(",", ":")),
                output_type=WritingResult, validate=check, operation=operation)
            output.extend(WrittenRequirement(internal_key=catalog.reverse.get(r.internal_key, r.internal_key),
                          name=catalog.expand_text(r.name), description=catalog.expand_text(r.description))
                          for r in result.requirements)
        result = WritingResult(requirements=output)
        if validate:
            validate(result)
        return result

    def _review(self, model, system, payload, catalog, validate, operation):
        sources = {d["document_id"]: d for d in payload["documents"]}
        prompt_payload = {**payload, "documents": [{**d, "content": "\n".join(
            f"{index}: {line}" for index, line in enumerate(d["content"].splitlines(), 1))}
            for d in payload["documents"]]}

        def selection(ref):
            document_id = catalog.reverse.get(ref.document_id, ref.document_id)
            if document_id not in sources:
                raise ValueError("Unknown review source")
            lines = sources[document_id]["content"].splitlines()
            if ref.end_line < ref.start_line or ref.end_line > len(lines):
                raise ValueError("Invalid review source range")
            return SourceReference(document_id=document_id, start_line=ref.start_line,
                end_line=ref.end_line, excerpt="\n".join(lines[ref.start_line - 1:ref.end_line]))

        def expand(result):
            issues = [ReviewIssue(issue_id=f"review-{index}", category=i.category,
                affected_keys=[catalog.reverse.get(key, key) for key in i.affected_keys],
                affected_candidate_ids=[catalog.reverse.get(key, key) for key in i.affected_candidate_ids],
                actionable=i.actionable, explanation=catalog.expand_text(i.explanation),
                requested_correction=catalog.expand_text(i.requested_correction),
                references=[catalog.ref(key) for key in i.evidence_ids] + [selection(ref) for ref in i.source_selections])
                for index, i in enumerate(result.issues, 1)]
            missing = [CandidateRequirement(candidate_id=c.candidate_id, statement=c.statement,
                kind=c.kind, references=[selection(ref) for ref in c.references],
                extraction_note=c.extraction_note) for c in result.missing_candidates]
            return ReviewResult(status=result.status, issues=issues, missing_candidates=missing)

        def check(result):
            expanded = expand(result)
            if validate:
                validate(expanded)
        extra = """\nWIRE FORMAT OVERRIDE: Use compact schema and supplied aliases (c####,
r####, d####, e####). The full original corpus is supplied; review ALL of it for
coverage, including facts missed in extraction. Existing exact evidence is supplied
once in evidence_catalog; cite its IDs. For new evidence use source_selections with
document_id and one-based normalized line ranges; application copies exact lines.
Each issue has evidence_ids and source_selections (empty arrays when not applicable).
Original source content is prefixed by its one-based line number; these prefixes
are not part of evidence text. Missing candidates select the displayed line ranges.
Do not invent IDs. The application assigns stable issue and new candidate IDs.
Assess every known unresolved conflict explicitly, preserving source ambiguities
as non-actionable; all genuinely correctable quality defects stay actionable.
"""
        result = super().generate(model=model, system_prompt=system + extra,
            user_prompt=catalog.prompt(prompt_payload, include_excerpts=False), output_type=CompactReview,
            validate=check, operation=operation)
        return expand(result)
