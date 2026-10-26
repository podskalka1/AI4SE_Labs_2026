"""Explicit budgeted full run, with persistent node snapshots and request reuse."""
import argparse
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace

from openai import OpenAI

from requirements_refiner.compact import CompactLLM
from requirements_refiner.llm import LLMError
from requirements_refiner.config import Settings, load_settings
from requirements_refiner.graph import build_graph, route_review
from requirements_refiner.models import CandidateRequirement, SourceDocument
from requirements_refiner.nodes.extractor import ExtractionResult
from requirements_refiner.output import atomic_write, validate_output_path
from requirements_refiner.run_support import MeteredRequests, decode_state, encode_state
from requirements_refiner.validation import validate_candidates


class FullRunLLM(CompactLLM):
    def __init__(self, settings, client, seed):
        super().__init__(settings, client=client)
        self.seed = seed
        self.seed_hits = 0

    def _request(self, model, messages, schema):
        response = super()._request(model, messages, schema)
        if response.choices and response.choices[0].finish_reason == "length":
            raise LLMError("Output limit reached; inspect cached response and adjust batching before retrying")
        return response

    def generate(self, **kwargs):
        output_type = kwargs["output_type"]
        if output_type is ExtractionResult:
            payload = json.loads(kwargs["user_prompt"])
            document_id = payload["document_id"]
            if document_id in self.seed:
                source, candidates = self.seed[document_id]
                if payload["start_line"] == 1 and payload["end_line"] == len(source.content.splitlines()):
                    result = ExtractionResult.model_validate({"candidates": [c.model_dump(exclude={"candidate_id"}) for c in candidates]})
                    kwargs["validate"](result)
                    self.seed_hits += 1
                    print(f"Reused validated extraction: {source.filename}", flush=True)
                    return result
        cap = {"RefinementResult": 96000, "WritingResult": 12000,
               "ReviewResult": 48000}.get(output_type.__name__, 24000)
        self.settings.max_output_tokens = cap
        return super().generate(**kwargs)


def run(settings: Settings, input_directory: Path, output_path: Path, run_directory: Path,
        allow_output_in_corpus: bool = False):
    args = SimpleNamespace(input=input_directory, output=output_path, run_directory=run_directory)
    settings.validate_llm_configuration()
    settings = Settings.model_validate({**settings.model_dump(), "max_revisions": min(settings.max_revisions, 3),
        "api_retries": 0, "extraction_attempts": 3, "request_timeout": 600})
    root = args.input.resolve()
    validate_output_path(root, args.output, allow_output_in_corpus)
    if args.run_directory.resolve().is_relative_to(root):
        raise ValueError("Recovery directory must be outside the source corpus")
    fingerprints = {path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                    for path in sorted(root.rglob("*")) if path.is_file()}
    identity = {"sources": fingerprints, "models": [settings.extractor_model, settings.refiner_model,
                settings.writer_model, settings.reviewer_model], "chunk_size": settings.chunk_size}
    directory = args.run_directory.resolve()
    directory.mkdir(parents=True, exist_ok=True)
    checkpoint = directory / "checkpoint.json"
    stage, state, sequence = "loader", {"input_directory": str(root), "output_path": str(args.output.resolve()),
                                       "allow_output_in_corpus": allow_output_in_corpus}, 0
    if checkpoint.exists():
        stored = json.loads(checkpoint.read_text(encoding="utf-8"))
        if stored["identity"] != identity:
            raise ValueError("Sources or model configuration changed; cannot reuse checkpoint")
        stage, state, sequence = stored["next_node"], decode_state(stored["state"]), stored["sequence"]
        if state.get("max_revisions", settings.max_revisions) != settings.max_revisions:
            raise ValueError("Saved revision budget differs from current configuration")
        if Path(state["output_path"]).resolve() != args.output.resolve():
            raise ValueError("Saved output path differs from current output argument")
        if stage == "END":
            print("Run already complete; preserving deliverables/checkpoints", flush=True)
            return 3 if state["completion_status"] == "incomplete_review" else 0
    seed = {}
    prior = Path("output/live_6a_retry/checkpoint.json")
    if prior.exists():
        old = json.loads(prior.read_text(encoding="utf-8"))
        candidates = [CandidateRequirement.model_validate(c) for c in old.get("candidates", [])]
        for value in old.get("documents", []):
            doc = SourceDocument.model_validate(value)
            original = root / doc.filename
            if original.is_file() and original.read_bytes().decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n") == doc.original_content.replace("\r\n", "\n").replace("\r", "\n"):
                selected = [c for c in candidates if all(r.document_id == doc.document_id for r in c.references)]
                validate_candidates(selected, [doc])
                seed[doc.document_id] = (doc, selected)
    client = OpenAI(api_key=settings.api_key.get_secret_value(), base_url=settings.base_url,
                    max_retries=0, timeout=600)
    meter = MeteredRequests(client, directory / "requests")
    client.chat.completions.create = meter
    llm = FullRunLLM(settings, client, seed)
    graph = build_graph(settings, llm=llm, entry_point=stage)
    try:
        for event in graph.stream(state, stream_mode="updates"):
            for node, update in event.items():
                state.update(update)
                sequence += 1
                next_node = {"loader": "extractor", "extractor": "refiner", "refiner": "writer",
                    "writer": "reviewer", "revise": "refiner", "complete": "formatter", "formatter": "END"}.get(node)
                if node == "reviewer":
                    next_node = route_review(state)
                record = {"identity": identity, "sequence": sequence, "next_node": next_node, "state": encode_state(state)}
                snapshot = directory / "snapshots" / f"{sequence:03d}_{node}.json"
                if snapshot.exists():
                    raise ValueError("Refusing to overwrite an existing successful snapshot")
                atomic_write(snapshot, json.dumps(record, ensure_ascii=False, indent=2))
                atomic_write(checkpoint, json.dumps(record, ensure_ascii=False, indent=2))
                print(f"Completed {node}: documents={len(state.get('documents', []))}, candidates={len(state.get('candidates', []))}, requirements={len(state.get('requirements', []))}, revisions={state.get('revision_count', 0)}", flush=True)
        summary = {"documents": len(state["documents"]), "candidates": len(state["candidates"]),
            "requirements": len(state["requirements"]), "blacklist": len(state["blacklist"]),
            "reviews": len(state["review_history"]), "revisions": state["revision_count"],
            "completion_status": str(state["completion_status"]), "api_calls": len(meter.calls),
            "input_tokens": sum(c.get("input_tokens", 0) for c in meter.calls),
            "output_tokens": sum(c.get("output_tokens", 0) for c in meter.calls),
            "estimated_eur_with_25pct_margin": meter.charged_estimate,
            "cache_hits_this_process": meter.cache_hits, "seed_hits_this_process": llm.seed_hits,
            "original_sources_unchanged": all(hashlib.sha256((root / name).read_bytes()).hexdigest() == value
                                               for name, value in fingerprints.items())}
        atomic_write(directory / "summary.json", json.dumps(summary, indent=2))
        print(json.dumps(summary, indent=2), flush=True)
        return 3 if state["completion_status"] == "incomplete_review" else 0
    finally:
        llm.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("data/corpus"))
    parser.add_argument("--output", type=Path, default=Path("output/requirements.md"))
    parser.add_argument("--run-directory", type=Path, default=Path("output/full_run"))
    args = parser.parse_args()
    return run(load_settings(), args.input, args.output, args.run_directory)


if __name__ == "__main__":
    raise SystemExit(main())
