---
metadata:
  version: "1.0.0"
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: icon-design
---

# Icon Design

Consistent, accessible SVG icon systems: grids, stroke rules, optical corrections, styles, alignment, animation and markup.

Tokens come from `.agents/design-context.md` (see [design-context](design-context.md)); with none, extend the project's existing CSS variables or Tailwind theme. Its Brand Marks "Icon Style" field (for example "Outlined, 2px stroke, rounded caps") sets fill, stroke width and cap/join for every icon you draw. Use the status scales (`--success-*`, `--error-*`) from [color-palette](color-palette.md). If the project already uses an icon library (Lucide, Heroicons, Phosphor, Material Symbols), match its grid and stroke and prefer its icons over drawing new ones. For a logo mark see [brand-identity](brand-identity.md).

## SVG base

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
  width="24" height="24" fill="none" stroke="currentColor"
  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <!-- paths -->
</svg>
```

| Attribute | Value | Why |
|-----------|-------|-----|
| fill | none | Outline by default |
| stroke | currentColor | Inherits text color |
| stroke-width | 2 | Same across the set |
| stroke-linecap / linejoin | round | Friendly; keep the two matched |
| viewBox | 0 0 24 24 | Standard grid |

## Grid

| Grid | Use | Stroke |
|------|-----|--------|
| 24x24 | Default UI | 2px (1.5px for a lighter set) |
| 20x20 | Compact UI, form fields | 1.5px |
| 16x16 | Inline text, badges | 1.5px, or filled |
| 32x32 | Feature icons, navigation | 2-2.5px |
| 48x48 | Illustration icons, hero | 3px |

Draw each size on its own grid, on whole-pixel coordinates where possible. Scaling a 24px icon to 16px in CSS also scales the stroke (2px becomes 1.33px, blurry). Draw a 16px variant or set `vector-effect="non-scaling-stroke"` on the paths.

Keylines (24x24, Material-style):

- Live area 20x20 (2px padding per side, for optical overshoot only).
- Circle 20 diameter; square 18x18 (circles look smaller than equal squares, so squares are drawn smaller).
- Portrait rectangle 16w x 20h; landscape 20w x 16h.

```css
.icon { width: 1.5rem; height: 1.5rem; flex-shrink: 0; display: inline-block; vertical-align: middle; }
.icon-sm { width: 1rem; height: 1rem; }
.icon-md { width: 1.25rem; height: 1.25rem; }
.icon-lg { width: 2rem; height: 2rem; }
.icon-xl { width: 3rem; height: 3rem; }
```

## Optical corrections

| Shape | Correction |
|-------|------------|
| Triangle / play | Shift right about 1px (optical center of mass) |
| Circle | Draw about 10% larger than a square (20 vs 18 keyline) |
| Tall shapes | Center vertically; may need a slight Y offset |
| Pointed tops | Let the point extend slightly above the grid boundary |

Keep stroke width identical across the set. Compensate with size and position, never by varying stroke: uneven weights are the most visible sign of an inconsistent set.

## Styles

- Outline: most versatile, scales well, low weight. `fill="none" stroke="currentColor"`.
- Filled: higher weight; good for active or selected states and small sizes. `fill="currentColor"`.
- Duotone: primary stroke plus a secondary filled area at low opacity.
- Rounded (round caps) feels friendly and modern; sharp (square or butt caps) feels precise and technical. Pick one for the whole set; never mix.

```css
.icon-duotone { --icon-primary: currentColor; --icon-secondary: currentColor; }
.icon-duotone .icon-bg { fill: var(--icon-secondary); opacity: 0.15; }
.icon-duotone .icon-fg { stroke: var(--icon-primary); fill: none; }
```

## Semantic icon choice

| Action | Icon | Note |
|--------|------|------|
| Close | X | Top-right of the container |
| Back | Arrow or chevron left | |
| Menu | Three horizontal bars | |
| Search | Magnifying glass | Usually in search inputs |
| Settings | Gear | Sliders for filter settings |
| User | Person silhouette | |
| Notification | Bell | Optional dot badge |
| Delete | Trash can | Use with confirmation |
| Edit | Pencil | |
| Add | Plus | In a circle for a FAB |
| Share | Arrow up from box | Or branching arrow |
| Download | Arrow down to bar | Distinct from chevron-down |
| Check / done | Checkmark | In a circle for confirmed state |
| Info | i in circle | Info (blue) color |
| Warning | Triangle with ! | Warning (amber) color |
| Error | Circle with X | Error (red) color |

## Custom SVG

Path commands: `M` move, `L` line, `H` / `V` horizontal / vertical line, `C` cubic bezier, `A` arc, `Z` close. Lowercase is relative (often shorter).

```svg
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
     stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
  <polyline points="3 11 12 3 21 11"/>
  <path d="M5 10v9a1 1 0 0 0 1 1h4v-6h4v6h4a1 1 0 0 0 1-1v-9"/>
</svg>
```

## Icon and text alignment

```css
.icon-text { display: inline-flex; align-items: center; gap: 0.5rem; }
.icon-text .icon { width: 1.25em; height: 1.25em; flex-shrink: 0; }

.btn-icon { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.625rem 1.25rem; }
.btn-icon .icon { width: 1.25em; height: 1.25em; margin-left: -0.125em; }

.btn-icon-only { display: inline-grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0; border-radius: 0.5rem; } /* 44px target */
```

## Animation

```css
.icon-interactive { transition: transform 0.2s ease; }
.icon-interactive:hover { transform: rotate(90deg); }

.icon-spinner { animation: spin 1s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
```

Checkmark draw-on. `pathLength="1"` normalizes the length, so no measuring:

```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
  <path class="draw" pathLength="1" d="M5 12.5l4.5 4.5L19 7.5"/>
</svg>
```

```css
.draw { stroke-dasharray: 1; stroke-dashoffset: 1; animation: draw 0.4s var(--ease-out, ease-out) forwards; }
@keyframes draw { to { stroke-dashoffset: 0; } }
@media (prefers-reduced-motion: reduce) { .draw { animation: none; stroke-dashoffset: 0; } }
```

Wrap hover rotations in the same reduced-motion guard. A spinner may keep rotating (it conveys state), but slow it or swap to a pulsing opacity. More in [motion-design](motion-design.md).

## Accessibility

1. Decorative icons (beside a text label): `aria-hidden="true" focusable="false"`.
2. Standalone meaningful icons: `aria-label` on the button (and `aria-hidden="true"` on the SVG inside), or `<title>` in the SVG with `role="img"` and `aria-labelledby`.
3. Never rely on an icon alone for a critical action; provide text.
4. Icon buttons: 24x24px is the WCAG 2.2 AA floor (SC 2.5.8); aim for 44x44px (Apple HIG, WCAG AAA 2.5.5) or 48x48dp (Material).
5. Meaningful icons need 3:1 contrast against their background (SC 1.4.11).

```css
.icon-button { min-width: 44px; min-height: 44px; display: inline-grid; place-items: center; }
```

## Common patterns

```css
.icon-with-badge { position: relative; display: inline-block; }
.icon-badge {
  position: absolute; top: -4px; right: -4px;
  width: 10px; height: 10px; background: var(--error-500);
  border-radius: 50%; border: 2px solid var(--bg-primary, white);
}

.status-icon { position: relative; }
.status-icon::after {
  content: ''; position: absolute; bottom: 0; right: 0;
  width: 8px; height: 8px; border-radius: 50%; border: 2px solid var(--bg-primary, white);
}
.status-icon--online::after  { background: var(--success-500); }
.status-icon--offline::after { background: var(--gray-400); }
.status-icon--busy::after    { background: var(--error-500); }
```

Status dots rely on color alone: pair with a text label or `aria-label` ("Online"). Ring with `var(--bg-primary)`, not `white`, so it works in dark mode.

## Review

Render every icon on one page at 16, 20, 24 and 32px, on light and dark backgrounds, beside a text label (view 16px zoomed 4x). Check:

- Equal visual weight across icons and identical stroke widths.
- Nothing clipped at the viewBox edge.
- Shapes aligned to keylines.
- Recognizable at 16px.
