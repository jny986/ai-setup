---
name: code-review
description: "Use to review a branch, PR or changes since a commit, branch, tag or merge-base. Reviews code, spec, UI/UX and security using the review custom agent when present, combines findings and optionally submits a user-approved PR review."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: code-review, retro
---

Review the diff between `HEAD` and a fixed point on four separate axes:

- **Standards (code review)**: does the code conform to this repo's documented coding standards?
- **Spec**: does the code faithfully implement the originating issue / spec?
- **UI/UX**: does changed UI hold up against the `design audit` lenses? Applies only when the diff changes user-facing UI.
- **Security**: does the diff introduce exploitable vulnerabilities?

Report issues introduced by the diff; read surrounding code for context. Keep findings separate by axis so a pass on one cannot mask a failure on another.

The issue tracker should have been provided to you. If `docs/agents/issue-tracker.md` is missing, tell the user to run `/setup`.

## Process

### 1. Determine what to review

**Target.** Name what's under review:

- **A branch or PR** the user named: first stop if the tree is dirty. Otherwise check it out (`gh pr checkout <n>` or `git checkout <branch>`), then `git fetch`, then `git pull --ff-only`, each its own call. Stop if the pull cannot fast-forward.
- **Nothing named**: review the local branch at `HEAD`, without checkout or pull. This diff excludes uncommitted changes.

**Fixed point.** Whatever the user said is the fixed point (a commit SHA, branch name, tag, `main`, `HEAD~5`, etc.). If they didn't specify one, default to the target branch of the PR (`gh pr view --json baseRefName -q .baseRefName`, then compare against `origin/<base>`). With no PR, default to the branch the review target was cut from, else the repo's default branch. Ask only if none of these resolves.

Capture the resolved base/head SHAs, diff command, changed-file list and commit list once. Normally use `git diff <fixed-point>...HEAD` and `git log <fixed-point>..HEAD --oneline`. When the invoking workflow includes pending changes, use its diff command (`git diff <fixed-point>` for `finalise`) and record intended working-tree and untracked files. Fingerprint pending file contents so changes can invalidate results even when HEAD stays the same.

Reuse this scope and fetched context throughout the run. Read independent local sources and remote metadata in parallel where possible; deduplicate linked tickets by identifier. Refresh only context that changed or that a later publication gate explicitly requires. Reuse unchanged specs and standards after fixes; analysis of the refreshed diff is still required.

Continue only when the fixed point resolves (`git rev-parse <fixed-point>`) and the captured change set is non-empty, including intended untracked files when they are in scope.

**Past reviews (PRs).** Before starting a fresh review, read the PR's conversation comments, review bodies, inline threads and replies from every author using [GitHub review operations](references/gh-review.md), exhausting pagination. Verify actionable findings from past reviews against the current code and relevant checks. Record each finding's author, URL, status (fixed, not fixed, partially fixed or unable to verify) and supporting evidence. Thread resolution, an outdated anchor or a "done" reply alone is not proof of a fix; distinguish findings explicitly withdrawn or accepted by the user from outstanding work.

If any prior findings remain not fixed or partially fixed, show them with links and evidence, recommend waiting for those issues to be addressed before reviewing again, and offer **Wait for fixes (recommended)** or **Continue review now**. Wait for the user's choice before step 2. Honour an explicit instruction already given to continue despite outstanding findings without asking again. If they choose to wait, end with the outstanding list and resume from this check when fixes are ready. If they choose to continue, carry the outstanding findings into the review; continuing does not mark them fixed or accepted.

Proceed automatically when no prior findings remain outstanding. Report any inaccessible history or findings that cannot be verified as limitations, rather than claiming they are fixed. Reuse this history and status evidence in step 5 and refresh it for step 8's duplicate check.

### 2. Identify the spec source

Look for the originating spec, in this order:

1. Issue references or spec URLs in the commit messages, branch name, and PR description (`#123`, `Closes #45`, GitLab `!67`, ticket/wiki/doc links, etc.). Collect every linked ticket, even when several are referenced. Fetch issues via the workflow in `docs/agents/issue-tracker.md`. Fetch URLs and ticket references via an available MCP server where one fits (e.g. Kanopi for tickets and wikis), falling back to a plain web fetch. Read each ticket's full description and comments, and follow further ticket links that supply requirements, acceptance criteria or decisions relevant to the diff.
2. A path the user passed as an argument.
3. A spec file in the project's configured documentation or local-tracker location, or under `docs/` or `specs/`, matching the branch name or feature.
4. If nothing is found, ask the user where the spec is. If they say there isn't one, the **Spec** reviewer will skip and report "no spec available".

Continue only when every discovered relevant ticket has been read or recorded as inaccessible with its reference and access failure. Include all fetched ticket context in the Spec review sources; use it to assess the implementation against the combined requirements and flag conflicting requirements. Report inaccessible tickets as review limitations.

### 3. Identify the standards sources

Locate the repository standards and instructions applicable to the changed paths, including root rules and nested rules governing those paths. Include `CODING_STANDARDS.md` and `CONTRIBUTING.md` when present. Follow their relevant references; exclude dependency and upstream-source trees unless the reviewed change targets them.

List lint, typecheck and test scripts, CI workflows and pre-commit hooks. Identify which rules tooling already enforces. If neither hooks nor CI run these checks, report the missing automated guardrail under Standards.

### 4. Dispatch parallel reviews

Check whether the `review` custom agent exists before dispatching. If it exists, you must use it: dispatch a separate instance for each applicable axis (Standards, Spec, UI/UX and Security), including re-reviews. Do not substitute another agent or review directly. If it exists but the client cannot launch it, report the blocker and stop; do not claim a completed review. Only if the custom agent does not exist, use available general-purpose review agents or, when delegation is unavailable, perform each applicable axis directly. Read [reviewer briefs and smell baseline](references/code-review-briefs.md) and apply the shared context and axis-specific brief to each review. The caller defines each review; do not ask any reviewer to run the whole `git code-review` workflow or recursively dispatch the four axes.

Report which review method was used and any resulting coverage limitations. Setup for the custom agent is documented on the [agents page](https://ai.jny986.com/agents.html#set-up-review).

Give every reviewer the captured scope from step 1 plus only its relevant sources, prior findings and axis-specific brief. Supply fetched text or exact local source paths so reviewers can inspect context without repeating discovery. The shared dispatch and output contract lives in the briefs reference; keep the full smell baseline in the Standards prompt.

**Browser pre-flight (UI/UX only).** Give the UI/UX reviewer a live browser when all hold, else tell it to review statically:

- A browser tool is available (an MCP browser server, Playwright or the host's embedded browser).
- A target URL exists: one the user gave, a running dev server, or a start command found in the repo's scripts or docs. With none, ask the user once for the URL, start command and any test login, and wait.
- The server serves the reviewed code: start it from the review checkout (the PR worktree when one is used).
- Code from another author (a PR) runs only after the user confirms the exact install and start commands, and the reviewer signs in with a test login only. Without that confirmation, review statically.


When delegating, launch as many applicable reviewers as client capacity permits before waiting for results, starting Security alongside the other axes. Queue any remaining reviewers and launch them as slots become available without changing the scope. In direct review, work the axes in turn, Security included. Keep reviewed files unchanged while reviews run. When delegating, check user comments in step 5 from the fetched history during the wait. Coordinate shared checks once per reviewed state and pass results to reviewers that need them. Use checks that preserve reviewed files; the coordinator owns shared servers and output paths to avoid races.

Dispatch UI/UX only when changed files include user-facing UI; otherwise record "no UI changes". Skip Spec only when the user confirms no spec exists, and record "no spec available". Security is required for every review, including `finalise` and `git review-prs`.
Wait for every dispatched report before making fixes or aggregating. Resolve questions through the coordinator; a failed reviewer or incomplete report is a coverage gap, not a clean result. If the reviewed revisions or pending files change during dispatch, refresh the scope and rerun affected reviews before using their results.

### 5. Check user comments

Use the complete history fetched in steps 1–2 to check review comments the user left on the PR or issue; fetch only missing history. Skip resolved threads and bot comments. If none exist, say so and move on.

For each comment, retain the author's GitHub username (`user.login`), quote the comment and verify its status against the current diff: fixed, not fixed or partially fixed, with file/line evidence. A "done" reply alone is not proof.

When a comment matches a pattern that recurs across the PR's comments, record it as a note for step 7: a standard or automated check could cover it.

### 6. Security review

Validate the returned Security report against the coverage contract in [its brief](references/code-review-briefs.md#reviewer-prompts). Confirm the scope, required guides, source-to-sink evidence, file accounting and limitations. Resolve unsupported findings against the code; do not repeat completed analysis solely to restate the reviewer's report. A missing skill or guide, failed reviewer or incomplete analysis blocks review completion and a PR verdict. A clean, complete report needs no second Security dispatch.

After all reviews finish, the coordinator handles confirmed findings and needs-verification items:

- On a PR, before making fixes in a detached worktree, create a local branch to retain the commits. After committing fixes, push them to the PR's head branch in its head repository when permitted, then confirm the PR's remote head includes them. Until that confirmation, keep the findings open, retain the local branch, and ask the user how to deliver the fixes if publication is blocked. Re-review the published diff before treating the PR's vulnerabilities as resolved.
- Fix confirmed vulnerabilities when remediation is clear and within scope. Run relevant checks, commit each pass in a new commit and re-review against the same fixed point.
- Investigate needs-verification items before confirming them. When a product, architecture or compatibility decision is needed, or a fix makes no progress, show severity, evidence, impact and options; ask the user and wait. Apply their instructions and re-review fixes. Record explicit decisions to ignore items; reopen them if later changes invalidate the decision.
- After each fix pass, use the re-review procedure in step 7. Repeat until every security finding and needs-verification item is verified resolved or explicitly ignored by the user; an instruction to attempt a fix leaves the item open.

### 7. Aggregate

If the reviewed state is unchanged, use the completed reports directly. After a fix pass or concurrent code change:

1. Refresh the captured scope against the same fixed point and identify which earlier conclusions the changed code can affect, including callers and shared dependencies.
2. Perform a fresh Security review of the complete refreshed diff using the same agent preference and fallback as step 4. In parallel when delegation is available, rerun affected Standards, Spec and UI/UX reviews. Carry unaffected reports forward only after recording why their reviewed paths and dependencies are unchanged; retain their original revisions and evidence. When impact is uncertain, rerun the axis. Supply earlier reports as context, never as a substitute for current analysis.
3. Wait for every required report, recheck affected user comments, and return unresolved security items to step 6. Combine reports only when they cover the current state and step 6's security exit condition is satisfied.

Combine the reports once, retaining each axis's severity, evidence and limitations. Merge duplicate findings within an axis; cross-reference overlapping findings across axes so their coverage and counts remain visible. Present:

- `## Standards`, `## Spec` and `## UI/UX`: reviewer reports, verbatim or lightly cleaned, with findings ordered from highest to lowest severity (reorder if a reviewer did not). Keep UI/UX findings' P0–P3 priorities and limits; say "no UI changes" when UI/UX was skipped.
- `## Security`: the coverage record from step 6, vulnerabilities found (highest severity first), fixes verified, and findings or needs-verification items explicitly ignored, with the user's decisions. When none qualify, report the completed review's clean result; distinguish it from an incomplete or blocked review.
- `## Comments`: a table with `Author | Comment | Status | Evidence`, one row per step 5 comment: `@username`, quote, fixed/not fixed/partially fixed, and file/line citations. Say when there are none.
- `## Notes`: standards that were vague, contradictory or stale, plus recurring comment patterns. Suggest standards or automated checks to add, clarify or remove. Notes are not findings.

End with one line: finding counts and worst issue within each axis, distinguishing resolved and explicitly ignored security items, plus the number of user comments still not fixed or partially fixed. Exclude Notes; preserve each axis's findings without merging or ranking across axes.

### 8. PR review hand-off

For a local review, finish after step 7. For a PR, follow [PR review publication](references/code-review-publication.md) for inline-comment selection, verdict approval, body preparation and submission. Read it only when this hand-off applies; `finalise` skips it even when a PR exists.
