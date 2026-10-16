# Handoff: design skill curation

Historical snapshot from an earlier curation session. The branch, work status, and open items below describe that session. Current workflows and references are indexed in [the design README](../skills/design/README.md).

Branch `bronze-whale`. All changes are uncommitted; see `git status` and `git diff`.

## Done

- **Email reference merged.** `skills/design/sub-skills/references/email-design.md` now includes the useful parts of `source-skills/CosmoBlk-email-design/SKILL.md`: archetypes, colour strategy, whitespace, footer, brief and handoff, iteration, and extra checklist items.
  - Dropped: Nitrosend-specific tool calls and the long JSON brief examples (the reference stays ESP-agnostic).
  - Frontmatter uses comma-separated `based_on_repo`, `based_on_version` (`ArnavPuri/designskills` at `main(c787301)` and `CosmoBlk/email-design` at `main(c56bfe0)`), matching the security sub-skills' convention.
- **Router fixed.** `skills/design/SKILL.md` routed only `brandkit`, leaving all 30 references unreachable.
  - Added a "References" section grouped by surface, linking every reference.
  - Added a step 3 telling the agent to read the reference for the surface when no sub-skill fits, starting with `design-context`.
  - Widened the description.
- **Indexes rebuilt** with `python3 scripts/build-marketing-index.py` (see `docs/agents/skills-html.md`).
  - The design row's description in `SKILLS.md` is hand-edited. The build doesn't sync that column, so keep it matching `skills/design/SKILL.md`.

## Not done / open

- **`brandkit.md` rewrite.** `skills/design/sub-skills/brandkit.md` is 851 lines, written as a persona plus a prompt template, derived from Leonxlnx/taste-skill. It's the main sprawl candidate; the user hasn't approved a rewrite.
- **References not deeply reviewed.** Only the first lines of each were read, plus `ui-design.md` and `email-design.md` in more detail. They looked tight, with scope lines, neighbour links and deferral to `design-context`, so no edits were made.
- **Reference rows avoid the sub-skill index.** The router's reference list uses bullets, not `| situation | [`name`](sub-skills/...) |` table rows. The build script's regex would otherwise list references as sub-skills.
- **Unused sources.** `source-skills/vercel-labs-web-interface-guidelin`, `jamditis-claude-skills-journalism` and `Leonxlnx/taste-skill` are staged as submodules, and their content isn't merged into the design skill.

## Notes

- **Docs location.** The user asked for this handoff in `docs/` (repo root), so it was not saved to the temp dir.
- **Conventions.** `docs/router-skills.md` covers router layout and the `based_on_*` metadata. User preferences: terse replies, and never make a class `final` or a method `private` without asking.

## Suggested skills

- `writing-for-agents`: when editing `SKILL.md`, sub-skills or references (pointers, pruning, negation).
- `design`: the router itself, to test that the pointers resolve.
- `git`: to commit the change set when the user asks.
