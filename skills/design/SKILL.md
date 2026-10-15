---
name: design
description: "Router for visual design work. Use to design or build app UI, dashboards, landing pages, design systems, brand identity, graphics, AI-generated images, slide decks or HTML email, or to critique or redesign an existing interface. Sub-skill: brandkit; plus reference guides per surface."
argument-hint: "[sub-skill] [task]"
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

A router over design sub-skills and reference guides, organised by situation. Sub-skills live at `sub-skills/<sub-skill>.md`, references at `sub-skills/references/<name>.md`.

## Steps

1. **Pick the sub-skill.**
   - Argument names a sub-skill: use it.
   - Otherwise match the task to a situation below, taking the first row that fits. When two fit equally, ask once.
2. **Follow it.** Read `sub-skills/<sub-skill>.md` and follow it as if it were the skill.
3. **No sub-skill fits:** read the reference for the surface below. Start with [design-context](sub-skills/references/design-context.md) when building in code: it defines `.agents/design-context.md`, the token source every other reference defers to. Each reference links its neighbours; follow those instead of loading the whole set.

## Sub-skills

| Situation | Sub-skill |
|---|---|
| Generate a brand-kit board: logo directions, identity system, palette, type, applications | [`brandkit`](sub-skills/brandkit.md) |

## References

Pick by surface. A task spanning two surfaces reads both.

- **App UI**: [ui-design](sub-skills/references/ui-design.md) (base rules), [dashboard-design](sub-skills/references/dashboard-design.md), [mobile-ui-design](sub-skills/references/mobile-ui-design.md), [card-design](sub-skills/references/card-design.md), [motion-design](sub-skills/references/motion-design.md), [icon-design](sub-skills/references/icon-design.md)
- **Foundations**: [design-system](sub-skills/references/design-system.md), [color-palette](sub-skills/references/color-palette.md), [dark-mode](sub-skills/references/dark-mode.md), [typography](sub-skills/references/typography.md), [layout-composition](sub-skills/references/layout-composition.md)
- **Marketing pages**: [landing-page-design](sub-skills/references/landing-page-design.md), [hero-section](sub-skills/references/hero-section.md)
- **Brand**: [brand-identity](sub-skills/references/brand-identity.md)
- **Graphics**: [graphic-design](sub-skills/references/graphic-design.md) (base rules), [social-media-graphic](sub-skills/references/social-media-graphic.md), [thumbnail-design](sub-skills/references/thumbnail-design.md), [poster-design](sub-skills/references/poster-design.md), [banner-design](sub-skills/references/banner-design.md), [ad-creative-design](sub-skills/references/ad-creative-design.md), [infographic](sub-skills/references/infographic.md), [product-mockup](sub-skills/references/product-mockup.md), [presentation-design](sub-skills/references/presentation-design.md)
- **Images**: [image-generation](sub-skills/references/image-generation.md) (create), [image-treatment](sub-skills/references/image-treatment.md) (edit existing in code)
- **Email**: [email-design](sub-skills/references/email-design.md)
- **Review**: [design-critique](sub-skills/references/design-critique.md)
