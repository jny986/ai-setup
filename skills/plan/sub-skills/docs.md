---
name: docs
description: "Interview while recording settled decisions, terminology, and unresolved questions."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: grill-with-docs
---

Use the root's project discovery and shared grilling procedure. Continue the existing design tree when entering from `me`; retain its answers and remaining frontier.

## Durable planning context

Find an existing plan for this topic before creating one. Respect the project's planning-document convention; otherwise maintain `docs/plans/<topic>.md`. If the project or destination is unclear, resolve that before writing. Use a stable topic slug and return the plan path.

Record the agreed outcome, scope and exclusions, settled decisions with their reasons, relevant source pointers, and unresolved questions with their prerequisites. Update the plan as answers settle; distinguish proposals from confirmed decisions. Revise superseded decisions explicitly rather than leaving contradictory instructions. Preserve unrelated content in an existing plan.

The plan carries implementation details and open questions; the glossary carries domain terms; ADRs carry qualifying architectural decisions. These artifacts give `spec` and `tickets` enough durable context to enter directly in a later session.

## Domain modeling

Locate the installed setup skill and read `references/modeling.md` relative to its directory (repository source: `skills/setup/references/modeling.md`). Use its configured glossary layout and formats to sharpen terminology and capture resolved terms inline; offer ADRs according to that procedure. Setup's `references/domain.md` contains consumer rules and is not the active modeling procedure.

If setup or its active modeling reference is unavailable, report the missing dependency and retain modeling questions in the plan. Continue the interview and plan maintenance, but mark glossary and ADR work as blocked. Do not substitute a standalone domain-modeling skill or invent a second modeling procedure here.

At completion, report the updated plan and any glossary or ADR changes, remaining questions, and modeling work blocked by dependencies. A request for a spec or tickets continues through that route with these sources and the same context.
