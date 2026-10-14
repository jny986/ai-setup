# Router skills

A router skill is one `SKILL.md` that picks among a group of related guides, so the model (or user) needs one entry point instead of remembering many skill names. The `git` skill is the worked example: it routes `commit-it`, `create-pr`, `finalise`, `code-review` and `resolving-merge-conflicts`.

## When to build one

- The group has 5+ members, or members nest. In `git`, `finalise` runs `code-review` then `create-pr`, which commits via `commit-it`.
- Every member is model-invocable. A router can't dispatch to skills with `disable-model-invocation: true`, which is why `git-guardrails-claude-code` and `setup-pre-commit` stayed out of it.
- Skip it when each skill already has a sharp trigger description. A router adds nothing then.

## Layout

```
skills/git/
  SKILL.md                         # router: steps + guide table
  agents/openai.yaml               # router metadata
  references/
    commit-it/
      GUIDE.md                     # the former SKILL.md
      agents/openai.yaml           # kept from the original skill
    create-pr/ finalise/ code-review/ resolving-merge-conflicts/   # same shape
```

A guide's own supporting files (`references/`, `assets/`) stay beside its `GUIDE.md` so relative links still resolve.

## How `git` was built

1. **Guides are not skills.** Each member moved to `references/<guide>/GUIDE.md`. The standalone slash commands (`/finalise`, `/create-pr`, ...) are gone; the user runs `/git finalise`.
2. **Router `SKILL.md` stays thin:** steps, a `Guide | Use when` table linking each `GUIDE.md`, and a short "How they nest" note. No guide content.
3. **Steps:** argument names a guide, use it; otherwise match the "Use when" row, asking once on a tie; then read the guide and follow it as if it were the skill.
4. **Description** names the task types and lists the guide names, so the model triggers on any of them.
5. **Cross-references rewritten.** Guides that called each other with the Skill tool now say "follow `../code-review/GUIDE.md`". Mentions elsewhere (`ask-matt`, `implement-spec`, `tdd`) became `/git <guide>`.
6. **Agents metadata.** The router has `agents/openai.yaml` with `allow_implicit_invocation: true`. Each guide keeps its original yaml; `create-pr` had none, so it got one in the same format (`interface.display_name`, `short_description`).
7. **Indexes.** The five former skills were removed from `SKILLS.md` and `skills.html`, and one `git` row added.
8. **Frontmatter:** `license`, `metadata.version`, `author`, `author-url`.

## Reference-only trees

A tree of guides with no router yet (`skills/dev/references`) has no `SKILL.md` or `agents/openai.yaml`. Its index is the Dev section of the owning router's `references/name-table.md`, and `scripts/check-marketing-structure.py` checks it.

## Checklist

- [ ] Every member is model-invocable
- [ ] Members moved to `references/<guide>/GUIDE.md`, own references intact
- [ ] No leftover Skill tool calls or `/<old-name>` mentions (`grep` the repo)
- [ ] Router table links resolve
- [ ] `agents/openai.yaml` on the router, and on each guide that had one (large nested trees like `marketing` skip it for guides that had none)
- [ ] `SKILLS.md` and `skills.html` updated
