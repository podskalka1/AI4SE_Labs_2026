"""Reusable synchronous OpenAI-compatible structured generation boundary."""
import json
import logging
from collections.abc import Callable
from typing import TypeVar

from openai import (APIConnectionError, APIStatusError, APITimeoutError,
                    AuthenticationError, BadRequestError, NotFoundError,
                    OpenAI, PermissionDeniedError, RateLimitError)
from pydantic import BaseModel, ValidationError

from .config import Settings

logger = logging.getLogger(__name__)
T = TypeVar("T", bound=BaseModel)


class LLMError(RuntimeError):
    """Sanitized API or structured-generation failure."""


def _strict_schema(schema: dict) -> dict:
    """Make Pydantic defaults explicit required fields for strict JSON schemas."""
    def visit(value):
        if isinstance(value, dict):
            value.pop("default", None)
            if value.get("type") == "object":
                value["additionalProperties"] = False
                value["required"] = list(value.get("properties", {}))
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)
    visit(schema)
    return schema


def _format_unsupported(error: BadRequestError) -> bool:
    body = error.body if isinstance(error.body, dict) else {}
    details = body.get("error", body)
    if not isinstance(details, dict):
        return False
    message = str(details.get("message", "")).lower()
    parameter = str(details.get("param", "")).lower()
    return ("response_format" in parameter or "response_format" in message
            or "json_schema" in message or "json_object" in message) and (
                "unsupported" in message or "not supported" in message
                or details.get("code") == "unsupported_parameter")


class StructuredLLM:
    def __init__(self, settings: Settings, client=None):
        self.settings = settings
        if client is None:
            if settings.api_key is None or not settings.api_key.get_secret_value().strip():
                raise LLMError("OPENAI_API_KEY is required for LLM stages")
            client = OpenAI(api_key=settings.api_key.get_secret_value(),
                            base_url=settings.base_url, timeout=settings.request_timeout,
                            max_retries=settings.api_retries)
        self.client = client
        self.mode = "json_schema" if settings.output_mode == "auto" else settings.output_mode

    def close(self) -> None:
        self.client.close()

    def _request(self, model: str, messages: list[dict], schema: dict):
        while True:
            options = {"model": model, "messages": messages,
                       self.settings.output_token_parameter: self.settings.max_output_tokens}
            if self.mode == "json_schema":
                options["response_format"] = {"type": "json_schema", "json_schema": {
                    "name": "structured_result", "strict": True, "schema": schema}}
            elif self.mode == "json_object":
                options["response_format"] = {"type": "json_object"}
            try:
                return self.client.chat.completions.create(**options)
            except BadRequestError as exc:
                if (self.settings.output_mode == "auto" and self.mode != "text"
                        and _format_unsupported(exc)):
                    self.mode = "json_object" if self.mode == "json_schema" else "text"
                    logger.warning("Endpoint rejected structured format; using %s with local validation",
                                   self.mode)
                    continue
                raise LLMError("API rejected request: check model, schema, and endpoint parameters") from None
            except AuthenticationError:
                raise LLMError("API authentication failed; check OPENAI_API_KEY") from None
            except PermissionDeniedError:
                raise LLMError("API permission denied for configured model or endpoint") from None
            except NotFoundError:
                raise LLMError("Configured model or API route was not found; check model and OPENAI_BASE_URL") from None
            except RateLimitError:
                raise LLMError("API rate limit or quota exhausted after bounded SDK retries") from None
            except APITimeoutError:
                raise LLMError("API request timed out after bounded SDK retries") from None
            except APIConnectionError:
                raise LLMError("API connection failed after bounded SDK retries") from None
            except APIStatusError as exc:
                raise LLMError(f"API request failed with HTTP {exc.status_code}") from None

    def generate(self, *, model: str, system_prompt: str, user_prompt: str,
                 output_type: type[T], validate: Callable[[T], None] | None = None,
                 operation: str = "Extraction") -> T:
        schema = _strict_schema(output_type.model_json_schema())
        messages = [{"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt + "\nJSON schema:\n" +
                     json.dumps(schema, ensure_ascii=False)}]
        reason = "invalid response"
        for attempt in range(self.settings.extraction_attempts):
            validation_detail = ""
            response = self._request(model, messages, schema)
            if not response.choices:
                reason = "empty response choices"
            else:
                choice = response.choices[0]
                if getattr(choice.message, "refusal", None) or choice.finish_reason == "content_filter":
                    raise LLMError(f"Model refused {operation.lower()} or content was filtered")
                if choice.finish_reason != "stop":
                    reason = "truncated response" if choice.finish_reason == "length" else "unsuccessful response"
                elif not choice.message.content or not choice.message.content.strip():
                    reason = "empty response content"
                else:
                    try:
                        result = output_type.model_validate_json(choice.message.content)
                        if validate:
                            validate(result)
                        return result
                    except ValidationError:
                        reason = "invalid JSON or schema validation failure"
                    except ValueError as exc:
                        reason = ("invalid evidence reference" if operation == "Extraction"
                                  else "cross-record validation failure")
                        # These callbacks are application-owned deterministic validators.
                        # Provide their constraint message, not Pydantic/provider bodies.
                        validation_detail = str(exc)[:300]
            if attempt + 1 < self.settings.extraction_attempts:
                if response.choices and response.choices[0].message.content:
                    messages.append({"role": "assistant", "content": response.choices[0].message.content})
                messages.append({"role": "user", "content":
                                 f"Previous response failed: {reason}. Repair the provided previous answer; "
                                 "preserve valid records, correct the named constraint, and return the COMPLETE valid JSON result. "
                                 + (f"Failed constraint: {validation_detail}" if validation_detail else "")})
        raise LLMError(f"{operation} failed after {self.settings.extraction_attempts} attempts: {reason}")
