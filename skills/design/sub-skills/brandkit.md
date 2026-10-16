---
name: brandkit
description: "Create a project brand kit: a written identity guide and an HTML specimen of its logos, colors, typography, and applications. Use for new identities, existing-brand extensions, scoped refreshes, or a requested brand-kit image."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: Leonxlnx/taste-skill
  based_on_version: main(a60a36d)
  based_on_skill: brandkit
---

# Brand kit

Create `BRANDKIT.md` in the project reference directory as the written source of truth and `brandkit.html` beside it as the visual specimen when project files can be written. For production logo assets and a fuller identity system, use [brand-identity](references/brand-identity.md). A raster presentation board is optional; use [image-generation](references/image-generation.md) when the user requests one or imagery would clarify the identity.

## Workflow

1. **Gather project references.** Look in the project reference directory for briefs, existing guidelines, logos, fonts, images, and earlier brand-kit files. Read `PRODUCT.md` for confirmed audience, positioning, and constraints. For an existing code project, read `DESIGN.md` and use [design-context](references/design-context.md) to find saved tokens and assets elsewhere. Use the request and supplied assets to decide whether this is a new identity, an extension, or a scoped refresh. Preserve existing decisions outside the requested scope. If sources conflict or a required asset is missing, resolve only the material gap with the user before proceeding.
2. **Set the concept.** Identify the audience, category, product or service, intended feeling, and one distinctive idea. For a new logo, explain its intended form and meaning; for an existing logo, document and show the supplied mark without inventing construction history. Choose colors, typography, imagery, and applications that express the same idea.
3. **Write `BRANDKIT.md`.** Record the brand name and promise in terms consistent with `PRODUCT.md`; audience and personality; logo or wordmark and usage; palette with exact values, roles, and contrast pairings; font families, weights, fallbacks, and roles; imagery and graphic rules; and representative applications. Link existing source assets with paths relative to the project reference directory. Mark proposed choices as proposals and unresolved items as undecided rather than presenting them as approved facts. Update the relevant sections when a file already exists.
4. **Build `brandkit.html`.** Make a self-contained HTML/CSS specimen that reads as a visual rendering of `BRANDKIT.md`: logo variants where assets exist, labeled color swatches with exact values and roles, type specimens using the chosen fonts and fallbacks, imagery or texture examples where available, and a few relevant applications. Keep values and labels aligned with the Markdown; use relative asset paths so the file opens from the project reference directory. For unlicensed or unavailable fonts, show the named stack with a fallback and state what is missing. Show undecided elements as such rather than inventing samples.
5. **Inspect and reconcile.** Open or render the HTML and check it at desktop and narrow widths. Compare every displayed brand value, logo, and text label with `BRANDKIT.md` and the source assets. Fix broken paths, clipping, unreadable contrast, font fallbacks, and mismatches. When an approved brand change affects an existing UI system, update the relevant `DESIGN.md` tokens and rules or identify the adaptation that keeps them different. Report any representation that could not be rendered faithfully.

The workflow is complete when both files exist in the chosen project location, the HTML has been viewed, and every decided identity element shown there agrees with the Markdown and source assets. If project files cannot be written, provide both drafts and state the intended paths.

## Optional presentation image

When a raster board is requested, build it from the decisions in `BRANDKIT.md` and save it in the project reference directory where possible. A 3 × 3 grid on a 4:3 or 16:10 canvas is a starting point when the user specifies neither layout nor size. Adapt the panel count and grid to the content and canvas. Canvas ratio describes the whole image, not the panel grid.

Use generous gutters, clear alignment, sparse readable labels, and enough quiet space for the mark to register. A useful sequence is: identity cover → visual system → applications. Pick application surfaces that fit the actual brand: a developer tool may use a terminal or app header; a hospitality brand may use a menu or sign. Treat atmosphere and texture as part of the brand world, rather than filler panels.

Use [image-generation](references/image-generation.md) for reference handling, aspect ratios, text limits, and inspection. If the generator cannot output the exact requested size or ratio, use the closest supported option that preserves the composition. Report the actual output size and any material difference.

## Identity and image rules

- **Existing brand:** Use the supplied files as the source of truth. Compare each representation against them. For exact logos and lettering, place the real asset in the HTML or over a generated background.
- **New mark:** Aim for one recognizable feature that survives small use and works on light and dark surfaces. Concept directions can be raster; final logos need clean vector assets and size checks in [brand-identity](references/brand-identity.md).
- **Type:** Render only essential words: brand name, a short tagline, and a few panel labels. Verify every letter. Add precise or dense copy after generation in a layout tool when needed.
- **Color:** Give each color a role and repeat accents across panels. Carry the brand's actual palette when one exists; otherwise choose a restrained palette from the concept.
- **Applications:** Show plausible touchpoints at enough scale to judge the system. Use mockups to demonstrate identity behavior rather than fill space with invented product details.
- **References:** Extract layout rhythm, material treatment, density, and color logic from inspiration. Preserve supplied identity assets as identity assets. Keep each reference's role explicit in the generation prompt.

## Image prompt brief

For an optional raster board, build the prompt from `BRANDKIT.md` using concrete details:

```text
Create one brand-kit presentation image for [brand] on [canvas / supported ratio].
Identity mode: [new / extend / refresh]; preserve [supplied assets and fixed elements].
Audience and promise: [who it serves; what it should communicate].
Concept: [one metaphor and how the mark or existing identity expresses it].
Visual system: [palette roles, type character, imagery or material treatment].
Composition: [panel sequence, dominant panel, gutters, quiet space].
Applications: [two or three relevant touchpoints].
Exact visible text: [short, quoted strings only].
References: [each image's role and what to preserve or borrow].
```

Review against the brief, then revise the prompt for any failed check. Follow [image-generation](references/image-generation.md) for tool-specific limits and iteration tactics.
