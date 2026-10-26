"""Persistent request cache, usage reservations and complete state checkpoints."""
import json
from hashlib import sha256
from pathlib import Path

from openai.types.chat import ChatCompletion

from .models import (
    CandidateDisposition, CandidateRequirement, DiscardedRequirement, GlossaryEntry,
    Requirement, ReviewIssue, ReviewResult, SourceDocument, UnresolvedConflict,
)
from .output import atomic_write

# Standard USD prices per million tokens, verified 2026-10-25 on OpenAI model pages.
PRICES = {"gpt-5-mini": (0.25, 2.0), "gpt-5.6-luna": (0.20, 1.20),
          "gpt-5.4-nano": (0.20, 1.25), "gpt-6-luna": (0.10, 0.50)}
USD_PER_EUR = 1.1193  # ECB reference rate 2026-10-23; estimate, not card billing FX.


class BudgetExceeded(RuntimeError):
    pass


class MeteredRequests:
    """Serial execution only. Cache keys exclude output cap but retain semantic input.

    Only stop-completed responses can be replayed under another output cap. Every
    actual call is reserved on disk before sending, including a safety margin.
    Reservations survive uncertain connection failures rather than assuming free use.
    """
    def __init__(self, client, directory: Path, ceiling_eur=30.0):
        self.client = client
        self.original_create = client.chat.completions.create
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.ceiling = ceiling_eur
        self.path = self.directory / "usage.json"
        self.calls = json.loads(self.path.read_text(encoding="utf-8")) if self.path.exists() else []
        self.cache_hits = 0

    def save(self):
        atomic_write(self.path, json.dumps(self.calls, indent=2))

    @property
    def charged_estimate(self):
        return sum(call.get("estimated_eur", call["reserved_eur"]) for call in self.calls)

    def __call__(self, **kwargs):
        model = kwargs["model"]
        if model not in PRICES:
            raise BudgetExceeded("No verified pricing for configured model; refusing unbounded request")
        semantic = {k: v for k, v in kwargs.items() if k not in {"max_tokens", "max_completion_tokens"}}
        key = sha256(json.dumps(semantic, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        cache = self.directory / f"{key}.json"
        if cache.exists():
            result = ChatCompletion.model_validate_json(cache.read_text(encoding="utf-8"))
            if result.choices and result.choices[0].finish_reason == "stop":
                self.cache_hits += 1
                print(f"Cache hit: {model}", flush=True)
                return result
        # Conservative upper token estimate: one token per UTF-8 byte plus protocol
        # headroom. A further factor of two covers long-context input pricing.
        input_upper = len(json.dumps(kwargs, ensure_ascii=False).encode("utf-8")) + 4096
        output_upper = kwargs.get("max_completion_tokens", kwargs.get("max_tokens", 0))
        if not output_upper:
            raise BudgetExceeded("Missing bounded output allowance")
        window = 400000 if model in {"gpt-5-mini", "gpt-5.4-nano"} else 1050000
        if input_upper + output_upper > window:
            raise BudgetExceeded("Conservative input/output bound exceeds model context; inspect checkpoint before retrying")
        input_price, output_price = PRICES[model]
        reserve = (input_upper * input_price * 2 + output_upper * output_price * 1.5) / 1e6 / USD_PER_EUR * 1.25
        if self.charged_estimate + reserve > self.ceiling:
            raise BudgetExceeded(f"Next request could exceed EUR {self.ceiling:.2f}; stopped before sending")
        call = {"model": model, "cache_key": key, "reserved_eur": reserve,
                "input_token_upper": input_upper, "output_token_upper": output_upper}
        self.calls.append(call)
        self.save()
        print(f"API call {len(self.calls)}: {model}; reserve EUR {reserve:.4f}; cumulative estimate EUR {self.charged_estimate:.4f}", flush=True)
        try:
            response = self.original_create(**kwargs)
        except Exception as exc:
            call["error_type"] = type(exc).__name__
            self.save()
            raise
        if response.usage:
            inp, out = response.usage.prompt_tokens, response.usage.completion_tokens
            multiplier = 2 if inp > 272000 else 1
            output_multiplier = 1.5 if inp > 272000 else 1
            call.update(input_tokens=inp, output_tokens=out,
                estimated_usd=(inp * input_price * multiplier + out * output_price * output_multiplier) / 1e6)
            call["estimated_eur"] = call["estimated_usd"] / USD_PER_EUR * 1.25
        call["finish_reason"] = response.choices[0].finish_reason if response.choices else "empty"
        self.save()
        # Keep immutable attempt records as well as the latest replayable completion.
        history = self.directory / "attempts" / f"{len(self.calls):05d}.json"
        if not history.exists():
            atomic_write(history, response.model_dump_json(indent=2))
        replace_cache = not cache.exists()
        if cache.exists():
            old = ChatCompletion.model_validate_json(cache.read_text(encoding="utf-8"))
            replace_cache = not old.choices or old.choices[0].finish_reason != "stop"
            if replace_cache:
                preserved = self.directory / "attempts" / f"previous-{key}.json"
                if not preserved.exists():
                    atomic_write(preserved, cache.read_text(encoding="utf-8"))
        if replace_cache:
            atomic_write(cache, response.model_dump_json(indent=2))
        return response


MODEL_LISTS = {"documents": SourceDocument, "candidates": CandidateRequirement,
    "requirements": Requirement, "blacklist": DiscardedRequirement,
    "dispositions": CandidateDisposition, "glossary": GlossaryEntry,
    "unresolved_conflicts": UnresolvedConflict, "review_history": ReviewResult,
    "unresolved_source_issues": ReviewIssue, "unresolved_quality_issues": ReviewIssue}


def encode_state(state):
    result = dict(state)
    for field in MODEL_LISTS:
        if field in state:
            result[field] = [item.model_dump(mode="json") for item in state[field]]
    if state.get("latest_review"):
        result["latest_review"] = state["latest_review"].model_dump(mode="json")
    return result


def decode_state(value):
    result = dict(value)
    for field, model in MODEL_LISTS.items():
        if field in value:
            result[field] = [model.model_validate(item) for item in value[field]]
    if value.get("latest_review"):
        result["latest_review"] = ReviewResult.model_validate(value["latest_review"])
    return result
