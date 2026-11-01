# Task 2: EventTicket ADR discussion notes

Started: 2026-11-01. Continue updating this file for the ADR discussion and subsequent revisions until the user asks to stop. These are summary notes rather than a verbatim transcript.

## User request

Create a separate Markdown ADR in the output folder covering context, alternatives, reasons for choosing a modular monolith with durable background workers, and accepted trade-offs. Use a conventional structure that another developer can understand without reading the full conversation, with sufficient detail but no unnecessary length. Rename the original discussion notes to Task_1_conversation_notes and begin a new record for this discussion.

## Work completed

- Read `../Task_2.md` and reviewed the final architectural conclusions from Task 1.
- Renamed `EventTicket_conversation_notes.md` to `Task_1_conversation_notes.md`, preserving the existing discussion.
- Created `ADR_001_EventTicket_architecture.md` with status, date, context, decision, alternatives, consequences, validation/review criteria and related records.
- Marked the architectural decision Accepted based on the user's request to document our decision; the wording and layout remain open to review. No implementation or technology stack selection is implied.

## Reasoning captured in the ADR

Keep the cohesive purchase core local to simplify consistency and testing. Use explicit module interfaces and owned tables; short database transactions protect capacity and reservations. External payments still require idempotency, verified callbacks, reconciliation and durable refund recovery. Use durable workers for secondary/retryable work, initially with a database-backed queue; an external broker is optional.

The alternatives table distinguishes application boundaries from communication style: event-driven web-queue-worker overlaps with the modular monolith and is adopted selectively, rather than presented as a wholly separate structural alternative. Microservices are deferred until measured scaling, team ownership or isolation requirements warrant their cost.

Accepted costs include coordinated releases, shared failure domains, hot-inventory contention, enforcement of module boundaries, delayed background results and operational recovery. The ADR includes focused failure/concurrency testing and explicit review triggers. Pre-sale, seating, hold/refund rules and load/availability targets remain unresolved business questions.

## Review status

Initial ADR created for user review. No user-requested revisions yet. Continue appending requested changes and their rationale here while retaining Task 1 notes as the previous discussion record.

## Revision 1: architecture overview and clearer alternatives

The user found the Decision section dense and requested a simple Mermaid diagram showing browser, backend modules, database, workers and payment provider, plus brief request/background flow explanations. They also requested a clearer relationship between options 1 and 3 without complicating the comparison.

Added an architecture overview inside Decision, showing web-process module calls and separately running workers within one backend codebase. Both use the shared relational database, including its durable jobs. The diagram includes provider callbacks, worker payment reconciliation/refund recovery and external email delivery. It deliberately shows no external broker because the initial design uses a database-backed queue. Worker database access represents job handling and persistence through the application modules, not bypassing module ownership.

Added short request-flow and background-flow paragraphs and grouped the existing detailed rules under Implementation constraints. Reworked the alternatives table around each approach's contribution and relationship to the decision: adopt option 1's structure, defer option 2, and adopt option 3 selectively within the monolith. Deferred broker fan-out and queued reservations remain explicit. Architectural scope/status and the existing reliability constraints are unchanged.

Revision delivered for user review; continue recording further requested changes here.

## Revision 2: architectural scope and proposal status

The user questioned prescribing a database-backed queue without technology evaluation, listing concurrency techniques without selecting one, and marking the ADR Accepted during design evaluation. They requested a less prescriptive revision while retaining reliability requirements.

Changed status to Proposed and explicitly stated that the preferred design remains under evaluation, without formal implementation approval. Earlier Accepted status was an assistant inference from the request to document the decision; it is superseded. Proposed versus Accepted reflects adoption status, not whether every implementation detail is settled.

Retained the architectural commitments: modular backend, shared relational business database, cohesive local purchase transactions and durable background work. Replaced queue-specific commitments and concurrency technique prescriptions with outcome requirements: atomic capacity allocation, no silently lost scheduled work, safe repeated processing, controlled retries and recovery visibility. Kept payment verification, idempotency, reconciliation and expiry/refund handling because they protect correctness across the external provider boundary.

Added Implementation choices left open: evaluate row locking versus conditional updates, database-backed jobs versus broker messaging, and detailed worker/retry/deployment mechanisms. Transactional job records and outbox are examples rather than mandated designs; unreliable database-plus-queue dual writes remain unacceptable. Updated the diagram to show a logical durable-work capability with mechanism TBD, separating it from the business database without implying a separate physical service. Revised background-flow text and alternatives wording consistently. Renamed accepted-risk wording to costs and risks of the proposal.

No queue technology or concurrency algorithm has been selected. Notes preserve earlier revisions as history; this entry describes the current ADR status and scope.
