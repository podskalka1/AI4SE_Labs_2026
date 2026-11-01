# EventTicket architecture conversation notes

## Current state

- Date: 2026-11-01.
- Phase: recommendation documented; Proposed ADR drafted for user review.
- Requirements source: [EventTicket.txt](../../data/EventTicket.txt), system description and user stories 1–20.
- Method: [architecture-dialogue skill](../../../../../.agents/skills/architecture-dialogue/SKILL.md).
- Output directory: `Week_05_Designing/Tasks/output/skill_test/`.
- Preference/status: user favors A and assistant recommends it under current evidence; design remains Proposed, not formally adopted. No implementation undertaken.
- ADR: [ADR 001](ADR_001_EventTicket_architecture.md); drafting/review tracked separately in [ADR review notes](adr_review_notes.md).
- Open questions: release capacity at expiry and refund late payments versus retain capacity during payment uncertainty; payment/refund provider capabilities and escalation policy; availability and recovery objectives. Traffic and team size remain deliberately unspecified.
- Next step: review the Proposed ADR and revise on feedback; exact expiry policy remains deliberately unresolved.
- Resume context: provide this output directory; continuity resides in these files.

## 2026-11-01 — Independent requirements analysis and initial alternatives

### Request and source boundaries

The user requested a fresh evaluation of at least three architectures, their trade-offs and difficult implementation work, followed eventually by a justified recommendation and ADR review. All artifacts belong here, separate from prior work. No previous architecture discussion notes or EventTicket ADR were read or used. The unrelated requirements document and task file visible in the IDE were not used. Read the actual EventTicket source and skill file; no applicable AGENTS.md was found in checked ancestor/task/output paths.

### Explicit requirements

- Visitors explore the application and events, register and log in (stories 1–4).
- Registered users access personal data, select favourite categories and receive related event emails, see pre-sales and purchased tickets, book pre-sales, purchase/pay online and obtain ticket codes (5–11).
- Managers view their proposed events and publish new events (13–15); admins add managers (17).
- Role-specific personal pages and logout, plus password recovery (12, 16, 18–20).
- The source supplies no numeric performance, availability, workload, budget, deployment or team constraints.

### Assumptions and gaps

- A payment provider and email delivery service are illustrative external dependencies, not selected providers or mandated integrations.
- Finite inventory and preventing overselling are conditional assumptions to test, not explicit source requirements. Assigned seats, refunds, cancellation, approval workflows and gate scanning are unspecified.
- Pre-sale could mean a capacity reservation, early paid sale, or registration for later sale. Its effect on inventory and expiry is unresolved.
- A proposed correctness rule is to issue a valid ticket only after verified payment, and avoid duplicate business effects on retried requests/callbacks. This requires agreement; it is not a quoted requirement.
- Password recovery, manager authorization and protection of personal data require security design; source gives no detailed policy or regulatory commitments.

### Alternatives explained

**A. Modular single application with a shared transactional database.** One backend deployment contains identity/access, catalog/publishing, booking/payment, tickets and preferences modules. Modules own logical tables within one database and call each other directly. A background worker, using the same codebase/store, sends email and resolves unfinished payment work. Browser calls are synchronous; payment/email cross external boundaries. Example purchase: atomically record an order and, if required, reserve capacity; initiate payment outside the database transaction; verify payment outcome and atomically finalize the order/ticket; deliver notification asynchronously. Benefits: local transaction boundaries and fewer deployment components. Costs: shared database/application bottlenecks, coordinated releases and broader failure impact. Hardest work: concurrency, uncertain payment outcomes, secure access and maintaining module boundaries. Database transactions cannot include an independent payment provider. Recovery requires durable state, duplicate handling and payment reconciliation. Test competing purchases, repeated callbacks and crashes around payment/finalization; operate with database recovery, pending-order monitoring and notification retries. Customers get prompt local results, but may see payment pending during external uncertainty.

**B. Independently deployed domain services with private data ownership.** Identity, catalog, sales (inventory/orders/tickets kept together), and notification capabilities are separate services/stores. Network APIs handle interactive requests and payment initiation; durable events carry sales/category notifications. Keep sales correctness in one local transaction boundary; avoid distributing inventory, orders and tickets merely to create services. Example purchase: UI queries catalog, submits to authoritative Sales; Sales validates sale eligibility, reserves capacity if needed and records the order, initiates payment, finalizes after verified outcome and emits notification work. Catalog changes/eligibility require an explicit synchronization/authority policy. Benefits: independent ownership/releases and targeted scaling. Costs: network dependencies, stale copies, more deployments and tracing/recovery work; separate services do not ensure failure isolation. Hardest work: contracts, publication reliability and cross-service consistency. An event and its state change must not be silently separated by a crash; durable publication/replay is needed, mechanism open. A notification outage need not block a sale, but Sales/store failure still blocks booking. Test service contracts, duplicates, missing/delayed events and network failure; monitor service health, delivery lag and unfinished sales. Customers may see delayed ticket-history views if those use replicated data; authoritative order status remains necessary.

**C. Durable queued booking with authoritative processing and separate read views.** An API durably accepts booking commands and returns an operation identifier; workers process orders/payment/ticket transitions. A sales write store owns truth; separate query views serve event discovery, personal history and preferences. Catalog/identity may remain ordinary application modules; this is an execution/data-flow choice rather than necessarily a service-per-domain design. Commands/events cross durable asynchronous boundaries; users query status or receive updates. Example purchase: command accepted, shown as processing (not reserved or paid), worker checks authoritative eligibility/capacity and records the outcome, payment proceeds with verified results, ticket is finalized, read views catch up. Ordering work by event is one possible technique, not a selected commitment; it can also create hot-event bottlenecks. Benefits: explicit durable workflows and demand buffering, independently optimized query views. Costs: additional states, delayed acceptance/rejection, queue/read-view operations and backlog management. A queue does not add processing capacity. Hardest work: duplicate-safe transitions, payment recovery, worker ordering and view rebuilding. Worker crashes can cause redelivery; durable deduplication/state transitions are required. Email/projection failures should not undo a finalized sale. Test replay, redelivery, concurrent workers, stale views, backlog and payment ambiguity; monitor oldest command age, queue depth and projection lag, and recover stalled work. Customers see pending work and may wait before learning that capacity is exhausted.

### Comparison and relationship

All three need secure access, concurrency-safe sales, verified payment, recoverable external effects and clear customer status. A emphasizes a shared transaction/deployment boundary; B emphasizes independent service/data ownership; C emphasizes asynchronous command execution and separate query models. They overlap: A can have background jobs, and B can use C's queued workflow. Merely adding an email queue does not turn A into C. No technology, provider, locking algorithm or hosting platform has been selected.

A has fewer operational pieces but shared scaling/failure boundaries. B permits independent scaling and releases at the cost of distributed contracts and consistency. C buffers bursts and supports explicit recovery but adds delay, backlog and read-model complexity. No unsupported traffic or reliability targets, numeric scores, recommendation or adopted choice were introduced.

### Questions for the next turn

1. What does a pre-sale grant, and do pre-sales and purchases consume limited capacity (general admission or assigned seats)?
2. If payment is slow or its result unknown, is a pending state acceptable, and should inventory be held while resolving it?
3. What demand pattern and delivery/operations team should the design accommodate? Unknown values can remain open; no invented estimates are needed.

Next discussion should test whether the benefits of independent deployments or queued acceptance justify their costs under the user's answers. No ADR or ADR-review notes created yet.

## 2026-11-01 — Purchasing failure scenarios and provisional comparison

### User guidance

- Evaluate pre-sales as temporary reservations of limited capacity, explicitly an assumption rather than a confirmed source requirement.
- Pending payment status is acceptable. User requires eventual resolution without overselling or leaving a customer charged without a ticket or refund. This extends the source requirements for this evaluation.
- Leave traffic and team size unspecified; do not invent estimates.
- Compare competing purchases for the last ticket, confirmation after reservation expiry, and failure during issuance, including complexity and significant trade-offs.

### Common correctness and recovery requirements

Under the capacity assumption, active holds plus sold tickets must not exceed capacity. Availability displays are advisory; the authoritative sales write must decide allocation atomically. Retried requests, payment notifications and recovery work must reuse stable operation/payment identities and avoid duplicate business effects. Separate payment state from reservation and ticket state: an expired reservation does not prove a charge failed.

Two valid expiry policies remain open: (1) release capacity at expiry and refund a verified late successful payment unless capacity can be atomically reacquired, or (2) retain capacity while payment is uncertain, accepting reduced availability and potentially long holds. For release-at-expiry, expiry and confirmation must compete through one authoritative conditional state transition; a late callback cannot revive a released hold blindly. Callback arrival time and provider payment time differ; even a payment made before expiry may need refund if its capacity was already reassigned. No expiry duration selected.

The eventual outcome is a durable recovery obligation, not a guarantee of bounded completion during permanent provider unavailability. Persist unresolved payments/refunds, reconcile provider state, retry safely, alert on age/failure and support operator intervention. External refund capability, duplicate-safe requests and status lookup must be evaluated; no provider or mechanism selected. Pending, ticket-ready and refund-pending must be distinguishable to customers.

### Scenario comparison

**Last ticket.** A atomically checks/claims capacity and records the hold/order in its shared database; one purchase succeeds and the other gets sold out. B can enforce exactly the same local invariant because Sales owns inventory/orders/tickets together; catalog caches cannot grant capacity. It adds network timeout/retry ambiguity requiring an order lookup and stable request identity. C durably accepts both commands, but acceptance grants no capacity. The authoritative worker transition allocates to one; concurrent workers/redelivery still need atomic storage enforcement. Queue order does not inherently promise user fairness or total processing order. Added cost is delayed rejection and backlog handling, without stronger correctness than A/B.

**Payment confirmation after expiry.** All three require an explicit expiry policy and coordination of reservation, payment and refund state. A can atomically arbitrate expiry/finalization in one database, then perform and reconcile refunds outside the transaction. B does the same within Sales; other services consume the result rather than making competing allocation decisions. It adds reliable result publication and potentially stale customer views. C handles expiry and payment as durable work, but message arrival order need not match real-world payment order; processing must recheck authoritative state. Worker lag can delay both confirmation and refunds and must not extend holds accidentally contrary to the agreed policy. Queuing does not remove the late-payment problem.

**Failure during issuance.** Treat ticket issuance as creating a durable entitlement/code in the authoritative sales database; this is a candidate boundary, not a selected external ticket provider. Once payment is verified, commit order finalization, capacity conversion and one ticket entitlement per purchased unit together. Crash before commit leaves no partial local finalization; recovery checks payment and retries. Crash after commit before response returns the same ticket on retry. A supports this locally; B supports it locally inside Sales, with reliable publication needed for notifications/history copies. C supports it locally in the worker, but crash before acknowledging work leads to redelivery and must recover the same entitlement. Email/document rendering should be retryable delivery of an existing entitlement, not create a new ticket. If issuance requires an external system, none of these local transactions can cover it; duplicate-safe external issuance and reconciliation would need separate evaluation.

### Significant trade-offs and assistant assessment

Correctness depends more on authoritative state ownership, atomic transitions and external-effect recovery than on deployment style. For these three scenarios alone, A provisionally offers the best correctness-to-complexity trade-off: it can preserve the sales transaction boundary and run durable recovery jobs without making initial booking asynchronous. B is equally capable within Sales but pays distributed coordination/operation costs for independent ownership and releases, whose value is not established by current requirements. C foregrounds durable recovery and buffers demand, but A/B can also have durable recovery; C adds queued acceptance, delayed outcomes, ordering/redelivery issues and lagging query views. It becomes more attractive if later evidence establishes a need for buffered asynchronous booking or separate query scaling. No performance ranking is claimed without workload evidence.

Most significant unresolved trade-off: prompt capacity release versus avoiding refunds/long pending states when payments are uncertain. No architecture removes this business decision. Next discussion should choose or refine this policy and challenge whether independent deployment or queued acceptance is justified. Provisional assistant preference is not user adoption; no ADR or ADR-review record created.

### Validation cases identified (design only; not executed)

- Two concurrent last-ticket attempts produce at most one active allocation.
- Expiry races with duplicate/late confirmation without reviving already reallocated capacity.
- Crash before/after local finalization and before worker acknowledgement returns the same entitlement on recovery.
- Provider charge/refund success with lost response remains discoverable and does not trigger duplicate effects.
- Unresolved payment/refund age, failed jobs and view lag are observable; recovery does not silently discard obligations.

## 2026-11-01 — Recommendation challenge and ADR request

User judged exploration sufficient, favored A for purchasing guarantees with lower operational complexity, and requested a brief challenge followed by a Proposed ADR if no compelling counterargument emerged. User explicitly left expiry policy unresolved while requiring safe handling of either policy. This supersedes the previous suggested next step of choosing expiry policy before a recommendation; it does not change the historical scenario analysis.

Assistant challenge: B becomes preferable with justified independent ownership/releases or demonstrated scaling/isolation needs; C with a demonstrated need for durable asynchronous booking or separate query scaling. These needs are not established by the source, so recommend A with synchronous initial allocation and durable background notifications/payment recovery. Shared failure/resource boundaries and operational payment-recovery obligations remain significant limitations. No performance claims or traffic/team estimates added.

Created [Proposed ADR 001](ADR_001_EventTicket_architecture.md) and [separate ADR-review notes](adr_review_notes.md). The ADR includes source traceability, module/data/deployment boundaries, diagram, comparison, hard-scenario outcomes, commitments, accepted costs, open business rules/implementation choices and validation/reconsideration triggers. User preference is not formal adoption; no implementation or benchmark performed. Next step is user feedback on the draft, with expiry policy intentionally open.
