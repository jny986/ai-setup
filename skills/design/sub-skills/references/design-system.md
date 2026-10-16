---
name: design-system
description: "Structure UI tokens, components, variants, themes, and documentation within the established project system."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: design-system
---

# Design System

Tokens, components and theming architecture for a coded design system.

For extracting and migrating existing patterns, follow [systematize](../systematize.md). The names, scales, variants, and CSS structures below are starting examples when a project lacks conventions; preserve an established system and deliberate exceptions. Native apps map these roles through [native-platforms](native-platforms.md).

Read `DESIGN.md` for UI tokens and the project brand kit for approved brand primitives (see [design-context](design-context.md)); when absent, inspect the project's existing CSS variables or Tailwind theme. Color scales come from [color-palette](color-palette.md), the type scale from [typography](typography.md). Do not re-derive them. Identify the framework (React, Vue, Svelte, vanilla) to pick component patterns.

## Token hierarchy

Three layers.

### Primitive tokens (what it is)

Raw values in `:root`, never used directly in components. Preserve the project's established color notation; OKLCH is useful when generating a new scale.

- Colors: `--brand-50` to `--brand-950`, `--gray-50` to `--gray-950`, `--success-*`, `--warning-*`, `--error-*`, `--info-*`.
- Spacing: `--space-N` = N x 4px in rem (see Spacing scale).
- Font sizes: `--text-xs` to `--text-5xl`, generated from Base Size x Scale Ratio. Do not hard-code a separate scale.
- Radii: none, sm 0.25rem, md 0.5rem, lg 0.75rem, xl 1rem, 2xl 1.5rem, full 9999px. Align the scale with the radius recorded in `DESIGN.md`.

### Semantic tokens (what it does)

The interface themes override.

- Backgrounds: `--bg-primary` (gray-50), `--bg-secondary` (white), `--bg-tertiary` (gray-100), `--bg-inverse` (gray-900).
- Text: primary (gray-900), secondary (gray-600), tertiary (gray-400), inverse, brand.
- Borders: default (gray-200), strong (gray-300), brand (brand-500).
- Interactive: `--interactive-primary` with `-hover` and `-active` (brand-500/600/700); secondary and its hover from the gray scale.
- Brand aliases: `--color-primary`, `--color-secondary`, `--color-accent`.
- Status: `--color-success`, `--color-warning`, `--color-error` (500 steps).
- Spacing: gap-xs through gap-section mapped to space tokens.
- Radius: button md, card lg, input md, badge full, modal xl.

### Component tokens (where it is used)

Optional, for complex systems. For `.btn` define `--btn-padding-x`, `--btn-padding-y`, `--btn-radius`, `--btn-font-size`, `--btn-bg`, `--btn-color`, `--btn-border` from semantic tokens and consume them in the same rule. Variants override only the tokens they change.

## CSS architecture

```text
tokens/
  _primitives.css   raw values
  _semantic.css     purpose mappings
  _themes.css       theme overrides
components/
  _button.css
  _card.css
  _input.css
index.css           imports all, in this order
```

### Theme scoping

```css
[data-theme="dark"] {
  --bg-primary: var(--gray-950);
  --bg-secondary: var(--gray-900);
  --bg-tertiary: var(--gray-800);
  --text-primary: var(--gray-50);
  --text-secondary: var(--gray-300);
  --border-default: var(--gray-700);
  --interactive-primary: var(--brand-400);
}

@media (prefers-contrast: more) {
  :root { --text-secondary: var(--text-primary); --border-default: var(--gray-900); }
}
```

Under Windows High Contrast (`forced-colors: active`) custom colors are replaced by system colors. Never convey state by background color alone, and keep a transparent `outline` or `border` on buttons so they stay visible.

### DTCG export

For Style Dictionary, Tokens Studio or Figma variables, also emit `tokens.json` in W3C DTCG format: each token has `$value` and `$type` (`$type` may be set once on a group), aliases use `{group.token}`, notes go in `$description`. The stable spec (2025.10) uses structured color and dimension values; older tools may expect strings like `"#0F74C5"` and `"16px"`. Check what the consumer supports.

```json
{
  "color": {
    "$type": "color",
    "brand": {
      "500": { "$value": { "colorSpace": "oklch", "components": [0.55, 0.15, 250], "hex": "#0F74C5" } }
    },
    "interactive": {
      "primary": { "$value": "{color.brand.500}", "$description": "Primary buttons, links" }
    }
  },
  "space": {
    "$type": "dimension",
    "4": { "$value": { "value": 1, "unit": "rem" } }
  },
  "duration": {
    "$type": "duration",
    "normal": { "$value": { "value": 200, "unit": "ms" } }
  },
  "easing": {
    "$type": "cubicBezier",
    "out": { "$value": [0, 0, 0.2, 1] }
  }
}
```

## Component API

Use consistent role names across components where their behavior agrees. The following API illustrates common variants; expose only those needed by actual consumers.

| Property | Options |
|----------|---------|
| Size | sm, md (default), lg |
| Variant | primary (default), secondary, ghost, outline, danger |
| State | default, hover, active, focus, disabled |
| Shape | default, pill (radius-full) |

- Size variants (`--sm`, `--lg`) override padding and font-size tokens. Style variants override bg, color and border tokens only.
- States: `:hover` adjusts bg; `:active` darker bg plus `scale(0.98)`; `:focus-visible` 2px outline, 2px offset, 3:1 contrast against the background; `:disabled` or `[aria-disabled="true"]` reduced opacity and `cursor: not-allowed`. For `aria-disabled` also block the click in JS (it stays focusable, which is the point).

### Card

`.card` (border, radius, overflow) with `.card-header`, `.card-body`, `.card-footer` (semantic-token padding; header and footer have border separators). `.card-media` uses `aspect-ratio: 16/9; object-fit: cover`. Variants: `--elevated` (shadow instead of border), `--interactive` (hover shadow plus translateY).

### Input

Component tokens `--input-height`, `--input-border`, `--input-radius`, `--input-bg`. Default 2.5rem tall, full width; `--sm` 2rem, `--lg` 3rem. States: hover stronger border, focus brand border plus 3px ring at 0.15 opacity, `--error` error border.

## Theming

- Switch with a `data-theme` attribute on `<html>`: read `localStorage`, fall back to `prefers-color-scheme: dark`, follow OS changes when nothing is saved.
- Run it as a tiny inline `<script>` in `<head>` before CSS paints to avoid a flash of the wrong theme. Set `color-scheme: light dark` so form controls and scrollbars match.
- Multi-brand: remap Layer 2 tokens (interactive colors, fonts) under `[data-brand="name"]`. Components stay unchanged.

## Spacing scale

With no established scale, a 4px base (`--space-N` = N x 4px) is a useful starting point. Preserve an existing scale and optical or content-driven exceptions. [layout-composition](layout-composition.md) covers grouping and rhythm.

| Token | px | rem | Use |
|-------|----|-----|-----|
| 0.5 | 2 | 0.125 | Hairline gaps |
| 1 | 4 | 0.25 | Tight internal padding |
| 2 | 8 | 0.5 | Icon gaps, compact padding |
| 3 | 12 | 0.75 | Button and input padding |
| 4 | 16 | 1 | Card padding, standard gap |
| 5 | 20 | 1.25 | Comfortable card padding |
| 6 | 24 | 1.5 | Section internal gap |
| 8 | 32 | 2 | Between component groups |
| 10 | 40 | 2.5 | Large component spacing |
| 12 | 48 | 3 | Section padding |
| 16 | 64 | 4 | Section margins |
| 20 | 80 | 5 | Hero padding |
| 24 | 96 | 6 | Major section breaks |

- Within a component (icon to text, label to input): space-1 to 3.
- Between siblings (card to card, field to field): space-4 to 6.
- Between sections: space-12 to 24.

## Shadow and elevation

Six levels, `--shadow-xs` to `--shadow-2xl`, multi-layer `oklch(0 0 0 / opacity)` with increasing blur and offset.

```css
:root {
  --shadow-sm: 0 1px 2px oklch(0 0 0 / 0.06), 0 1px 3px oklch(0 0 0 / 0.08);
  --shadow-md: 0 2px 4px oklch(0 0 0 / 0.06), 0 4px 12px oklch(0 0 0 / 0.10);
  --shadow-lg: 0 4px 8px oklch(0 0 0 / 0.06), 0 12px 32px oklch(0 0 0 / 0.14);
}
```

Scale to the context Shadow Style: none = borders and surface color only; subtle = values above; medium = about 1.5x; dramatic = about 2x with larger offsets.

| Level | Shadow | Use |
|-------|--------|-----|
| 0 | none | Flush with surface |
| 1 | xs / sm | Cards, buttons |
| 2 | md | Dropdowns, popovers |
| 3 | lg | Modals, drawers |
| 4 | xl / 2xl | Toasts, elevated modals |

In dark mode raise shadow opacity (0.3+) or rely on surface color differences.

## Radius

none 0, sm 4px, md 8px, lg 12px, xl 16px, 2xl 24px, full 9999px. Nested radius: inner = outer - padding. If that is 0 or negative, use the next size down.

## Motion tokens

Durations: `--duration-fast` 100ms, `--duration-normal` 200ms, `--duration-slow` 300ms, `--duration-slower` 500ms. Easings: `--ease-out`, `--ease-in`, `--ease-in-out`, `--ease-spring`, with the same names and values as [motion-design](motion-design.md). Combine into `--transition-colors`, `--transition-transform`, `--transition-shadow`, `--transition-opacity`; components compose them, for example `var(--transition-colors), var(--transition-transform)`.

Always include reduced motion:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

## Component documentation

Per component: description and when to use it; variants; sizes; states; anatomy with tokens; do and don't; copy-paste code. Use a Storybook-style HTML page: one `<section>` per component with `.doc-row` containers (flex wrap, gap, tertiary bg) showing every variant, size and state side by side.

## Review checklist

1. Primitives (colors, spacing, font sizes, radii) derive from the context, not invented values.
2. Semantic tokens map backgrounds, text, borders, interactive states.
3. Light and dark themes via data attributes.
4. Components use tokens only: no raw hex in component CSS.
5. Consistent sizes and variants; all interactive states present, focus rings visible, disabled looks disabled.
6. Text and button pairs pass contrast in both themes.
7. Shadow, motion and reduced-motion tokens defined.
8. Every component documented.
9. If primitives changed within the task, update the corresponding `DESIGN.md` tokens and explain the change.
