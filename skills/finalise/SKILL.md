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

Run when the user explicitly invokes `/finalise` or `$finalise`, or as the required branch-finalisation step of `git pr-fixes`, `implement ticket`, or `implement spec`.

Take a branch from "dev work done" to "PR open" by running `git code-review` (including security), fixing its findings, and handing off to `git create-pr`. Requires the `git` and `security` skills. Read the `git` skill's `sub-skills/code-review.md`, `sub-skills/commit.md`, and `sub-skills/create-pr.md` when following those workflows. Work the steps in order. Use code-review as internal branch validation even when a PR already exists.

## Steps

1. **Diff base.** Use a fixed point supplied by the invoking workflow. Otherwise determine what this branch's changes should be measured against:
   - If the current branch tracks an upstream, use `git merge-base @{u} HEAD`.
   - Else if the branch was forked from a traceable parent (`git merge-base --fork-point <default-branch> HEAD` succeeds), use that.
   - Else fall back to the repo's default branch (`gh repo view --json defaultBranchRef -q .defaultBranchRef.name`) merge-base with `HEAD`.
   - If none of these resolve confidently, ask the user which fixed point to use.

2. **Code review.** Follow `git code-review`, passing the fixed point from step 1. Include pending branch changes in every review axis: use `git diff <fixed-point>` for tracked changes and read untracked files intended for this change. Preserve unrelated user work. If essential coverage is incomplete, stop and report the gap. If there are no findings or security items needing verification, skip to step 6.

3. **Fix code review findings.** Fix actionable Standards, Spec, UI/UX and confirmed Security findings. Investigate security items needing verification. When a decision is needed or a fix makes no progress, explain the evidence and options, ask the user and wait. Record explicit decisions to ignore items. Keep the list of fixes and decisions.

4. **Commit the fixes.** If step 3 changed files, make one new commit for everything fixed, e.g. `fix: address review findings`. Never amend or fold into existing commits.

5. **Re-review code.** Follow `git code-review` again against the same fixed point after fixes. Repeat steps 3–5 for security findings and needs-verification items until each is resolved or explicitly ignored; report other remaining findings. Incomplete security coverage blocks finalisation.

6. **Summarise.** Tell the user what was fixed (or "no issues found"), including the security review result and any findings or unverified items explicitly ignored by the user, with their decisions, then proceed to step 7 without waiting for a response.

7. **Create the PR.** Follow `git create-pr`. The `finalise` invocation or required hand-off from `git pr-fixes`, `implement ticket`, or `implement spec` is itself the user's go-ahead: commit, push, and PR creation (and anything `git create-pr` delegates to `git commit`) proceed without a separate confirmation step once the review and remediation are complete. When called by `implement ticket` or `implement spec`, keep the implementation branch through the commit and PR hand-offs; do not switch branches based on a ticket reference. When called by `git pr-fixes`, update its existing PR on the same head branch and base, then return to that workflow for approval before replying to or resolving review threads.
