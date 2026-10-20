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

2. **Code review.** Follow `git code-review`, passing the fixed point from step 1. No Standards or Spec findings: skip straight to step 6.

3. **Fix code review findings.** Fix every Standards and Spec finding directly. Keep the list of what was fixed.

4. **Commit the fixes.** If step 3 changed files, make one new commit for everything fixed, e.g. `fix: address review findings`. Never amend or fold into existing commits.

5. **Re-review code.** If every fix in step 3 was purely cosmetic (formatting, naming, comments, dead-code removal — no behavioral change), skip re-review. Otherwise follow `git code-review` again against the same fixed point, once, to check the fixes and confirm nothing new was introduced. Then continue to step 6 regardless of outcome.

6. **Security review.** Follow `security review-code` on the updated branch diff (`git diff <fixed-point>...HEAD`), using the fixed point from step 1. Report vulnerabilities introduced by the branch, reading surrounding code for context. If the security skill is unavailable, report the missing dependency and stop before creating the PR.
   - Fix straightforward, confirmed vulnerabilities whose remediation is clear and stays within the task's scope. Run relevant checks and commit each pass's fixes in a new commit before reviewing the updated diff again against the same fixed point. Allow at most two automatic fix passes, each followed by a security review.
   - Investigate needs-verification items before treating them as confirmed findings. For findings requiring a product, architecture or compatibility decision, or anything still unresolved after the automatic passes, show the severity, evidence, impact and recommended options. Ask the user how to proceed and wait for instructions before continuing to PR creation. Apply their instructions, then re-review any resulting fixes; a new unresolved decision requires further instructions.
   - Continue when there are no remaining findings or verification items, or the user has explicitly instructed how to handle each remaining item. Keep security results separate from Standards and Spec.

7. **Summarise.** Tell the user what was fixed (or "no issues found"), including the security review result and any remaining findings or unverified items with the user's instructions for handling them, then proceed to step 8 without waiting for a response.

8. **Create the PR.** Follow `git create-pr`. The `finalise` invocation is itself the user's go-ahead: commit, push, and PR creation (and anything `git create-pr` delegates to `git commit`) proceed without a separate confirmation step once step 6's completion criterion is met.
