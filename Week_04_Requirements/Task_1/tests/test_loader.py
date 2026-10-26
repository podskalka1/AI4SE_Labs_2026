from email.message import EmailMessage

import pytest

from requirements_refiner.models import SourceReference
from requirements_refiner.nodes.loader import CorpusLoadError, corpus_loader, load_corpus


def test_recursive_sorted_supported_and_stable(tmp_path):
    (tmp_path / "nested").mkdir()
    (tmp_path / "nested" / "b.md").write_text("B", encoding="utf-8")
    (tmp_path / "a.TXT").write_bytes(b"\xef\xbb\xbfFirst\r\nSecond\rThird")
    (tmp_path / "ignored.py").write_text("ignored")
    (tmp_path / ".venv").mkdir()
    (tmp_path / ".venv" / "ignored.txt").write_text("ignored")
    first = load_corpus(tmp_path)
    assert [d.filename for d in first] == ["a.TXT", "nested/b.md"]
    assert first[0].content == "First\nSecond\nThird"
    assert first[0].original_content == "First\r\nSecond\rThird"
    assert [d.document_id for d in first] == [d.document_id for d in load_corpus(tmp_path)]
    (tmp_path / "a.TXT").write_text("Edited", encoding="utf-8")
    assert load_corpus(tmp_path)[0].document_id == first[0].document_id
    update = corpus_loader({"input_directory": str(tmp_path), "requirements": []})
    assert list(update) == ["documents"]


def test_multipart_email_attachments_and_evidence(tmp_path):
    message = EmailMessage()
    message["Subject"] = "Access"
    message["From"] = "staff@example.org"
    message.set_content("Require login.\nKeep fallback.")
    message.add_alternative("<p>Require login.</p>", subtype="html")
    message.add_attachment("Do not extract me", subtype="plain", filename="notes.txt")
    message.add_attachment(b"binary", maintype="application", subtype="octet-stream",
                           filename="binary.dat")
    (tmp_path / "mail.eml").write_bytes(message.as_bytes())
    document = load_corpus(tmp_path)[0]
    assert document.metadata["subject"] == "Access"
    assert "Require login." in document.content
    assert "Do not extract me" not in document.content
    assert "<p>" not in document.content
    reference = SourceReference(document_id=document.document_id, start_line=1,
                                end_line=2, excerpt="Require login.\nKeep fallback.")
    reference.validate_against(document)
    with pytest.raises(ValueError, match="exactly match"):
        reference.model_copy(update={"excerpt": "incorrect"}).validate_against(document)
    with pytest.raises(ValueError, match="locate"):
        reference.model_copy(update={"end_line": 999}).validate_against(document)


def test_multiple_plain_parts(tmp_path):
    message = EmailMessage()
    message.make_mixed()
    for text in ("First body", "Second body"):
        part = EmailMessage()
        part.set_content(text)
        message.attach(part)
    (tmp_path / "parts.eml").write_bytes(message.as_bytes())
    content = load_corpus(tmp_path)[0].content
    assert "First body" in content and "Second body" in content


def test_empty_and_malformed_are_visible(tmp_path):
    (tmp_path / "empty.txt").write_text("")
    (tmp_path / "bad.eml").write_text("Not a header\nRequirement body", encoding="utf-8")
    documents = load_corpus(tmp_path)
    assert "Requirement body" in documents[0].content
    assert any("defect" in warning for warning in documents[0].warnings)
    assert documents[1].warnings == ["Document has no readable text"]


def test_html_only_is_reported(tmp_path):
    message = EmailMessage()
    message.set_content("<p>HTML only</p>", subtype="html")
    (tmp_path / "html.eml").write_bytes(message.as_bytes())
    document = load_corpus(tmp_path)[0]
    assert not document.content
    assert any("unsupported" in warning for warning in document.warnings)


def test_bad_encoding_fails_with_filename(tmp_path):
    (tmp_path / "broken.txt").write_bytes(b"\xff\xfe")
    with pytest.raises(CorpusLoadError, match="broken.txt"):
        load_corpus(tmp_path)


def test_invalid_email_charset(tmp_path):
    (tmp_path / "broken.eml").write_text(
        'Content-Type: text/plain; charset="unknown-charset"\n\nBody', encoding="utf-8")
    with pytest.raises(CorpusLoadError, match="broken.eml"):
        load_corpus(tmp_path)


def test_read_error_is_not_silenced(tmp_path, monkeypatch):
    (tmp_path / "unreadable.txt").write_text("content")
    def denied(self):
        raise PermissionError("Access denied")
    monkeypatch.setattr(type(tmp_path), "read_bytes", denied)
    with pytest.raises(CorpusLoadError, match="unreadable.txt"):
        load_corpus(tmp_path)


def test_missing_empty_directory_and_output_exclusion(tmp_path):
    with pytest.raises(CorpusLoadError, match="does not exist"):
        load_corpus(tmp_path / "missing")
    with pytest.raises(CorpusLoadError, match="No supported"):
        load_corpus(tmp_path)
    (tmp_path / "source.txt").write_text("source")
    output = tmp_path / "result.md"
    output.write_text("generated")
    assert len(load_corpus(tmp_path, output_path=output)) == 1


def test_ids_independent_of_corpus_location(tmp_path):
    roots = [tmp_path / "one", tmp_path / "two"]
    for root in roots:
        root.mkdir()
        (root / "same.txt").write_text("same")
    assert load_corpus(roots[0])[0].document_id == load_corpus(roots[1])[0].document_id
