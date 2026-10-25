# Plan router

Status: router implemented; setup's modeling reference restored. Implementation requested via `/implement spec docs/plans/planning-router.md`.

## Agreed scope

- One router covers the journey from an unclear idea to an implementation-ready plan.
- Absorb `grill-me`, `grill-with-docs`, `grilling`, `to-spec`, and `to-tickets` into the router.
- Name the root skill `plan`; keep the shared grilling procedure in its `SKILL.md`, applying it to interview routes.
- Provide sub-skills `me`, `docs`, `spec`, and `tickets`.
- Domain-modeling guidance is moving into `setup` under its modeling reference; the `docs` sub-skill must use that reference rather than absorb a standalone domain-modeling skill.
- Grilling is the shared interview foundation. The router also produces specs and ticket breakdowns without requiring users to repeat an interview.
- Users can enter any route directly without repeating earlier work.
- A root invocation without an explicit sub-skill starts the `grill-me` interview behavior and asks once whether the user wants to create docs as they go, like `grill-with-docs`.
- Accepting that offer enables the `docs` sub-skill using the same interview context. Declining keeps the interview in `me` mode.
- Explicit `me`, `docs`, `spec`, or `tickets` arguments select that sub-skill directly; the root's documentation offer applies only when no sub-skill was selected.
- The `docs` sub-skill maintains `docs/plans/<topic>.md` with settled decisions and unresolved questions, respecting any existing project convention for planning documents. This provides durable context for `spec` and `tickets`.
- Project context includes all files under `docs/` plus other documentation identified by setup's project instructions and configured pointers, including files outside `docs/`.
- Discover the full documentation set, read material relevant to the topic, and follow its references before asking questions or writing outputs. Reuse existing plans, terminology, and decisions; surface conflicts for resolution.
- Documentation discovery is separate from output creation: `me` can consult existing project docs while remaining an interview without writing documents.
- Implementation stays outside the router.

## Behavior before migration

- `grill-me` invokes `grilling`; `grill-with-docs` also invokes `domain-modeling`.
- `to-spec` synthesizes existing context instead of repeating the interview.
- `to-tickets` drafts dependency-linked slices and gets approval of the breakdown before publishing.
- Setup's modeling reference (`skills/setup/references/modeling.md`, with `glossary-format.md` and `adr-format.md`) holds the active modeling procedure; `references/domain.md` holds consumer rules only.
- Repo router conventions: [router-skills.md](../agents/router-skills.md).

## Implementation choices

- Hand-offs: use `research`, `prototype`, and `wayfinder` for their respective unresolved questions; carry findings back. Hand build requests to `implement` with the source context.
- Progression: switch when requested, preserving context; do not automatically run later routes. The root documentation offer occurs once, and explicit routes bypass it.
- Artifacts: preserve project planning conventions, defaulting to `docs/plans/<topic>.md`; reuse existing plans. Specs publish through the configured tracker; ticket output retains the existing local-file or remote-tracker behavior and approval of the breakdown. Honor explicit draft-only requests.
- Migration: replace the five standalone skills with the four plain sub-skills; update callers and generated indexes. Former names remain only as source tracking or historical context, without standalone compatibility wrappers.
- Validation: repository structural checks, YAML and Markdown lint, skill validation, and 39 checker tests pass. Standards and spec reviews found modeling-pointer inconsistencies that were corrected. A read-only interview trial followed configured references outside `docs/`, surfaced a source conflict, and wrote no files.

## Modeling dependency

The docs route reads the installed setup skill's `references/modeling.md` (repository source: `skills/setup/references/modeling.md`), restored from the removed standalone domain-modeling skill along with its glossary and ADR format files. If setup or the reference is unavailable, the route reports the dependency, records modeling questions in the plan, and blocks glossary and ADR work. It uses neither the consumer-only `references/domain.md` nor a standalone fallback.
