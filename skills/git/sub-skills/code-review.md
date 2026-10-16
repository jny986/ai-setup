---
name: code-review
description: "Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/spec asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to \"review since X\"."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: code-review, retro
---

Two-axis review of the diff between `HEAD` and a fixed point, defaulted when the user supplies none:

- **Standards**: does the code conform to this repo's documented coding standards?
- **Spec**: does the code faithfully implement the originating issue / spec?

Both axes run as **parallel sub-agents** so they don't pollute each other's context, then this skill aggregates their findings.

**Scope: only the changes in the branch or PR.** Review the diff, not the surrounding codebase. Don't flag pre-existing issues in untouched code; read it only for context.

The issue tracker should have been provided to you. If `docs/agents/issue-tracker.md` is missing, tell the user to run `/setup-matt-pocock-skills`.

## Process

### 1. Determine what to review

**Target.** Name what's under review:

- **A branch or PR** the user named: check it out and bring it up to date with its remote (`gh pr checkout <n>` for a PR, otherwise `git checkout <branch>`; then `git fetch` and `git pull --ff-only`). Review is of the *current* branch at its latest commit. Stop and tell the user if the tree is dirty or the pull can't fast-forward.
- **Nothing named**: review the local branch as it stands, with no checkout or pull.

**Fixed point.** Whatever the user said is the fixed point (a commit SHA, branch name, tag, `main`, `HEAD~5`, etc.). If they didn't specify one, default to the target branch of the PR (`gh pr view --json baseRefName -q .baseRefName`, then compare against `origin/<base>`). With no PR, default to the branch the review target was cut from, else the repo's default branch. Ask only if none of these resolves.

Capture the diff command once: `git diff <fixed-point>...HEAD` (three-dot, so the comparison is against the merge-base). Also note the list of commits via `git log <fixed-point>..HEAD --oneline`.

Before going further, confirm the fixed point resolves (`git rev-parse <fixed-point>`) and the diff is non-empty. A bad ref or empty diff should fail here, not inside two parallel sub-agents.

### 2. Identify the spec source

Look for the originating spec, in this order:

1. Issue references or spec URLs in the commit messages, branch name, and PR description (`#123`, `Closes #45`, GitLab `!67`, ticket/wiki/doc links, etc.). Fetch issues via the workflow in `docs/agents/issue-tracker.md`. Fetch URLs and ticket references via an available MCP server where one fits (e.g. Kanopi for tickets and wikis), falling back to a plain web fetch.
2. A path the user passed as an argument.
3. A spec file under `docs/`, `specs/`, or `.scratch/` matching the branch name or feature.
4. If nothing is found, ask the user where the spec is. If they say there isn't one, the **Spec** sub-agent will skip and report "no spec available".

### 3. Identify the standards sources

Search the repo for every file that documents how code should be written. When `CODING_STANDARDS.md` or `CONTRIBUTING.md` exists, it must be on the list.

Then list the repo's automated checks: lint, typecheck and test scripts (`package.json` or the build tool), the CI workflow, and pre-commit hooks. These define "tooling already enforces". A repo with no pre-commit hook and no CI job running its lint/typecheck/test command has no guardrail; report that in the Standards section.

On top of whatever the repo documents, the Standards axis always carries the **smell baseline** below: a fixed set of Fowler code smells (_Refactoring_, ch.3) that applies even when a repo documents nothing. Two rules bind it:

- **The repo overrides.** A documented repo standard always wins; where it endorses something the baseline would flag, suppress the smell.
- **Always a judgement call.** Each smell is a labelled heuristic ("possible Feature Envy"), never a hard violation. Like any standard here, skip anything tooling already enforces.

Each smell reads *what it is* → *how to fix*; match it against the diff:

- **Mysterious Name**: a function, variable, or type whose name doesn't reveal what it does or holds. → rename it; if no honest name comes, the design's murky.
- **Duplicated Code**: the same logic shape appears in more than one hunk or file in the change. → extract the shared shape, call it from both.
- **Feature Envy**: a method that reaches into another object's data more than its own. → move the method onto the data it envies.
- **Data Clumps**: the same few fields or params keep travelling together (a type wanting to be born). → bundle them into one type, pass that.
- **Primitive Obsession**: a primitive or string standing in for a domain concept that deserves its own type. → give the concept its own small type.
- **Repeated Switches**: the same `switch`/`if`-cascade on the same type recurs across the change. → replace with polymorphism, or one map both sites share.
- **Shotgun Surgery**: one logical change forces scattered edits across many files in the diff. → gather what changes together into one module.
- **Divergent Change**: one file or module is edited for several unrelated reasons. → split so each module changes for one reason.
- **Speculative Generality**: abstraction, parameters, or hooks added for needs the spec doesn't have. → delete it; inline back until a real need shows.
- **Message Chains**: long `a.b().c().d()` navigation the caller shouldn't depend on. → hide the walk behind one method on the first object.
- **Middle Man**: a class or function that mostly just delegates onward. → cut it, call the real target direct.
- **Refused Bequest**: a subclass or implementer that ignores or overrides most of what it inherits. → drop the inheritance, use composition.

### 4. Spawn both sub-agents in parallel

Issue both sub-agent calls together, in the foreground, and aggregate the reports they return.

**Standards sub-agent prompt** should include:

- The full diff command and commit list, with the instruction to report only on lines changed in the diff.
- The list of standards-source files and the automated checks you found in step 3, **plus the smell baseline from step 3** pasted in full (the sub-agent has no other access to it).
- The brief: "Report, per file/hunk where relevant, (a) every place the diff violates a documented standard: cite the standard (file + the rule); and (b) any baseline smell you spot: name it and quote the hunk. Distinguish hard violations from judgement calls: documented-standard breaches can be hard, but baseline smells are always judgement calls, and a documented repo standard overrides the baseline. Skip anything the listed automated checks enforce. Tag each hard breach that is a fixed syntactic pattern, banned API, import shape or file-location rule as mechanical (a lint rule or hook could catch it); leave judgement calls untagged. After the findings, add a separate Notes list of documented standards you found vague, contradictory or stale while applying them, and say if no CODING_STANDARDS.md exists; Notes are not findings. Under 400 words."

**Spec sub-agent prompt** should include:

- The diff command and commit list, with the instruction to judge only what the diff changes.
- The path or fetched contents of the spec.
- The brief: "Report: (a) requirements the spec asked for that are missing or partial; (b) behaviour in the diff that wasn't asked for (scope creep); (c) requirements that look implemented but where the implementation looks wrong. Quote the spec line for each finding. Under 400 words."

If the spec is missing, skip the Spec sub-agent and note this in the final report.

### 5. Check user comments

Look for review comments the user left on the PR (`gh pr view --json comments,reviews` and `gh api repos/{owner}/{repo}/pulls/<n>/comments` for inline ones) or in the issue. Skip resolved threads and bot comments. If none exist, say so and move on.

For each comment, check the current diff: has the issue it raises actually been fixed? Report each as fixed, not fixed, or partially fixed, quoting the comment and citing the file/lines that show it. Don't take a "done" reply or a resolved thread as proof.

When a comment matches a pattern that recurs across the PR's comments, record it as a note for step 6: a standard or automated check could cover it.

### 6. Aggregate

Present the two reports under `## Standards` and `## Spec` headings, verbatim or lightly cleaned, then the step 5 results under `## Comments`. Format `## Comments` as a Markdown table with `Comment | Status | Evidence` columns: one row per comment, with its quote, fixed/not fixed/partially fixed status, and file/line citations. If there are no comments, say so under the heading. Close with `## Notes`: the Standards sub-agent's Notes and step 5's recurring-pattern notes, each as a suggestion to add, clarify or remove a standard or automated check. Notes are additional comments, not findings. Do **not** merge or rerank findings, because the two axes are deliberately separate (see _Why two axes_).

End with a one-line summary: total findings per axis (Notes excluded), the worst issue _within each axis_ (if any), and how many user comments remain unfixed. Don't pick a single winner across axes: that's the reranking the separation exists to prevent.

### 7. Select PR inline comments

If the review is of a PR, recommend inline comments for findings (Notes excluded). Leave out any finding that an existing PR comment already raises, whether fixed or not, from any author (users, bots, and resolved threads included; step 5's filters don't apply here): don't create it again. Present the remaining recommendations as a numbered list, each with its file, changed line, and proposed comment text. Say when there are none. Ask which numbers, if any, the user wants to add. Wait for their answer before step 8; keep only the selected comments, anchored to changed lines. Skip steps 7–10 when there's no PR.

### 8. Choose the review result

After the inline-comment selection, recommend a result and ask the user which result to apply:

- **Approve**: only minor issues, or none.
- **Request changes**: issues that need to be looked at before merge.

Wait for their answer before step 9.

### 9. Choose the review comment

After the review result, ask what review-level comment, if any, the user wants to add; suggest a short draft based on the findings. Wait for their answer before step 10. GitHub requires a review body for **Request changes**: if the user chooses that result and declines a comment, explain the requirement and ask them to approve a short summary or supply their own text.

### 10. Submit the review

Once the user has answered each question, submit one review on the PR with the chosen result, review comment (if any), and inline comments selected in step 7 (e.g. `gh api repos/{owner}/{repo}/pulls/{n}/reviews` with `event` set to `APPROVE` or `REQUEST_CHANGES`).

## Why two axes

A change can pass one axis and fail the other:

- Code that follows every standard but implements the wrong thing → **Standards pass, Spec fail.**
- Code that does exactly what the issue asked but breaks the project's conventions → **Spec pass, Standards fail.**

Reporting them separately stops one axis from masking the other.
