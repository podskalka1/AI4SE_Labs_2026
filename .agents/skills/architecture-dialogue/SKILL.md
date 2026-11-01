---
name: architecture-dialogue
description: Explore software architectures from requirements through critical discussion, compare trade-offs, and draft and iteratively review an ADR with separate persistent discussion notes. Use for architecture selection or ADR review, not implementation or deployment.
---

# Architecture dialogue

Guide a requirements-grounded architectural discussion and an ADR that another developer can understand independently. Do not assume that the project will be implemented. Do not default to a particular architecture, stack or hosting platform.

## Start or resume

1. Read applicable repository instructions and inspect supplied requirements and relevant project artifacts. Read the actual files before proposing architectures; do not infer requirements from filenames. If sources are unavailable, identify the gap rather than claiming to have read them.
2. Determine the requested phase: exploration, comparison/recommendation, ADR drafting, or ADR revision. Resume that phase from existing notes and ADRs instead of restarting a completed discussion. Preserve explicit user choices; do not force another architecture evaluation during an ADR-only request.
3. Use the requested output directory. Otherwise follow the project's documentation convention, or use `output/<project-slug>/` under the working directory. Announce the paths. Reuse matching records; never overwrite another project's files or renumber an existing ADR silently.

## Persistent records

Maintain two separate Markdown records:

- `architecture_conversation_notes.md`: requirements sources, alternatives, assumptions, questions, explanations, comparisons, recommendations and user decisions.
- `adr_review_notes.md`: ADR drafting requests, feedback, revisions and reasons for changes. Create this when ADR work starts, keeping architecture notes intact.

Respect existing filenames or user-requested task naming. Append a concise entry each substantive turn in the active phase, before returning the answer. Capture what was asked, what was explained or changed, and what remains unresolved; a transcript is unnecessary. Distinguish user decisions from assistant recommendations and examples from commitments. When a conclusion changes, retain the historical entry and mark it superseded in the new entry.

Keep a short current-state summary in each active record: source/artifact paths, phase, current preference and status, open questions, and next discussion step. On a fresh session, read these records and the current ADR before continuing. Notes are file-based continuity, not automatic memory: tell the user which directory to provide when resuming. Follow requests to stop recording.

## Explore before selecting

Summarize functional needs, actors, critical workflows and stated quality constraints. Separate explicit requirements, inferred assumptions and missing information. Identify decision drivers such as consistency, latency, workload, team ownership, operating cost, security or deployment constraints only where relevant. Do not invent traffic estimates, budgets or availability targets. Ask a small number of consequential questions; continue independent analysis with labelled assumptions where possible.

Present **at least three meaningfully different architectural approaches** tailored to these requirements. Differences must affect boundaries, data ownership, execution, deployment or failure behavior, not merely technology brands. Do not offer the same design under three labels. If approaches combine or overlap, state the axes they describe and their concrete differences. Do not imply that communication patterns, code organization and deployment styles are mutually exclusive. A hybrid is valid, but explain which parts it combines.

For each approach explain:

- Components, responsibilities, data ownership and deployment units.
- Communication: direct calls, network APIs, commands/events, synchronous and asynchronous boundaries as applicable.
- One critical end-to-end workflow grounded in the requirements.
- Benefits, disadvantages, infrastructure/operational burden and the most difficult implementation aspects.
- Relevant failure, concurrency and recovery behavior; distinguish guarantees from assumptions.
- How it would be tested and operated, and what the user experiences during delays or failures.

Use plain language and concrete scenarios before code. Match depth to the user's understanding. Define unfamiliar terms when needed. Where relevant, probe transaction boundaries, partial failure, retries/duplicates, authoritative state, backlog growth and shared bottlenecks. Do not claim queues create throughput, retries guarantee exactly-once external effects, or decomposition automatically creates isolation. Apply these questions to the actual domain rather than assuming every project needs transactions or messaging.

Invite critical discussion after the initial alternatives and leave room for the user's response before declaring a selection or generating an unsolicited ADR. Useful questions test whether a benefit justifies its cost, which assumption could reverse a preference, and what happens when a critical dependency fails. Respond to challenges by revising the design, not defending an initial proposal mechanically. If the user requests a complete one-pass result, provide it with clearly provisional assumptions instead of manufacturing discussion turns.

## Compare and recommend

Build a compact comparison using requirements-relevant criteria. Usually cover complexity, scalability, reliability, maintainability, testing/operations and hardest implementation work; add domain-specific criteria and explain important priorities. Avoid unsupported numeric scores or generic claims that one style is always best.

Recommend an approach only after the requested exploration, linking reasons to drivers and user feedback. State accepted costs, unresolved risks, alternatives' conditions of suitability and evidence that would trigger reconsideration. A simpler design may win, but is not predetermined. Distinguish a preferred proposal from an adopted decision, and neither from permission to implement it.

## Draft the ADR

When requested after discussion, use the repository ADR convention; otherwise create `ADR_<next-number>_<decision-slug>.md` in the chosen output directory. Use this conventional structure:

1. Title/identifier, date and status.
2. Context: problem, requirements, constraints, assumptions and decision drivers.
3. Decision: proposed or adopted architecture, boundaries, key flows and reliability commitments.
4. Alternatives considered: meaningful benefits, drawbacks and disposition; explicitly explain overlap or hybrid choices.
5. Consequences: benefits, costs, risks and operational/testing implications.
6. Unresolved questions and choices left open.
7. Validation/review triggers and links to requirements and both note records.

Default to **Proposed** during design evaluation. Use **Accepted** only when the user or existing project governance establishes adoption. Open implementation questions do not alone prevent acceptance. Document status changes and their reasons in ADR-review notes.

Keep the ADR self-contained and proportionate. Separate architectural commitments and required outcomes from possible mechanisms. Do not select queues, locking algorithms, databases, providers or infrastructure because they appeared in an explanatory example. Label evaluated choices explicitly; leave unevaluated specifics open or suggest a focused later ADR. Keep necessary correctness requirements even when mechanisms remain undecided.

## Review and revise

Inspect the draft for missing context, unsupported assumptions, unclear alternative relationships, unexplained jargon, excessive detail and contradictions between status and wording. Invite feedback on structure, completeness and technical depth without demanding arbitrary revision rounds. Make requested revisions and record their rationale; do not start implementation.

Add a concise comparison table or Mermaid diagram when requested or when it materially clarifies the design. Show boundaries, data stores, external dependencies and labelled request/background flows. Distinguish logical capabilities from selected technologies; use placeholders for open choices. Explain the main flows briefly and ensure the diagram agrees with the prose. Inspect Mermaid syntax and render if a suitable renderer is available; do not claim visual validation otherwise.

Before delivery, check file links, status consistency, requirements traceability, notes updates and whether implementation examples accidentally became commitments. Report created/changed files, current proposal/adoption status and substantive open questions. Do not claim the design is implemented, benchmarked or approved without evidence.
