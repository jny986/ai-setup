---
metadata:
  version: "1.0.0"
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: code-review, retro
---

# Publish a PR review

Use from [pr-review](../pr-review.md) after code-review reports its findings.

## Suggest and select

Consider all outstanding findings, including prior findings and those the user may not select. Recommend **Approve** when no issues require fixes before approval, including when only minor optional issues remain; recommend **Request changes** when issues need attention before merge. Explain the recommendation. An incomplete essential axis cannot support approval; a missing spec alone need not prevent it.

Present the completed review for the user's decisions in exactly these five sections, in order. Keep each clear and concise; retain the evidence, limitations and choices needed to complete the review. State when a section has no items.

1. **Findings of the review:** findings by axis, with severity, file/line evidence, impact and remedy. Include findings that cannot be anchored to changed lines and consider them for the verdict.
2. **Existing issues and status:** a table of relevant existing PR issues, their status, evidence, author and link. Include outstanding prior findings and identify duplicate concerns.
3. **Issues recommended to add to the PR:** a numbered list of actionable, still-present, nonduplicate findings anchored to changed lines. Order them Critical, High, Medium, Low across axes; include the file, line and complete proposed comment for each.
4. **Code review notes:** decision-relevant notes and limitations, including missing or inaccessible specs, incomplete coverage and evidence limitations when applicable.
5. **Recommended review result:** the recommended outcome and concise reason. Ask which numbered comments to include and which outcome to submit: Approve, Request changes or Comment.

Show no other information in this decision display. The prior-findings continue question, security investigation ticket choices and submission errors remain separate interactions when applicable.

Start each comment with `[Severity][Issue type][Required]` or `[Severity][Issue type][Optional]`, then state concern, impact and suggested change. Required means a fix is needed for approval; Optional means it is not. Severity and required status are independent; explain unusual combinations. Issue types are Security, Code smell, Standard violation, Spec mismatch and UI/UX. Name the affected state or step and audit lens for UI/UX; frame smells as judgment calls.

Preserve security severity. For other axes, Critical means severe failure such as data loss; High, major functional or design impact; Medium, meaningful localized impact; Low, minor improvement. Map UI/UX P0–P3 to Critical–Low.

Before suggesting comments, use [GitHub review operations](gh-review.md) to read all PR conversation comments, review bodies, inline threads and replies from every author, including resolved and outdated entries, exhausting pagination. Compare the underlying concern and requested change, not just wording or line. Suppress duplicates and show their authors and links; retain distinct concerns. If history is inaccessible, report the gap and complete the duplicate check before proposing comments.

Wait for both choices; the user may supply an overall comment.

## Prepare and submit

Use the user's overall comment if supplied. Otherwise generate it after the outcome choice using this template, and submit without separate approval:

```markdown
[Approving / Requesting changes / Commenting] — [one-sentence reason consistent with the chosen result].

[If needed: one short sentence highlighting important concerns or a material review limitation.]
```

Keep it to one or two sentences, grounded in the review; avoid repeated details, links, test summaries and issue lists. If the user explicitly requests no overall comment, omit it for Approve. GitHub requires a body for Request changes and Comment; explain this and ask for the generated summary or replacement.

Before submission, check the PR head and refresh comment history and the duplicate check. If the head changed, refresh scope and rerun affected reviews, then present updated suggestions and obtain selections again. Remove newly duplicated selected comments and report their links.

Submit one review with the chosen outcome, body and remaining selected inline comments using [GitHub review operations](gh-review.md). If submission fails, report the failure and retain the full proposed review; do not claim success or silently change the outcome. Check whether a review was posted before retrying.
