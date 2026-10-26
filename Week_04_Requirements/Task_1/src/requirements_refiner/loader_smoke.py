"""Loader-only diagnostic command; never constructs an API client."""
import argparse
import logging

from .nodes.loader import CorpusLoadError, load_corpus


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_directory")
    args = parser.parse_args()
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
    try:
        documents = load_corpus(args.input_directory)
    except CorpusLoadError as exc:
        logging.error("%s", exc)
        return 1
    print(f"Loaded files: {len(documents)}")
    print(f"Warnings: {sum(len(d.warnings) for d in documents)}")
    print("Errors: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
