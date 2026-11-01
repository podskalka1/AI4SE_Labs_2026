# EventTicket ADR review notes

## Current state

- Date: 2026-11-01.
- Phase: initial draft and author review complete; user review pending.
- ADR: [ADR 001](ADR_001_EventTicket_architecture.md), status **Proposed**.
- Sources: [requirements](../../data/EventTicket.txt), [new architecture conversation](architecture_conversation_notes.md).
- Preference: A, modular application with synchronous initial allocation and durable background notifications/payment recovery. This is a design preference, not formal adoption.
- Open issues: expiry policy and other business rules, provider capabilities, implementation choices and measurable service/recovery objectives.
- Next step: user review of commitments, completeness and technical depth; revise on feedback.
- Resume: provide `Week_05_Designing/Tasks/output/skill_test/`.

## 2026-11-01 — Draft requested, written and reviewed

The user requested a brief challenge to A, then a conventional, reasonably concise Proposed ADR with a Mermaid diagram, comparison, commitments, trade-offs and open rules/implementation choices. Exact expiry policy must remain unresolved; either policy must preserve capacity, ticket uniqueness and payment tracking. Initial booking must remain synchronous, with durable background recovery and notifications.

Challenge outcome: B would be preferable if independent ownership/releases or demonstrated scaling/isolation needs justified distributed overhead. C would be preferable if asynchronous booking acceptance or separate query scaling became necessary. Neither is established by the current requirements. Continued with A as the proposed recommendation; no adoption or implementation claimed.

Created ADR 001 in this isolated directory (no prior ADR here; did not inspect or renumber the previous-work ADR). Kept sales data in one local transaction boundary; specified durable recovery outcomes without selecting a broker, database, locking algorithm or provider. Included security responsibilities and all source capabilities, the three difficult purchase scenarios, comparison and reconsideration triggers. Expiry policy remains open, superseding any suggestion that a policy choice is needed before drafting the architecture.

Author review checked status/wording consistency, source-story traceability, separation of assumptions from user-added requirements, alternatives' overlap, local versus external transaction limits, duplicate-safe recovery obligations and file references. Diagram source was inspected for boundaries/labelled flows and agreement with prose. Rendering capability is checked separately; no visual rendering or implementation test is claimed. User review has not occurred; no mandatory revision round imposed.

Delivery checks: all ADR relative file links resolve; status is Proposed; one Mermaid block is present. Mermaid CLI (`mmdc`) is unavailable, so diagram source inspection was performed without visual rendering. No implementation tests or benchmarks were run for this documentation-only evaluation.
