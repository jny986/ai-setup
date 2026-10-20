---
name: git
description: "Router for git and PR workflows. Use for any commit, push, pull request, branch wrap-up, diff review, or merge/rebase conflict task. Sub-skills: commit, create-pr, finalise, code-review, review-prs, resolving-merge-conflicts."
argument-hint: "[sub-skill] [task]"
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

A router over six git sub-skills. Each lives at `sub-skills/<sub-skill>.md` in this skill's folder.

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
| [`finalise`](sub-skills/finalise.md) | The user explicitly asks to finalise a branch whose dev work is done: review, fix findings, then open the PR |
| [`code-review`](sub-skills/code-review.md) | Review changes since a commit, branch, tag or merge-base, against repo standards and the spec |
| [`review-prs`](sub-skills/review-prs.md) | Review the open PRs awaiting the user's review, asking continue or skip for each |
| [`resolving-merge-conflicts`](sub-skills/resolving-merge-conflicts.md) | A merge or rebase is in progress with conflicts |

## How they nest

`git finalise` runs `git code-review` and fixes its findings, then runs `security review-code` with a fix/review loop and user instructions for unresolved issues. It hands off to `git create-pr`, which commits and pushes via `git commit`. Pick the outermost one that matches the intent.
