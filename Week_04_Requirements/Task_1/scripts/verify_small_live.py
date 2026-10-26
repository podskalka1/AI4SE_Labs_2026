"""Explicit live verification on one or two copied source documents only.

Run from Task_1 after the minimal model probes. No credentials are recorded.
Artifacts and copied evidence stay together under the ignored output directory.
"""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

from openai import OpenAI

from requirements_refiner.config import Settings, load_settings
from requirements_refiner.graph import build_graph
from requirements_refiner.llm import StructuredLLM
from requirements_refiner.models import (
    CandidateDisposition, CandidateRequirement, DiscardedRequirement, GlossaryEntry,
    Requirement, ReviewIssue, ReviewResult, SourceDocument, UnresolvedConflict,
)
from requirements_refiner.validation import validate_candidates


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("data/corpus"))
    parser.add_argument("--document", action="append", required=True)
    parser.add_argument("--artifacts", type=Path, default=Path("output/live_6a"))
    parser.add_argument("--pause-after-extraction", action="store_true")
    parser.add_argument("--resume-artifacts", type=Path,
                        help="Resume only a failed refiner pass from a saved checkpoint")
    parser.add_argument("--refinement-feedback", default="",
                        help="Trusted deterministic diagnosis for the failed refinement response")
    args = parser.parse_args()
    names = sorted(set(args.document))
    if not 1 <= len(names) <= 2:
        parser.error("Select exactly one or two relative source filenames")
    original_root = args.input.resolve()
    artifacts = args.artifacts.resolve()
    if artifacts.exists():
        parser.error("Artifact directory already exists; choose a fresh path")
    selected = []
    for name in names:
        relative = Path(name)
        source = (original_root / relative).resolve()
        if relative.is_absolute() or not source.is_relative_to(original_root) or not source.is_file():
            parser.error("Selected document must be an existing corpus-relative file")
        selected.append((relative, source, hashlib.sha256(source.read_bytes()).hexdigest()))
    settings = load_settings()
    settings.validate_llm_configuration()
    settings = Settings.model_validate({**settings.model_dump(), "max_revisions": 1,
                                       "api_retries": 0, "extraction_attempts": 1,
                                       "request_timeout": 120})
    staged_root = artifacts / "corpus"
    for relative, source, digest in selected:
        destination = staged_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        assert hashlib.sha256(destination.read_bytes()).hexdigest() == digest
    client = OpenAI(api_key=settings.api_key.get_secret_value(), base_url=settings.base_url,
                    max_retries=0, timeout=settings.request_timeout)
    original_create = client.chat.completions.create
    calls = []

    def tracked(**kwargs):
        call = {"model": kwargs["model"], "number": len(calls) + 1}
        calls.append(call)
        print(f"API call {call['number']}: {call['model']}", flush=True)
        try:
            completion = original_create(**kwargs)
        except Exception as exc:
            call["error_type"] = type(exc).__name__
            # Never serialize SDK exceptions, request objects or headers.
            raise
        call["finish_reason"] = completion.choices[0].finish_reason
        call["tokens"] = completion.usage.total_tokens if completion.usage else None
        (artifacts / f"response_{call['number']:02d}.json").write_text(
            completion.model_dump_json(indent=2), encoding="utf-8")
        return completion

    client.chat.completions.create = tracked
    llm = StructuredLLM(settings, client=client)
    if args.refinement_feedback:
        generate = llm.generate
        def with_feedback(**kwargs):
            if kwargs["model"] == settings.refiner_model:
                kwargs["user_prompt"] += "\nDeterministic validation of the previous failed response: " + args.refinement_feedback
            return generate(**kwargs)
        llm.generate = with_feedback
    accumulated = {"input_directory": str(staged_root), "output_path": str(artifacts / "requirements.md")}
    if args.resume_artifacts:
        saved = json.loads((args.resume_artifacts / "checkpoint.json").read_text(encoding="utf-8"))
        classes = {"documents": SourceDocument, "candidates": CandidateRequirement,
                   "requirements": Requirement, "blacklist": DiscardedRequirement,
                   "dispositions": CandidateDisposition, "glossary": GlossaryEntry,
                   "unresolved_conflicts": UnresolvedConflict, "review_history": ReviewResult,
                   "unresolved_source_issues": ReviewIssue, "unresolved_quality_issues": ReviewIssue}
        for field, model in classes.items():
            if field in saved:
                accumulated[field] = [model.model_validate(item) for item in saved[field]]
        history = accumulated.get("review_history", [])
        accumulated.update(latest_review=history[-1] if history else None,
                           revision_count=len(history), max_revisions=1,
                           completion_status="pending", termination_reason=None)
        if accumulated["revision_count"] > 1:
            raise ValueError("Saved state exceeds the one-revision verification budget")
    graph = build_graph(settings, llm=llm, entry_point="refiner" if args.resume_artifacts else "loader")
    summary = {"selected_documents": names, "max_revisions": 1, "calls": calls, "status": "started"}
    try:
        for update in graph.stream(accumulated, stream_mode="updates"):
            for node, values in update.items():
                accumulated.update(values)
                print("Completed:", node, flush=True)
                snapshot = {key: [item.model_dump(mode="json") for item in value]
                            for key, value in accumulated.items()
                            if isinstance(value, list) and (not value or hasattr(value[0], "model_dump"))}
                (artifacts / "checkpoint.json").write_text(json.dumps(snapshot, indent=2, ensure_ascii=False), encoding="utf-8")
                if node == "extractor":
                    validate_candidates(values["candidates"], accumulated["documents"])
                    summary["extracted_candidates"] = len(values["candidates"])
                    print("Validated candidates:", len(values["candidates"]), flush=True)
                    for candidate in values["candidates"]:
                        print(json.dumps({"candidate_id": candidate.candidate_id, "statement": candidate.statement,
                                          "evidence": [r.model_dump(mode="json") for r in candidate.references]}, ensure_ascii=False), flush=True)
                    if not values["candidates"]:
                        raise RuntimeError("Live extraction returned no candidates")
                    if args.pause_after_extraction:
                        input("Extraction inspection checkpoint; press Enter to continue: ")
        summary.update(status="completed", review_status=str(accumulated["completion_status"]),
                       revision_count=accumulated["revision_count"] ,
                       retained_requirements=len(accumulated["requirements"]),
                       discarded_requirements=len(accumulated["blacklist"]),
                       models_used=sorted({call["model"] for call in calls}), structured_mode=llm.mode)
        print(json.dumps(summary, indent=2), flush=True)
    except Exception as exc:
        summary.update(status="failed", error_type=type(exc).__name__)
        print("Stopped:", type(exc).__name__, str(exc) if type(exc).__name__ == "LLMError" else "See saved response and checkpoint for diagnosis", flush=True)
        return 1
    finally:
        summary["original_sources_unchanged"] = all(hashlib.sha256(source.read_bytes()).hexdigest() == digest for _, source, digest in selected)
        (artifacts / "verification.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
        llm.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
