---
name: pr-fixes
description: "Address unanswered PR review threads. Use when the user asks to handle PR review feedback or fix review comments. Invoked as /git pr-fixes."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

Turn unanswered inline PR review threads into verified fixes. The user chooses each issue's resolution before implementation and approves GitHub replies and thread resolution after branch finalisation.

## Steps

1. **Identify the PR and user.** Read the project's agent instructions. Use the supplied PR number or URL, otherwise the current branch's PR. Ask if the target remains ambiguous. Get the authenticated GitHub login; use it as the user unless the conversation identifies another login. Record the PR repository, head branch and SHA. Inspect the working tree before editing; preserve existing user changes and ensure fixes target the PR head.

2. **Collect unanswered threads.** Follow "Read review threads" in [references/gh-review.md](references/gh-review.md), including pagination and failed-read handling. Include unresolved threads with no replies authored by the user, regardless of who started them. The user's own review comments are eligible: the root comment creates the thread and does not count as a reply. Include outdated threads; assess their concerns against the current code in step 3.

   Retain each thread's GraphQL ID, root comment's REST ID and URL, author, location and complete discussion. Assign one issue per independent request, keeping its link to the source thread when several requests share a thread. Discovery is complete when all threads and their discussions have been fetched. Report gaps and finish discovery before presenting an exhaustive inventory. If there are no eligible threads, report that and stop. State that the inventory covers inline review threads; PR conversation comments and review summaries are outside this inventory.

3. **Propose and wait.** Read the relevant code and show the complete issue inventory as a Markdown table before changing files. Use one row per issue with stable numbered IDs and these columns:

   | ID | Comment / location | Concern | Still applies? | Suggested resolution | Verification | Decision / outcome |
   |---|---|---|---|---|---|---|

   Link to the review comment and give its file and current or original line, where available. Explain applicability against the current code, include alternatives for material tradeoffs, and propose concrete verification. Start each decision as pending.

   Ask the user to choose for each ID: use the suggestion, provide another approach, skip, or discuss. Accept batch or individual answers. Implement only explicitly approved resolutions; unanswered or discussion-only items remain pending. Maintain the table as the ledger of chosen approaches, outcomes and evidence across turns, and reuse it in the final report.

4. **Delegate fixes, one sub-agent per issue.** For each approved code or documentation fix, launch a dedicated sub-agent with the issue ID, full discussion, chosen approach, relevant project instructions, PR head context, allowed scope and verification expectations. Each worker owns only that issue and returns its changes, checks and remaining concerns. Workers must not post, resolve, commit or push; the parent owns those actions.

   Run independent fixes concurrently only when their edits can coexist safely. Sequence issues with overlapping files or dependencies, giving later workers the integrated result. Preserve unrelated changes. If sub-agents are unavailable, report the limitation and ask how to proceed rather than substituting parent-only fixes. Skips and explanation-only decisions need no fix worker.

5. **Integrate and verify.** Inspect every worker's changes against the chosen resolution and run the relevant combined checks. Record verification evidence and whether each fix exists locally or on the PR head. Keep failed or blocked issues open and ask for direction when the approved approach cannot complete them.

   Return to pending decisions or fixes until every issue is verified as fixed, already addressed with evidence, handled by an agreed explanation, or explicitly skipped. Proceed to finalise only when every issue has one of these outcomes; a blocked issue requires further work or an explicit user decision to skip.

6. **Finalise the branch.** Follow the [finalise skill](../../finalise/SKILL.md) on this PR's head branch. This workflow authorizes that hand-off, including its commit and push steps for the approved work. Pass the merge-base of the PR's base branch and head as its fixed point so review covers the PR's changes even when the head tracks an already-pushed remote branch. Retain the existing PR, branch and base through its `git create-pr` hand-off.

   Proceed only after finalise and its delegated CI monitoring complete. Report blockers and resume here once cleared. Refresh the ledger and verification evidence after any finalise fixes.

7. **Prepare replies and ask.** Show a proposal for each thread, identifying its issue IDs: exact reply text, supporting changes and checks, whether required fixes reached the PR head, and whether to resolve or leave open. Default skipped issues to no reply and leave open. An agreed explanation may justify a reply; disagreement alone does not establish resolution. A thread is eligible for resolution only when every concern in it has been addressed and every required fix is on the PR head.

   Ask whether to post the proposed replies and resolve the indicated threads, allowing approval of selected actions. **Wait for the user's answer.** Implementation and finalisation approval do not authorize these GitHub actions. Keep unapproved actions pending. If approval is declined, leave the prepared replies available and finish with the branch results.

8. **Publish approved actions.** Re-fetch the affected threads and PR head before writing. Return invalidated proposals to the user for a new decision. Follow "Reply to a review comment" and "Resolve an approved thread" in [references/gh-review.md](references/gh-review.md): post approved replies first, then resolve approved eligible threads. Check current replies and resolution state before retrying an uncertain request so partial failures do not create duplicates.

   Finish with the issue table updated to show verification, whether fixes reached the PR, and which replies and resolutions succeeded. Keep skipped, unapproved and failed actions visible.
