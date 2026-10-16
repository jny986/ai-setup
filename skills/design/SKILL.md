---
name: design
description: "Router for visual design work. Use to capture product context in PRODUCT.md, document a visual system in DESIGN.md, create brand kits, plan a UI, improve task flows, consolidate UI patterns, design or build UI and graphics, implement visual references, adapt interfaces, generate variants, or audit and refine an interface. Sub-skills: product, shape, document, brandkit, audit, flow, systematize, refine; plus reference guides per surface."
argument-hint: "[sub-skill] [task]"
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable
  based_on_version: 4.5.2(2f98774)
  based_on_skill: impeccable
---

# Design

A router over design sub-skills and reference guides, organised by situation. Sub-skills live at `sub-skills/<sub-skill>.md`, references at `sub-skills/references/<name>.md`.

## Project reference directory

Use project-root `docs/branding/` by default for project-specific design reference files and deliverables. Look there first and link to existing assets at their current paths. Root `PRODUCT.md` and `DESIGN.md` are explicit exceptions for tool discovery. Use a location specified by the user when given.

`PRODUCT.md` owns confirmed product facts. `docs/branding/BRANDKIT.md` owns brand identity and `brandkit.html` presents it. `DESIGN.md` owns the applied UI system and its tokens. A brand value used in UI should agree with the approved brand kit; record any intentional UI adaptation in `DESIGN.md`. If an older project has `.agents/design-context.md`, use it as migration evidence, then treat `DESIGN.md` as authoritative. Do not maintain two independently editable token records.

## Steps

1. **Pick the sub-skill.**
   - Argument names a sub-skill: use it.
   - Otherwise match the task to a situation below, taking the first row that fits. When two fit equally, ask once.
2. **Follow it.** Read `sub-skills/<sub-skill>.md` and follow it as if it were the skill.
3. **No sub-skill fits:** read the reference for the surface below. For implementation, read existing `DESIGN.md` and relevant product or brand context, then [design-context](sub-skills/references/design-context.md) for token discovery and fallbacks when needed. Each reference links its neighbours; follow those instead of loading the whole set.

Read `PRODUCT.md` for work involving users, jobs, positioning, or product constraints; `DESIGN.md` for UI design and implementation; and `BRANDKIT.md` for brand identity. Create a missing document when the user requests it or durable decisions made in the task need recording. Routine edits do not require creating every file.

Treat example palettes, font counts, spacing scales, breakpoints, and layouts in references as fallbacks. Follow the user's brief and established project system, with deliberate adaptations for content, platform, and accessibility. Verify applicable accessibility requirements separately from stylistic defaults.

## Sub-skills

| Situation | Sub-skill |
|---|---|
| Capture or update confirmed product facts, users, jobs, and constraints in `PRODUCT.md` | [`product`](sub-skills/product.md) |
| Plan a UI surface or feature before implementation: task, hierarchy, interactions, states, and direction | [`shape`](sub-skills/shape.md) |
| Document the current UI system or seed an approved direction in `DESIGN.md` | [`document`](sub-skills/document.md) |
| Create a project brand kit: written identity guide, HTML specimen, or presentation image | [`brandkit`](sub-skills/brandkit.md) |
| Audit an existing website or app interface: UX, visual design, accessibility, performance, responsive behavior, and implementation | [`audit`](sub-skills/audit.md) |
| Design or improve a task journey: steps, forms, onboarding, interface copy, feedback, and recovery | [`flow`](sub-skills/flow.md) |
| Consolidate repeated UI patterns into shared tokens and components, migrate consumers, and verify parity | [`systematize`](sub-skills/systematize.md) |
| Improve an existing interface's hierarchy, density, typography, color, layout, motion, or final finish | [`refine`](sub-skills/refine.md) |

For combined requests, follow the relevant sub-skills in task order: shape a brief, implement the flow, then refine its presentation. Audit supplies findings when requested; a request to audit and fix continues into the applicable implementation sub-skill. Reuse established context and findings across these steps.

## References

Pick by surface. A task spanning two surfaces reads both.

- **App UI**: [ui-design](sub-skills/references/ui-design.md) (base rules), [dashboard-design](sub-skills/references/dashboard-design.md), [mobile-ui-design](sub-skills/references/mobile-ui-design.md), [card-design](sub-skills/references/card-design.md), [motion-design](sub-skills/references/motion-design.md), [icon-design](sub-skills/references/icon-design.md)
- **Platform and adaptation**: [adapt](sub-skills/references/adapt.md) (change device, window, input, or platform), [native-platforms](sub-skills/references/native-platforms.md) (build native iOS, iPadOS, and Android UI)
- **Direction and fidelity**: [surface-purpose](sub-skills/references/surface-purpose.md) (choose hierarchy, density, and expression by user outcome), [reference-to-ui](sub-skills/references/reference-to-ui.md) (implement an approved screenshot, mockup, or design frame)
- **Foundations**: [design-system](sub-skills/references/design-system.md), [color-palette](sub-skills/references/color-palette.md), [dark-mode](sub-skills/references/dark-mode.md), [typography](sub-skills/references/typography.md), [layout-composition](sub-skills/references/layout-composition.md)
- **Marketing pages**: [landing-page-design](sub-skills/references/landing-page-design.md), [hero-section](sub-skills/references/hero-section.md)
- **Brand**: [brand-identity](sub-skills/references/brand-identity.md)
- **Graphics**: [graphic-design](sub-skills/references/graphic-design.md) (base rules), [social-media-graphic](sub-skills/references/social-media-graphic.md), [thumbnail-design](sub-skills/references/thumbnail-design.md), [poster-design](sub-skills/references/poster-design.md), [banner-design](sub-skills/references/banner-design.md), [ad-creative-design](sub-skills/references/ad-creative-design.md), [infographic](sub-skills/references/infographic.md), [product-mockup](sub-skills/references/product-mockup.md), [presentation-design](sub-skills/references/presentation-design.md)
- **Images**: [image-generation](sub-skills/references/image-generation.md) (create), [image-treatment](sub-skills/references/image-treatment.md) (edit existing in code)
- **Email**: [email-design](sub-skills/references/email-design.md)
- **Iterate**: [generate](sub-skills/references/generate.md) (viewable variants of an existing web element)
- **Review and finish**: [design-critique](sub-skills/references/design-critique.md) (visual critique, including static images and design frames), [native-audit](sub-skills/references/native-audit.md) (native app checks with the audit sub-skill), [polish](sub-skills/references/polish.md) (final finish pass), [harden](sub-skills/references/harden.md) (edge cases and recovery), [optimize](sub-skills/references/optimize.md) (measured UI performance)
