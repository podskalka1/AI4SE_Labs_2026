# Agentic Software Requirements Refinement

## 1. Introduction

This project implements an agentic network that converts a directory of software
descriptions into one structured requirements document. The input combines an
early specification, interviews, surveys, meeting minutes and email discussions
about library management and reporting. These sources contain overlapping requests,
background information and unresolved business decisions. The network extracts
requirements, consolidates them, checks their quality and preserves their provenance.

The full corpus was processed using Python and LangGraph. The resulting document
is [output/requirements.md](../output/requirements.md). Execution completed, but
the final review remains **incomplete**: outstanding quality defects are disclosed
rather than presented as resolved.

## 2. Architecture and model selection

The implementation separates six logical responsibilities:

| Node | Implementation | Responsibility |
| --- | --- | --- |
| Corpus Loader | Deterministic Python | Recursively read text, Markdown and email; preserve source identity and normalized evidence locations |
| Requirements Extractor | `gpt-5-mini` | Extract functional/nonfunctional candidates with supporting source selections |
| Requirements Refiner | `gpt-5.6-luna` | Consolidate candidates, identify conflicts, assign priorities, maintain glossary, dispositions and blacklist |
| Requirements Writer | `gpt-5.4-nano` | Produce descriptive names and paragraph explanations while preserving authoritative metadata |
| Requirements Reviewer | `gpt-6-luna` | Assess OS2–OS9 against the original corpus and current results; request specific corrections |
| Document Formatter | Deterministic Python | Validate structure, assign final IDs and atomically write UTF-8 Markdown |

These are the actual configured models used in the full execution; none was
substituted. Local extraction is separated from global consolidation. Prose writing
is isolated so it cannot modify priorities or provenance, while a different model
provides an independent review. The smaller writer handles constrained presentation
work. Model choices were verified through live API calls, but no comparative model
benchmark was performed. Deterministic validation complements, rather than replaces,
model-based semantic judgments.

## 3. LangGraph orchestration

The main path is `Loader → Extractor → Refiner → Writer → Reviewer`. Conditional
edges return actionable findings to the Refiner through a deterministic revision
counter node. Accepted results, source-only ambiguities, or exhaustion of the
revision allowance lead through completion classification and the Formatter to END.

The initial pass does not count as a revision. At most three additional refinement
passes and four structured reviews are allowed. LangGraph's separate recursion
limit accommodates these passes. Source ambiguities can terminate without an
invented business decision; actionable defects remaining at the limit produce
`incomplete_review`. Current collections are replaced on revision, while source
documents, candidate lineage and review history are preserved.

## 4. Requirements processing

The loader reads UTF-8 files recursively and uses Python's email parser for `.eml`
bodies. Relative filenames determine stable document IDs. References use one-based
inclusive lines of normalized extracted text, not purported raw-email line numbers.
The extractor processes every chunk with bounded overlap. Models select evidence
coordinates; the application copies exact source lines and rejects invalid locations
or supplied quotations. Candidate IDs are deterministic hashes of canonical records.

Full-run mode uses compact aliases and a shared evidence catalog to avoid repeatedly
transcribing quotations. Large refinements are partitioned into batches of at most
36 candidates, with exact partition coverage checked. Explicit reviewer duplicate
targets are co-located, but the model still decides whether their meanings should
be merged. A global reviewer sees the complete corpus and resulting collection,
including cross-batch requirements. This preserves global review scope without
requiring one enormous refinement response.

Every incorporated candidate belongs to exactly one retained requirement or
blacklist entry. Each retained group has one representative disposition; other
contributors are marked merged. Complete original evidence unions and original
rejected statements are restored deterministically. Merging is not rejection.
The glossary supplies shared terminology. Priorities use **P1 Critical**, **P2 High**,
**P3 Medium** and **P4 Low**, with rationale and an explicit/inferred flag; the full
definitions appear in the output.

The Writer edits only names and descriptions, in batches of 20. The application
merges those fields into copies of authoritative requirements. Reviewer targets,
evidence, status consistency and newly discovered candidates are validated. The
Formatter rechecks ledger coverage, source references, keys, priorities, history
and termination state before generating final IDs and traceability tables.

## 5. Assignment compliance

| Network specification | Implementation evidence |
| --- | --- |
| ANS1: at least three LLM nodes | Four separate LLM-invoking nodes |
| ANS2: deterministic node | Loader and Formatter; deterministic routing bookkeeping |
| ANS3: feedback loop | Reviewer conditional edge triggers Refiner/Writer/review revision |
| ANS4: three distinct models | Four configured models, all invoked in live execution |
| ANS5: Python LangGraph | `StateGraph`, typed shared state, ordinary and conditional edges |

| Output specification | Implementation and observed limitation |
| --- | --- |
| OS1: single document | One generated Markdown requirements document |
| OS2: unique IDs | 497 unique readable final IDs, with separate internal keys |
| OS3: semantic deduplication | Refiner grouping and global review; ten duplicate-group findings remain |
| OS4: traceability | Validated document IDs, normalized line ranges and exact excerpts; all 20 sources represented |
| OS5: names and explanations | Writer presentation schema and deterministic metadata merge |
| OS6: priorities | Documented scale, rationale and inference flag; two priority findings remain |
| OS7: consistency | Glossary, conflict records and review; four further semantic findings and two source ambiguities remain |
| OS8: completeness | All chunks processed; reviewer added nine candidates; no final pending candidates, but completeness is not proven |
| OS9: blacklist | 14 entries preserve 16 rejected candidates, statements, evidence and reasons |

## 6. Evaluation and execution results

The corpus contained **148,942 bytes**, or **143,412 normalized characters**, and
produced 22 extraction chunks. One unchanged document's validated extraction was
reused from the small-scale test; the other chunks were processed live. Recovery
used saved state and request caches rather than restarting extraction.

| Measurement | Actual result |
| --- | ---: |
| Source documents processed | 20 |
| Initial extracted candidates | 539 |
| Additional candidates incorporated from review | 9 |
| Final accounted-for candidates | 548 |
| Retained requirements | 497 |
| Merged candidate dispositions | 35 |
| Blacklist entries / discarded candidates | 14 / 16 |
| Structured review passes / revision passes | 4 / 3 |
| Final status | `incomplete_review` |
| Outstanding quality findings / source ambiguities | 16 / 2 |
| Automated tests | 173 passed |

All 548 dispositions are accounted for: 497 retained representatives, 35 merged
contributors and 16 discarded candidates. Deterministic validation confirmed unique
final IDs, complete source-reference preservation, valid ledger destinations and
consistency between the generated document and validated state. Source hashes
confirmed that none of the 20 input files changed.

The final Reviewer identified ten duplicate-group findings, two priority findings
and four other semantic findings. Examples include an incorrect transfer-reversion
condition and unsupported WorldCat integration or exact operating-system-version
mandates. Two genuine source questions remain: whether the delivery address book
is mandatory or optional, and how branch capacity should be defined. These findings
remain visible in the output; they were not silently accepted as corrected.

The execution initiated **171 API requests**. Usage was reported for 169; two
interrupted requests have unknown usage and retain conservative cost reservations.
Reported usage totals **1,813,750 input tokens** and **463,786 output tokens**
(**2,277,536 combined**), excluding the previously paid extraction reused from 6A.
The cumulative estimate is **€1.464**, including a 25% margin and both unknown-usage
reservations, below the €20 target and €30 authorized estimated ceiling. This is
not an exact invoice or provider-enforced billing cap.

The ledger uses published model-specific input/output prices, ignores cached-input
discounts conservatively, and uses the 23 October 2026 ECB reference of USD 1.1193
per EUR. Pricing sources: [Extractor](https://developers.openai.com/api/docs/models/gpt-5-mini),
[Refiner](https://developers.openai.com/api/docs/models/gpt-5.6-luna),
[Writer](https://developers.openai.com/api/docs/models/gpt-5.4-nano),
[Reviewer](https://developers.openai.com/api/docs/models/gpt-6-luna),
and [ECB reference rates](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html).
The run directory retains state snapshots, raw response caches and the usage ledger.

## 7. Reproduction and limitations

After installing the project and configuring the ignored `.env`, run from `Task_1`:

```powershell
python -m requirements_refiner.cli data/corpus --output output/requirements.md --run-directory output/full_run
python -m pytest -q
```

The same run directory resumes a failed stage or preserves a completed run. Recovery
checks source hashes, model configuration and output path. Request reservations
precede each API call; unknown prices or conservative context/budget overflow stop
execution. API credentials are excluded from graph state, caches and generated
deliverables. Serial execution is required for a run directory.

The network addresses every assignment specification, but model-based evaluation
does not establish perfect semantic completeness or consistency. Topic batches can
leave cross-batch duplicates, and repeated rewriting can reintroduce priority or
interpretation errors. The current output therefore needs manual semantic review
before being treated as an approved specification. Future improvements should apply
review corrections as targeted patches, strengthen cross-batch consolidation and
benchmark model choices, while retaining the existing provenance and validation.

## 8. Conclusion

The implementation demonstrates a working multi-model LangGraph requirements
network with live feedback, complete candidate accounting and deterministic document
generation. Full-corpus execution and structural validation succeeded within the
authorized budget. Its final review did not pass: the disclosed semantic defects
and unresolved business questions define the practical limits of this evaluation.
