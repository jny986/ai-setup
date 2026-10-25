---
name: plan
description: "Sharpen an idea, plan, or decision through grilling; maintain planning docs; synthesize a spec; or split work into dependency-linked tickets. Use for the journey from an unclear idea to an implementation-ready plan. Sub-skills: me, docs, spec, tickets. Implementation uses implement."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: grilling
---

Take an idea as far as the user requests: an interview, durable planning context, a spec, or tickets. Implementation stays outside this router.

## Routing

1. **Select the route.** An explicit `me`, `docs`, `spec`, or `tickets` argument selects that sub-skill directly. Otherwise start the `me` interview and ask once whether to create docs as decisions settle. Accepting selects `docs` with the same interview context; declining keeps `me`. While the offer is unanswered, remain in `me`. The offer applies only to a root invocation with no selected sub-skill.
2. **Gather context.** Follow [Project context](#project-context), reusing discovery and material already read in this session.
3. **Follow the route.** Read the selected sub-skill and follow it as the workflow. Apply [Grilling](#grilling) to `me` and `docs`; `spec` and `tickets` synthesize existing context without restarting the interview.

## Sub-skills

| Sub-skill | Use when |
|---|---|
| [`me`](sub-skills/me.md) | Interview and stress-test an idea without writing documents |
| [`docs`](sub-skills/docs.md) | Interview while maintaining a plan, terminology, and decisions |
| [`spec`](sub-skills/spec.md) | Synthesize existing context into a spec for the configured tracker |
| [`tickets`](sub-skills/tickets.md) | Break a plan, spec, or conversation into dependency-linked tickets |

## Project context

Read project agent instructions and follow setup's configured pointers. Discover the full documentation set: enumerate all files under `docs/` and documentation identified by project instructions, imports, maps, and configured pointers, including files outside `docs/`. Respect project exclusions for dependencies and upstream checkouts. Discovering the set does not require loading every unrelated document.

Read the material relevant to the topic and follow its references before asking interview questions or writing outputs. Include existing plans, glossary entries, applicable ADRs, and supplied artifacts. Fetch the full body and comments of supplied tracker references using the configured tracker. Reuse settled decisions and the project's vocabulary. Surface conflicting sources for resolution rather than silently choosing one; distinguish confirmed decisions from proposals and open questions. Report inaccessible relevant sources as gaps rather than pretending they were read.

Discovery is independent of output: `me` consults project docs but writes none. Without a project, use the supplied conversation and references; no setup is needed for an interview.

## Grilling

Interview the user relentlessly until you reach a shared understanding. Map a **design tree**: every decision branches into the decisions that hang off it.

Work in **rounds**. The **frontier** contains every decision whose prerequisites are settled: questions you can ask now without guessing at answers you have not heard. Ask the whole frontier in a numbered round, with your recommended answer for each question. Word each question so “yes” accepts the recommendation.

```text
❓ Q1 - <question title>: <question and choices>
➡️ <recommended answer>

❓ Q2 - <question title>: <question and choices>
➡️ <recommended answer>
```

Wait for the user's answers, then recompute the frontier. A question depending on an open answer belongs in a later round. Facts are the agent's job; decisions are the user's. Look up environmental facts, using an exploration subagent when available. An unfinished exploration is an unsettled prerequisite; ask the independent questions while it runs.

The interview is complete when every in-scope branch has been visited and the frontier is empty. Show the settled outcome and obtain confirmation of shared understanding. A request to stop or change scope bounds the interview. Recording confirmed decisions in `docs` happens during the interview; confirmation of shared understanding does not authorize implementation.

## Progression and hand-offs

Enter any route directly. Carry the current conversation, source pointers, confirmed decisions, unresolved questions, and artifacts when switching; reuse an existing plan rather than requiring an earlier route to run. Switch routes when requested. At a route's end, report its result and any next step without automatically starting another route or implementing the plan.

For questions requiring reading, use `research`; for a runnable answer, use `prototype`; for an effort too broad for one interview, use `wayfinder`. Bring their findings back into the current route. A build request goes to `implement` with the plan, spec, or tickets and their source context.
