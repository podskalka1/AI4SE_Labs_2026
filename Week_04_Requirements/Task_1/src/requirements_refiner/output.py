"""Output destination checks and atomic UTF-8 writes."""
import os
import tempfile
from pathlib import Path

from .nodes.loader import SUPPORTED


class OutputError(ValueError):
    """An output destination cannot be used safely."""


def validate_output_path(input_directory: str | Path, output_path: str | Path,
                         allow_inside: bool = False) -> Path:
    root = Path(input_directory).resolve()
    target = Path(output_path).resolve()
    if not root.is_dir():
        raise OutputError("Input directory does not exist or is not a directory")
    if target.is_dir():
        raise OutputError("Output path is a directory")
    if target.suffix.lower() != ".md":
        raise OutputError("Output path must have a .md extension")
    if target.is_relative_to(root):
        if not allow_inside:
            raise OutputError("Output inside the corpus requires --allow-output-in-corpus")
        # Do not guess whether an existing Markdown file is source or generated.
        if target.exists():
            raise OutputError("Refusing to overwrite an existing file inside the input corpus")
    if target.exists():
        # Also protect source files reached through a hard link outside the corpus.
        for source in root.rglob("*"):
            if source.suffix.lower() in SUPPORTED and source.is_file() and target.samefile(source):
                raise OutputError("Output refers to an input corpus document")
    return target


def atomic_write(target: Path, content: str) -> None:
    temporary: Path | None = None
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n",
                                         dir=target.parent, prefix=".requirements-refiner-",
                                         suffix=".tmp", delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, target)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
