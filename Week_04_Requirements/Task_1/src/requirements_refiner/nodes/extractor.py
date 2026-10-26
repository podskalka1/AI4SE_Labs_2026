"""First LLM node: chunk-local extraction with deterministic provenance checks."""
import json
from hashlib import sha256

from pydantic import Field

from ..chunking import DocumentChunk, chunk_document
from ..config import Settings, load_settings
from ..llm import LLMError, StructuredLLM
from ..models import (CandidateRequirement, Record, RequirementType, SourceDocument,
                      SourceReference, Text)
from ..prompts import EXTRACTION_SYSTEM_PROMPT
from ..state import GraphState


class SelectedReference(SourceReference):
    """The model selects coordinates; exact evidence text is application-owned.

    A supplied quotation remains supported and must validate without repairs.
    """
    excerpt: Text | None = None


class ExtractedCandidate(Record):
    statement: Text
    kind: RequirementType
    references: list[SelectedReference] = Field(min_length=1)
    extraction_note: Text | None = None


class ExtractionResult(Record):
    candidates: list[ExtractedCandidate]


def materialize_reference(reference: SelectedReference, document: SourceDocument) -> SourceReference:
    lines = document.content.splitlines()
    if reference.document_id != document.document_id or reference.end_line > len(lines):
        raise ValueError("Reference does not locate lines in this document")
    excerpt = reference.excerpt
    if excerpt is None:
        excerpt = "\n".join(lines[reference.start_line - 1:reference.end_line])
    result = SourceReference(**{**reference.model_dump(), "excerpt": excerpt})
    result.validate_against(document)
    return result


def validate_evidence(result: ExtractionResult, chunk: DocumentChunk,
                      documents: dict[str, SourceDocument]) -> None:
    for candidate in result.candidates:
        for reference in candidate.references:
            if reference.document_id not in documents:
                raise ValueError("Unknown source document ID")
            if (reference.document_id != chunk.document_id
                    or reference.start_line < chunk.start_line
                    or reference.end_line > chunk.end_line):
                raise ValueError("Evidence must refer to the supplied chunk")
            materialize_reference(reference, documents[reference.document_id])


def extract_requirements(documents: list[SourceDocument], settings: Settings,
                         llm: StructuredLLM) -> list[CandidateRequirement]:
    if not documents:
        raise ValueError("Extraction requires loaded documents")
    sources = {document.document_id: document for document in documents}
    if len(sources) != len(documents):
        raise ValueError("Document IDs must be unique")
    # Prepare all chunks first, so oversized lines fail before any API calls.
    chunks = [chunk for document in sorted(documents, key=lambda d: d.filename)
              for chunk in chunk_document(document, settings.chunk_size,
                                          settings.chunk_overlap_lines)]
    candidates = []
    seen_ids: set[str] = set()
    for chunk in chunks:
        numbered = "\n".join(f"{number}: {line}" for number, line in
                             enumerate(chunk.text.split("\n"), chunk.start_line))
        prompt = json.dumps({"document_id": chunk.document_id, "filename": chunk.filename,
                             "metadata": sources[chunk.document_id].metadata,
                             "start_line": chunk.start_line, "end_line": chunk.end_line,
                             "numbered_source": numbered}, ensure_ascii=False)
        try:
            result = llm.generate(
                model=settings.extractor_model, system_prompt=EXTRACTION_SYSTEM_PROMPT,
                user_prompt=prompt, output_type=ExtractionResult,
                validate=lambda output: validate_evidence(output, chunk, sources))
        except LLMError as exc:
            raise LLMError(f"{chunk.label}: {exc}") from None
        for draft in result.candidates:
            # Canonical reference ordering makes IDs independent of response order.
            references = sorted(set(materialize_reference(ref, sources[ref.document_id]).model_dump_json()
                                    for ref in draft.references))
            canonical = {**draft.model_dump(mode="json"),
                         "references": [json.loads(ref) for ref in references]}
            digest = sha256(json.dumps(canonical, sort_keys=True, ensure_ascii=False,
                                      separators=(",", ":")).encode("utf-8")).hexdigest()
            candidate_id = "CAND-" + digest
            # Only exact record duplicates caused by chunk overlap are coalesced.
            if candidate_id not in seen_ids:
                candidates.append(CandidateRequirement(candidate_id=candidate_id, **canonical))
                seen_ids.add(candidate_id)
    return sorted(candidates, key=lambda candidate: candidate.candidate_id)


def requirements_extractor(state: GraphState, *, settings: Settings | None = None,
                           llm: StructuredLLM | None = None) -> GraphState:
    if not state.get("documents"):
        raise ValueError("Extractor state requires loaded documents")
    settings = settings or load_settings()
    owned_client = llm is None
    llm = llm or StructuredLLM(settings)
    try:
        return {"candidates": extract_requirements(state["documents"], settings, llm)}
    finally:
        if owned_client:
            llm.close()
