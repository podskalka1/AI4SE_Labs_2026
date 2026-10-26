"""Presentation-only writing with deterministic authoritative metadata merge."""
import json

from ..config import Settings, load_settings
from ..llm import LLMError, StructuredLLM
from ..models import WritingResult
from ..prompts import WRITING_SYSTEM_PROMPT
from ..state import GraphState
from ..validation import unique, validate_writing


def requirements_writer(state: GraphState, *, settings: Settings | None = None,
                        llm: StructuredLLM | None = None) -> GraphState:
    if "requirements" not in state:
        raise ValueError("Writer state requires refined requirements")
    requirements = state["requirements"]
    unique((r.internal_key for r in requirements), "input requirement keys")
    if not requirements:
        return {"requirements": []}
    settings = settings or load_settings()
    payload = {
        "requirements": [r.model_dump(mode="json") for r in requirements],
        "glossary": [g.model_dump(mode="json") for g in state.get("glossary", [])],
        "unresolved_conflicts": [c.model_dump(mode="json") for c in state.get("unresolved_conflicts", [])],
    }
    owned_client = llm is None
    llm = llm or StructuredLLM(settings)
    try:
        result = llm.generate(
            model=settings.writer_model, system_prompt=WRITING_SYSTEM_PROMPT,
            user_prompt=json.dumps(payload, ensure_ascii=False), output_type=WritingResult,
            validate=lambda output: validate_writing(output, requirements), operation="Writing")
        written = {r.internal_key: r for r in result.requirements}
        return {"requirements": [r.model_copy(deep=True, update={
            "name": written[r.internal_key].name,
            "description": written[r.internal_key].description,
        }) for r in requirements]}
    except LLMError as exc:
        raise LLMError(f"Requirements writer: {exc}") from None
    finally:
        if owned_client:
            llm.close()
