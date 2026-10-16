---
name: reference-to-ui
description: "Translate an approved screenshot, mockup, or design frame into a working UI and compare equivalent rendered states."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable
  based_on_version: main(2f98774), main(2f98774), main(2f98774), main(2f98774)
  based_on_skill: new-work, visualize, region-map, component-review
---

# Implement a visual reference

Use when a screenshot, mockup, or design frame is the implementation target. Establish whether it is an exact reference, a composition guide, or inspiration; preserve any authority the user already specified. A mood board supports direction but does not define every region. For open design decisions use [shape](../shape.md); for generated assets use [image-generation](image-generation.md).

## Workflow

1. **Inspect the reference and project.** Open the original at full resolution and inspect detail crops. Record its dimensions, content, available source assets, and any known fonts or tokens. Read existing `DESIGN.md` and the brief. Resolve material conflicts between the reference and confirmed product behavior, brand, or accessibility needs. Finish with the target, fidelity expected, and explicit unknowns.
2. **Map salient regions.** Identify navigation, text blocks, controls, content images, decorative assets, and major containers. Record relative position and size, alignment, spacing, type hierarchy, surface colors, and layering. Keep separately changing or moving content separate from its frame. Check crops against the original so gaps between text blocks do not hide artwork. Finish when every important visible region has a role and implementation approach.
3. **Choose media and prepare assets.** Use semantic UI for live text and controls, vectors or code for suitable diagrams and geometry, and source or generated image assets for photographic or painted material. Reuse supplied assets at their existing paths where practical. A flattened mockup is reference evidence; extracting production artwork from it requires sufficient resolution and a suitable source. Keep functional text, data, and controls live. Finish when required assets exist or unavailable inputs are named, with their intended scale, crop, and transparency checked.
4. **Build the composition.** Translate measured relationships into the project's layout system. Match type character, scale, line breaks, image placement, and hierarchy at the reference viewport, then define reflow for other sizes. Use the first viewport to calibrate shared decisions before repeating them across the rest of the surface. Preserve required behavior and accessibility; explain consequential adaptations rather than silently changing the composition. Finish when all mapped regions appear and the surface works beyond a fixed screenshot size.
5. **Compare equivalent renders.** Capture with the reference's viewport and, when known, pixel density. Wait for fonts and images; settle entrance motion and confirm the capture shows the intended state. Compare side by side, using overlays or region crops where useful. Diagnose missing content, incorrect structure, type metrics, spacing, color, and crop separately. Fix observed discrepancies in a batch, then recapture affected sizes. Completion requires evidence of the intended fidelity and working responsive behavior, with remaining differences and unavailable assets stated.

## Comparison rules

- Keep the original reference intact. Compare current output against that file rather than a remembered impression or a regenerated substitute.
- Compare whole-page structure and detailed regions; a small full-page thumbnail can hide typography and placement errors.
- Align viewport, scroll position, theme, content, and interaction state before interpreting a difference. Pixel diffs can expose drift but also reflect font rasterization or image noise.
- Record concrete mismatches such as line count, width, alignment, or displacement. Numeric similarity alone does not prove that a control is usable or the composition is correct.
- When iteration stops improving the result, report the remaining cause and options; an unavailable font, asset, or runtime needs an explicit fidelity limit.

Use [polish](polish.md) for finish, [adapt](adapt.md) for a new target context, and [native-platforms](native-platforms.md) for native implementation. Retain durable approved system changes through [document](../document.md); task-specific measurements can stay with the brief in the router's project reference directory.
