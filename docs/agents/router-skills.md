# Router skills

A router skill is one `SKILL.md` that picks among a group of related sub-skills, so the model (or user) needs one entry point instead of remembering many skill names. The `git` skill is the worked example: it routes `commit`, `create-pr`, `code-review`, `pr-review`, `review-prs`, `pr-fixes`, `ci-fix` and `resolving-merge-conflicts`.

## When to build one

- The group has 5+ members, or members nest. In `git`, `create-pr` commits via `commit`.
- Members become plain Markdown files read by the router. Keep user-only workflows as standalone skills with `disable-model-invocation: true` and `allow_implicit_invocation: false`, or consolidate them under a router with the same explicit invocation policy. An implicitly invoked router must not invoke user-only workflows, except for the required `finalise` hand-offs from `git pr-fixes`, `implement ticket`, and `implement spec`.
- Skip it when each skill already has a sharp trigger description. A router adds nothing then.

The `writing` router consolidates user-invoked interactive workflows under an explicitly invoked router. Its shared `agents` and `humanize` documents can also be read directly by other workflows; these links load guidance without starting an interactive session.

## Layout

```
skills/git/
  SKILL.md                         # router: steps + sub-skill table
  agents/openai.yaml               # router metadata
  sub-skills/
    commit.md                      # the former SKILL.md
    create-pr.md code-review.md pr-review.md review-prs.md pr-fixes.md ci-fix.md resolving-merge-conflicts.md
```

A sub-skill with supporting files (`references/`, `assets/`) keeps them in a `references/` or `assets/` folder beside it, shared with the other sub-skills in that folder, so relative links still resolve. References can nest (`security` has `references/languages/` and `references/infrastructure/`).

`security` is a second worked example. Its router table reads `| situation | [`name`](sub-skills/x.md) |`, and content adapted from several upstream skills is merged into the sub-skills, with long sections moved into references. Every adapted file keeps `based_on_*` metadata for its source.

## How `git` was built

1. **Sub-skills are not skills.** Each member moved to `sub-skills/<sub-skill>.md`. The user invokes each sub-skill through its router, for example `/git code-review` or `/git create-pr`.
2. **Router `SKILL.md` stays thin:** steps, a `Sub-skill | Use when` table linking each sub-skill (`security` flips the columns to `Situation | Sub-skill`), and a short "How they nest" note. No sub-skill content.
3. **Steps:** argument names a sub-skill, use it; otherwise match the "Use when" row, asking once on a tie; then read the sub-skill and follow it as if it were the skill.
4. **Description** names the task types and lists the sub-skill names, so the model triggers on any of them.
5. **Cross-references rewritten.** Sub-skills that called each other with the Skill tool now say "follow `code-review.md`". Mentions elsewhere (`what-to-use`, `ticket`, `tdd`) became `/git <sub-skill>`.
6. **Agents metadata.** The router has `agents/openai.yaml` with `allow_implicit_invocation: true`. Sub-skills carry no yaml: they aren't skills, so nothing reads it.
7. **Docs site.** The skills page generates from the router table, so the five former skills drop out and the `git` sub-skills appear on rebuild.
8. **Frontmatter:** `license`, `metadata.version`, `author`, `author-url`. Sub-skills adapted from upstream also carry `based_on_repo`, `based_on_version` and `based_on_skill`.

## Reference-only trees

The former dev reference tree now lives at `skills/implement/sub-skills/references`, inside the implement router package. Its build-guide index is `skills/implement/sub-skills/name-table.md`; `scripts/check-marketing-structure.py` checks that every guide is listed and marketing hand-offs resolve.

## Checklist

- [ ] Every member is a plain sub-skill file reachable from the router
- [ ] Members moved to `sub-skills/<sub-skill>.md` (supporting files in a `references/` folder beside it), own references intact
- [ ] No leftover Skill tool calls or `/<old-name>` mentions (`grep` the repo)
- [ ] Router table links resolve
- [ ] `agents/openai.yaml` on the router
- [ ] Docs site builds and the skills page shows the router and its sub-skills
