---
name: design-context
description: "Discover existing project design decisions, reconcile legacy context, and identify supported visual defaults."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: design-context
---

# Design context

Use this reference to discover a project's existing visual decisions and supply defaults when no system has been established. Project-root `DESIGN.md` is the authoritative applied UI system; [document](../document.md) explains how to create or update it. The brand kit in the project reference directory owns approved brand identity. `PRODUCT.md` owns users, jobs, and product constraints.

## Discovery and migration

1. Read `DESIGN.md` when present. Read the brand kit for identity constraints and `PRODUCT.md` when product context matters.
2. If `DESIGN.md` is absent or incomplete, inspect `.agents/design-context.md` as legacy evidence, then theme and token files (`tailwind.config.*`, Tailwind `@theme`, CSS custom properties, `tokens.json`, `theme.*`), font loading, manifest, assets, recurring component values, and any connected design tool.
3. Map observed roles to the existing system: `primary`, `secondary`, `accent`; `heading`, `body`, `mono`; radius, spacing, shadows, and component states. Preserve the project's normative value notation (hex, HSL, OKLCH, or another CSS color format) in `DESIGN.md`.
4. Reconcile conflicts using approved brand decisions and the implemented UI. Mark uncertain or proposed values as such. When the user asks to establish durable guidance, use [document](../document.md) to write `DESIGN.md`.
5. Treat `.agents/design-context.md` as a legacy import. If another tool still needs it, generate a compatibility copy from `DESIGN.md` and label it as generated with the source path and date. Update `DESIGN.md` first; never independently edit both files.

With no established system, use the project's existing CSS or theme before choosing defaults. State any defaults used. Avoid presenting a fallback palette as an approved brand.

For legacy files, migrate color, typography, radius, spacing, and UI behavior into `DESIGN.md`; brand name, logo assets, imagery, and identity rules into the brand kit; and confirmed audience, mission, and operating constraints into `PRODUCT.md`. Keep unresolved claims marked as such. A legacy field is evidence, not automatic approval.

## Role mapping

| Found in code | UI role |
|---|---|
| `colors.primary`, `--color-primary`, `--primary` | Primary |
| `colors.secondary`, `--color-secondary`, `--secondary` | Secondary |
| `colors.accent`, `--color-accent`, `--accent` | Accent |
| `fontFamily.heading` / `.display`, `--font-heading`, `--font-display` | Heading font |
| `fontFamily.sans`, `--font-body`, `--font-sans` | Body font |
| `--radius`, `--border-radius` | Radius |

For shadcn/ui also inspect `--muted`, `--destructive`, and semantic surface values.

## Design dimensions to record

Document only values that are established by code, assets, or a decision. Useful dimensions include color roles and accessible pairs; font stacks, size, weight, and line height; spacing and grid; radius and elevation; icon and image treatment; component variants and states; responsive behavior; and motion. Keep brand names, logo usage, and voice in the brand kit, referring to them from `DESIGN.md` where they affect UI.

When a project describes its style by an archetype, translate that label into observed rules rather than applying a preset. For example, a minimal system may use sparse color and restrained depth; a bold one may use large type and strong contrast; a playful one may use rounded shapes and lively motion; a luxurious one may use quiet spacing and fine detail. Record the project's actual choices in `DESIGN.md`.

## Validation

Compute contrast for actual foreground/background pairs. WCAG AA requires 4.5:1 for normal text and 3:1 for large text; non-text UI indicators generally need 3:1 against adjacent colors. Report failures and propose an adjusted shade without silently changing an approved brand color. Check focus indicators against their adjacent colors and inspect light/dark variants separately.

## Naming conventions

When a project has no convention, these CSS names provide a starting point. Keep existing names when they already form a coherent system.

| Group | Example |
|---|---|
| Brand scale | `--brand-50` … `--brand-950` |
| Neutral scale | `--gray-50` … `--gray-950` |
| Status scales | `--success-*`, `--warning-*`, `--error-*` |
| Type scale | `--text-xs` … `--text-5xl` |
| Fonts | `--font-heading`, `--font-body`, `--font-mono` |
| Radius | `--radius` |

Scale generation: [color-palette](color-palette.md). Type scale: [typography](typography.md). Token layering: [design-system](design-system.md).

## Fallbacks

Use only when the project has no established values and the user wants to proceed. These are working defaults, not brand decisions.

| Token | Working value |
|---|---|
| Primary | `#2563EB` |
| Secondary | `#7C3AED` |
| Accent | `#F59E0B` |
| Neutral | Tailwind gray scale |
| Heading and body font | Inter |
| Success | `#10B981` fills and icons; `#047857` text |
| Warning | `#F59E0B` fills and icons; `#B45309` text |
| Error | `#EF4444` fills and icons; `#B91C1C` text |
| Border radius | `8px` |

The light status colors do not meet 4.5:1 as text on white. Use the darker text shades. For expressive work, ask for visual references or preferences before relying on the generic blue and Inter pair.
