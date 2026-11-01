# EventTicket architecture discussion notes

Started: 2026-11-01. These are discussion notes, not a verbatim transcript. Continue updating this file during this conversation until the user asks to stop.

## User request

Read `../data/EventTicket.txt`, propose three architectures, and keep notes in a new file in the output folder. The assignment in `../Task_1.md` calls for discussing architectural trade-offs and difficult implementation details.

## Requirements read

The application supports anonymous event browsing; registration, login, logout and password recovery; user, manager and admin roles; personal profiles; favourite categories and related email notifications; pre-sale bookings; online ticket purchases and ticket codes; purchase and booking history; managers publishing and listing their events; and admins adding managers.

No scale, budget, deployment environment, availability target, seating model, refund policy or precise pre-sale semantics are specified. Do not treat proposed design choices as requirements. Capacity limits, expiring reservations and an external payment provider are useful working assumptions to validate.

## Initial proposals

### 1. Layered modular monolith

Browser -> one backend application -> relational database. Backend modules: identity/roles, events/categories, bookings/inventory, orders/payments/tickets, notifications. Presentation, business logic and persistence form layers within the backend. Background jobs handle email and reservation expiry.

Purchase example: atomically reserve capacity, create a pending order, request payment from an external provider, then process its verified callback to confirm the order and issue a unique ticket code. A database transaction cannot atomically include an external payment operation.

Benefits: simplest deployment, local debugging, straightforward database transactions and low operational overhead. Costs: backend modules deploy together; independent scaling is limited; boundaries can erode without discipline. Difficult parts: concurrent reservations, expiry versus payment races, idempotent callbacks and durable background jobs.

### 2. Microservices organized by business capability

Browser -> API gateway -> identity, event catalogue, booking/order/ticket, payment and notification services. Each service owns its data; avoid direct cross-service database reads. Keep inventory and booking decisions together initially to reduce distributed consistency problems.

Purchase example: booking service reserves stock and records an order; payment service communicates with the provider; confirmed payment triggers ticket issuance. Failures require an explicit workflow and compensating actions, such as releasing reservations or refunding a late payment.

Benefits: independent deployment and scaling, and clear ownership for multiple teams. Costs: network failures, eventual consistency, more infrastructure and harder end-to-end testing. Difficult parts: durable inter-service messages, duplicate processing, workflow recovery, tracing and API evolution. Likely excessive for a small student project without substantial scale or multiple teams.

### 3. Event-driven web-queue-worker architecture

Browser -> web/API application -> transactional database. The API records durable work; a queue routes it to workers for payment processing, ticket issuance and email. This proposal can retain one codebase and database while deploying API and workers separately. Event-driven communication can also be used inside the other proposals; these styles are not mutually exclusive.

Purchase example: API reserves capacity and records a pending order plus an outbox entry in one database transaction. A dispatcher sends the entry to a queue. Workers perform asynchronous work; a verified payment callback advances the order and schedules ticket issuance. The UI displays pending status until confirmation.

Benefits: responsive API, worker scaling and isolation of slow external calls. Costs: broker/worker operations and asynchronous user experience. Difficult parts: atomic database/message handoff (transactional outbox), retries, idempotency, dead-letter handling and out-of-order events. Inventory checks remain transactional; a queue alone does not prevent overselling.

## Initial recommendation

Start with option 1 for the stated requirements and unspecified scale. Add durable jobs for emails and reservation expiry. Consider option 3 if asynchronous processing becomes central, and option 2 when independent team ownership or scaling warrants its operational cost. No architecture has been selected by the user.

## Common implementation concerns and open questions

- Enforce role and event ownership checks on the server.
- Use secure password storage and expiring single-use password-reset tokens.
- Never issue tickets based solely on a browser payment-success redirect; verify the provider callback and reconcile uncertain results.
- Handle concurrent purchases, duplicate callbacks, reservation expiry and payment completion races.
- Clarify whether a pre-sale is an unpaid reservation, early paid access, or a waiting-list entry; this changes the booking lifecycle.
- Clarify general admission versus numbered seats, expected traffic, payment/refund rules and team/deployment constraints.

## Reference material

Architecture definitions and general trade-offs were checked against Microsoft primary documentation. EventTicket-specific mappings and the recommendation are the assistant's design judgment.

- https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures
- https://learn.microsoft.com/en-us/azure/architecture/microservices/
- https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven

## Discussion status

All three proposals have now been explored. The user's preferred conclusion is a modular monolith with durable background workers, supported by the assistant's recommendation. The final comparison and reasoning appear at the end of this file. Earlier statements about selection status describe the discussion at that time. Continue recording any further discussion until asked to stop.

## Follow-up: modular monolith communication and concurrent purchases

The user chose to discuss the modular monolith first; this is not yet a final architecture selection. They asked whether modules call methods directly or use an intermediary, and how transactions prevent two buyers obtaining the last ticket. Requested a conceptual explanation without deep code.

Proposed communication: synchronous in-process calls through each module's public application interface for immediate answers. Modules must not reach into another module's private classes or tables. A small checkout application service can coordinate calls to booking and payment interfaces; it is an ordinary part of the application, not a separate server or mandatory message broker. Keep dependencies directional to avoid circular calls. Use durable background jobs/events for email and other work that can happen after confirmation. Record pending work transactionally with the business change so crashes cannot silently lose it; handlers tolerate duplicates. A shared database permits a short transaction across cooperating modules when they use the same transaction context, but direct method calls do not automatically provide that transaction.

Last-ticket example assumes general admission and one inventory row per event/ticket category. Within a short transaction, lock the inventory row for update before checking remaining capacity. Buyer A locks it, sees one available, decrements availability and inserts a pending reservation/order, then commits. Buyer B's competing locking operation waits; after A commits, B reads zero and cannot reserve. If A rolls back, its changes disappear and B can reserve. Ordinary reads need not block and may display stale availability. Transactions alone, with an ordinary read-then-write at default isolation, do not guarantee this result. All capacity-changing paths must follow the same locking protocol. A conditional atomic decrement is another valid implementation, with affected-row count checked.

Commit both capacity change and reservation creation together. Never hold a database lock while a customer completes payment. The committed reservation holds capacity for a defined duration (policy still unspecified). Payment confirmation converts held capacity to sold capacity without decrementing availability again. Expiry releases a hold once; payment and expiry must coordinate on the reservation's state so only one transition wins. Late payment requires an explicit recovery/refund policy. Unique constraints/idempotency prevent repeated callbacks issuing duplicate tickets. Numbered seating would instead require per-seat ownership/uniqueness rules. A busy inventory row may become a contention point; keep transactions short and retry deadlocks where appropriate.

Database behavior checked against PostgreSQL primary documentation (illustrative database, not a selected technology):
- https://www.postgresql.org/docs/17/explicit-locking.html
- https://www.postgresql.org/docs/18/transaction-iso.html

## Follow-up: popularity, multiple instances and service extraction

User asked whether thousands of buyers for one event make its inventory row a bottleneck, whether multiple monolith instances help or create consistency problems, and how difficult later migration to microservices would be.

The inventory row is a serialization point for competing capacity changes. Thousands of simultaneous attempts can cause lock waits, exhausted database connections and timeouts. Actual throughput depends on measured transaction duration and database workload; no capacity estimate can be inferred from the requirements. Short transactions and conditional atomic decrements reduce overhead but still contend on the same row. Optimistic concurrency can exchange waiting for retries and does not remove contention.

Scale the monolith horizontally behind a load balancer to improve request handling and availability. All instances use the same authoritative inventory database; its locks coordinate across processes. Avoid per-instance inventory copies or in-memory locks for correctness. Keep request handling stateless or share sessions, bound the total database connection count, and make payment callbacks and job claims idempotent. Replicas/caches may serve event descriptions and approximate availability, but reservations must check authoritative data. Additional application instances can worsen database overload if admitted work is unbounded.

For a popular sale, cache browsing, keep reservation transactions short, and use a controlled waiting room/admission limit before the database. A queue buffers demand rather than creating more inventory-write capacity; users need explicit waiting/pending status. At a measured higher scale, divide capacity into disjoint ticket pools or individual seats with local consistency. Allocation/rebalancing becomes harder and a global counter on every purchase would recreate the bottleneck. Microservices alone do not remove contention for the same inventory.

Migration ease depends on actual coupling, not the module names. Public interfaces, owned tables, identifier-based references and limited cross-module transactions help. Extract notifications first as a relatively low-risk example, then consider catalogue reads. Booking/inventory is harder and should generally retain one authority and local transactional consistency. Replace local calls with network APIs or durable messages; add authentication, timeouts, retry/idempotency rules, monitoring and independent deployment. Move data ownership through an explicit cutover rather than leaving two writable authorities. Any former cross-module atomic transaction must be redesigned as a workflow with intermediate states, retries and compensation when it spans service databases. Not every module needs to become a service.

Suggested approach: measure/load-test first, scale the modular monolith and control admission, then extract services incrementally when evidence or team ownership warrants it (strangler fig approach). No final architecture selection or implementation requested yet.

References checked:
- https://learn.microsoft.com/en-us/azure/wellarchitected/scalability/design-scale
- https://learn.microsoft.com/en-in/azure/architecture/patterns/competing-consumers
- https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/strangler-fig.html

## Follow-up: microservice purchase, recovery and infrastructure

User moved the discussion to microservices and requested a full purchase flow, recovery when payment succeeds but Booking crashes before confirmation, additional infrastructure, and whether complexity is justified.

Proposed an orchestrated saga: a durable checkout workflow coordinates local service transactions instead of assuming one transaction spans services and the payment provider. Booking owns inventory and reservations together. Payment owns provider integration and payment records. Ticket owns ticket issuance. Notifications handles delivery. The workflow can live in Booking initially; it need not be another separately deployed service.

Flow: client supplies a stable checkout request ID; Booking atomically reserves capacity and records an expiring reservation/order and pending workflow work. Payment starts one provider payment with a stable idempotency key and booking reference. A verified provider callback is durably recorded with a PaymentSucceeded outbox event in one Payment database transaction before acknowledging receipt. A relay publishes the event to a durable broker. Booking consumes it, atomically records deduplication plus reservation confirmation and a BookingConfirmed outbox event. Ticket creates one ticket per purchased entitlement, using uniqueness/idempotency, and schedules notification. The UI reports processing until ticket availability; browser redirects are not payment evidence.

Crash recovery: before Booking commits, event delivery is retried after recovery; after Booking commits but before acknowledgement, a duplicate is ignored using persistent identifiers and state. Outboxes bridge database commit/message publication gaps on both sides. Payment-provider success before Payment persists its result is covered by provider retry where available plus periodic provider reconciliation; a timeout means unknown, not failed. Retries must reuse operation keys. Failed messages require alerting and replay/manual recovery, not silent abandonment. Durable storage, recoverable backups and eventual service/provider recovery are assumptions; this is not an absolute guarantee under permanent data loss.

Expiry race: Booking serializes expiry and confirmation using its own reservation record. If confirmation wins on a valid hold, reserved becomes sold with no second decrement. If expiry wins and releases capacity, a late payment cannot confirm the expired hold. This proposal records a durable refund workflow; payment is refunded idempotently, retried and reconciled, with customer-visible refund-pending status and operational escalation if stuck. A refund is a compensating business action, not an atomic rollback; customer money can be temporarily captured without a ticket. Never release a reservation twice or issue a ticket against already reassigned capacity. Conservative alternative: hold uncertain-payment capacity pending reconciliation, trading availability for fewer refunds. Provider authorization/capture could reduce exposure if supported, but also needs durable recovery.

Additional capabilities versus a basic monolith: independently deployable services and owned schemas/databases (not necessarily separate physical servers); durable broker/outbox dispatchers and safe consumers; persisted saga/timers/reconciliation; service routing and authentication/secrets; bounded retries/timeouts; centralized correlated logs, metrics/traces and alerts; versioned API/event contracts and integration/failure testing; per-service backups/deployment operations. A gateway is useful, and Kubernetes, service mesh, event sourcing and dedicated workflow products are optional. Some durability, payment reconciliation and monitoring are required for a reliable monolith too; microservices add distributed handoffs and operational multiplicity.

Judgment: not justified by EventTicket's stated requirements alone for a small/student team. Benefits become material with independent teams/releases, differing scaling needs or strong isolation needs; boundaries must actually isolate failures. Microservices do not remove hot-inventory contention. Continue discussing the remaining architecture before a final selection.

References:
- https://microservices.io/patterns/data/transactional-outbox
- https://microservices.io/patterns/data/saga.html
- https://learn.microsoft.com/en-us/azure/architecture/patterns/saga

## Follow-up: cohesive purchase boundary and testing strategy

User challenged splitting tightly related Booking, Payment and Ticket and asked which capabilities merit extraction and how to test distributed purchases. This refines the earlier illustrative service decomposition, not a final architecture selection.

Proposed keeping inventory, reservations/orders, payment integration/records and ticket issuance as internal modules in one Ticket Sales service with one owned database. A verified payment callback can update payment status, confirm a still-valid reservation and create ticket records in one local transaction. External provider operations still cannot join that transaction: retain stable idempotency keys, verified callbacks, reconciliation, reservation-expiry rules and refund recovery. Notifications remain asynchronous. Service boundaries should enclose cohesive business operations, not mirror every code module.

Conditional extraction candidates: notifications for independent delivery retries/scaling and isolation from email outages; catalogue/search for browsing-heavy traffic and read-specific indexing; recommendations/analytics only if later requirements justify them. Search is optional, and recommendations/analytics are not current requirements. Catalogue may own descriptive event data, but Sales owns authoritative sellable inventory, prices and sale eligibility; checkout must validate its own authoritative offer. Synchronization/versioning between event publishing and sales configuration must be explicit. Authentication may use an existing identity provider rather than a new custom microservice; profile/admin screens alone do not justify services. For the current project, a modular monolith plus worker may remain simpler than extracting any service.

Testing plan: many unit tests for state transitions with a controllable clock; service component tests against a real disposable database and simulated external services; focused integration tests using the real database/broker for locks, outbox, redelivery and job claims; consumer/provider contract tests for API and event compatibility (including required meaning, not just field shapes); a small end-to-end suite running participating real services and infrastructure, with deterministic provider simulation for injected failures plus selected provider-sandbox integration checks. An automated container setup can start/clean isolated environments; CI should isolate records/queues. Contract tests do not prove end-to-end correctness and simulations do not prove provider compatibility. End-to-end async assertions should poll for states with deadlines, not fixed sleeps.

Key scenarios: successful purchase; payment decline; many concurrent attempts for one ticket; duplicate/delayed/out-of-order callbacks/messages; crash before commit; crash after commit before acknowledgement; payment timeout followed by provider success; expiry competing with payment; refund retry; broker outage and eventual recovery; notification failure without losing ticket access. Assert invariants: no negative availability or double allocation; one effective charge per intended payment attempt; one ticket per entitlement; every captured but unfulfilled payment reaches durable refund/recovery status. Use load tests separately for throughput and lock contention.

Answer to infrastructure concern: a true multi-service purchase end-to-end test does need its actual participating services, databases and messaging; most tests should not. Consolidating the purchase boundary permits most purchase tests to exercise one service plus database and provider simulation, with broader tests for catalogue and notification integration. This is another reason to avoid unnecessary splitting.

References checked:
- https://learn.microsoft.com/ga-ie/azure/architecture/microservices/model/microservice-boundaries
- https://martinfowler.com/articles/microservice-testing/fallback.html
- https://microservices.io/patterns/testing/service-component-test.html

### Repeated follow-up: purchase cohesion and test environment

User repeated the question about keeping Booking, Payment and Ticket together and the cost of distributed testing. Reaffirmed the previous recommendation: one cohesive Ticket Sales boundary with internal modules, conditional extraction of notifications and catalogue/search, and mostly isolated/component tests plus a smaller real multi-service end-to-end suite. No new architecture decision or implementation request was made. Existing references and detailed scenarios above still apply. Payment-provider interaction remains outside the local database transaction even when all purchase modules share a process.

## Follow-up: event-driven workers versus modular monolith

User asked whether option 3 is essentially the recommended monolith with workers, which operations use events, practical benefits, and worker/queue outage recovery.

Clarification: the proposals overlap. Modular monolith describes code/deployment boundaries; event-driven describes communication, and web-queue-worker describes running web and background workloads. A modular monolith can use both patterns. The earlier recommendation evolved toward this hybrid, so option 3 is a deployment/interaction variant rather than a mutually exclusive alternative. Microservices too may be event-driven. Keeping one codebase/database with separately running worker processes avoids separate service-owned purchase databases, but the broker/process boundary still introduces distributed failures. Event-driven does not imply event sourcing.

Keep synchronous: authorization, browse requests, authoritative capacity checks/reservations, and local reservation/payment-record/ticket confirmation transactions where practical. Proposed events: EventPublished -> category-notification and optional search-index subscribers; TicketIssued/PurchaseConfirmed -> receipt/email workers; ReservationCreated -> durable expiry scheduling if chosen. Expiry workers always recheck authoritative state/time, since a timer message is not proof a reservation remains pending. Payment processing can be queued when the UI supports pending state and recovery, but need not be asynchronous solely to use this style. A command asks for an action (SendReceipt); an event states a fact (TicketIssued). Independent subscribers need separate subscriptions/queues; competing workers on one queue divide work rather than each receiving a copy.

Advantages: API does not wait for email/indexing; workers can scale independently; backlog buffers bursts; notification failure does not invalidate purchase; adding subscribers reduces producer coupling. Costs: delayed outcomes, event contracts, observability, retry/deduplication and queue operations. No gain in authoritative inventory-write capacity just from adding a broker.

Worker recovery: acknowledge only after committing durable effects. Crash before commit -> redeliver and retry; crash after commit before acknowledgement -> redeliver and skip duplicate using handler/event identifiers committed with effects. External effects such as email are not atomic with the database: provider idempotency helps if available, otherwise duplicate delivery can remain possible. Use bounded retries/backoff, dead-letter handling, alerts and replay; handle ordering/version conflicts rather than assuming global order.

Queue outage: commit purchase and outbox together, then publish asynchronously with broker confirmation and correct durable routing. If queue unavailable, outbox accumulates and worker effects are delayed. Lost publisher confirmation can cause republication, so consumers still deduplicate. Critical synchronous purchase operations may continue while asynchronous capacity remains safe; monitor outbox age/size, disk, worker lag and reservation/payment deadlines, and throttle/pause checkout if limits or safe timing are exceeded. Pending is not completed. Durable/replicated broker configuration and recovery procedures matter; queues are not unlimited storage. Reconciliation still covers external payment uncertainty.

Conclusion: this reuses some messaging reliability problems from microservices, but shared database transactions keep the core purchase consistency local. For EventTicket, keep the purchase core synchronous/local and start with durable background work for email. A database-backed job queue could suffice initially; introduce an external broker when independent subscribers, buffering or workload scaling justify it. No final user selection yet.

References checked:
- https://learn.microsoft.com/en-gb/azure/architecture/guide/architecture-styles/
- https://www.rabbitmq.com/docs/confirms
- https://www.rabbitmq.com/docs/reliability

## Follow-up: queuing purchase requests and customer experience

User asked how much of purchasing can realistically be asynchronous, whether queuing requests before reservation relieves the database bottleneck or moves waiting, and when delay is worth its complexity.

Yes, the API can durably accept a ReserveTickets command and return a request ID with pending status (for HTTP, 202 Accepted is suitable). Accepted means recorded for processing, not reserved or purchased. A worker later validates the current offer and atomically reserves capacity, persists the result, and exposes it through authenticated status polling or push. Only after a successful hold should the customer be invited to pay; the hold duration starts at reservation, not queue entry. Stable request identifiers prevent refresh/retry creating additional reservations. Cancellation, abandoned requests, expiry and offer/price changes need explicit rules and customer consent; a worker must not silently purchase a changed offer.

Queuing moves waiting out of open database transactions/connections and enables bounded consumer concurrency. It can improve useful throughput by avoiding overload and retry storms, but does not remove hot-row serialization or increase stock. Illustrative numbers only: at 200 completed reservation decisions/second, a burst of 2,000 requests takes roughly 10 seconds to drain under simplified steady processing assumptions. If arrivals exceed processing continually, backlog grows; queues need admission limits, deadlines and monitoring. Adding unrestricted workers can recreate contention. FIFO broker intake does not guarantee fair completion with parallel workers, retries or multiple queues; strict ordering needs an explicit sequencer/partition policy and has costs.

Customer trade-off: quick acceptance is not quick confirmation. Under ordinary load asynchronous reservation adds status tracking and latency for little benefit. Under an exceptional sale a visible waiting room can be better than timeouts, but cannot promise a ticket or precise waiting time. Prefer admission before checkout for such sales: waiting room -> short transactional reservation -> payment -> verified confirmation/ticket -> asynchronous email. Stop or clearly reject new requests when inventory is committed and no current allocation is possible, rather than building a misleading unlimited queue. Existing holds may later expire; waiting-list behavior is a separate policy, not assumed.

Recommended async boundary: email/category alerts, optional indexing, reconciliation and refund recovery, and expensive optional ticket-file rendering. Keep basic ticket entitlement/code creation local and fast; payment completion is externally asynchronous regardless of whether payment initiation uses a queue. Queue critical purchase stages only when measured burst buffering or slow processing warrants pending-state UX and robust recovery. Async network I/O that keeps a server responsive is distinct from durably queueing a business operation. No final user architecture selection yet.

References checked:
- https://learn.microsoft.com/en-us/azure/architecture/patterns/asynchronous-request-reply
- https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling

## Final comparison and architectural conclusion

The user considers the three approaches sufficiently explored and leans toward a modular monolith with background workers. They requested a final comparison and explicit treatment of the overlap between event-driven and monolithic designs. The assistant agrees with that preference for the stated requirements; there is no implementation request or chosen technology stack.

| Criterion | Primarily synchronous modular monolith | Microservices with service-owned data | Event-driven web-queue-worker variant |
|---|---|---|---|
| Complexity | Lowest initial development/deployment overhead; still needs safe external payment handling | Highest: network boundaries, independent deployments, contracts, distributed workflows | Moderate with one codebase/database; broker, workers, outboxes and delayed outcomes add work |
| Scalability | Multiple app instances, caching and database tuning; modules generally scale together | Services scale independently; shared inventory contention still remains | API and workers scale separately; queues buffer bursts but do not increase inventory-write capacity |
| Reliability | Local transactions simplify purchase consistency; app/database are shared failure domains | Can isolate failures if dependencies are designed appropriately; partial failures and reconciliation are harder | Durable work survives temporary outages; duplicate/out-of-order delivery and growing backlogs require handling |
| Maintainability | Easier tracing, refactoring and testing for a small team if module boundaries stay enforced | Independent ownership/releases help larger teams; contracts, distributed diagnostics and integration tests cost more | Easier addition of subscribers and isolation of slow work; asynchronous flows are harder to follow/debug |
| Hardest implementation aspects | Concurrent reservations, payment/expiry races, idempotent callbacks, keeping boundaries clean | Data ownership and migration, sagas/compensation, safe retries, observability and multi-service testing | Atomic database/message handoff, idempotent effects, acknowledgements, retry/dead-letter recovery, ordering and pending-state UX |

Terminology correction: these are three investigated design approaches, not three mutually exclusive categories. Modular monolith versus microservices concerns application/service boundaries; event-driven concerns interaction. Web-queue-worker is a concrete deployment pattern that can use a modular monolithic codebase. Thus option 3 is an event-driven deployment/communication variant and a compatible extension of option 1, not a completely separate structural alternative. More asynchronous stages would make its runtime flow more distinct, but EventTicket does not benefit from inventing such stages merely to differentiate proposals. Event-driven does not require event sourcing.

Preferred EventTicket design:
- One modular backend/codebase and relational database, with clear ownership and public interfaces for accounts/roles, event management, bookings/inventory, payment integration, tickets and notifications.
- Keep the purchase core in one process/transactional boundary. Database transactions protect short local changes; verified callbacks, reconciliation and refund recovery bridge external payment operations.
- Use durable background workers for receipts, category notifications, reservation cleanup and payment reconciliation/refund recovery. Expiry always rechecks authoritative reservation state. A database-backed job queue is a valid starting point; an external broker is optional until justified.
- Record pending work atomically with relevant business changes and make handlers idempotent; do not pretend this makes external effects exactly once.
- Scale app instances and cache browsing when measured demand warrants it. Load-test purchase concurrency; use bounded admission/waiting room for exceptional sales before considering complex inventory partitioning.
- Maintain focused business/component/database-concurrency tests plus a smaller end-to-end and failure-recovery suite.

Reasoning: requirements emphasize a cohesive transaction-oriented purchase flow and ordinary account/event administration. No stated team structure, traffic measurements, independent-release needs or availability targets justify distributed service ownership. The hybrid retains local consistency and simpler development/testing while isolating slow secondary work. This is an initial architecture choice based on available evidence, not proof of unlimited scalability.

Reasons to revisit: independently staffed domains needing separate releases, measured scaling differences that cannot economically be met by the hybrid, justified isolation requirements, or a substantial increase in asynchronous workflows/subscribers. Extract notifications or catalogue selectively before splitting the purchase core; microservices do not automatically improve reliability or remove the last-ticket serialization point.

Unresolved business details remain: meaning of pre-sale, seating/capacity model, hold duration, refunds/late-payment policy, and concrete load/availability targets. These need clarification before detailed implementation but do not overturn the current architectural preference.

Reference for final terminology comparison:
- https://learn.microsoft.com/en-gb/azure/architecture/guide/architecture-styles/

Notes remain active for any further conversation; the user has not asked to stop recording.
