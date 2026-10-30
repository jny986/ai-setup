---
name: git
description: "Router for git and PR workflows. Use for commits, pushes, pull requests, code or repository review, PR review fixes, failing PR CI, or merge/rebase conflicts. Sub-skills: commit, create-pr, code-review, pr-review, review-prs, pr-fixes, ci-fix, resolving-merge-conflicts."
argument-hint: "[sub-skill] [task]"
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

A router over git sub-skills. Each lives at `sub-skills/<sub-skill>.md` in this skill's folder.

## Steps

1. **Pick the sub-skill.**
   - Argument names a sub-skill: use it. `commit-it` is the old name for `commit`.
   - Otherwise pick the row whose "Use when" fits the task. When two fit equally, take the narrower one, or ask once.
2. **Follow it.** Read `sub-skills/<sub-skill>.md` and follow it as if it were the skill. When a sub-skill hands off to another by name, open that sub-skill.

## Sub-skills

| Sub-skill | Use when |
|---|---|
| [`commit`](sub-skills/commit.md) | Commit and push the current work, on the branch its ticket calls for |
| [`create-pr`](sub-skills/create-pr.md) | Open a GitHub PR from the current branch (commits and pushes first if needed) |
| [`code-review`](sub-skills/code-review.md) | Review development changes or a repository against standards, requirements, UI/UX and security |
| [`pr-review`](sub-skills/pr-review.md) | Review a single PR, including prior feedback and selected review publication |
| [`review-prs`](sub-skills/review-prs.md) | Review the open PRs awaiting the user's review, asking continue or skip for each |
| [`pr-fixes`](sub-skills/pr-fixes.md) | Address unresolved PR review threads without a user reply, including threads the user created, with user decisions and one fix sub-agent per issue |
| [`ci-fix`](sub-skills/ci-fix.md) | Fix failing CI and merge conflicts on an existing PR, then monitor and repair until its latest head passes |
| [`resolving-merge-conflicts`](sub-skills/resolving-merge-conflicts.md) | A merge or rebase is in progress with conflicts |

## How they nest

`git code-review` prefers separate `review` agents for its axes, with a direct-review fallback. It reports findings without fixing them; Security uses `security review-code`. `git pr-review` uses `git code-review` for its review axes and handles PR feedback and publication. `git create-pr` commits and pushes via `git commit`, then monitors and repairs CI via `git ci-fix`. Pick the outermost one that matches the intent.
