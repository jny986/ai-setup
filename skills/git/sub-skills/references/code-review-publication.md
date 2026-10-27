---
metadata:
  version: "1.0.0"
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: code-review, retro
---

# Publish a PR review

## 8. Select PR inline comments

Read only for the PR review hand-off in [code-review](../code-review.md), after its analysis and security loop are complete. Follow steps 8–11 in order. Internal branch validation such as `finalise` skips this hand-off.

Start with `## Suggested review result: APPROVE` or `## Suggested review result: REQUEST CHANGES`, using step 9's criteria. Follow with one sentence explaining the recommendation, then `### Suggested inline comments`. Show the verdict even when there are no suggested comments.

Recommend inline comments only for findings still present in the current diff, excluding Notes and verified fixes.

**Duplicate check.** Before proposing comments, read all PR conversation comments, review bodies, inline threads and replies using [GitHub review operations](gh-review.md), exhausting pagination. Include every author (the user, other reviewers, the PR author and bots), resolved threads and outdated comments; step 5's filters apply only to status reporting. Compare each candidate's underlying concern and requested change with this history, even when wording or line anchors differ. Suppress candidates already raised, retaining the existing comment's author and URL as evidence. A related comment counts as a duplicate only when it covers the same concern; keep distinct issues. Continue only when every candidate has been checked; if a source is inaccessible, report the gap and complete the check before proposing inline comments.

Show the recommendations in the review response as a numbered list ordered from highest to lowest severity (severities as defined below, across all axes), each with its file, changed line and full proposed comment text; say when there are none. Briefly list suppressed duplicates with links to the existing comments so the user can see where they were already raised. After showing the verdict and list, ask which numbers, if any, to add and wait before step 9. Keep only the selected comments, anchored to changed lines.

Start every proposed and submitted inline comment with `[Severity][Issue type]`, followed by the concern, impact and suggested change. Use `Security`, `Code smell`, `Standard violation`, `Spec mismatch` or `UI/UX` to match the finding. A UI/UX comment names the affected state or step and the audit lens. For example: `[Low][Code smell] Possible Duplicated Code: ...`. Keep code smells framed as judgement calls.

Preserve the security review's severity. For other findings, use `Critical` for severe failures such as data loss, `High` for major functional or design impact, `Medium` for a meaningful localized issue, and `Low` for a minor improvement. Map UI/UX P0 to `Critical`, P1 to `High`, P2 to `Medium` and P3 to `Low`. Base severity on demonstrated impact, not issue type. These labels describe individual findings; retain the separate review axes and use step 9 to choose the verdict.

## 9. Choose the review result

After the inline-comment selection, repeat the suggested review result prominently and ask the user which result to apply. Use these criteria for the recommendation:

- **Approve**: only minor issues, or none.
- **Request changes**: issues that need to be looked at before merge.

Wait for their answer before step 10.

## 10. Prepare the review comment

Once the user has selected the review result in step 9, draft the overall comment using the template below and show it under `## Suggested review comment`. Generate it only after their selection, including when it differs from the recommended result.

### Overall comment template

```markdown
[Approving / Requesting changes] — [one-sentence reason consistent with the chosen result].

[If present: one short sentence highlighting security issues covered in a separate comment or high-severity issues raised elsewhere in the review.]
```

Aim for 1–2 sentences, grounded in steps 1–7. Refer to important concerns in plain text, without links or repeated details. Include only context needed to understand the verdict; omit repeated assessments, test summaries and issue lists. Flag a material review limitation or accepted risk briefly when it affects merge readiness. Omit the second sentence when there is nothing important to highlight. The draft is ready when its status matches the user's choice and it accurately reflects outstanding concerns, including when the chosen result differs from the recommendation.

Use this generated comment as the review body and continue to step 11. If the user supplied replacement text, use it instead. Their inline-comment and review-result answers complete the required selections; the generated body needs no separate confirmation. If they explicitly request no overall comment, omit it for **Approve**. GitHub requires a review body for **Request changes**: if the user chooses that result and declines a comment, explain the requirement and ask them to use the generated summary or supply their own text.

## 11. Submit the review

After both selections, refresh the PR comment history and repeat step 8's duplicate check for the selected inline comments. Remove any newly duplicated comments and report their existing links; submit the remaining selection with the chosen result even when no inline comments remain.

Submit one review with the chosen result (`APPROVE` or `REQUEST_CHANGES`), the body from step 10, and remaining selected inline comments. Follow [GitHub review operations](gh-review.md) for the payload file and single `gh api` call, including any thread replies or other review writes.
