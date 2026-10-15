---
name: finalise
description: Finalise a branch's dev work — run code review, fix findings, then create the PR. Use when the user asks to finalise, finish, or wrap up a branch. Invoked as /git finalise.
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

Take a branch from "dev work done" to "PR open" by running code review, fixing what it finds, and handing off to `create-pr`. Work the steps in order.

## Steps

1. **Diff base.** Determine what this branch's changes should be measured against:
   - If the current branch tracks an upstream, use `git merge-base @{u} HEAD`.
   - Else if the branch was forked from a traceable parent (`git merge-base --fork-point <default-branch> HEAD` succeeds), use that.
   - Else fall back to the repo's default branch (`gh repo view --json defaultBranchRef -q .defaultBranchRef.name`) merge-base with `HEAD`.
   - If none of these resolve confidently, ask the user which fixed point to use.

2. **Review.** Follow `code-review.md`, passing the fixed point from step 1. No findings on either axis: skip straight to step 6.

3. **Fix findings.** For every finding under `## Standards` and `## Spec`, fix it directly. Keep the list of what was fixed.

4. **Commit the fixes.** One new commit for everything fixed in step 3, e.g. `fix: address code review findings`. Never amend or fold into existing commits.

5. **Re-review.** If every fix in step 3 was purely cosmetic (formatting, naming, comments, dead-code removal — no behavioral change), skip re-review. Otherwise follow `code-review.md` again against the same fixed point, once, to confirm nothing new was introduced. Don't loop further regardless of outcome.

6. **Summarise.** Tell the user what was fixed (or "no issues found"), then proceed to step 7 without waiting for a response.

7. **Create the PR.** Follow `create-pr.md`. The `finalise` invocation is itself the user's go-ahead: commit, push, and PR creation (and anything `create-pr` delegates to `commit`) proceed without a separate confirmation step.
