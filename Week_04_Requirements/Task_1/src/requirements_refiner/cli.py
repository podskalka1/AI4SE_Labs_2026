"""Command-line execution of the complete requirements refinement network."""
import argparse
import logging
import sys
from pathlib import Path

from pydantic import ValidationError

from .config import Settings, load_settings
from .graph import build_graph
from .models import CompletionStatus
from .output import validate_output_path


def nonnegative(value: str) -> int:
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("Must be an integer") from None
    if number < 0:
        raise argparse.ArgumentTypeError("Must be nonnegative")
    return number


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Generate a traceable Markdown requirements document using LangGraph.")
    result.add_argument("input_directory", type=Path, help="Corpus directory (.txt, .md, .eml; searched recursively)")
    result.add_argument("--output", type=Path, required=True, help="Destination Markdown file")
    result.add_argument("--env-file", type=Path, default=Path(".env"), help="Optional dotenv file (default: .env)")
    result.add_argument("--max-revisions", type=nonnegative, help="Revision passes after the initial review (default: configuration or 3)")
    result.add_argument("--run-directory", type=Path,
                        help="Enable compact, cached, budgeted full-run mode; store recovery files here")
    for role in ("extractor", "refiner", "writer", "reviewer"):
        result.add_argument(f"--{role}-model", help=f"Override configured {role} model")
    result.add_argument("--allow-output-in-corpus", action="store_true", help="Permit a NEW output file inside the corpus; it is excluded from ingestion")
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
    try:
        target = validate_output_path(args.input_directory, args.output, args.allow_output_in_corpus)
        settings = load_settings(args.env_file)
        overrides = {field: getattr(args, field) for field in (
            "max_revisions", "extractor_model", "refiner_model", "writer_model", "reviewer_model")
                     if getattr(args, field) is not None}
        settings = Settings.model_validate({**settings.model_dump(), **overrides})
        settings.validate_llm_configuration()
        if args.run_directory:
            from .full_run import run
            return run(settings, args.input_directory, target, args.run_directory, args.allow_output_in_corpus)
        graph = build_graph(settings)
        final = None
        source_count = discarded_count = 0
        for update in graph.stream({"input_directory": str(args.input_directory.resolve()),
                                    "output_path": str(target),
                                    "allow_output_in_corpus": args.allow_output_in_corpus}, stream_mode="updates"):
            for node, values in update.items():
                print(f"Completed: {node}")
                if "documents" in values:
                    source_count = len(values["documents"])
                if "blacklist" in values:
                    discarded_count = len(values["blacklist"])
                if node == "complete":
                    final = values["completion_status"]
                if node == "formatter":
                    print(f"Sources: {source_count}; retained requirements: {len(values['final_requirement_ids'])}; "
                          f"discarded requirements: {discarded_count}; review status: {final}")
        print(f"Output: {target}")
        return 3 if final == CompletionStatus.INCOMPLETE_REVIEW else 0
    except ValidationError:
        print("Error: invalid configuration or structured data; check environment and overrides", file=sys.stderr)
        return 2
    except (ValueError, OSError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("Execution interrupted", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
