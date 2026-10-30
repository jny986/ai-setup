# Git code-review sub-skill spec

Status: local behavioral contract, based on the agreed interview decisions and the split of PR review into its own sub-skill. This spec does not establish that the implementation passes it.

## Purpose and scope

A reviewer needs findings against a known scope, with evidence and coverage reported separately for each review axis. `/git code-review` reviews development changes or existing repository code and returns a report. It also supplies the shared analysis for `/git pr-review`. Review is inspection and reporting; remediation belongs to the caller.

The [PR-review spec](git-pr-review-spec.md) defines PR-specific scope, prior feedback, recommendations and publication. `finalise` uses code-review for internal branch validation even when a PR exists; it handles remediation separately.

## Acceptance criteria

### Scope

1. For a development review, capture the requested committed changes, pending changes or both, including intended untracked files. Record base and head SHAs, diff command, changed files and commits. With no stated base, use the PR base, the branch's origin or the repository default branch, in that order; ask if none resolves. Fingerprint pending contents. Honor a caller-supplied scope and fixed point.
2. For a repository review, capture the revision, included and excluded paths and practical coverage limits. Review existing code without requiring a diff or changed-line anchor.
3. Resolve scope before analysis and report an empty change set for a diff review. Keep reviewed files unchanged. If state changes, recapture it and rerun affected axes and dependencies; rerun the axis when impact is uncertain. Surrounding code may provide context.

### Sources and analysis

4. Find applicable root and nested instructions, standards and relevant references, including `CODING_STANDARDS.md` and `CONTRIBUTING.md` when present. Identify lint, typecheck, test, CI and hook checks and note missing automated guardrails.
5. Find relevant requirements in user-supplied paths, PR descriptions, commits, branches, linked tickets and configured documentation. Use the configured tracker to fetch full relevant ticket descriptions and comments and follow requirements links. Record inaccessible sources and conflicts. If no spec is found, continue without asking and report **unable to find a spec**; report a known inaccessible spec separately.
6. Review Standards, Spec, applicable UI/UX and Security separately. UI/UX applies when the selected scope includes user-facing UI; Security always receives the applicable `security review-code` analysis, including matching guides and file accounting. Apply documented standards and the smell baseline, distinguishing documented violations from judgment calls. Skip the Spec axis if requirements cannot be found and report the gap.
7. Prefer a separate `review` agent for each applicable axis when available and permitted; otherwise use available reviewers or review directly with equivalent coverage. Give reviewers the scope, relevant sources, caller-supplied findings and shared checks. Wait for each review or report its failure as a coverage gap. Verify unsupported findings against the code. Report the method and limitations.
8. For UI/UX, apply design audit lenses and use a live browser when available and a target serving the reviewed code exists; otherwise report a static review. Ask once for a URL, start command and test login if needed. Provide linked annotated screenshots or video of the affected state or interaction when possible; otherwise report the limitation and cite the best available evidence.
9. Distinguish confirmed security vulnerabilities from items needing verification. Offer an investigation ticket for each distinct uncertain item; create only tickets the user selects, with evidence, potential impact and investigation needed, appropriate to the tracker's sensitivity.

### Report and hand-offs

10. Report each axis separately with severity, file and line evidence, impact, remedy, covered files, exclusions and limitations. Include confirmed security findings and items needing verification. State the review method and counts by axis. Record vague or contradictory standards and recurring comment patterns as notes, not findings. Report missing specs and inaccessible sources.
11. Do not present incomplete essential coverage as clean or use it to support an approval recommendation. A spec that cannot be found alone does not prevent approval; assess an inaccessible known spec's effect in context. If state changed, refresh scope and re-review affected areas before reporting.
12. Return the report to the caller without fixing code, committing or pushing. When the user invoked code-review directly, end the report by asking only what they want to do about the issues found, and wait for the answer; take no action on it within code-review. Development and repository reviews otherwise end with the report. `finalise` receives the development review results for its separate remediation workflow; `pr-review` receives the shared analysis for its separate PR workflow. Code-review itself does not publish a PR review.

## Agent verification

Read `skills/git/SKILL.md`, `skills/git/sub-skills/code-review.md`, its reviewer briefs, the applicable security review guidance, and the `finalise` and `pr-review` hand-offs. Trace each criterion through the instructions. Report each as pass, fail or unverified with evidence and coverage gaps. Instruction inspection establishes what the workflow directs, not that a live review or agent execution succeeds.

Use [workflow scenarios](../../tests/code-review-scenarios.md) as a starting point and simulate the review without changing code. Cover these cases even if a scenario must be added or extended:

- Committed and pending development changes, including an intended untracked file; an empty diff; a caller-supplied fixed point; and a changed review state.
- A repository or selected path with existing issues, no diff and explicit coverage limits.
- Separate axis reports, applicable UI/UX, missing and inaccessible specs, unavailable reviewers and incomplete security coverage.
- Confirmed and uncertain security findings, with an investigation ticket selected or declined.
- A `finalise` hand-off with pending changes and an existing PR, and a `pr-review` hand-off carrying scope and prior findings. Verify code-review makes no fixes, commits, pushes or publication.

Use automated checks where practical and report their limits. Run applicable repository skill and documentation checks when changing the implementation. Do not treat a simulation as a live browser, tracker or agent execution.

## Out of scope

Fixing reviewed code, defining remediation, automatically creating investigation tickets, and PR-specific history and publication are outside this contract.
