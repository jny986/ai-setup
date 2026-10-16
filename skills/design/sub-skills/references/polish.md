---
name: polish
description: "Finish an implemented interface through targeted checks of system consistency, task states, interaction, and visual detail."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable
  based_on_version: main(2f98774)
  based_on_skill: polish
---

# UI polish

Use for a final finish pass on an implemented interface whose direction is settled. Preserve the product's identity, content, behavior, and task scope. For a diagnosis before editing, use [audit](../audit.md); for stress conditions, use [harden](harden.md); for a measured speed problem, use [optimize](optimize.md).

1. **Establish the system.** Read `DESIGN.md`, the relevant brand kit, tokens, shared components, and neighboring flows; use [design-context](design-context.md) for missing decisions. Classify each discrepancy as a missing token, duplicated pattern, flow mismatch, or local defect. Finish when each proposed change has a clear owner and fits the existing system.
2. **Walk the whole path.** Use the feature at representative screen sizes and input methods. Include arrival, loading, empty, success, error, disabled, long-content, and permission states where they can occur. Record the rough edges and any existing audit findings. Finish when every reachable step and state has been viewed or listed as unavailable.
3. **Fix by impact.** Address blocked tasks, data loss, misleading state, and inaccessible paths first; then missing states, flow and hierarchy, responsive or token drift, and visual detail. Change the narrowest correct layer: a shared token or component for repeated drift, a local fix for a local defect. Finish when the recorded problems are resolved without unrelated visual changes.
4. **Verify.** Rewalk the path with keyboard and touch where applicable. Check supported widths, themes, zoom or large text, focus, contrast, content variants, image loading, console or runtime errors, and the source diff. Finish when each changed behavior has been observed in its relevant state and temporary code or assets are cleared.

A clean automated scan is supporting evidence; the rendered experience and task path decide whether the polish pass is complete. Report the changes and any remaining limitation.
