import json
from types import SimpleNamespace
from unittest.mock import Mock

import httpx
import pytest
from openai import BadRequestError, OpenAI

from requirements_refiner.chunking import chunk_document
from requirements_refiner.config import Settings
from requirements_refiner.llm import LLMError, StructuredLLM
from requirements_refiner.models import SourceDocument
from requirements_refiner.nodes.extractor import (
    ExtractionResult, requirements_extractor,
)


def document(identifier="DOC-1", filename="source.txt", content="Support login.\nRespond in 2 seconds."):
    return SourceDocument(document_id=identifier, filename=filename,
                          original_content=content, content=content)


def candidate(doc="DOC-1", start=1, end=1, excerpt="Support login.",
              kind="functional", statement="Support login."):
    return {"statement": statement, "kind": kind, "extraction_note": None,
            "references": [{"document_id": doc, "start_line": start,
                            "end_line": end, "excerpt": excerpt,
                            "evidence_basis": "normalized_text"}]}


def response(content, finish="stop", refusal=None):
    return SimpleNamespace(choices=[SimpleNamespace(finish_reason=finish,
                           message=SimpleNamespace(content=content, refusal=refusal))])


def service(*outputs, **settings):
    client = Mock()
    client.chat.completions.create.side_effect = outputs
    llm = StructuredLLM(Settings(**settings), client=client)
    return llm, client.chat.completions.create


def run(llm, docs=None):
    return requirements_extractor({"documents": docs or [document()], "requirements": []},
                                  settings=llm.settings, llm=llm)


def test_valid_multiple_requirements_documents_and_stable_ids():
    first = candidate()
    second = candidate(start=2, end=2, excerpt="Respond in 2 seconds.",
                       kind="nonfunctional", statement="Respond within two seconds.")
    third = candidate(doc="DOC-2", excerpt="Keep backups.", statement="Keep backups.")
    llm, create = service(response(json.dumps({"candidates": [first, second]})),
                          response(json.dumps({"candidates": [third]})),
                          response(json.dumps({"candidates": [second, first]})),
                          response(json.dumps({"candidates": [third]})))
    docs = [document(), document("DOC-2", "two.md", "Keep backups.")]
    update = run(llm, docs)
    assert list(update) == ["candidates"]
    assert len(update["candidates"]) == 3
    assert {c.kind for c in update["candidates"]} == {"functional", "nonfunctional"}
    assert update == run(llm, list(reversed(docs)))
    assert len({c.candidate_id for c in update["candidates"]}) == 3
    for item in update["candidates"]:
        item.references[0].validate_against(next(d for d in docs if d.document_id == item.references[0].document_id))
    assert create.call_args.kwargs["model"] == "gpt-5-mini"
    assert create.call_args.kwargs["response_format"]["type"] == "json_schema"


@pytest.mark.parametrize("bad", [
    candidate(doc="invented"), candidate(start=1, end=20),
    candidate(excerpt="fabricated"), candidate(start=2, end=1),
    {"statement": "Missing fields"},
])
def test_invalid_evidence_and_schema_retry_then_fail(bad):
    payload = response(json.dumps({"candidates": [bad]}))
    llm, create = service(payload, payload, extraction_attempts=2)
    with pytest.raises(LLMError, match=r"source.txt lines 1-2:.*2 attempts"):
        run(llm)
    assert create.call_count == 2


@pytest.mark.parametrize("bad", [response("invalid JSON"), response("{}"),
                                response(""), response(None),
                                response('{"candidates":', finish="length"),
                                SimpleNamespace(choices=[]),
                                response("{}", finish="tool_calls")])
def test_bad_responses_can_recover(bad):
    llm, create = service(bad, response('{"candidates": []}'))
    assert run(llm) == {"candidates": []}
    assert create.call_count == 2


def test_refusal_is_explicit_and_not_retried():
    llm, create = service(response(None, refusal="refused"))
    with pytest.raises(LLMError, match="refused"):
        run(llm)
    assert create.call_count == 1


def test_chunking_covers_every_line_and_respects_limit():
    doc = document(content="\n".join(f"line {i} " + "x" * 12 for i in range(30)))
    chunks = chunk_document(doc, max_chars=100, overlap_lines=2)
    assert chunks == chunk_document(doc, max_chars=100, overlap_lines=2)
    assert len(chunks) > 1
    assert {i for chunk in chunks for i in range(chunk.start_line, chunk.end_line + 1)} == set(range(1, 31))
    assert all(len(chunk.text) <= 100 for chunk in chunks)
    assert chunks[1].start_line <= chunks[0].end_line
    for chunk in chunks:
        assert chunk.text == "\n".join(doc.content.splitlines()[chunk.start_line - 1:chunk.end_line])


def test_chunk_mapping_and_exact_overlap_duplicates():
    doc = document(content="A" * 50 + "\nB" + "\n" + "C" * 50)
    same = candidate(start=2, end=2, excerpt="B", statement="Support B")
    llm, create = service(response(json.dumps({"candidates": [same]})),
                          response(json.dumps({"candidates": [same]})),
                          chunk_size=100, chunk_overlap_lines=1)
    assert len(run(llm, [doc])["candidates"]) == 1
    assert create.call_count == 2
    assert '2: B' in create.call_args.kwargs["messages"][1]["content"]


def test_outside_chunk_reference_rejected():
    doc = document(content="A" * 60 + "\n" + "B" * 60)
    bad = candidate(start=2, end=2, excerpt="B" * 60)
    llm, _ = service(response(json.dumps({"candidates": [bad]})),
                     chunk_size=100, extraction_attempts=1)
    with pytest.raises(LLMError, match="invalid evidence"):
        run(llm, [doc])


def test_long_lines_fail_before_api_and_empty_documents_no_calls():
    llm, create = service(chunk_size=100)
    with pytest.raises(ValueError, match="exceeds chunk size"):
        run(llm, [document(content="x" * 101)])
    assert run(llm, [document(content="")]) == {"candidates": []}
    create.assert_not_called()


def unsupported(mode):
    return BadRequestError("unsupported", response=httpx.Response(400, request=httpx.Request("POST", "https://test/v1")),
                           body={"message": f"{mode} is not supported", "param": "response_format"})


def test_auto_fallback_schema_json_text_keeps_model():
    llm, create = service(unsupported("json_schema"), unsupported("json_object"),
                          response('{"candidates": []}'), extractor_model="university-model")
    assert run(llm) == {"candidates": []}
    assert [call.kwargs.get("response_format", {}).get("type") for call in create.call_args_list] == ["json_schema", "json_object", None]
    assert {call.kwargs["model"] for call in create.call_args_list} == {"university-model"}


def test_explicit_format_and_invalid_schema_do_not_fallback():
    llm, create = service(unsupported("json_schema"), output_mode="json_schema")
    with pytest.raises(LLMError, match="API rejected"):
        run(llm)
    assert create.call_count == 1
    error = BadRequestError("bad schema", response=httpx.Response(400, request=httpx.Request("POST", "https://test/v1")),
                            body={"message": "Invalid schema", "param": "response_format"})
    llm, create = service(error)
    with pytest.raises(LLMError):
        run(llm)
    assert create.call_count == 1


@pytest.mark.parametrize("status,expected,count", [(401, "authentication", 1),
    (403, "permission", 1), (404, "not found", 1), (429, "rate limit", 3),
    (500, "HTTP 500", 3), (400, "rejected", 1)])
def test_sdk_api_errors_and_bounded_retries(status, expected, count, monkeypatch):
    calls = []
    def handler(request):
        calls.append(request)
        return httpx.Response(status, json={"error": {"message": "private server details"}})
    monkeypatch.setattr("openai._base_client.time.sleep", lambda _: None)
    client = OpenAI(api_key="fake-key", base_url="https://university.example/v1",
                    max_retries=2, http_client=httpx.Client(transport=httpx.MockTransport(handler)))
    llm = StructuredLLM(Settings(), client=client)
    with pytest.raises(LLMError, match=expected) as error:
        run(llm)
    assert "fake-key" not in str(error.value)
    assert "private server details" not in str(error.value)
    assert len(calls) == count
    client.close()


@pytest.mark.parametrize("exception,expected", [(httpx.ConnectError, "connection"),
                                               (httpx.ReadTimeout, "timed out")])
def test_connection_failures(exception, expected, monkeypatch):
    calls = []
    def handler(request):
        calls.append(request)
        raise exception("private details", request=request)
    monkeypatch.setattr("openai._base_client.time.sleep", lambda _: None)
    client = OpenAI(api_key="fake", max_retries=1,
                    http_client=httpx.Client(transport=httpx.MockTransport(handler)))
    with pytest.raises(LLMError, match=expected):
        run(StructuredLLM(Settings(), client=client))
    assert len(calls) == 2
    client.close()


def test_configuration_passed_to_client(monkeypatch):
    constructor = Mock()
    monkeypatch.setattr("requirements_refiner.llm.OpenAI", constructor)
    settings = Settings(api_key="fake", base_url="https://university.example/v1",
                        request_timeout=12, api_retries=1)
    llm = StructuredLLM(settings)
    constructor.assert_called_once_with(api_key="fake", base_url=settings.base_url,
                                        timeout=12, max_retries=1)
    llm.close()
    constructor.return_value.close.assert_called_once()


def test_no_key_fails_before_client_creation():
    with pytest.raises(LLMError, match="OPENAI_API_KEY"):
        StructuredLLM(Settings())


def test_selected_line_evidence_is_copied_exactly_and_has_same_id():
    doc = document(content="Context\n  1. Support login.\n     Keep fallback.")
    selected = candidate(start=2, end=3, excerpt=None)
    quoted = candidate(start=2, end=3, excerpt="  1. Support login.\n     Keep fallback.")
    llm, _ = service(response(json.dumps({"candidates": [selected]})),
                     response(json.dumps({"candidates": [quoted]})))
    first = run(llm, [doc])["candidates"][0]
    second = run(llm, [doc])["candidates"][0]
    assert first == second
    assert first.references[0].excerpt == "  1. Support login.\n     Keep fallback."
    first.references[0].validate_against(doc)


@pytest.mark.parametrize("selection", [candidate(start=1, end=99, excerpt=None),
                                        candidate(doc="invented", excerpt=None),
                                        candidate(excerpt="Support login")])
def test_coordinate_mode_does_not_repair_invalid_ranges_or_supplied_quotes(selection):
    llm, _ = service(response(json.dumps({"candidates": [selection]})), extraction_attempts=1)
    with pytest.raises(LLMError):
        run(llm)
