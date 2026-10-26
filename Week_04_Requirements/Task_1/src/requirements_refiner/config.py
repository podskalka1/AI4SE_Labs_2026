"""Environment configuration; no API client is created here."""
import os
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from pydantic import BaseModel, Field, SecretStr, field_validator


class Settings(BaseModel):
    api_key: SecretStr | None = None
    base_url: str | None = None
    extractor_model: str = Field(default="gpt-5-mini", min_length=1)
    refiner_model: str = Field(default="gpt-5.6-luna", min_length=1)
    writer_model: str = Field(default="gpt-5.4-nano", min_length=1)
    reviewer_model: str = Field(default="gpt-6-luna", min_length=1)
    max_revisions: int = Field(default=3, ge=0)
    chunk_size: int = Field(default=12000, ge=100)
    chunk_overlap_lines: int = Field(default=2, ge=0)
    request_timeout: float = Field(default=60, gt=0, le=600)
    api_retries: int = Field(default=2, ge=0, le=5)
    extraction_attempts: int = Field(default=3, ge=1, le=5)
    output_mode: Literal["auto", "json_schema", "json_object", "text"] = "auto"
    max_output_tokens: int = Field(default=8000, ge=100)
    output_token_parameter: Literal["max_completion_tokens", "max_tokens"] = "max_completion_tokens"

    @field_validator("base_url")
    @classmethod
    def validate_url(cls, value: str | None) -> str | None:
        if value is not None and not value.startswith(("http://", "https://")):
            raise ValueError("OPENAI_BASE_URL must be an HTTP(S) URL")
        return value

    def validate_llm_configuration(self) -> None:
        """Call only when an LLM stage is requested."""
        if self.api_key is None or not self.api_key.get_secret_value().strip():
            raise ValueError("OPENAI_API_KEY is required for LLM stages")
        self.validate_model_diversity()

    def validate_model_diversity(self) -> None:
        if len({self.extractor_model, self.refiner_model,
                self.writer_model, self.reviewer_model}) < 3:
            raise ValueError("At least three distinct LLM models are required")


def load_settings(env_file: str | Path = ".env") -> Settings:
    load_dotenv(env_file, override=False)
    mapping = {
        "api_key": "OPENAI_API_KEY", "base_url": "OPENAI_BASE_URL",
        "extractor_model": "EXTRACTOR_MODEL", "refiner_model": "REFINER_MODEL",
        "writer_model": "WRITER_MODEL", "reviewer_model": "REVIEWER_MODEL",
        "max_revisions": "MAX_REVISIONS",
        "chunk_size": "EXTRACTION_CHUNK_SIZE",
        "chunk_overlap_lines": "EXTRACTION_OVERLAP_LINES",
        "request_timeout": "OPENAI_TIMEOUT",
        "api_retries": "OPENAI_MAX_RETRIES",
        "extraction_attempts": "EXTRACTION_ATTEMPTS",
        "output_mode": "OPENAI_OUTPUT_MODE",
        "max_output_tokens": "OPENAI_MAX_OUTPUT_TOKENS",
        "output_token_parameter": "OPENAI_OUTPUT_TOKEN_PARAMETER",
    }
    return Settings(**{field: os.environ[key] for field, key in mapping.items()
                       if os.environ.get(key, "").strip()})
