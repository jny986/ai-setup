---
name: harden
description: "Exercise and improve UI resilience for content extremes, localization, failure, interruption, and recovery."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable
  based_on_version: main(2f98774)
  based_on_skill: harden
---

# UI hardening

Use when an interface must keep working beyond the happy path: unusual content, failures, interrupted interaction, slow networks, or localized text. For a final finish pass, use [polish](polish.md). This reference covers user-visible resilience; route server-side input security to the project's security guidance.

1. **Build an edge-case matrix.** For each primary task, select the cases it can encounter from the table below. Record the expected visible state and recovery action. Finish when every selected case has an expected result.
2. **Exercise and fix.** Reproduce each case in the running interface or a representative component state. Preserve user input and task progress through validation and network errors. Keep controls usable after an interrupted gesture or repeated action. Finish when every reproduced failure has a specific fix and the same case succeeds on retry.
3. **Verify the path.** Rerun the selected matrix at supported widths and input methods. Add a behavioral regression for a confirmed failure when the project can test it meaningfully. Report the environment used for touch, network, and locale checks and what remained untested.

| Case | Check |
|---|---|
| Content extremes | Empty and single-character values; long names, titles, and labels; large counts; many list items; missing images. Text wraps or truncates without hiding essential meaning. |
| Language and format | Longer translations, RTL layout, CJK and emoji, plural forms, dates, numbers, and currency. Containers and controls expand with content. |
| Network and API | Slow, offline, timeout, validation, unauthorized, forbidden, missing, rate-limited, and server-error responses. Show status, a useful next step, and retry where appropriate. |
| State transitions | Initial load, pagination, refresh, empty result, success, disabled and permission-limited states. Feedback names what changed. |
| Repeated or interrupted input | Double submit, concurrent edits, canceled drag, lost pointer capture, release outside the control, app or window blur. The next attempt works without reset. |
| Accessibility resilience | Keyboard and screen-reader paths after dynamic updates, large text or zoom, high contrast, reduced motion, and non-color status cues. |

Choose test values and failure modes from the actual product. The matrix is complete when each applicable row has a reproduced result or a stated verification limit, and the primary task still succeeds after recovery.
