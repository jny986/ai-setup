---
metadata:
  version: "1.0.0"
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: code-review, retro
---

# Publish a PR review

Use after [code-review](../code-review.md) reports its findings. Internal validation such as `finalise` skips this hand-off.

## Suggest and select

Consider all outstanding findings, including prior findings and those the user may not select. Recommend **Approve** when no issues require fixes before approval, including when only minor optional issues remain; recommend **Request changes** when issues need attention before merge. Explain the recommendation. An incomplete essential axis cannot support approval; a missing spec alone need not prevent it.

Present the recommendation first under **Overall recommendation**, with its outcome and reason. Follow it with **Recommended issues to add to the PR**, a numbered list of actionable findings still present on changed lines, ordered Critical, High, Medium, Low across axes. Include the file, line and complete proposed comment for each issue so the user can select by number. If there are none, say so. Report findings that cannot be anchored in the review report and consider them for the verdict.

Start each comment with `[Severity][Issue type][Required]` or `[Severity][Issue type][Optional]`, then state concern, impact and suggested change. Required means a fix is needed for approval; Optional means it is not. Severity and required status are independent; explain unusual combinations. Issue types are Security, Code smell, Standard violation, Spec mismatch and UI/UX. Name the affected state or step and audit lens for UI/UX; frame smells as judgment calls.

Preserve security severity. For other axes, Critical means severe failure such as data loss; High, major functional or design impact; Medium, meaningful localized impact; Low, minor improvement. Map UI/UX P0–P3 to Critical–Low.

Before suggesting comments, use [GitHub review operations](gh-review.md) to read all PR conversation comments, review bodies, inline threads and replies from every author, including resolved and outdated entries, exhausting pagination. Compare the underlying concern and requested change, not just wording or line. Suppress duplicates and show their authors and links; retain distinct concerns. If history is inaccessible, report the gap and complete the duplicate check before proposing comments.

Show the recommendation even with no inline suggestions. Ask the user which numbered comments to include and which outcome to submit: Approve, Request changes or Comment. Wait for both choices; the user may supply an overall comment.

## Prepare and submit

Use the user's overall comment if supplied. Otherwise generate it after the outcome choice using this template, and submit without separate approval:

```markdown
[Approving / Requesting changes / Commenting] — [one-sentence reason consistent with the chosen result].

[If needed: one short sentence highlighting important concerns or a material review limitation.]
```

Keep it to one or two sentences, grounded in the review; avoid repeated details, links, test summaries and issue lists. If the user explicitly requests no overall comment, omit it for Approve. GitHub requires a body for Request changes and Comment; explain this and ask for the generated summary or replacement.

Before submission, check the PR head and refresh comment history and the duplicate check. If the head changed, refresh scope and rerun affected reviews, then present updated suggestions and obtain selections again. Remove newly duplicated selected comments and report their links.

Submit one review with the chosen outcome, body and remaining selected inline comments using [GitHub review operations](gh-review.md). If submission fails, report the failure and retain the full proposed review; do not claim success or silently change the outcome. Check whether a review was posted before retrying.
