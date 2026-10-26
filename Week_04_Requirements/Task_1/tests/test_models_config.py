import pytest
from pydantic import ValidationError

from requirements_refiner.config import Settings, load_settings
from requirements_refiner.models import (
    CandidateDisposition, Requirement, ReviewResult, SourceReference,
)


def test_reference_bounds():
    with pytest.raises(ValidationError):
        SourceReference(document_id="doc", start_line=2, end_line=1, excerpt="text")
    with pytest.raises(ValidationError):
        SourceReference(document_id="doc", start_line=0, end_line=1, excerpt="text")


def test_disposition_destinations():
    CandidateDisposition(candidate_id="C1", status="merged", requirement_key="R1")
    CandidateDisposition(candidate_id="C2", status="discarded", blacklist_id="B1")
    with pytest.raises(ValidationError):
        CandidateDisposition(candidate_id="C1", status="retained")
    with pytest.raises(ValidationError):
        CandidateDisposition(candidate_id="C1", status="discarded", requirement_key="R1")


def test_review_consistency():
    ReviewResult(status="accepted", issues=[])
    with pytest.raises(ValidationError):
        ReviewResult(status="needs_revision", issues=[])


def test_requirement_provenance_roundtrip():
    reference = SourceReference(document_id="DOC-1", start_line=1, end_line=1,
                                excerpt="Support login")
    requirement = Requirement(
        internal_key="R1", candidate_ids=["C1", "C2"], name="Staff login",
        description="The system shall support staff login.", kind="functional",
        priority="P2", priority_rationale="Supports daily operations",
        priority_inferred=True, references=[reference],
    )
    assert Requirement.model_validate_json(requirement.model_dump_json()) == requirement
    with pytest.raises(ValidationError):
        Requirement.model_validate({**requirement.model_dump(), "references": []})
    with pytest.raises(ValidationError):
        Requirement.model_validate({**requirement.model_dump(), "candidate_ids": []})


def test_config_without_key_and_env_precedence(tmp_path, monkeypatch):
    keys = ["OPENAI_API_KEY", "OPENAI_BASE_URL", "EXTRACTOR_MODEL", "REFINER_MODEL",
            "WRITER_MODEL", "REVIEWER_MODEL", "MAX_REVISIONS"]
    for key in keys:
        monkeypatch.delenv(key, raising=False)
    env = tmp_path / ".env"
    env.write_text("MAX_REVISIONS=2\nEXTRACTOR_MODEL=from-file\n")
    monkeypatch.setenv("MAX_REVISIONS", "4")
    settings = load_settings(env)
    assert settings.api_key is None
    assert settings.max_revisions == 4
    assert settings.extractor_model == "from-file"
    with pytest.raises(ValueError, match="OPENAI_API_KEY"):
        settings.validate_llm_configuration()


def test_secret_and_invalid_configuration():
    settings = Settings(api_key="test-secret")
    assert "test-secret" not in repr(settings)
    settings.validate_llm_configuration()
    with pytest.raises(ValidationError):
        Settings(max_revisions=-1)
    with pytest.raises(ValidationError):
        Settings(base_url="invalid")
    with pytest.raises(ValueError, match="three distinct"):
        Settings(api_key="test", extractor_model="same", refiner_model="same",
                 writer_model="same", reviewer_model="same").validate_llm_configuration()
