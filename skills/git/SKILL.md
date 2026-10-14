---
name: git
description: "Router for git and PR workflows. Use for any commit, push, pull request, branch wrap-up, diff review, or merge/rebase conflict task. Guides: commit-it, create-pr, finalise, code-review, resolving-merge-conflicts."
argument-hint: "[guide] [task]"
license: MIT
metadata:
  version: "1.0"
  author: jny986
  author-url: https://jny986.com
---

A router over five git guides. Each lives at `references/<guide>/GUIDE.md` in this skill's folder.

## Steps

1. **Pick the guide.**
   - Argument names a guide: use it.
   - Otherwise pick the row whose "Use when" fits the task. When two fit equally, take the narrower one, or ask once.
2. **Follow it.** Read `references/<guide>/GUIDE.md` and follow it as if it were the skill. When a guide hands off to another by name, open that guide.

## Guides

| Guide | Use when |
|---|---|
| [`commit-it`](references/commit-it/GUIDE.md) | Commit and push the current work, on the branch its ticket calls for |
| [`create-pr`](references/create-pr/GUIDE.md) | Open a GitHub PR from the current branch (commits and pushes first if needed) |
| [`finalise`](references/finalise/GUIDE.md) | The branch's dev work is done: review, fix findings, then open the PR |
| [`code-review`](references/code-review/GUIDE.md) | Review changes since a commit, branch, tag or merge-base, against repo standards and the spec |
| [`resolving-merge-conflicts`](references/resolving-merge-conflicts/GUIDE.md) | A merge or rebase is in progress with conflicts |

## How they nest

`finalise` runs `code-review`, fixes findings, then hands off to `create-pr`, which commits and pushes via `commit-it`. Pick the outermost one that matches the intent.
