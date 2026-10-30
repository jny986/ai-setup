---
name: code-review
description: "Use to review development changes or a repository against standards, requirements, UI/UX and security; report findings."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: code-review, retro
---

Review and report; do not fix code, commit or push. The caller handles remediation. Apply Standards, Spec, applicable UI/UX and Security separately. Findings need evidence, impact and a suggested remedy; a coverage gap is not a clean result.

## 1. Capture scope

Identify the context from the request. If it names a PR to review, use `pr-review` instead.

- **Development:** review the requested committed changes, pending changes or both. Record base/head SHAs, diff command, changed files and commits, plus intended untracked files. With no stated base, use the PR base, the branch's origin or the repository default branch, in that order. Ask if none resolves. For pending changes fingerprint their contents. A caller such as `finalise` may supply its own diff and scope.
- **Repository:** review the repository or requested paths, including existing code without a diff. Record the revision, included and excluded paths, and practical coverage limits.

Resolve the scope before review; report an empty change set for a diff review. Keep reviewed files unchanged during analysis. If the state changes, recapture it and rerun affected axes, including dependencies; when impact is uncertain, rerun the axis.

## 2. Gather sources

Find applicable root and nested repository instructions and standards, including `CODING_STANDARDS.md` and `CONTRIBUTING.md` when present. Follow relevant references and identify lint, typecheck, test, CI and hook checks; note missing automated guardrails.

Find relevant requirements from user-supplied paths, PR descriptions, commits, branches and linked tickets, then configured docs, `docs/` and `specs/`. Use the configured issue tracker and fetch full relevant ticket descriptions and comments, following requirements links. Record inaccessible sources and conflicts. If no spec is found, continue without asking and report **unable to find a spec**. An inaccessible known spec is a separate limitation.

## 3. Review

Read [reviewer briefs and smell baseline](references/code-review-briefs.md). Prefer a separate `review` agent for each applicable axis; if unavailable or unable to launch, use available general-purpose reviewers or review directly. Launch applicable reviewers in parallel when permitted and capacity allows. Give each the captured scope, relevant sources, any findings supplied by the caller and shared checks. Report the method and limitations. Reviewers inspect and report only; the coordinator owns questions and ticket choices; the caller owns any publication.

- **Standards:** apply documented rules and the smell baseline; distinguish documented violations from judgment calls.
- **Spec:** assess the selected scope against available requirements. If none were found, skip and report the missing spec.
- **UI/UX:** apply when the selected scope includes user-facing UI. Use the design audit lenses. Use a live browser when available and a target serving the reviewed code exists; otherwise report a static review. Ask once for a URL, start command and test login if needed. Capture linked annotated screenshots or video of each affected state or interaction when possible; otherwise report the limitation and the best available evidence.
- **Security:** always perform the applicable `security review-code` analysis, including every matching guide and file accounting. Validate its coverage and distinguish confirmed vulnerabilities from needs-verification items. Missing dependencies or incomplete analysis are coverage gaps.

Wait for every review or report its failure as a gap. Verify unsupported findings against the code. For each distinct security item needing verification, offer to create an investigation ticket; create only selected tickets using the configured tracker, with evidence, potential impact and investigation needed, appropriate to the tracker's sensitivity.

## 4. Report

Report each axis separately with severity, file/line evidence, impact, remedy, covered files, exclusions and limitations. Include confirmed security findings and needs-verification items. Record vague or contradictory standards and recurring comment patterns as notes, not findings. State the review method and counts by axis. Report missing specs and inaccessible sources.

An incomplete essential axis must not be presented as clean or support an approval recommendation. A spec that cannot be found alone does not prevent approval; assess an inaccessible known spec's impact in context. If the reviewed state changed, refresh and re-review affected areas before reporting.

Return the report to a calling workflow such as `finalise` or `pr-review`. When the user invoked code-review directly, end by asking only what they want to do about the issues found, then wait; with no issues, report that and end. Do not fix, commit, push or publish, and do not offer other next steps.
