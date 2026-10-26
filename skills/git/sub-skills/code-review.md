---
name: code-review
description: "Use to review a branch, PR or changes since a commit, branch, tag or merge-base. Reviews Standards, Spec and UI/UX (for UI changes) in parallel, runs the full security review on the current diff with a fix/review loop, checks prior comments, and optionally submits a user-approved PR review."
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

- **Standards**: does the code conform to this repo's documented coding standards?
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

Capture the diff command once: `git diff <fixed-point>...HEAD` (three-dot, so the comparison is against the merge-base). Also note the list of commits via `git log <fixed-point>..HEAD --oneline`.

Continue only when the fixed point resolves (`git rev-parse <fixed-point>`) and the diff is non-empty.

**Past reviews (PRs).** Before starting a fresh review, read the PR's conversation comments, review bodies, inline threads and replies from every author using [GitHub review operations](references/gh-review.md), exhausting pagination. Verify actionable findings from past reviews against the current code and relevant checks. Record each finding's author, URL, status (fixed, not fixed, partially fixed or unable to verify) and supporting evidence. Thread resolution, an outdated anchor or a "done" reply alone is not proof of a fix; distinguish findings explicitly withdrawn or accepted by the user from outstanding work.

If any prior findings remain not fixed or partially fixed, show them with links and evidence, recommend waiting for those issues to be addressed before reviewing again, and offer **Wait for fixes (recommended)** or **Continue review now**. Wait for the user's choice before step 2. Honour an explicit instruction already given to continue despite outstanding findings without asking again. If they choose to wait, end with the outstanding list and resume from this check when fixes are ready. If they choose to continue, carry the outstanding findings into the review; continuing does not mark them fixed or accepted.

Proceed automatically when no prior findings remain outstanding. Report any inaccessible history or findings that cannot be verified as limitations, rather than claiming they are fixed. Reuse this history and status evidence in step 5 and refresh it for step 8's duplicate check.

### 2. Identify the spec source

Look for the originating spec, in this order:

1. Issue references or spec URLs in the commit messages, branch name, and PR description (`#123`, `Closes #45`, GitLab `!67`, ticket/wiki/doc links, etc.). Collect every linked ticket, even when several are referenced. Fetch issues via the workflow in `docs/agents/issue-tracker.md`. Fetch URLs and ticket references via an available MCP server where one fits (e.g. Kanopi for tickets and wikis), falling back to a plain web fetch. Read each ticket's full description and comments, and follow further ticket links that supply requirements, acceptance criteria or decisions relevant to the diff.
2. A path the user passed as an argument.
3. A spec file in the project's configured documentation or local-tracker location, or under `docs/` or `specs/`, matching the branch name or feature.
4. If nothing is found, ask the user where the spec is. If they say there isn't one, the **Spec** sub-agent will skip and report "no spec available".

Continue only when every discovered relevant ticket has been read or recorded as inaccessible with its reference and access failure. Include all fetched ticket context in the Spec review sources; use it to assess the implementation against the combined requirements and flag conflicting requirements. Report inaccessible tickets as review limitations.

### 3. Identify the standards sources

Search the repo for every file that documents how code should be written. When `CODING_STANDARDS.md` or `CONTRIBUTING.md` exists, it must be on the list.

List lint, typecheck and test scripts, CI workflows and pre-commit hooks. Identify which rules tooling already enforces. If neither hooks nor CI run these checks, report the missing automated guardrail under Standards.

### 4. Review Standards, Spec and UI/UX

Read [reviewer briefs and smell baseline](references/code-review-briefs.md). Dispatch Standards, Spec and UI/UX reviewers in parallel with the diff command, commit list, their respective sources from steps 1–3 and their respective briefs. Paste the full baseline into the Standards prompt. Dispatch UI/UX only when the changed files include user-facing UI; otherwise report "no UI changes".

**Browser pre-flight (UI/UX only).** Give the UI/UX reviewer a live browser when all hold, else tell it to review statically:

- A browser tool is available (an MCP browser server, Playwright or the host's embedded browser).
- A target URL exists: one the user gave, a running dev server, or a start command found in the repo's scripts or docs. With none, ask the user once for the URL, start command and any test login, and wait.
- The server serves the reviewed code: start it from the review checkout (the PR worktree when one is used).
- Code from another author (a PR) runs only after the user confirms the exact install and start commands, and the reviewer signs in with a test login only. Without that confirmation, review statically.

Wait for every dispatched report; skip Spec only when the user confirms no spec exists, and report "no spec available".

### 5. Check user comments

Look for review comments the user left on the PR (read commands in [references/gh-review.md](references/gh-review.md)) or in the issue. Skip resolved threads and bot comments. If none exist, say so and move on.

For each comment, retain the author's GitHub username (`user.login`), quote the comment and verify its status against the current diff: fixed, not fixed or partially fixed, with file/line evidence. A "done" reply alone is not proof.

When a comment matches a pattern that recurs across the PR's comments, record it as a note for step 7: a standard or automated check could cover it.

### 6. Security review

Run the full `security review-code` workflow on the complete change set established for this review, including reviews invoked through `git review-prs` or `finalise`. Use the captured diff from step 1; when the invoking workflow includes pending changes (as `finalise` does), use `git diff <fixed-point>` and read intended untracked files so security covers the same changes as Standards, Spec and UI/UX. Read the security router and its `sub-skills/review-code.md`, then execute every applicable step: scope the actual current diff, load the matching guides, trace suspect patterns through the surrounding code, classify them and produce the security report. A PR overview, prior security report or verification of earlier fixes cannot substitute for this run. If the skill or a required guide is unavailable, or the workflow cannot be completed, report the missing dependency or coverage gap and stop before completing the code review or recommending a PR verdict.

Record the resolved base and head commit SHAs, diff command, any reviewed working-tree changes and untracked files, changed files covered, guides applied and any coverage limitations. Account for every changed file, explaining any exclusions. A clean result requires this completed review even when there are no prior security findings.

- On a PR, before making fixes in a detached worktree, create a local branch to retain the commits. After committing fixes, push them to the PR's head branch in its head repository when permitted, then confirm the PR's remote head includes them. Until that confirmation, keep the findings open, retain the local branch, and ask the user how to deliver the fixes if publication is blocked. Re-review the published diff before treating the PR's vulnerabilities as resolved.
- Fix confirmed vulnerabilities when remediation is clear and within scope. Run relevant checks, commit each pass in a new commit and re-review against the same fixed point.
- Investigate needs-verification items before confirming them. When a product, architecture or compatibility decision is needed, or a fix makes no progress, show severity, evidence, impact and options; ask the user and wait. Apply their instructions and re-review fixes. Record explicit decisions to ignore items; reopen them if later changes invalidate the decision.
- After each fix pass, rerun the full security workflow on the refreshed diff against the same fixed point, including checks for new vulnerabilities introduced by the fixes. Update the coverage record to the reviewed head. Continue only when every finding and needs-verification item is verified resolved or explicitly ignored by the user; an instruction to attempt a fix leaves the item open.

### 7. Aggregate

After security fixes, refresh the diff and repeat Standards, Spec, UI/UX and comment checks for affected hunks. Present:

- `## Standards`, `## Spec` and `## UI/UX`: reviewer reports, verbatim or lightly cleaned. Keep UI/UX findings' P0–P3 priorities and limits; say "no UI changes" when UI/UX was skipped.
- `## Security`: the coverage record from step 6, vulnerabilities found, fixes verified, and findings or needs-verification items explicitly ignored, with the user's decisions. When none qualify, report the completed review's clean result; distinguish it from an incomplete or blocked review.
- `## Comments`: a table with `Author | Comment | Status | Evidence`, one row per step 5 comment: `@username`, quote, fixed/not fixed/partially fixed, and file/line citations. Say when there are none.
- `## Notes`: standards that were vague, contradictory or stale, plus recurring comment patterns. Suggest standards or automated checks to add, clarify or remove. Notes are not findings.

End with one line: finding counts and worst issue within each axis, distinguishing resolved and explicitly ignored security items, plus the number of user comments still not fixed or partially fixed. Exclude Notes; preserve each axis's findings without merging or ranking across axes.

### 8. Select PR inline comments

For a PR, complete steps 8–11 below. For a local review, finish after step 7.

Start with `## Suggested review result: APPROVE` or `## Suggested review result: REQUEST CHANGES`, using step 9's criteria. Follow with one sentence explaining the recommendation, then `### Suggested inline comments`. Show the verdict even when there are no suggested comments.

Recommend inline comments only for findings still present in the current diff, excluding Notes and verified fixes.

**Duplicate check.** Before proposing comments, read all PR conversation comments, review bodies, inline threads and replies using [GitHub review operations](references/gh-review.md), exhausting pagination. Include every author (the user, other reviewers, the PR author and bots), resolved threads and outdated comments; step 5's filters apply only to status reporting. Compare each candidate's underlying concern and requested change with this history, even when wording or line anchors differ. Suppress candidates already raised, retaining the existing comment's author and URL as evidence. A related comment counts as a duplicate only when it covers the same concern; keep distinct issues. Continue only when every candidate has been checked; if a source is inaccessible, report the gap and complete the check before proposing inline comments.

Show the recommendations in the review response as a numbered list, each with its file, changed line and full proposed comment text; say when there are none. Briefly list suppressed duplicates with links to the existing comments so the user can see where they were already raised. After showing the verdict and list, ask which numbers, if any, to add and wait before step 9. Keep only the selected comments, anchored to changed lines.

Start every proposed and submitted inline comment with `[Severity][Issue type]`, followed by the concern, impact and suggested change. Use `Security`, `Code smell`, `Standard violation`, `Spec mismatch` or `UI/UX` to match the finding. A UI/UX comment names the affected state or step and the audit lens. For example: `[Low][Code smell] Possible Duplicated Code: ...`. Keep code smells framed as judgement calls.

Preserve the security review's severity. For other findings, use `Critical` for severe failures such as data loss, `High` for major functional or design impact, `Medium` for a meaningful localized issue, and `Low` for a minor improvement. Map UI/UX P0 to `Critical`, P1 to `High`, P2 to `Medium` and P3 to `Low`. Base severity on demonstrated impact, not issue type. These labels describe individual findings; retain the separate review axes and use step 9 to choose the verdict.

### 9. Choose the review result

After the inline-comment selection, repeat the suggested review result prominently and ask the user which result to apply. Use these criteria for the recommendation:

- **Approve**: only minor issues, or none.
- **Request changes**: issues that need to be looked at before merge.

Wait for their answer before step 10.

### 10. Prepare the review comment

Once the user has selected the review result in step 9, draft the overall comment using the template below and show it under `## Suggested review comment`. Generate it only after their selection, including when it differs from the recommended result.

#### Overall comment template

```markdown
[Approving / Requesting changes] — [one-sentence reason consistent with the chosen result].

[If present: one short sentence highlighting security issues covered in a separate comment or high-severity issues raised elsewhere in the review.]
```

Aim for 1–2 sentences, grounded in steps 1–7. Refer to important concerns in plain text, without links or repeated details. Include only context needed to understand the verdict; omit repeated assessments, test summaries and issue lists. Flag a material review limitation or accepted risk briefly when it affects merge readiness. Omit the second sentence when there is nothing important to highlight. The draft is ready when its status matches the user's choice and it accurately reflects outstanding concerns, including when the chosen result differs from the recommendation.

Use this generated comment as the review body and continue to step 11. If the user supplied replacement text, use it instead. Their inline-comment and review-result answers complete the required selections; the generated body needs no separate confirmation. If they explicitly request no overall comment, omit it for **Approve**. GitHub requires a review body for **Request changes**: if the user chooses that result and declines a comment, explain the requirement and ask them to use the generated summary or supply their own text.

### 11. Submit the review

After both selections, refresh the PR comment history and repeat step 8's duplicate check for the selected inline comments. Remove any newly duplicated comments and report their existing links; submit the remaining selection with the chosen result even when no inline comments remain.

Submit one review with the chosen result (`APPROVE` or `REQUEST_CHANGES`), the body from step 10, and remaining selected inline comments. Follow [GitHub review operations](references/gh-review.md) for the payload file and single `gh api` call, including any thread replies or other review writes.
