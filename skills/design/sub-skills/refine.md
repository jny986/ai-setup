---
name: refine
description: "Improve an existing interface's hierarchy, density, typography, color, layout, motion, or finish while preserving its established identity and behavior."
license: Apache-2.0
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable
  based_on_version: main(2f98774), main(2f98774), main(2f98774), main(2f98774), main(2f98774), main(2f98774), main(2f98774), main(2f98774), main(2f98774)
  based_on_skill: bolder, quieter, distill, typeset, layout, colorize, animate, delight, polish
---

# Refine an interface

Translate an improvement request into targeted changes to an implemented interface. Preserve confirmed identity, factual content, functionality, and scope. A requested replacement direction belongs in [shape](shape.md); a diagnosis-only request belongs in [audit](audit.md); changes to the task's steps or recovery path belong in [flow](flow.md).

## Workflow

1. **Inspect the target in context.** Read existing `DESIGN.md`, relevant product and brand guidance, tokens, components, and neighboring screens. Use [design-context](references/design-context.md) where decisions are missing. View the target at representative sizes and exercise the affected interactions. Finish with the user's intended improvement, observed friction, and the established system the changes must fit. If rendering is unavailable, identify the evidence available and limit visual claims accordingly.
2. **Diagnose the cause.** Explain why the target feels flat, noisy, dense, inconsistent, or unfinished in terms of hierarchy, grouping, emphasis, reading, or feedback. Use the reference table below for the dimensions implicated by that diagnosis. State the intended user effect and the smallest coherent set of changes. Finish when every planned change addresses an observed problem or the user's explicit direction.
3. **Apply the refinement.** Work at the narrowest correct layer: adjust a shared token or component for repeated drift, or the local composition for an isolated issue. Check the callers of shared changes. Strengthen emphasis through deliberate contrast and quieter surroundings; reduce noise while preserving useful hierarchy and access to required information. Introduce personality at moments where it supports comprehension, confidence, or a meaningful achievement. Finish when the target expresses the requested direction and affected uses remain coherent.
4. **Verify and report.** Inspect the changed states at relevant widths, themes, and input methods; check long content, zoom or text scaling, focus, contrast, and reduced motion where affected. Batch the observed fixes, then confirm them. For a confirmed behavioral defect, use an existing meaningful regression check where available. Record durable approved system changes through [document](document.md). Finish with the actual changes, evidence checked, and remaining limits.

## Choose references by cause

Read only the references needed for the target.

| Cause or requested effect | Reference and decision |
|---|---|
| Flat or competing emphasis; unclear reading order | [layout-composition](references/layout-composition.md): focal point, grouping, density, alignment, and rhythm. |
| Weak hierarchy or uncomfortable reading | [typography](references/typography.md): established faces, role scale, measure, weight, wrapping, and font delivery. |
| Color lacks meaning or feels excessive | [color-palette](references/color-palette.md), plus [dark-mode](references/dark-mode.md) for themes: semantic roles, dosage, and actual foreground/background contrast. |
| Motion lacks purpose or feedback feels abrupt | [motion-design](references/motion-design.md): continuity, acknowledgment, interruption, reduced motion, and rendering cost. |
| Inconsistent components or repeated style drift | [design-system](references/design-system.md): existing tokens, variants, and states. |
| Repeated implementations need consolidation | [systematize](systematize.md): extract shared patterns, migrate consumers, and verify parity. |
| A new device, input method, or platform | [adapt](references/adapt.md), with [native-platforms](references/native-platforms.md) for native apps. |
| A screenshot or mockup defines the target | [reference-to-ui](references/reference-to-ui.md): map regions, implement, and compare equivalent renders. |
| Final finish across an otherwise settled experience | [polish](references/polish.md): inspect the whole affected path and resolve its rough edges. |
| Failures under unusual content, interruption, or localization | [harden](references/harden.md): reproduce applicable stress cases and verify recovery. |
| A measured load or interaction delay | [optimize](references/optimize.md): establish a baseline, fix the evidenced bottleneck, and compare under the same conditions. |
| The user needs alternatives before choosing | [generate](references/generate.md): build comparable, viewable variants. |

A request for “bolder” can be met with clearer structure or stronger use of existing type and motifs. A request for “quieter” can be met with fewer competing accents or less motion. Choose the treatment from the target's purpose and identity rather than a fixed palette, font count, or decorative recipe. Preserve factual meaning and required capabilities when simplifying.

Completion: the requested improvement is visible in the rendered target, affected interactions still work, and verification limits are stated.
