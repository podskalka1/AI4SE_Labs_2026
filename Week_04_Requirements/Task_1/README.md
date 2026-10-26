# Requirements refiner

University laboratory project: refine a directory of software descriptions into
one traceable requirements document using Python and LangGraph.

## Setup

Install Python 3.11 or later. From this directory, in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[test]"
Copy-Item .env.example .env
```

If using uv, `uv venv` and `uv pip install -e ".[test]"` are equivalent.
Use the interpreter's full path if `python` resolves to a Windows Store alias.

Configure `.env` with the university API key and optional `OPENAI_BASE_URL`.
Never commit `.env`. Existing environment variables override file values.
`load_settings()` reads `.env` relative to the working directory, or accepts an
explicit file path. Four model variables and `MAX_REVISIONS` have defaults in
`.env.example`. The revision limit means revisions after the initial review.
No credentials are required for loading or mocked tests. Live extraction requires
an API key. Secrets are masked in configuration reprs.

## Implemented

- Pydantic v2 source, provenance, requirement, disposition, glossary and review models.
- TypedDict graph state using replacement updates, without append reducers.
- Deterministic recursive loader for UTF-8 `.txt`, `.md`, and `.eml` files.
- Case-sensitive relative-path ordering and SHA-256 document IDs derived from
  relative filenames: stable across moves of the corpus and edits to content.
- Email metadata and plain-text MIME bodies; attachments are excluded.
  Multipart alternatives prefer plain text to avoid duplicate representations.
  HTML-only bodies are unsupported and produce explicit warnings.
- Empty documents and recoverable email defects are retained with warnings.
  Invalid UTF-8, invalid body charsets, read errors and traversal errors fail
  explicitly rather than returning an incomplete corpus.
- A Requirements Extractor node with configurable OpenAI-compatible client,
  deterministic chunking, validated evidence and stable candidate identifiers.
- Requirements Refiner and Writer nodes with complete candidate disposition
  accounting, glossary, unresolved conflicts and protected writer metadata.
- Evidence-grounded Reviewer and a compiled LangGraph workflow with bounded
  conditional feedback from review to refinement.
- Deterministic Markdown Formatter and an argparse CLI for complete execution.

All evidence locations are one-based inclusive lines of `SourceDocument.content`,
with LF newlines and `evidence_basis="normalized_text"`. For email this is the
extracted body, not raw email line numbers. `original_content` preserves decoded
source text (excluding a UTF-8 BOM); references can validate their exact excerpt
against the normalized text. Document IDs are corpus-local; candidate and
requirement keys must be assigned once and preserved on revision. The extractor
assigns candidate IDs from SHA-256 hashes of canonical candidate records, including
their source document IDs and evidence. Exact duplicate records from overlap are
coalesced; semantic deduplication remains a later-stage responsibility.

The loader skips known environment/build/output directories, does not traverse
directory symlinks, and rejects supported file symlinks. Pass `output_path` to
exclude the specific generated output if it lies inside the corpus. Select a
dedicated input directory: arbitrary generated text cannot be recognized reliably.
Logging reports warnings and counts, never document bodies or credentials.

## Tests and loader smoke test

```powershell
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m requirements_refiner.loader_smoke data/corpus
```

The smoke command accepts any directory, reports the loaded count and warnings,
and returns a nonzero exit code on loading errors. It never invokes an LLM.

## Requirements extraction

`requirements_extractor(state)` reads loaded `documents` and returns only a
`candidates` update. It can also accept explicit settings and an injected client
for testing. No graph or later agent is constructed. Empty documents require no
API requests. Failures return no partial candidate update.

The dedicated system prompt covers functional/nonfunctional behavior, constraints,
business rules and quality attributes. It favors completeness, preserves
contradictions, and records uncertain or implied requirements in `extraction_note`.
It assigns no priorities and performs no global semantic deduplication.

Chunks use normalized complete lines, prefer paragraph boundaries near the size
limit, and include bounded overlap. Every normalized line is covered; absolute
line numbers accompany the text. `EXTRACTION_CHUNK_SIZE` (default 12000) counts
source characters, not tokens or total prompt size. `EXTRACTION_OVERLAP_LINES`
defaults to 2 and shrinks if needed to ensure progress. A single oversized line
fails explicitly before API calls: increase the size or prepare a line-wrapped
input copy. Text is never silently truncated. Metadata, instructions, numbering,
schema and output also consume context, so choose a conservative size for the
configured model. Requirements spanning chunk boundaries may need later review.

Each reference must point to the current supplied chunk, with an existing
document ID, valid line bounds and an exact full-line excerpt. The extraction
wire schema permits `excerpt=null`: the model selects normalized line coordinates
and the application copies those exact complete lines, preserving indentation and
list prefixes. This avoids transcription errors without guessing source locations.
If a quotation is supplied, it must match exactly; incorrect quotations and invalid
line ranges are rejected, never repaired. All stored candidates still contain
the ordinary non-null `SourceReference` evidence. Invalid JSON,
schema failures, empty/truncated output and invalid evidence trigger at most
`EXTRACTION_ATTEMPTS` generation attempts (default 3), then an error identifies
the affected document and chunk. Refusals and terminal API errors fail explicitly.
Evidence validation proves text location; it cannot prove semantic support or
extraction completeness.

The client uses Chat Completions for OpenAI-compatible endpoints. In
`OPENAI_OUTPUT_MODE=auto`, it first requests strict `json_schema`. Only explicit
format-unsupported errors trigger a warning and a retry using `json_object`, then
prompted JSON without `response_format`. All modes use the same model and local
Pydantic/evidence validation. A malformed schema or unrelated request error does
not trigger fallback. Set `json_schema`, `json_object` or `text` to require a
particular mode. JSON mode alone does not enforce the schema; see the
[official OpenAI structured-output guide](https://developers.openai.com/api/docs/guides/structured-outputs).

`OPENAI_TIMEOUT` defaults to 60 seconds per request. The SDK handles transient
connection, timeout, rate-limit and server failures with `OPENAI_MAX_RETRIES=2`
(at most three transport attempts per request). Validation attempts are separate;
auto format negotiation can add at most two format requests per client. There
is no unlimited retry or model substitution. API errors exposed by this layer
omit raw provider messages, response bodies and credentials.
`OPENAI_MAX_OUTPUT_TOKENS` defaults to 8000, including reasoning tokens on models
that count them. Truncation retries do not raise that cap automatically; increase
it or reduce chunk size after a persistent failure. Older endpoints may require
`OPENAI_OUTPUT_TOKEN_PARAMETER=max_tokens`; the default is `max_completion_tokens`.
All four assigned models and native JSON Schema output were verified against the
official OpenAI endpoint. Other compatible gateways may have different capabilities.

## Refinement and writing

`requirements_refiner(state)` uses `REFINER_MODEL` (default `gpt-5.6-luna`).
It receives extracted candidates and their original evidence, consolidates genuine
semantic duplicates, rewrites requirements, identifies conflicts, assigns priorities
and maintains a domain glossary. Related but distinct requirements remain separate.
Only evidence-backed decisions may resolve conflicts. Rejected alternatives retain
their original statements and sources in the blacklist. Unresolved alternatives
remain active and are recorded in `unresolved_conflicts` for later review; document
dates alone confer no precedence.

The priority scale is:

| Priority | Meaning |
| --- | --- |
| P1 Critical | Essential for core operation, safety, security or mandatory compliance |
| P2 High | Important functionality with substantial impact |
| P3 Medium | Useful functionality not essential for basic operation |
| P4 Low | Optional enhancements or convenience features |

Source priorities take precedence when available. Otherwise the refiner marks the
priority as inferred. Every requirement includes a brief rationale.

Every candidate must have exactly one ledger entry and belong to exactly one
requirement or blacklist entry. Each requirement has one `retained` representative;
other candidates describing the same requirement are `merged` into it. Merging
does not imply rejection and does not create blacklist entries. `discarded`
candidates point to a blacklist entry with a rejection reason. For grouped
discarded candidates, `original_statement` preserves their original statements
joined with two newlines in `candidate_ids` order. The historical blacklist field
`merged_into_key` optionally points to a related retained requirement, including
the accepted alternative in a resolved conflict.

Deterministic validation enforces unique keys and dispositions, complete coverage,
valid candidate/document IDs, exact evidence excerpts, valid priority enums,
consistent ledger destinations and the complete union of all originating source
references. These checks also run on incoming candidate evidence before API calls.
Unresolved conflict records must reference distinct existing requirements and
their original evidence. Invalid results use the existing bounded structured-output
retry mechanism, then fail without returning partial updates. The historically
named `EXTRACTION_ATTEMPTS` currently controls validation attempts for all three
implemented agents; SDK transient retries and format fallback are unchanged.

For revision, supply existing requirements, blacklist, glossary, unresolved
conflicts and `latest_review` along with the original candidates/documents.
The refiner returns a complete replacement of all refinement fields. Validated
`latest_review.missing_candidates` are incorporated into the candidate collection
and returned as a replacement candidate update when needed. An existing candidate
ID cannot be reused for different content. Existing requirement keys survive
exact lineage matches first; deterministic greatest-overlap matching then preserves
one old key per continuing group in merges/splits. New groups receive SHA-256 keys
derived from sorted candidate IDs. All ledger/conflict/blacklist destinations are
remapped together. There is no internal review loop or revision-counter update;
LangGraph routing controls revisions.

`requirements_writer(state)` uses `WRITER_MODEL` (default `gpt-5.4-nano`). It receives
requirements, glossary and unresolved conflicts, and returns only a replacement
`requirements` list. Its schema permits only `internal_key`, `name` and `description`.
Each input key must appear exactly once. Names are at most 120 characters and
descriptions use a single paragraph. Only those two presentation fields are merged
into deep copies of the authoritative requirements. Priorities, rationale, inferred
status, type, lineage, keys and references cannot be altered by writer output.
The writer is instructed to preserve meaning, qualifiers and unresolved conflicts.

Both nodes support injected settings and mocked clients, require no credentials
for empty inputs, and do not mutate their input state. No live API requests are
performed automatically. The refiner needs `candidates` and their `documents`;
the writer needs `requirements`. Tests cover both nodes without API credits.

Limitations: semantic equivalence, justified conflict resolution, priority inference
and meaning preservation remain model-based. The reviewer assesses them.
Stable key matching tracks lineage rather than proving semantic identity. Basic mode
submits complete refinement/writing collections and is appropriate only for small
inputs. Use compact full-run mode below for larger corpora. No source text is
silently truncated. Feedback revisions are orchestrated by LangGraph.

## Reviewer and LangGraph workflow

`requirements_reviewer(state)` uses `REVIEWER_MODEL` (default `gpt-6-luna`). It
receives complete normalized source documents, all extracted candidates, current
requirements, dispositions, blacklist, glossary, unresolved conflicts and the
previous review. Its prompt explicitly checks OS2–OS9, including corpus coverage,
unsupported claims, semantic duplicates, contradictions, priority scale and
discard justification. OS1 remains the formatter's responsibility.

Issues distinguish actionable quality defects (`actionable=true`) from source
ambiguities that cannot be resolved from evidence (`actionable=false`). Each issue
has a valid OS category, explanation, correction request, requirement/candidate
targets and supporting normalized evidence where applicable. The node validates
target IDs, exact evidence, unique issue IDs and status consistency before accepting
a response. Supplied unresolved conflicts must be explicitly assessed. Stable issue
IDs are hashes of canonical findings, independent of the model's temporary IDs;
changed wording can produce a new issue ID. Previously missed candidates receive
deterministic candidate IDs and validated evidence for the next refinement pass.

`build_graph(settings, llm=...)` constructs and compiles the actual `StateGraph`:

```text
START → Loader → Extractor → Refiner → Writer → Reviewer
                              ↑                    │
                              └── Revise ←─────────┤ actionable + budget
                                                   ↓ otherwise
                                                Complete → Formatter → END
```

`add_conditional_edges` routes review results; there is no outer Python review loop.
The deterministic `Revise` node increments `revision_count` exactly once. Loader
and Extractor execute only on the initial pass. Refiner/Writer run again on feedback,
replacing current results. Reviewer replaces `latest_review` and explicitly appends
a new `review_history` list. Original documents and candidates survive revisions;
validated review-discovered candidates are added by the Refiner.

`MAX_REVISIONS=3` permits three revision passes after the initial review, at most
four reviews total. The graph takes this setting from `Settings` when built and
initializes it together with a zero counter; incoming stale counters/history are
reset for a fresh invocation. Its independent LangGraph recursion limit is
`10 + 4 * max_revisions`, allowing every planned pass plus completion. Explicitly
overriding that runnable configuration with a smaller limit can still interrupt a run.

| Latest review | Completion status | Termination reason |
| --- | --- | --- |
| `accepted` | `complete` | `accepted` |
| `accepted_with_unresolved` (only source ambiguities) | `complete_with_unresolved` | `source_ambiguity` |
| `needs_revision` with no revision budget left | `incomplete_review` | `revision_limit` |

Actionable findings or missing candidates require `needs_revision`. Genuine source
ambiguity alone does not consume revision attempts or demand invented decisions.
The completion update separates `unresolved_source_issues` and
`unresolved_quality_issues`; unincorporated missing candidates remain in
`latest_review.missing_candidates`. Review history and unresolved conflict records
are preserved for the formatter. Earlier corrected quality findings remain
in history, rather than contaminating the latest result.

Building/importing the graph makes no API calls. Explicitly invoking it runs the
LLM stages and requires configured credentials, unless a mocked client is injected.
Graph construction enforces at least three distinct configured model names, even
when mocked. Owned node clients close after use; an injected client is caller-owned.

All graph tests use mocked API responses and actual node implementations, including
loader traversal and LangGraph conditional routing. They exercise initial acceptance,
feedback/state replacement, missing-candidate recovery, source-only termination,
the default three revisions and longer configured limits. See [design notes](docs/design.md).

The reviewer currently sends the complete corpus/state in one request. Large inputs
may exceed endpoint limits and fail explicitly. Quality judgments and classification
of source ambiguity remain model-dependent; deterministic validation proves record
integrity, not semantic correctness. Full live evaluation results appear below.

### Explicit live smoke test (uses API credits)

After configuring `.env`, select one to three exact relative filenames:

```powershell
.\.venv\Scripts\python.exe -m requirements_refiner.extraction_smoke data/corpus --document "<relative-filename>"
```

Replace the placeholder with a supported filename. Repeat `--document` for up to
three selections. The script loads the corpus locally but sends only selected
documents to the API, displays the configured model and candidate count, and
returns a nonzero status on error. It does not print credentials or save a final
requirements document. Tests never invoke this command or make live API calls.

## Run the complete network

After installation and environment configuration, run from `Task_1`:

```powershell
.\.venv\Scripts\python.exe -m requirements_refiner.cli data/corpus --output output/requirements.md --run-directory output/full_run
```

This explicitly invokes the configured live API for the corpus and consumes credits.
It is not run by imports, installation or automated tests. The equivalent installed
command is `requirements-refiner data/corpus --output output/requirements.md --run-directory output/full_run`.
Use `--help` for all options. An example with overrides is:

```powershell
.\.venv\Scripts\python.exe -m requirements_refiner.cli data/corpus --output output/requirements.md --max-revisions 2 --env-file .env --run-directory output/new_run
```

`--extractor-model`, `--refiner-model`, `--writer-model` and `--reviewer-model`
override environment values while preserving the at-least-three-model rule.
CLI options take precedence over environment variables, which override `.env`.
Input and output paths remain dynamic. The CLI reports completed nodes, source and
retained/discarded requirement counts, review status and output path without printing
the full document or secrets. Errors go to stderr.

| Exit code | Meaning |
| --- | --- |
| 0 | Document written; review accepted, possibly with disclosed source ambiguities |
| 1 | Input, API, structural validation, or filesystem failure |
| 2 | Invalid CLI arguments or invalid configuration values |
| 3 | Document written with actionable quality defects or coverage gaps after the revision limit |
| 130 | Interrupted by the user |

The implementation includes complete document generation. Full-corpus execution
uses the compact, checkpointed mode described below.

For a diagnostic retry after a failed refinement response,
`build_graph(settings, llm=client, entry_point="refiner")` accepts a saved complete
state without reloading or re-extracting. Supply its original documents/candidates,
current requirements, latest review/history and existing revision counters; this
entry point does not reset the review budget. The default entry remains Loader.
`scripts/verify_small_live.py` supports an explicitly selected one/two-document
live run and saved-refiner recovery, saving copied evidence, responses and counts
under an ignored output directory. It uses no automatic request retries and
limits review revisions to one. It is a diagnostic tool, not the full-corpus CLI.

## Document format and output safety

The deterministic Formatter validates the complete candidate ledger, requirement
keys, priorities, original evidence unions, blacklist, latest review, revision counters
and completion status before writing anything. Structural errors prevent output;
semantic review findings remain visible in the document. It reuses the existing
cross-record validators and revalidates Pydantic records to catch invalid mutations.

The single UTF-8 Markdown document contains overview/counts/status, the established
priority scale, detailed requirements, glossary, blacklist, unresolved source and
quality issues, traceability summary and a source inventory. Requirements include
names, descriptions, type, priority basis/rationale, candidate lineage and exact
evidence excerpts. Source locations always refer to normalized text; email links
open the raw source file without claiming raw-file line-number anchors.

Final readable IDs (`REQ-001`, etc.) are assigned by sorted stable internal key.
The separate `final_requirement_ids` mapping is used by all cross-reference sections
and returned in graph state. Internal keys remain visible separately. IDs are
deterministic for the same retained set but can shift when that set changes.
Traceability and detailed entries are rendered from the same validated records.
Markdown metacharacters and HTML in supplied fields are escaped; source links use
URL-encoded relative paths (file URIs if Windows drives differ). Output paths must
use a `.md` extension.

Parent output directories are created as needed. The complete document is written
to a temporary file in the destination directory, flushed, then atomically replaced.
A failed write leaves the previous output intact and cleans up the temporary file.
The graph preflights output safety before API calls and checks again before writing.
Input corpus files, including detected hard-link aliases, cannot be overwritten.

By default output inside the corpus is rejected. `--allow-output-in-corpus` permits
a NEW Markdown path there; it is explicitly excluded from loading. Existing files
inside the corpus are never overwritten, even when they may be previous output.
Choose a fresh name or keep output outside the corpus. Other generated documents
already inside the corpus cannot be recognized reliably; use a dedicated source
directory. Previously existing outputs outside the corpus may be atomically replaced.

For programmatic use, provide `output_path` to `graph.invoke`. Omitting it retains
the document in `final_document` without writing a file, preserving offline graph
inspection/testing. No API call occurs in the Formatter itself.

Run all offline tests with `.\.venv\Scripts\python.exe -m pytest -q`. They cover
real graph/node execution with mocked LLM responses, feedback and termination,
multiple sources, final IDs, traceability, blacklist/glossary, Markdown escaping,
structural rejection, CLI parsing/exit codes and atomic output failure handling.

## Budgeted, recoverable full-corpus mode

For the full corpus, use:

```powershell
.\.venv\Scripts\python.exe -m requirements_refiner.cli data/corpus --output output/requirements.md --run-directory output/full_run
```

`python scripts/run_full.py` is a convenience equivalent using the same defaults.
This mode keeps the six logical nodes and actual LangGraph conditional feedback.
`CompactLLM` is an optional wire adapter: model-facing IDs are short aliases and
original source references are catalogued once. The application restores full
identifiers and exact evidence before existing validators run. The refiner outputs
candidate groups and rejection reasons; source unions, original blacklist text and
the complete disposition ledger are constructed deterministically. The model still
decides semantic grouping, rejection, priority and conflict interpretation.

For more than 36 candidates, the refiner first makes a complete, validated topical
partition (at most 36 candidates per batch). Each batch produces distinct atomic
requirements rather than an omnibus summary. The partition covers every candidate
exactly once, including reviewer-discovered candidates; global feedback is projected
without reintroducing out-of-batch candidates. Explicit reviewer duplicate targets
are co-located deterministically; the refiner still decides whether/how to merge.
The global reviewer checks cross-batch
duplication, contradictions and completeness. The original global structural
validator checks the assembled requirements, dispositions and exact evidence.

Writer requests contain only editable prose and terminology, in batches of 20
requirements. The complete original corpus, all candidates and current requirements
remain available in the global reviewer request. Reviewer source text is numbered;
new evidence selections are copied from authoritative normalized lines. No source
document is truncated or excluded to save cost. Global refiner/reviewer inputs
remain subject to context limits for substantially larger corpora.

Stage output allowances are 24,000 extraction tokens, 16,000 refinement-planning
tokens, 24,000 per refinement batch (96,000 for a direct unbatched refinement),
12,000 per writer batch and 48,000 review tokens. At most three review revisions
are allowed (a smaller configured maximum is respected). These are upper allowances,
not compulsory output lengths. Full-run transport retries are disabled; structured
validation permits three attempts, with the rejected answer and exact failed
constraint supplied for repair. A truncated full-run response stops immediately
for a batching/output-limit adjustment instead of repeating the same allowance.

`run_support.py` maintains a persistent usage ledger and request cache. Each request
is reserved on disk before sending. Conservative input estimates use UTF-8 byte
length plus protocol headroom, long-context price margins and the bounded output
allowance. The request is refused if the conservative context or cumulative EUR 30
budget estimate would be exceeded. Unknown model prices also stop the run.

Pricing assumptions, per million uncached input/output tokens, verified 2026-10-25:

| Model | Input USD | Output USD | Source |
| --- | ---: | ---: | --- |
| gpt-5-mini | 0.25 | 2.00 | [OpenAI](https://developers.openai.com/api/docs/models/gpt-5-mini) |
| gpt-5.6-luna | 0.20 | 1.20 | [OpenAI](https://developers.openai.com/api/docs/models/gpt-5.6-luna) |
| gpt-5.4-nano | 0.20 | 1.25 | [OpenAI](https://developers.openai.com/api/docs/models/gpt-5.4-nano) |
| gpt-6-luna | 0.10 | 0.50 | [OpenAI](https://developers.openai.com/api/docs/models/gpt-6-luna) |

Currency conversion uses the 2026-10-23 [ECB reference](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html)
of USD 1.1193 per EUR, plus 25% headroom. Estimates ignore cached-input discounts
and are not account billing limits or exact card charges. Unknown-usage failures
retain their full reservation. Taxes, FX changes and provider billing may differ.

Run data is stored under the selected directory: immutable successful stage
snapshots, an atomic current checkpoint, raw completion caches and a usage ledger.
Snapshots include scalar counters, latest review, complete history and next node.
On restart the runner checks source hashes, model configuration and output path,
then resumes the failed stage. Cached completed responses are replayed locally
without billing, including successful extraction chunks and writer batches within
a failed node. Existing checkpoints and raw responses are not overwritten.
If a matching validated extraction from the earlier small-scale verification is
available, it is reused only after checking original source content and evidence.

Use the same command/run directory to resume. Do not run two processes against the
same directory concurrently. A completed checkpoint is preserved on repeat invocation.
Run artifacts stay local. Live requests send source text and intermediate records
to the configured API. No credentials enter graph state, snapshots, request cache
keys or the usage ledger.

## Full-corpus evaluation

The completed run processed all 20 documents and 22 chunks. It extracted 539 initial
candidates and incorporated nine more from review. Final accounting contains 548
candidates, 497 retained requirements, 35 merged contributors and 16 discarded
candidates in 14 blacklist entries. Four reviews and three revisions ended with
`incomplete_review`: 16 actionable findings and two source ambiguities remain.
They are disclosed in the generated document; it needs semantic review before
being treated as an approved specification.

Reported usage was 1,813,750 input and 463,786 output tokens across 169 usage-confirmed
requests. Two further interrupted requests have unknown usage and retain maximum
reservations. The total estimate including those reservations and 25% headroom is
EUR 1.464. No further review revision was run after the configured limit.

The final suite passed 173 tests. Offline verification confirmed 497 unique final
IDs, 1,241 working source links, exact agreement with validated rendering, unchanged
hashes for all 20 sources and no API key in generated files. The completed-run CLI
returns code 3, correctly signalling remaining quality defects without making new
API requests. See [requirements](output/requirements.md) and the
[assignment report](docs/report.md). The final requirements document is visible to
Git; local caches, logs, snapshots and credentials remain ignored.
