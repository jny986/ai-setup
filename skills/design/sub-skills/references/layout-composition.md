---
metadata:
  version: "1.0.0"
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: layout-composition
---

# Layout and Composition

Grid systems, visual hierarchy, whitespace and modern CSS layout patterns for pages and screens.

Tokens come from `.agents/design-context.md` (see [design-context](design-context.md)); with none, extend the project's existing CSS variables or Tailwind theme. Use its Spacing System, Border Radius, style archetype and platform priority. Spacing tokens follow the [design-system](design-system.md) scale (`--space-N` = N x 4px); colors use the `--brand-*` and `--gray-*` primitives from [color-palette](color-palette.md). Pick patterns by content type (text-heavy, media-heavy, dashboard, marketing). For slide layouts see [presentation-design](presentation-design.md).

## CSS Grid

### 12-column

```css
.grid-12 {
  display: grid; grid-template-columns: repeat(12, 1fr);
  gap: 1.5rem; max-width: 1280px; margin-inline: auto; padding-inline: 1.5rem;
}
.col-full    { grid-column: 1 / -1; }
.col-half    { grid-column: span 6; }
.col-third   { grid-column: span 4; }
.col-quarter { grid-column: span 3; }
@media (max-width: 768px) { .grid-12 > * { grid-column: 1 / -1; } }
```

### Auto-fit (no media queries)

```css
.grid-auto { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; }
```

### Named areas

```css
.page-layout {
  display: grid; grid-template-columns: 250px 1fr 300px;
  grid-template-rows: auto 1fr auto; min-height: 100dvh;
  grid-template-areas: "header header header" "sidebar main aside" "footer footer footer";
}
.header { grid-area: header; } .sidebar { grid-area: sidebar; }
.main { grid-area: main; } .aside { grid-area: aside; } .footer { grid-area: footer; }
@media (max-width: 1024px) {
  .page-layout { grid-template-columns: 1fr; grid-template-areas: "header" "main" "sidebar" "aside" "footer"; }
}
```

## Flexbox

```css
/* Navbar */
.navbar { display: flex; align-items: center; justify-content: space-between; padding: 1rem 2rem; gap: 2rem; }

/* Centered content page */
.centered-page { display: flex; flex-direction: column; align-items: center; min-height: 100dvh; }
.centered-page main { flex: 1; width: 100%; max-width: 65ch; padding: 2rem; }

/* Equal-height card row: wraps instead of squashing on mobile */
.card-row { display: flex; flex-wrap: wrap; gap: 1.5rem; }
.card-row > * { flex: 1 1 260px; display: flex; flex-direction: column; }
.card-row .card-footer { margin-top: auto; }
```

## Bento grids

```css
.bento { display: grid; grid-template-columns: repeat(4, 1fr); grid-auto-rows: 200px; gap: 1rem; }
.bento-large { grid-column: span 2; grid-row: span 2; }
.bento-wide  { grid-column: span 2; }
.bento-tall  { grid-row: span 2; }
```

Feature showcase with explicit placement:

```css
.bento-showcase {
  display: grid; grid-template-columns: repeat(6, 1fr);
  grid-template-rows: repeat(4, 180px); gap: 1rem; padding: 1rem;
}
.bento-showcase > :nth-child(1) { grid-column: 1 / 4; grid-row: 1 / 3; }
.bento-showcase > :nth-child(2) { grid-column: 4 / 7; grid-row: 1 / 2; }
.bento-showcase > :nth-child(5) { grid-column: 1 / 3; grid-row: 3 / 5; }
.bento-showcase > * { border-radius: 1rem; padding: 1.5rem; overflow: hidden; background: var(--gray-100); }
@media (max-width: 768px) {
  .bento-showcase { grid-template-columns: 1fr 1fr; grid-template-rows: auto; }
  .bento-showcase > * { grid-column: auto !important; grid-row: auto !important; }
}
```

Card styling:

```css
.bento-card { border-radius: 1.25rem; padding: 2rem; overflow: hidden; position: relative; display: flex; flex-direction: column; justify-content: space-between; }
.bento-card--gradient { background: linear-gradient(135deg, var(--brand-100), var(--brand-50)); }
.bento-card--dark { background: var(--gray-900); color: var(--gray-50); }
```

## Whitespace

Use the design-system scale; do not redefine it if the project has one.

```css
:root {
  --space-1: 0.25rem; --space-2: 0.5rem; --space-3: 0.75rem; --space-4: 1rem;
  --space-5: 1.25rem; --space-6: 1.5rem; --space-8: 2rem; --space-10: 2.5rem;
  --space-12: 3rem; --space-16: 4rem; --space-20: 5rem; --space-24: 6rem;
}
section { padding-block: clamp(4rem, 8vw, 8rem); }
.hero { padding-block: clamp(6rem, 12vw, 12rem); }
```

| Density | Gaps | Padding |
|---------|------|---------|
| Dense UI (dashboards) | 4-8px | 12-16px |
| Standard UI (apps) | 8-16px | 16-24px |
| Marketing / editorial | 16-32px | 32-64px section |
| Luxury / premium | double the above | double the above |

## Visual hierarchy

Techniques, strongest first:

1. Size: the most important element is the largest.
2. Color and contrast: brand color for CTAs, muted grays for secondary.
3. Weight and typeface: bold signals importance.
4. Position: top-left is read first (LTR); key content above the fold.
5. Proximity and grouping: related items close, unrelated clearly separated.
6. Negative space: whitespace adds visual weight.

Section header pattern:

```css
.section-header { max-width: 600px; margin-inline: auto; text-align: center; margin-bottom: var(--space-16); }
.section-label { font-size: var(--text-sm); font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: var(--brand-600); margin-bottom: var(--space-3); } /* 600: small text needs 4.5:1 */
.section-title { font-size: var(--text-4xl); font-weight: 800; line-height: 1.1; color: var(--gray-900); margin-bottom: var(--space-4); }
.section-description { font-size: var(--text-lg); color: var(--gray-600); line-height: 1.6; } /* gray-500 is borderline 4.5:1 */
```

Type sizing: [typography](typography.md).

## Reading patterns

- F-pattern (text-heavy pages): users scan across the top, partway across the middle, then down the left. Put key info in the first two paragraphs, start sections with bold keywords, left-align headings.
- Z-pattern (landing pages): top-left logo, top-right nav, diagonal to the center CTA, then bottom. Build along that diagonal. See [landing-page-design](landing-page-design.md).

## Thirds and asymmetry

Place focal points at the 1/3 intersections, not dead center.

```css
.hero-content { display: grid; grid-template-columns: 2fr 1fr; align-items: center; min-height: 80vh; }

.asymmetric { display: grid; grid-template-columns: 1.5fr 1fr; gap: 4rem; align-items: center; }
.asymmetric--reversed { grid-template-columns: 1fr 1.5fr; }

.offset-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; padding-bottom: 3rem; } /* transform doesn't reserve space */
.offset-grid > :nth-child(3n+2) { transform: translateY(3rem); }
@media (max-width: 768px) { .offset-grid { grid-template-columns: 1fr; } .offset-grid > * { transform: none; } }
```

## Responsive strategies

```css
/* Stack: auto-responsive */
.layout { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 350px), 1fr)); gap: 1.5rem; }

/* Reflow: explicit breakpoints */
.reflow { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
@media (max-width: 768px) { .reflow { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 480px) { .reflow { grid-template-columns: 1fr; } }
```

## Container queries

```css
.card-container { container-type: inline-size; container-name: card; }
.card { display: flex; flex-direction: column; }
@container card (min-width: 500px) {
  .card { flex-direction: row; align-items: center; gap: 2rem; }
  .card-image { flex: 0 0 200px; }
}
```

## Aspect ratio

```css
.thumbnail { aspect-ratio: 16 / 9; object-fit: cover; border-radius: 0.75rem; width: 100%; }
.avatar { aspect-ratio: 1; object-fit: cover; border-radius: 50%; }
```

Common ratios: 1:1 avatars, 4:3 cards, 16:9 video, 3:2 photos, 21:9 cinematic.

## Layout by content type

| Content | Layout |
|---------|--------|
| Landing page | Single column, full-width sections |
| Blog / article | Centered single column, max 65ch |
| Dashboard | 12-column grid or sidebar + main |
| Feature showcase | Bento grid |
| Card listing | Auto-fit grid |
| Portfolio | Masonry or offset grid |
| Documentation | Sidebar nav + centered content |
| E-commerce product | 2-column asymmetric (image + details) |

## Review

Render and view the page at 375, 768 and 1440px wide before shipping. Check:

- One clear focal point per section.
- Consistent left edges and gutters.
- No horizontal overflow: `document.documentElement.scrollWidth > innerWidth` must be false.
- Mobile stacking follows DOM order. Do not reorder visually with `order` or grid placement in a way that breaks keyboard tab order.
- No orphaned single card on the last grid row.

Fix and re-render until clean.
