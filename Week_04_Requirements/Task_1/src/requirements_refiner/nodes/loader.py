"""Recursive, deterministic corpus ingestion without LLM calls."""
import logging
import os
from email import policy
from email.parser import Parser
from hashlib import sha256
from pathlib import Path

from ..models import SourceDocument
from ..state import GraphState

logger = logging.getLogger(__name__)
SUPPORTED = {".txt", ".md", ".eml"}
EXCLUDED = {".git", ".venv", "venv", "env", "node_modules", "__pycache__",
            ".pytest_cache", ".uv-cache", "outputs", "output", "build", "dist"}


class CorpusLoadError(ValueError):
    """A supported source could not be loaded; no partial corpus is returned."""


def _normalize(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _email_text(raw: str) -> tuple[str, dict[str, str], list[str]]:
    message = Parser(policy=policy.default).parsestr(raw)
    metadata = {key.lower(): str(message[key]) for key in
                ("From", "To", "Subject", "Date", "Message-ID") if message[key]}
    warnings: list[str] = []

    def extract(part) -> str:
        warnings.extend(f"Email defect: {type(d).__name__}" for d in part.defects)
        if part.get_content_disposition() == "attachment" or part.get_filename():
            return ""
        if part.is_multipart():
            children = list(part.iter_parts())
            if part.get_content_subtype() == "alternative":
                plain = [p for p in children if p.get_content_type() == "text/plain"]
                children = plain[:1] if plain else children
            return "\n\n".join(filter(None, (extract(p) for p in children)))
        if part.get_content_type() != "text/plain":
            warnings.append(f"Skipped unsupported email body: {part.get_content_type()}")
            return ""
        payload = part.get_payload(decode=True)
        if payload is None:
            return str(part.get_payload())
        try:
            result = payload.decode(part.get_content_charset() or "utf-8", errors="strict")
        except (UnicodeError, LookupError) as exc:
            raise CorpusLoadError("Email body has invalid encoding or charset") from exc
        # Transfer decoding may discover additional defects.
        for defect in part.defects:
            warning = f"Email defect: {type(defect).__name__}"
            if warning not in warnings:
                warnings.append(warning)
        return result

    return _normalize(extract(message)), metadata, warnings


def load_corpus(input_directory: str | Path, *, output_path: str | Path | None = None
                ) -> list[SourceDocument]:
    root = Path(input_directory).resolve()
    if not root.is_dir():
        raise CorpusLoadError(f"Input directory does not exist or is not a directory: {root}")
    excluded_output = Path(output_path).resolve() if output_path else None
    paths: list[Path] = []

    def traversal_error(error: OSError) -> None:
        raise CorpusLoadError(f"Cannot traverse input directory: {error}") from error

    for current, directories, files in os.walk(root, onerror=traversal_error):
        directories[:] = sorted(d for d in directories if d.lower() not in EXCLUDED
                                and not (Path(current) / d).is_symlink())
        for name in files:
            path = Path(current) / name
            if path.suffix.lower() in SUPPORTED and path.resolve() != excluded_output:
                if path.is_symlink():
                    raise CorpusLoadError(f"Supported source is a symlink: {path}")
                paths.append(path)
    documents = []
    for path in sorted(paths, key=lambda p: p.relative_to(root).as_posix()):
        filename = path.relative_to(root).as_posix()
        try:
            raw = path.read_bytes().decode("utf-8-sig", errors="strict")
            content, metadata, warnings = (_email_text(raw) if path.suffix.lower() == ".eml"
                                           else (_normalize(raw), {}, []))
        except (OSError, UnicodeError, ValueError) as exc:
            raise CorpusLoadError(f"Cannot load supported source {filename}: {exc}") from exc
        if not content.strip():
            warnings.append("Document has no readable text")
        for warning in warnings:
            logger.warning("%s: %s", filename, warning)
        documents.append(SourceDocument(
            document_id="DOC-" + sha256(filename.encode("utf-8")).hexdigest(),
            filename=filename, original_content=raw, content=content,
            metadata=metadata, warnings=warnings,
        ))
    if not documents:
        raise CorpusLoadError(f"No supported documents found in {root}")
    logger.info("Loaded %d documents", len(documents))
    return documents


def corpus_loader(state: GraphState) -> GraphState:
    if "input_directory" not in state:
        raise CorpusLoadError("Graph state requires input_directory")
    return {"documents": load_corpus(state["input_directory"],
                                      output_path=state.get("output_path"))}
