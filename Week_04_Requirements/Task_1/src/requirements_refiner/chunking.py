"""Bounded, line-aligned chunks in the canonical evidence coordinate system."""
from dataclasses import dataclass

from .models import SourceDocument


@dataclass(frozen=True)
class DocumentChunk:
    document_id: str
    filename: str
    start_line: int
    end_line: int
    text: str

    @property
    def label(self) -> str:
        return f"{self.filename} lines {self.start_line}-{self.end_line}"


def chunk_document(document: SourceDocument, max_chars: int = 12000,
                   overlap_lines: int = 2) -> list[DocumentChunk]:
    if max_chars < 1 or overlap_lines < 0:
        raise ValueError("Chunk size must be positive and overlap nonnegative")
    lines = document.content.splitlines()
    for index, line in enumerate(lines, 1):
        if len(line) > max_chars:
            raise ValueError(f"{document.filename} line {index} exceeds chunk size; "
                             "increase EXTRACTION_CHUNK_SIZE (no text was truncated)")
    chunks = []
    start = 0
    while start < len(lines):
        end, size = start, 0
        while end < len(lines):
            added = len(lines[end]) + (1 if end > start else 0)
            if size + added > max_chars:
                break
            size += added
            end += 1
        # Prefer a paragraph boundary near the end without creating tiny chunks.
        if end < len(lines):
            boundaries = [i + 1 for i in range(start, end) if not lines[i].strip()
                          and i + 1 >= start + max(1, (end - start) * 3 // 4)]
            if boundaries:
                end = boundaries[-1]
        chunks.append(DocumentChunk(document.document_id, document.filename, start + 1,
                                    end, "\n".join(lines[start:end])))
        if end == len(lines):
            break
        next_start = max(start + 1, end - overlap_lines)
        # Overlap must leave room for at least one new line on the next pass.
        while next_start < end and len("\n".join(lines[next_start:end + 1])) > max_chars:
            next_start += 1
        start = next_start
    return chunks
