# Git code-review sub-skill spec

Status: local spec, based on the agreed interview decisions. Implementation is not included.

## Problem Statement

Changes to the code-review sub-skill have disrupted the expected pull request review experience. A reviewer needs ordered, actionable inline suggestions, a recommended review outcome, and an appropriate overall comment. The sub-skill also needs a durable contract so future changes can be checked against its requirements.

## Solution

Define the behavior of code review in three contexts: checking code during development, reviewing a repository for fixes that should be made, and reviewing a pull request. Review the selected scope against separate axes, report evidence and coverage, and let the user decide what to publish on a PR. Review is inspection and reporting only; fixes belong to another workflow.

## User Stories

1. As a reviewer, I want a fixed and recorded review scope, so that findings refer to a known set of changes.
2. As a reviewer, I want standards, spec, applicable UI/UX and security reviewed separately, so that a clean result on one axis does not hide a problem on another.
3. As a reviewer, I want each finding supported by evidence and impact, so that I can judge the suggested change.
4. As a reviewer, I want missing or incomplete coverage reported, so that I can assess the confidence of the review.
5. As a reviewer, I want the review to continue when no spec is found, so that other useful analysis is not blocked.
6. As a PR reviewer, I want previous findings checked against current code, so that the review reflects outstanding work.
7. As a PR reviewer, I want a clear choice to continue when previous non-minor findings are unfixed or cannot be verified, so that I control whether a fresh review proceeds.
8. As a PR reviewer, I want actionable inline suggestions ordered by severity, so that I can address the most important concerns first.
9. As a PR reviewer, I want suggestions marked required or optional for approval, so that their merge implications are clear.
10. As a PR reviewer, I want duplicate concerns suppressed with links to existing comments, so that I do not repeat feedback.
11. As a PR reviewer, I want a recommended review outcome and the choice of final outcome, so that I retain control of my review.
12. As a PR reviewer, I want an overall comment generated when I do not provide one, so that the submitted review explains its outcome.
13. As a reviewer, I want uncertain security concerns identified and an investigation ticket offered, so that they can be followed up without being misrepresented as confirmed vulnerabilities.
14. As a reviewer, I want the review to avoid making fixes, so that remediation stays in its own workflow.
15. As a maintainer, I want regression scenarios for the contract, so that future skill changes do not silently remove expected behavior.
16. As a developer, I want to review committed or pending code during development, so that I can identify issues before proceeding.
17. As a repository maintainer, I want to review a repository or a specified part of it for issues that need fixing, so that I can plan remediation even when there is no change set to compare.
18. As a PR reviewer, I want findings tailored to the PR's changes and publication workflow, so that feedback is actionable for its author.

## Implementation Decisions

- Retain the git router and code-review sub-skill, its reviewer briefs and publication hand-off. Update their instructions and affected callers together so that no caller expects code review to perform fixes or a fix/re-review loop. Keep public skill documentation current.
- Identify the review context and scope from the user's request:
  - **Development review:** review the requested committed changes, pending changes or both, including intended untracked files. Record the base and head or other selected scope, diff and file list; surrounding code supplies context.
  - **Repository review:** review the repository or the paths the user specifies for issues that should be fixed. Capture the revision and included and excluded paths; findings may concern existing code and do not require a diff or changed-line anchor. Report practical coverage limits when the repository is too large to review completely.
  - **PR review:** capture the resolved base and head, diff and changed files. Findings concern the PR's changes; surrounding code supplies context. Apply the PR history and publication requirements below.
- For all contexts, record the scope before analysis. If the reviewed state changes, refresh the scope and re-review affected areas before using findings or submitting a review.
- Review Standards, Spec, applicable UI/UX and Security on every review. UI/UX applies when the selected scope includes user-facing UI. Keep their findings and coverage separate in the report. Identify skipped axes, limitations and incomplete work; never describe incomplete coverage as a clean result.
- For UI/UX findings, provide linked, annotated screenshots or video showing the issue and affected state or interaction when possible. If capture or annotation is unavailable, report the limitation and cite the best available evidence.
- Prefer a separate `review` agent for each applicable axis when available. When delegation or that agent is unavailable, review directly with equivalent coverage. Report the method and any resulting limitations.
- Discover relevant specs and linked requirements using the existing project and tracker context. If no spec can be found, continue without asking and report **unable to find a spec** at the end. Report a known but inaccessible spec separately, including its reference and access failure. A missing spec alone does not preclude recommending approval; assess the effect of an inaccessible known spec in context. An essential incomplete review otherwise must not be presented as clean or result in an unsupported approval recommendation.
- On PRs, inspect complete prior review history and verify actionable prior findings against current code. For an unfixed non-minor finding, or one whose status cannot be verified, show the evidence and explicitly ask **Continue the review?** Distinguish this choice from the results already shown. Honor an existing explicit instruction to continue. If the user stops, report outstanding or uncertain items; if they continue, carry those items forward without treating them as fixed.
- Suggest inline comments for actionable, still-present findings that can be anchored to changed lines. Include unanchorable findings in the report and consider them for the verdict. Order suggestions across axes from Critical to High, Medium and Low. Preserve security severity; map UI/UX priorities consistently with the publication guidance.
- Format each inline suggestion with `[Severity][Issue type][Required]` or `[Severity][Issue type][Optional]`, followed by the concern, impact and suggested change. Required means a fix is needed for approval; Optional means it is not. Severity describes impact independently, so an unusual combination is allowed and explained.
- Check all PR conversation comments, review bodies, threads and replies, including resolved and outdated entries, for the same underlying concern. Suppress duplicates and show the existing author and link. Refresh this check before submission; report inaccessible history as a limitation and do not claim the duplicate check is complete until it is complete.
- Recommend **Approve** when no outstanding issues require a fix before approval, including when only minor optional issues remain. Recommend **Request changes** when issues need attention before merge. Explain the recommendation and consider all outstanding findings, including prior findings and suggestions the user does not select. The user may select Approve, Request changes or a neutral Comment outcome.
- Present the overall recommendation prominently before a numbered list of recommended issues to add as PR inline comments. Include the full proposed comment and its location for each numbered issue, so the user can select items by number. State explicitly when there are no recommended issues.
- Present the ordered suggestions and recommended outcome, then let the user select inline comments and the final outcome. Use a user-supplied overall comment when provided. Otherwise generate the overall comment from the existing publication reference template, adapted to the selected outcome, and submit it without a separate approval step. The template is a concise outcome and reason, with a second sentence only when needed for important concerns or limitations.
- Submit the selected outcome, body and selected nonduplicate inline comments as one PR review. If submission fails, report the failure and retain the complete proposed review; do not claim success or silently substitute another outcome.
- Report security findings and distinguish confirmed vulnerabilities from items needing verification. Offer to create an investigation ticket for each distinct needs-verification item; create only the tickets the user selects, with evidence, potential impact and investigation needed, appropriate to the tracker's sensitivity.
- The sub-skill performs no fixes, commits or pushes, including for security findings, local reviews and `finalise`. Return findings to the caller for any separate remediation workflow.
- Development and repository reviews end with the report, including actionable findings and suggested fixes, without changing code. `finalise` receives the development review results without the PR publication hand-off. PR reviews use the publication hand-off after analysis.

## Testing Decisions

- Test observable workflow behavior and hand-offs rather than reproducing the instruction text in assertions. Prefer existing repository skill and checker test seams; use the highest practical seam and avoid introducing a new one unless needed.
- Add automated regression checks where practical, supplemented by realistic end-to-end review scenarios where static checks cannot establish behavior. Cover the code-review sub-skill, its publication hand-off and affected callers.
- Exercise at least: development reviews of committed and pending code, including intended untracked files; a repository review that finds existing issues without requiring a diff; a PR with findings across axes ordered by severity and labeled required/optional; minor optional findings yielding an approval recommendation; selected comments and each review outcome; a generated template comment without separate confirmation; a supplied comment; duplicate suppression; prior non-minor findings prompting a clearly named continue decision; missing and inaccessible specs; incomplete security coverage; a needs-verification ticket choice; a changed PR; failed publication; and development, repository and `finalise` reviews that make no fixes.
- Verify that the review considers unselected and prior findings in its recommendation and never makes fixes, commits or pushes. Run the repository's applicable skill, documentation-site and overall checks when implementing the change.

## Out of Scope

- Implementing or publishing the skill changes as part of this spec.
- Fixing reviewed code or defining the separate remediation workflow.
- Automatically creating security investigation tickets without the user's selection.

## Further Notes

This local spec captures the agreed requirements; it does not itself establish that the existing implementation satisfies them. The existing publication template uses Approving and Requesting changes wording; its neutral Comment wording needs to be defined during implementation while retaining the same concise structure.
