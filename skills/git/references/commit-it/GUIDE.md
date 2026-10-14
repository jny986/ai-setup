---
name: commit-it
description: Commit and push the current work, first making sure you're on the branch its ticket calls for. Resolves any ticket in context (explicit reference, one already discussed, or inferred from the branch name), switches to or creates its branch when it has one, stages everything, commits, and pushes to origin. Use when the user asks to commit and push, or another skill needs that done before continuing (e.g. create-pr).
license: MIT
metadata:
  version: "1.0"
  author: jny986
  author-url: https://jny986.com
---

Get the current work committed and pushed to `origin`, on the branch its ticket calls for. Work the steps in order.

## Steps

1. **Preflight.** Confirm the working directory is inside a git repo with an `origin` remote configured. On failure, stop and say which.

2. **Ticket reference.** Try each of the following in order, stopping at the first success:

   1. **Invocation.** An explicit ticket link or ID in the invocation wins outright.
   2. **Conversation.** A ticket already looked up or discussed earlier in this conversation, from any tracker (Kanopi, GitHub, Jira, Linear, whatever's in play).
   3. **Branch name.** Infer from the current branch name using whatever ticket-search capability is available in context (e.g. Kanopi's `search-tickets`, `gh issue list`). No results: unresolved. One or more results: show the top few to the user and ask them to pick, or say none match.

   None resolved at all is fine — proceed without one.

3. **Branch.**
   - Ticket resolved and it carries a pre-formatted branch name field (like Kanopi's `branch_name`): that name wins verbatim, regardless of what branch you're currently on.
   - Ticket resolved but it has no such field (e.g. a GitHub issue): derive a name from it — `<id>-<slug of its title>`, lowercase, hyphen-separated, about 50 characters or fewer.
   - No ticket resolved: derive a short kebab-case summary of the diff instead, same length limit.
   - Whichever name results: switch to it if it exists locally, switch with tracking if it exists only on `origin`, otherwise create it fresh.
   - Let `git switch` carry uncommitted changes over naturally — no stashing. If it refuses because of a conflicting tracked-file diff, stop and surface its error.

4. **Commit.** Clean tree: skip. Else stage tracked and untracked files (`git add -A`), generate one conventional-commit message from the diff. Exactly one commit for the uncommitted work — never rewrite, squash, or split existing commits.

5. **Push.** `git push -u origin HEAD` — do this even when step 4 was a no-op, as long as local is ahead of `origin`. If the branch has diverged so the push needs `--force`, stop and report. Never force-push.

6. **Report.** Branch, ticket (if any), commit summary, push result.
