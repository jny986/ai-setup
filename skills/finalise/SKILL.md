---
name: finalise
description: Finalise a branch's dev work — run code and security reviews, fix findings, then create the PR.
disable-model-invocation: true
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

Run only when the user explicitly invokes `/finalise` or `$finalise`.

Take a branch from "dev work done" to "PR open" by running `git code-review` (including security), fixing its findings, and handing off to `git create-pr`. Requires the `git` and `security` skills. Read the `git` skill's `sub-skills/code-review.md`, `sub-skills/commit.md`, and `sub-skills/create-pr.md` when following those workflows. Work the steps in order.

## Steps

1. **Diff base.** Determine what this branch's changes should be measured against:
   - If the current branch tracks an upstream, use `git merge-base @{u} HEAD`.
   - Else if the branch was forked from a traceable parent (`git merge-base --fork-point <default-branch> HEAD` succeeds), use that.
   - Else fall back to the repo's default branch (`gh repo view --json defaultBranchRef -q .defaultBranchRef.name`) merge-base with `HEAD`.
   - If none of these resolve confidently, ask the user which fixed point to use.

2. **Code review.** Follow `git code-review`, passing the fixed point from step 1. Once code-review completes its security loop, if there are no Standards or Spec findings, skip straight to step 6.

3. **Fix code review findings.** Fix every Standards and Spec finding directly. Keep the list of what was fixed.

4. **Commit the fixes.** If step 3 changed files, make one new commit for everything fixed, e.g. `fix: address review findings`. Never amend or fold into existing commits.

5. **Re-review code.** If every fix in step 3 was purely cosmetic (formatting, naming, comments, dead-code removal — no behavioral change), skip re-review. Otherwise follow `git code-review` again against the same fixed point, once, to check the fixes and confirm nothing new was introduced. Continue to step 6 after code-review completes its security loop; report any remaining Standards or Spec findings.

6. **Summarise.** Tell the user what was fixed (or "no issues found"), including the security review result and any findings or unverified items explicitly ignored by the user, with their decisions, then proceed to step 7 without waiting for a response.

7. **Create the PR.** Follow `git create-pr`. The `finalise` invocation is itself the user's go-ahead: commit, push, and PR creation (and anything `git create-pr` delegates to `git commit`) proceed without a separate confirmation step once `git code-review` completes, including its security loop.
