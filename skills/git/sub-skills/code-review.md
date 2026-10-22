---
name: code-review
description: "Use to review a branch, PR or changes since a commit, branch, tag or merge-base. Reviews Standards and Spec in parallel, verifies security remediation, checks prior comments, and optionally submits a user-approved PR review."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: code-review, retro
---

Review the diff between `HEAD` and a fixed point on three separate axes:

- **Standards**: does the code conform to this repo's documented coding standards?
- **Spec**: does the code faithfully implement the originating issue / spec?
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

### 4. Review Standards and Spec

Read [reviewer briefs and smell baseline](references/code-review-briefs.md). Dispatch Standards and Spec reviewers in parallel with the diff command, commit list, their respective sources from steps 1–3 and their respective briefs. Paste the full baseline into the Standards prompt. Wait for both reports; skip Spec only when the user confirms no spec exists, and report "no spec available".

### 5. Check user comments

Look for review comments the user left on the PR (read commands in [references/gh-review.md](references/gh-review.md)) or in the issue. Skip resolved threads and bot comments. If none exist, say so and move on.

For each comment, retain the author's GitHub username (`user.login`), quote the comment and verify its status against the current diff: fixed, not fixed or partially fixed, with file/line evidence. A "done" reply alone is not proof.

When a comment matches a pattern that recurs across the PR's comments, record it as a note for step 7: a standard or automated check could cover it.

### 6. Security review

Follow `security review-code` on `git diff <fixed-point>...HEAD`. If the skill is unavailable, report the missing dependency and stop before completing the review.

- On a PR, before making fixes in a detached worktree, create a local branch to retain the commits. After committing fixes, push them to the PR's head branch in its head repository when permitted, then confirm the PR's remote head includes them. Until that confirmation, keep the findings open, retain the local branch, and ask the user how to deliver the fixes if publication is blocked. Re-review the published diff before treating the PR's vulnerabilities as resolved.
- Fix confirmed vulnerabilities when remediation is clear and within scope. Run relevant checks, commit each pass in a new commit and re-review against the same fixed point.
- Investigate needs-verification items before confirming them. When a product, architecture or compatibility decision is needed, or a fix makes no progress, show severity, evidence, impact and options; ask the user and wait. Apply their instructions and re-review fixes. Record explicit decisions to ignore items; reopen them if later changes invalidate the decision.
- Repeat for new findings. Continue only when every finding and needs-verification item is verified resolved or explicitly ignored by the user; an instruction to attempt a fix leaves the item open.

### 7. Aggregate

After security fixes, refresh the diff and repeat Standards, Spec and comment checks for affected hunks. Present:

- `## Standards` and `## Spec`: reviewer reports, verbatim or lightly cleaned.
- `## Security`: vulnerabilities found, fixes verified, and findings or needs-verification items explicitly ignored, with the user's decisions.
- `## Comments`: a table with `Author | Comment | Status | Evidence`, one row per step 5 comment: `@username`, quote, fixed/not fixed/partially fixed, and file/line citations. Say when there are none.
- `## Notes`: standards that were vague, contradictory or stale, plus recurring comment patterns. Suggest standards or automated checks to add, clarify or remove. Notes are not findings.

End with one line: finding counts and worst issue within each axis, distinguishing resolved and explicitly ignored security items, plus the number of user comments still not fixed or partially fixed. Exclude Notes; preserve each axis's findings without merging or ranking across axes.

### 8. PR review

For a PR, follow [selection, overall comment and submission](references/code-review-pr.md): ask which findings to include and which result to use, then submit with the generated overall comment unless the user supplies their own. For a local review, finish after step 7.
