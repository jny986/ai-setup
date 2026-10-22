---
name: ci-fix
description: "Use to fix failing CI and merge conflicts on an existing GitHub PR, monitoring and repairing until its latest head passes."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

Fix the referenced PR's CI and merge conflicts. This workflow includes committing and pushing repairs to its existing head branch, subject to repository permissions and user restrictions. Merging the PR, posting review replies and changing branch protection require separate authorization.

## Steps

1. **Identify the PR.** Read project instructions and confirm GitHub authentication. Resolve the target in order: explicit PR number/URL, conversation reference, current branch's PR. Ask if ambiguous. Confirm it is open; record its URL, head and base repositories, branches and SHAs.

2. **Prepare the head branch.** Inspect the working tree and any merge/rebase in progress. Preserve unrelated work using a clean checkout or isolated worktree; continue an existing operation only if it belongs to this PR. Fetch head and base from their actual repositories, including forks. Keep the PR branch: commit here directly rather than following `commit.md`, which may select another branch. Incorporate concurrent head updates without overwriting others' commits.

3. **Diagnose.** Read mergeability, required checks and all reported checks for the current revisions. Keep a brief ledger of failures, causes, repairs and verification. Follow failing check links to their provider's diagnostics. For Actions, read `gh run view <run-id> --repo <run-owner/repo> --log-failed`, supplementing with job details or artifacts when needed. Include external CI; inaccessible diagnostics remain a gap to resolve.

4. **Repair and publish.**
   - **Conflicts or required base updates:** integrate the current base according to repository policy, preferring a merge that preserves published history. For conflicts, follow [resolving-merge-conflicts.md](resolving-merge-conflicts.md), then return here. Rewriting published history requires explicit authorization. Refresh diagnostics after integration.
   - **Failing checks:** reproduce using the workflow's commands and environment, fix the cause, and run affected checks plus required project verification. Add regression coverage where useful. Preserve meaningful assertions and required checks. If local reproduction is unavailable, document what CI must verify.
   - **Publish:** review and stage only these repairs, commit with hooks and signing intact, and push to the recorded head repository and branch using an ordinary push. Confirm GitHub's head SHA matches. Skip committing when nothing changed.

5. **Monitor and repeat.** Watch all checks with `gh pr checks <PR> --repo <base-owner/repo> --watch --interval 30`, keeping waits interruptible and sharing progress. After watching, re-read head/base SHAs, mergeability and check results. Changed revisions invalidate earlier evidence: reassess and wait for applicable runs. Failures return to step 3; conflicts return to step 4. Pending checks, unknown mergeability and unregistered expected checks require further observation or diagnosis.

   Rerun an evidenced transient failure once if permitted; repeated failures require diagnosis. Continue actionable repairs until completion. When progress requires external access, credentials, maintainer approval, infrastructure recovery or a user decision, report the concrete blocker and action needed, then resume when cleared.

6. **Verify completion.** A fresh read must confirm unchanged head/base revisions, no merge conflicts, satisfied required checks, and successful completion of every applicable reported check. Accept skipped/neutral results only when intentional and compatible with required-check policy. Investigate cancelled or missing expected checks; an empty check list does not prove CI passed. Report approval or other merge-policy blockers separately.

   Report the PR link, verified head SHA, repairs/commits, local checks and CI run links. If blocked, identify remaining failures or conflicts and mark the work incomplete.
