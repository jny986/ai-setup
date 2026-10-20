---
name: finalise
description: Finalise a branch's dev work — run code and security reviews, fix findings, then create the PR. Use when the user asks to finalise, finish, or wrap up a branch. Invoked as /git finalise.
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

Take a branch from "dev work done" to "PR open" by running code and security reviews, fixing their findings, and handing off to `git create-pr`. Work the steps in order.

## Steps

1. **Diff base.** Determine what this branch's changes should be measured against:
   - If the current branch tracks an upstream, use `git merge-base @{u} HEAD`.
   - Else if the branch was forked from a traceable parent (`git merge-base --fork-point <default-branch> HEAD` succeeds), use that.
   - Else fall back to the repo's default branch (`gh repo view --json defaultBranchRef -q .defaultBranchRef.name`) merge-base with `HEAD`.
   - If none of these resolve confidently, ask the user which fixed point to use.

2. **Review.** Follow `git code-review`, passing the fixed point from step 1. Then follow `security review-code` on the same diff (`git diff <fixed-point>...HEAD`), reporting vulnerabilities introduced by the branch and reading surrounding code for context. Keep its findings and needs-verification items separate from Standards and Spec. If the security skill is unavailable, report the missing dependency and stop before creating the PR. No findings or needs-verification items from either review: skip straight to step 6.

3. **Fix findings.** Fix every Standards, Spec and confirmed security finding directly. Investigate security needs-verification items; fix any confirmed vulnerabilities and record anything still unverified. Keep the list of what was fixed.

4. **Commit the fixes.** If step 3 changed files, make one new commit for everything fixed, e.g. `fix: address review findings`. Never amend or fold into existing commits.

5. **Re-review.** If every fix in step 3 was purely cosmetic (formatting, naming, comments, dead-code removal — no behavioral change), skip re-review. Otherwise run both reviews from step 2 again against the same fixed point, once, to check the fixes and confirm nothing new was introduced. Don't loop further regardless of outcome.

6. **Summarise.** Tell the user what was fixed (or "no issues found"), including the security review result and any remaining findings or unverified items, then proceed to step 7 without waiting for a response.

7. **Create the PR.** Follow `git create-pr`. The `finalise` invocation is itself the user's go-ahead: commit, push, and PR creation (and anything `git create-pr` delegates to `git commit`) proceed without a separate confirmation step.
