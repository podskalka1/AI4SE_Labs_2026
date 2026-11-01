# Task 3: Original versus Skill-assisted architecture process

## Evidence and counting method

Compared the original [architecture notes](Task_1_conversation_notes.md), [ADR-review notes](Task_2_conversation_notes.md) and [final ADR](ADR_001_EventTicket_architecture.md) with the Skill test's [architecture notes](skill_test/architecture_conversation_notes.md), [ADR-review notes](skill_test/adr_review_notes.md) and [ADR](skill_test/ADR_001_EventTicket_architecture.md).

These are summary records, not complete transcripts. Counts below identify recorded request-bearing exchanges, not every heading or assistant/tool action. Exact total user prompts and elapsed time cannot be verified from these files. Quality judgments are qualitative assessments of the recorded analysis and documents, not implementation results.

## Comparison

| Aspect | Original process | Skill-assisted process |
|---|---|---|
| Recorded exchanges | 9 architecture exchanges: initial request, 6 distinct follow-ups, 1 repeated follow-up, final comparison. Another 3 cover ADR creation and 2 revisions: **12 total**, or **11 excluding the repeat** | **3 distinct exchanges**: initial analysis, purchase-failure scenarios, recommendation challenge plus ADR request. The final exchange appears in both note files and is counted once |
| Architecture exploration | Extensive sequential explanation of monolith, microservices and queue workers; overlap and purchase-service boundaries clarified through questions | All three initially described with components, ownership, communication, workflows, operational costs and tests; alternatives differentiated earlier |
| Difficult scenarios | Detailed locking, hot-event bottlenecks, horizontal scaling, migration, distributed recovery, worker crashes and queue outages | Focused cross-architecture analysis of last-ticket allocation, late payment and issuance crashes; explicit lost charge/refund responses and recovery obligations |
| Final ADR | Conventional structure, Mermaid overview, flows, alternatives, consequences and open mechanisms; improved through review | Includes those elements plus story references, explicit failure-outcome table, fuller ownership/security responsibilities and unresolved policy alternatives |
| Recorded ADR revisions | **2 user-requested rounds** after initial creation: diagram/alternative clarity, then prescription/status corrections | **0 post-draft revision rounds recorded**; author review completed, but notes explicitly say user review is pending |
| Explicit guidance | User elicited depth topic by topic and corrected diagram omission, overlapping alternatives, premature technology choices and Accepted status | User still supplied capacity/pending-state assumptions, three difficult scenarios, preferred direction and a specific Proposed ADR/diagram request |

Evidence for the original count is the initial request, six distinct “Follow-up” sections, “Repeated follow-up” and “Final comparison” in Task 1, plus Task 2's creation request and “Revision 1/2.” The Skill record has three dated discussion entries; its single ADR-review entry documents the third exchange rather than a fourth prompt. This yields **11 distinct substantive original rounds versus 3 recorded Skill-assisted rounds**, under this counting method. It does not establish a timed speed-up.

## Main improvements

The Skill-assisted process front-loaded useful reasoning. Its first exchange already covered failure behavior, testing, customer-visible delays and operational requirements. It kept inventory, orders and tickets together in Sales when discussing microservices, avoiding the original need to challenge an unnecessarily fragmented purchase workflow.

The third alternative was also more distinct: **queued initial booking with separate read views**, rather than background notifications that largely overlapped with the monolith. Both records acknowledge that deployment and communication styles can combine. The new record explains this distinction before selection, while the original refined it through several follow-ups.

Core architectural rigor appears preserved. Both address atomic allocation, duplicate-safe processing, uncertain payments, expiry races and reconciliation. The Skill run states more explicitly that a timeout is not payment failure, callbacks can arrive after capacity reassignment, and eventual refund resolution depends on provider recovery and operational action. It leaves the release-versus-retain expiry policy unresolved instead of silently selecting it.

Both final ADRs are usable, self-contained Proposed designs. The new ADR provides stronger requirement traceability and more directly checkable failure outcomes. Its first draft already leaves queue/concurrency technologies open and uses Proposed status, addressing issues corrected during the original review. However, its diagram labels the database as holding “durable work” while the prose leaves durable-work storage open; that could still be read as an implementation commitment and merits clarification. It is also longer and denser than the original final ADR.

## Limitations and conclusion

The original discussion offers more tutorial depth on locks, scaling, migration and test layering. Fewer exchanges do not prove equal user understanding. The new process still required meaningful scenario and drafting guidance; it was not autonomous, and zero revisions does **not** establish satisfaction when user review remains pending. Neither process implemented or tested the architecture; Mermaid rendering was unavailable in the Skill run.

Both evaluations used the same EventTicket requirements. Although the test notes say previous artifacts were excluded, the Skill was derived from that earlier discussion and the user had already learned from it. Prompt scope and stopping points differed; model/settings and time were not controlled. Skill-authoring effort is also excluded from the interaction comparison. This is not a fully controlled experiment or evidence of general performance on other domains.

**The Skill achieved its intended purpose provisionally:** the recorded process reached a justified recommendation and a strong first ADR draft with fewer discussion exchanges and less corrective steering, without an evident loss of core failure-analysis quality. It has not yet demonstrated fewer revisions to a user-approved ADR, measured time savings, or transfer to unfamiliar requirements.
