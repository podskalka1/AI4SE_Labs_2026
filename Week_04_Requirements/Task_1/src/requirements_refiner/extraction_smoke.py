"""Explicit opt-in live extraction of one to three selected corpus documents."""
import argparse

from .config import load_settings
from .llm import LLMError
from .nodes.extractor import requirements_extractor
from .nodes.loader import CorpusLoadError, load_corpus


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_directory")
    parser.add_argument("--document", action="append", required=True,
                        help="Exact relative filename; repeat for at most three documents")
    args = parser.parse_args()
    names = set(args.document)
    if not 1 <= len(names) <= 3:
        parser.error("Select between one and three documents")
    try:
        settings = load_settings()
        print(f"Selected model: {settings.extractor_model}")
        documents = load_corpus(args.input_directory)
        selected = [document for document in documents if document.filename in names]
        if len(selected) != len(names):
            raise ValueError("One or more selected relative filenames were not found")
        print(f"Selected documents: {len(selected)}")
        result = requirements_extractor({"documents": selected}, settings=settings)
        print(f"Candidate requirements: {len(result['candidates'])}")
        print("Errors: 0")
    except (LLMError, CorpusLoadError) as exc:
        print(f"Error: {exc}")
        return 1
    except ValueError:
        # Configuration validation errors can include input values; do not print them.
        print("Error: invalid configuration, document selection, or chunk size; check settings")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
