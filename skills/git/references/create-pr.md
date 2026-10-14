---
name: create-pr
description: "Create a GitHub pull request from the current branch: branch if needed, commit outstanding changes, push, and open the PR with gh. Use when the user asks to create/open/raise a PR or pull request."
license: MIT
metadata:
  version: "1.0"
  author: jny986
  author-url: https://jny986.com
---

Take the current work to an open GitHub PR. GitHub and `gh` only. Read the invocation for hints (see Reference), then work the steps in order.

## Steps

1. **Preflight.** Confirm `gh auth status` passes and `origin` is GitHub. On failure, stop and say which.

2. **Base branch.** `gh repo view --json defaultBranchRef -q .defaultBranchRef.name`, unless the invocation names another base.

3. **Commit and push.** Verify opt-in in effect (see Reference): run the repo's test, lint, and typecheck scripts now, abort on any failure, before doing anything below. Then follow `commit.md`: it resolves any ticket in context, switches to or creates the branch that ticket calls for (or a diff-summary branch if none), stages, commits, confirms, and pushes.

4. **Ticket reference for the PR.** If the `commit` guide resolved a ticket, use it. Otherwise check specifically for a GitHub issue number (in the branch name or commit messages) since the `commit` guide doesn't look for those. Note whether it's a GitHub issue number (allows `Closes #N`) or a non-GitHub ID (text only). None found is fine.

5. **Something to PR.** No commits ahead of base: stop with "no changes relative to `<base>`".

6. **Assemble.**
   - Title: the commit subject for a single commit ahead of base, else a conventional-style summary of the branch's commits. An explicit title in the invocation wins.
   - Body: fill a PR template if one exists (`.github/PULL_REQUEST_TEMPLATE.md`, `.github/PULL_REQUEST_TEMPLATE/*`, `docs/PULL_REQUEST_TEMPLATE.md`, repo root), else use `## Summary`, `## Changes`, `## Test plan`. Add `Closes #N` for a GitHub issue number; reference a non-GitHub ID in the body text. Nothing after the last section or field.
   - Draft only if the invocation says draft.

7. **Open.** If `gh pr view` shows an open PR for the branch, the push already updated it: report its URL, offer to update the body. Else `gh pr create` with the title, body, and base, plus `--assignee @me` to assign the authenticated GitHub user, `--draft` if requested, and `--reviewer` for any named reviewers.

8. **Report.** Print the PR URL and a one-line status. No browser. No reviewers or labels unless the invocation asked or a template or CODEOWNERS dictates.

9. **Monitor CI.** `gh pr checks <PR> --watch` until all checks complete. Any failure: pull the failing job's log (`gh run view <run-id> --log-failed`), fix the root cause, commit, push, then re-watch. Repeat until every check passes or a failure isn't fixable from the diff (e.g. flaky infra, missing external secret) — stop and report that one to the user instead of looping indefinitely.

## Reference

**Invocation hints.** Freeform text after `/git create-pr`, parsed for: draft flag, base branch, explicit title, reviewer names, verify opt-in ("verify", "run the checks"). No strict flags.

**Verify opt-in.** When asked, run the repo's test, lint, and typecheck scripts before step 3 and abort on any failure. Off otherwise.

**Guardrails.** The user's git hooks (destructive-git prompt, commit-signing) stay in force. Never pass `--no-verify`, never disable signing, expect a hook prompt mid-run.
