import json
import re
from copy import deepcopy
from pathlib import Path

import pytest

from requirements_refiner import cli
from requirements_refiner.config import Settings
from requirements_refiner.graph import build_graph, complete_review
from requirements_refiner.llm import StructuredLLM
from requirements_refiner.models import (
    CandidateDisposition, CandidateRequirement, DiscardedRequirement, GlossaryEntry,
    Requirement, ReviewIssue, ReviewResult, SourceDocument, SourceReference, UnresolvedConflict,
)
from requirements_refiner.nodes.formatter import FormatterError, document_formatter
from requirements_refiner.output import OutputError, atomic_write, validate_output_path
from test_reviewer_graph import FakeAPI


@pytest.fixture
def state(tmp_path):
    root = tmp_path / "corpus"
    root.mkdir()
    records = [("D1", "a [draft].txt", "Support login."), ("D2", "nested/b.md", "Retain backups.")]
    documents, candidates, requirements, dispositions = [], [], [], []
    for index, (identifier, filename, text) in enumerate(records, 1):
        path = root / filename
        path.parent.mkdir(exist_ok=True)
        path.write_text(text, encoding="utf-8")
        reference = SourceReference(document_id=identifier, start_line=1, end_line=1, excerpt=text)
        documents.append(SourceDocument(document_id=identifier, filename=filename, content=text, original_content=text))
        candidates.append(CandidateRequirement(candidate_id=f"C{index}", statement=text, kind="functional", references=[reference]))
        requirements.append(Requirement(internal_key=f"internal-{index}", candidate_ids=[f"C{index}"],
            name=f"Feature {index}", description=f"The system shall implement feature {index}.", kind="functional",
            priority="P2", priority_inferred=index == 1, priority_rationale="Daily operation", references=[reference]))
        dispositions.append(CandidateDisposition(candidate_id=f"C{index}", status="retained", requirement_key=f"internal-{index}"))
    review = ReviewResult(status="accepted", issues=[])
    result = {"input_directory": str(root), "output_path": str(tmp_path / "output" / "requirements.md"),
              "documents": documents, "candidates": candidates, "requirements": requirements,
              "dispositions": dispositions, "blacklist": [], "glossary": [GlossaryEntry(term="staff", definition="Library employees", aliases=["operators"])],
              "unresolved_conflicts": [], "latest_review": review, "review_history": [review],
              "revision_count": 0, "max_revisions": 3}
    result.update(complete_review(result))
    return result


def test_format_full_document_ids_links_and_traceability(state):
    before = deepcopy(state)
    result = document_formatter(state)
    text = result["final_document"]
    assert Path(state["output_path"]).read_text(encoding="utf-8") == text
    assert state == before
    assert result["final_requirement_ids"] == {"internal-1": "REQ-001", "internal-2": "REQ-002"}
    assert re.findall(r"^### (REQ-\d+)", text, re.MULTILINE) == ["REQ-001", "REQ-002"]
    for heading in ("Document overview", "Priority scale", "Requirements", "Glossary", "Blacklist", "Unresolved issues", "Traceability summary"):
        assert f"## {heading}" in text
    for priority in ("P1 Critical", "P2 High", "P3 Medium", "P4 Low"):
        assert priority in text
    assert "Priority basis: inferred" in text and "Priority basis: explicitly specified" in text
    assert "normalized lines 1–1" in text
    assert "a%20%5Bdraft%5D.txt" in text
    assert "../corpus/nested/b.md" in text
    assert "| REQ-001 | internal-1 | C1 |" in text
    assert "| staff | Library employees | operators |" in text
    assert "No unresolved issues remain." in text


def test_deterministic_order_and_markdown_escaping(state):
    state["requirements"][0].name = "Login | [admin] <script> *test*"
    first = document_formatter(state)["final_document"]
    state["requirements"].reverse()
    state["documents"].reverse()
    state["candidates"].reverse()
    state["dispositions"].reverse()
    second = document_formatter(state)["final_document"]
    assert first == second
    assert r"Login \| \[admin\] &lt;script&gt; \*test\*" in first


def test_blacklist_originals_and_related_final_id(state):
    rejected = state["candidates"][1]
    state["requirements"] = state["requirements"][:1]
    state["dispositions"][1] = CandidateDisposition(candidate_id="C2", status="discarded", blacklist_id="B1")
    state["blacklist"] = [DiscardedRequirement(blacklist_id="B1", candidate_ids=["C2"], original_statement=rejected.statement,
        rejection_reason="Source decision favors internal-1.", references=rejected.references, merged_into_key="internal-1")]
    text = document_formatter(state)["final_document"]
    assert "Discarded requirements: 1 (1 candidates)" in text
    assert "Related retained requirement: REQ-001" in text
    assert "Source decision favors REQ-001" in text
    assert "Retain backups" in text


def test_unresolved_conflicts_and_quality_defects_disclosed_separately(state):
    source = ReviewIssue(issue_id="I-source", category="OS7", actionable=False,
        affected_keys=["internal-1", "internal-2"], explanation="Sources contradict.", requested_correction="Request clarification.",
        references=state["candidates"][0].references)
    quality = ReviewIssue(issue_id="I-quality", category="OS5", affected_keys=["internal-1"],
        explanation="internal-1 needs a clearer description.", requested_correction="Expand description.")
    state["unresolved_conflicts"] = [UnresolvedConflict(conflict_id="F1", requirement_keys=["internal-1", "internal-2"],
        explanation="Decision unavailable.", references=state["candidates"][0].references)]
    review = ReviewResult(status="needs_revision", issues=[source, quality])
    state.update(latest_review=review, review_history=[review] * 4, revision_count=3)
    state.update(complete_review(state))
    text = document_formatter(state)["final_document"]
    assert "Source ambiguities requiring clarification" in text
    assert "Quality defects remaining after the revision limit" in text
    assert "REQ-001 needs a clearer description" in text
    assert "F1: REQ-001, REQ-002" in text
    assert "incomplete_review" in text


def test_unincorporated_missing_candidates_disclosed(state):
    missing = state["candidates"][0].model_copy(update={"candidate_id": "missed"})
    review = ReviewResult(status="needs_revision", issues=[], missing_candidates=[missing])
    state.update(latest_review=review, review_history=[review] * 4, revision_count=3)
    state.update(complete_review(state))
    text = document_formatter(state)["final_document"]
    assert "Coverage gaps remaining after the revision limit" in text
    assert "missed: Support login" in text


@pytest.mark.parametrize("corruption", ["duplicate_key", "empty_name", "priority", "reference", "disposition", "blacklist", "status", "traceability", "history"])
def test_structural_failures_preserve_existing_output(state, corruption):
    output = Path(state["output_path"])
    output.parent.mkdir()
    output.write_text("existing valid output", encoding="utf-8")
    if corruption == "duplicate_key": state["requirements"][1].internal_key = "internal-1"
    elif corruption == "empty_name": state["requirements"][0].name = ""
    elif corruption == "priority": state["requirements"][0].priority = "P99"
    elif corruption == "reference": state["requirements"][0].references[0].document_id = "unknown"
    elif corruption == "disposition": state["dispositions"].pop()
    elif corruption == "blacklist": state["blacklist"] = [DiscardedRequirement(blacklist_id="B", candidate_ids=["C1"], original_statement="changed", rejection_reason="Reject", references=state["candidates"][0].references)]
    elif corruption == "status": state["completion_status"] = "incomplete_review"
    elif corruption == "traceability": state["requirements"][0].candidate_ids = ["unknown"]
    else: state["review_history"] = []
    with pytest.raises(FormatterError):
        document_formatter(state)
    assert output.read_text(encoding="utf-8") == "existing valid output"


def test_output_safety_and_explicit_in_corpus_exclusion(state):
    root = Path(state["input_directory"])
    with pytest.raises(OutputError, match="requires"):
        validate_output_path(root, root / "new.md")
    with pytest.raises(OutputError, match="overwrite"):
        validate_output_path(root, root / "nested/b.md", True)
    state.update(output_path=str(root / "generated.md"), allow_output_in_corpus=True)
    document_formatter(state)
    assert (root / "generated.md").exists()


def test_atomic_failure_keeps_old_file_and_cleans_temp(state, monkeypatch):
    target = Path(state["output_path"])
    target.parent.mkdir()
    target.write_text("old", encoding="utf-8")
    def denied(*args):
        raise PermissionError("Permission denied")
    monkeypatch.setattr("requirements_refiner.output.os.replace", denied)
    with pytest.raises(FormatterError, match="Permission denied"):
        document_formatter(state)
    assert target.read_text(encoding="utf-8") == "old"
    assert list(target.parent.glob(".requirements-refiner-*.tmp")) == []


def test_parent_creation_error_is_reported(state):
    parent = Path(state["output_path"]).parent
    parent.write_text("This is a file, not a directory", encoding="utf-8")
    with pytest.raises(FormatterError, match="Cannot generate"):
        document_formatter(state)
    assert parent.read_text(encoding="utf-8") == "This is a file, not a directory"


def test_external_hardlink_to_source_is_protected(state, tmp_path):
    alias = tmp_path / "alias.md"
    source = Path(state["input_directory"]) / "nested/b.md"
    try:
        alias.hardlink_to(source)
    except OSError as exc:
        pytest.skip(f"Filesystem does not permit hard links: {exc}")
    with pytest.raises(OutputError, match="input corpus document"):
        validate_output_path(state["input_directory"], alias)


def test_unsafe_graph_output_fails_before_api(tmp_path):
    graph, api, inputs = make_graph(tmp_path, ["accepted"])
    inputs["output_path"] = str(Path(inputs["input_directory"]) / "unsafe.md")
    with pytest.raises(OutputError, match="requires"):
        graph.invoke(inputs)
    assert api.calls == []


def make_graph(tmp_path, outcomes, maximum=3, reject=False, documents=1, inside=False):
    root = tmp_path / "corpus"
    root.mkdir()
    for index in range(documents):
        (root / f"{index}.txt").write_text("Support login.\nKeep backups.", encoding="utf-8")
    api = FakeAPI(outcomes, reject_initial=reject)
    settings = Settings(max_revisions=maximum)
    llm = StructuredLLM(settings, client=api.client)
    graph = build_graph(settings, llm=llm)
    output = root / "new.md" if inside else tmp_path / "nested/output.md"
    return graph, api, {"input_directory": str(root), "output_path": str(output), "allow_output_in_corpus": inside}


@pytest.mark.parametrize("outcomes,maximum,status", [(["accepted"], 3, "complete"),
    (["actionable", "accepted"], 3, "complete"), (["actionable"], 3, "incomplete_review"),
    (["ambiguity"], 3, "complete_with_unresolved")])
def test_mocked_end_to_end_file_generation(tmp_path, outcomes, maximum, status):
    graph, api, inputs = make_graph(tmp_path, outcomes, maximum, documents=2)
    result = graph.invoke(inputs)
    assert result["completion_status"] == status
    assert len(result["documents"]) == 2
    assert len(result["final_requirement_ids"]) == 4
    assert Path(inputs["output_path"]).read_text(encoding="utf-8") == result["final_document"]
    assert len(re.findall(r"^### REQ-\d+", result["final_document"], re.MULTILINE)) == 4


def test_mocked_end_to_end_blacklist_and_allowed_inside_output(tmp_path):
    graph, api, inputs = make_graph(tmp_path, ["accepted"], reject=True, inside=True)
    result = graph.invoke(inputs)
    assert len(result["documents"]) == 1
    assert len(result["blacklist"]) == 1
    assert "### B1" in result["final_document"]


def test_cli_mocked_complete_network(tmp_path, monkeypatch, capsys):
    root = tmp_path / "corpus"
    root.mkdir()
    (root / "input.txt").write_text("Support login.\nKeep backups.", encoding="utf-8")
    output = tmp_path / "new/output.md"
    settings = Settings(api_key="fake-for-tests")
    api = FakeAPI(["accepted"])
    monkeypatch.setattr(cli, "load_settings", lambda path: settings)
    def mocked_build(config):
        assert config.max_revisions == 2
        return build_graph(config, llm=StructuredLLM(config, client=api.client))
    monkeypatch.setattr(cli, "build_graph", mocked_build)
    assert cli.main([str(root), "--output", str(output), "--max-revisions", "2"]) == 0
    assert output.is_file()
    captured = capsys.readouterr().out
    assert "Completed: formatter" in captured
    assert "retained requirements: 2" in captured
    assert "fake-for-tests" not in captured


@pytest.mark.parametrize("outcome,expected", [("actionable", 3), ("ambiguity", 0)])
def test_cli_review_exit_codes(tmp_path, monkeypatch, outcome, expected):
    root = tmp_path / "corpus"
    root.mkdir()
    (root / "input.txt").write_text("Support login.\nKeep backups.", encoding="utf-8")
    settings = Settings(api_key="fake")
    api = FakeAPI([outcome])
    monkeypatch.setattr(cli, "load_settings", lambda path: settings)
    monkeypatch.setattr(cli, "build_graph", lambda config: build_graph(config, llm=StructuredLLM(config, client=api.client)))
    assert cli.main([str(root), "--output", str(tmp_path / "out.md"), "--max-revisions", "0"]) == expected
    assert (tmp_path / "out.md").exists()


def test_cli_parsing_overrides_and_errors(tmp_path, monkeypatch, capsys):
    args = cli.parser().parse_args([str(tmp_path), "--output", "out.md", "--reviewer-model", "custom", "--env-file", "custom.env"])
    assert args.reviewer_model == "custom" and args.env_file == Path("custom.env")
    with pytest.raises(SystemExit) as error:
        cli.main([str(tmp_path), "--output", "out.md", "--max-revisions", "-1"])
    assert error.value.code == 2
    assert cli.main([str(tmp_path / "missing"), "--output", str(tmp_path / "out.md")]) == 1
    monkeypatch.setattr(cli, "load_settings", lambda path: Settings())
    assert cli.main([str(tmp_path), "--output", str(tmp_path / "outside/out.md"), "--allow-output-in-corpus"]) == 1
    assert "OPENAI_API_KEY" in capsys.readouterr().err
