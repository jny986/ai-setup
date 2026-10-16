# Router skills

A router skill is one `SKILL.md` that picks among a group of related sub-skills, so the model (or user) needs one entry point instead of remembering many skill names. The `git` skill is the worked example: it routes `commit`, `create-pr`, `finalise`, `code-review`, `review-prs` and `resolving-merge-conflicts`.

## When to build one

- The group has 5+ members, or members nest. In `git`, `finalise` runs `code-review` then `create-pr`, which commits via `commit`.
- Every member is model-invocable. A router can't dispatch to skills with `disable-model-invocation: true`, which is why `git-guardrails-claude-code` and `setup-pre-commit` stayed out of it.
- Skip it when each skill already has a sharp trigger description. A router adds nothing then.

## Layout

```
skills/git/
  SKILL.md                         # router: steps + sub-skill table
  agents/openai.yaml               # router metadata
  sub-skills/
    commit.md                      # the former SKILL.md
    create-pr.md finalise.md code-review.md review-prs.md resolving-merge-conflicts.md
```

A sub-skill with supporting files (`references/`, `assets/`) keeps them in a `references/` or `assets/` folder beside it, shared with the other sub-skills in that folder, so relative links still resolve. References can nest (`security` has `references/languages/` and `references/infrastructure/`).

`security` is a second worked example. Its router table reads `| situation | [`name`](sub-skills/x.md) |`, and content adapted from several upstream skills is merged into the sub-skills, with long sections moved into references. Every adapted file keeps `based_on_*` metadata for its source.

## How `git` was built

1. **Sub-skills are not skills.** Each member moved to `sub-skills/<sub-skill>.md`. The user invokes each sub-skill through its router, for example `/git finalise` or `/git create-pr`.
2. **Router `SKILL.md` stays thin:** steps, a `Sub-skill | Use when` table linking each sub-skill (`security` flips the columns to `Situation | Sub-skill`), and a short "How they nest" note. No sub-skill content.
3. **Steps:** argument names a sub-skill, use it; otherwise match the "Use when" row, asking once on a tie; then read the sub-skill and follow it as if it were the skill.
4. **Description** names the task types and lists the sub-skill names, so the model triggers on any of them.
5. **Cross-references rewritten.** Sub-skills that called each other with the Skill tool now say "follow `code-review.md`". Mentions elsewhere (`what-to-use`, `implement-ticket`, `tdd`) became `/git <sub-skill>`.
6. **Agents metadata.** The router has `agents/openai.yaml` with `allow_implicit_invocation: true`. Sub-skills carry no yaml: they aren't skills, so nothing reads it.
7. **Indexes.** The five former skills were removed from `SKILLS.md` and `skills.html`, and one `git` row added.
8. **Frontmatter:** `license`, `metadata.version`, `author`, `author-url`. Sub-skills adapted from upstream also carry `based_on_repo`, `based_on_version` and `based_on_skill`.

## Reference-only trees

A tree of guides with no router yet (`skills/dev/references`) has no `SKILL.md` or `agents/openai.yaml`. Its index is the Dev section of the owning router's `sub-skills/name-table.md`, and `scripts/check-marketing-structure.py` checks it.

## Checklist

- [ ] Every member is model-invocable
- [ ] Members moved to `sub-skills/<sub-skill>.md` (supporting files in a `references/` folder beside it), own references intact
- [ ] No leftover Skill tool calls or `/<old-name>` mentions (`grep` the repo)
- [ ] Router table links resolve
- [ ] `agents/openai.yaml` on the router
- [ ] `SKILLS.md` and `skills.html` updated
