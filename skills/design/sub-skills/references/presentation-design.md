---
metadata:
  version: "1.0.0"
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: presentation-design
---

# Presentation Design

Slide decks as HTML/CSS (custom or reveal.js): layouts on a fixed 16:9 canvas, typography, charts, builds, speaker notes, PDF export. For native .pptx files use a PowerPoint-specific tool.

Tokens come from `.agents/design-context.md` (see [design-context](design-context.md)); with none, extend the project's existing CSS variables or Tailwind theme. Map them to the `--slide-*` variables below and use the shared `--brand-*` / `--gray-*` scales from [color-palette](color-palette.md).

Before designing, settle the audience, purpose, length, and whether the deck is projected, screen-shared, or sent as a PDF. For photographic backgrounds or illustrations, generate them at 16:9 (see [image-generation](image-generation.md)) and keep text on a solid or overlaid area, not on busy image regions.

Assumed easing token (define it if the project has none): `--ease-out: cubic-bezier(0.16, 1, 0.3, 1);`

## Canvas

Design every slide on a fixed 1280x720 canvas and scale the whole canvas to the screen. All rem/px sizes here assume that canvas, so type stays proportional on a laptop, projector, or PDF page.

```css
html, body { margin: 0; height: 100%; background: black; overflow: hidden; }
.deck { position: fixed; inset: 0; }
.slide {
  position: absolute; left: 50%; top: 50%; width: 1280px; height: 720px;
  transform: translate(-50%, -50%) scale(var(--deck-scale, 1));
  overflow: hidden; font-family: var(--font-body); background: var(--slide-bg, white);
}
.slide-content { padding: 4rem 6rem; } /* Safe margins: keep text out of the outer ~5% */
```

```js
const fit = () => document.documentElement.style.setProperty(
  '--deck-scale', Math.min(innerWidth / 1280, innerHeight / 720));
addEventListener('resize', fit); fit();
```

## One idea per slide

Each slide makes one point:

1. **Headline:** the takeaway, one line, 6-8 words max.
2. **Support:** a visual or 3-4 bullets reinforcing it.
3. **Visual anchor:** an image, chart, icon, or number.

Cut paragraphs, more than 4-5 bullets, and busy diagrams; split or simplify instead.

## Typography

| Element | Size | Weight | Notes |
|---------|------|--------|-------|
| Headline | 3-4.5rem | 700-800 | 1 line, max 2 |
| Subhead | 1.5-2rem | 500 | Supporting context |
| Body | 1.25-1.5rem | 400 | Bullets, descriptions |
| Caption | 1-1.125rem | 400 | Attribution, fine print |
| Stat | 4-6rem | 800 | Key metrics |

```css
.slide-dark { background: var(--gray-900); color: var(--gray-50); }
.slide-dark .slide-heading { color: white; }
.slide-dark .slide-body { color: var(--gray-300); }
```

Use `font-display: block` for presentation fonts to avoid a flash of fallback text mid-talk. More: [typography](typography.md).

## Layout templates

### Title slide

```css
.slide-title {
  display: flex; align-items: center; justify-content: center;
  text-align: center; background: var(--brand-500); color: white;
}
.slide-title .slide-headline { font-size: 4rem; font-weight: 800; line-height: 1.05; letter-spacing: -0.03em; margin-bottom: 1rem; }
.slide-title .slide-subtitle { font-size: 1.5rem; opacity: 0.85; margin-bottom: 2rem; }
.slide-title .slide-meta { display: flex; gap: 2rem; font-size: 1rem; opacity: 0.7; }
```

### Content (text + bullets)

```css
.slide-content-layout { display: flex; flex-direction: column; justify-content: center; padding: 4rem 6rem; }
.slide-heading { font-size: 2.5rem; font-weight: 700; margin-bottom: 2rem; color: var(--gray-900); }
.slide-bullets { list-style: none; padding: 0; display: flex; flex-direction: column; gap: 1.25rem; }
.slide-bullets li { font-size: 1.5rem; line-height: 1.4; color: var(--gray-700); padding-left: 2rem; position: relative; }
.slide-bullets li::before { content: ''; position: absolute; left: 0; top: 0.55em; width: 8px; height: 8px; background: var(--brand-500); border-radius: 50%; }
```

### Two-column comparison

```css
.slide-columns { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; margin-top: 2rem; }
.slide-col h3 { font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem; padding-bottom: 0.75rem; border-bottom: 3px solid var(--brand-500); }
```

### Quote

```css
.slide-quote { display: grid; place-items: center; padding: 4rem 8rem; background: var(--gray-50); }
.slide-blockquote p { font-size: 2.5rem; font-weight: 500; font-style: italic; line-height: 1.3; text-align: center; margin-bottom: 1.5rem; }
.slide-blockquote cite { display: block; font-size: 1.125rem; font-style: normal; color: var(--brand-500); font-weight: 600; text-align: center; }
```

### Data / stats

```css
.stats-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 3rem; margin-top: 3rem; text-align: center; }
.stat-number { display: block; font-size: 4rem; font-weight: 800; color: var(--brand-500); line-height: 1; margin-bottom: 0.5rem; }
.stat-label { font-size: 1.125rem; color: var(--gray-500); }
```

### Image + text

```css
.slide-image-text { display: grid; grid-template-columns: 1fr 1fr; gap: 0; }
.slide-image-text .slide-image { background-size: cover; background-position: center; }
.slide-image-text .slide-text { display: flex; flex-direction: column; justify-content: center; padding: 4rem; }
```

### Closing / CTA

The last slide stays up longest during Q&A. Include a clear next step (URL, QR code), contact info, and optionally the key takeaway in one line.

```css
.slide-closing { display: grid; place-items: center; text-align: center; background: var(--gray-900); color: white; }
.closing-headline { font-size: 4rem; font-weight: 800; margin-bottom: 2rem; }
.closing-link { font-size: 2rem; color: var(--brand-300); font-weight: 600; }
.closing-contact { font-size: 1.125rem; opacity: 0.6; display: flex; gap: 2rem; }
```

## Charts

### CSS bar chart

```css
.chart-bars { display: flex; align-items: flex-end; gap: 2rem; height: 300px; padding-top: 2rem; margin-bottom: 2.5rem; /* room for .bar-label */ }
.bar { flex: 1; height: calc(var(--value) * 1%); background: var(--brand-500); border-radius: 0.5rem 0.5rem 0 0; position: relative; transition: height 0.6s var(--ease-out); }
.bar-value, .bar-label { position: absolute; left: 0; right: 0; text-align: center; }
.bar-value { top: -2rem; font-weight: 700; font-size: 1.25rem; }
.bar-label { bottom: -2rem; font-size: 1rem; color: var(--gray-600); }
```

```html
<div class="chart-bars" role="img" aria-label="Revenue by quarter: Q1 40%, Q2 55%, Q3 70%, Q4 90%">
  <div class="bar" style="--value: 40"><span class="bar-value">40%</span><span class="bar-label">Q1</span></div>
  <!-- ... -->
</div>
```

### CSS donut

```css
.donut { --pct: 65%; width: 200px; height: 200px; border-radius: 50%; background: conic-gradient(var(--brand-500) 0 var(--pct), var(--gray-200) var(--pct) 100%); display: grid; place-items: center; }
.donut-label { width: 140px; height: 140px; background: var(--slide-bg, white); border-radius: 50%; display: grid; place-items: center; font-size: 2rem; font-weight: 800; }
```

```html
<div class="donut" style="--pct: 65%" role="img" aria-label="65% of customers renewed"><span class="donut-label" aria-hidden="true">65%</span></div>
```

Beyond one or two series, use a real chart library or SVG (see [infographic](infographic.md)).

Rules:

1. Minimize gridlines and labels: show a trend, not precise data.
2. Highlight the key data point (larger, different color, labeled).
3. Marks need 3:1 contrast against the slide background (WCAG 1.4.11); label values directly instead of using a color legend.
4. Animate chart elements on slide entrance for emphasis.

## Transitions and builds

Slide fade is defined in the framework section below. Other builds:

```css
/* Progressive bullet reveal */
.slide-bullets li { opacity: 0; transform: translateX(-20px); transition: opacity 0.3s var(--ease-out), transform 0.3s var(--ease-out); }
.slide-bullets li.is-revealed { opacity: 1; transform: translateX(0); }
```

```css
/* Number count-up */
@property --num { syntax: '<integer>'; initial-value: 0; inherits: false; }
.stat-countup { --target: 65; animation: count-up 2s var(--ease-out) forwards; counter-reset: num var(--num); }
.stat-countup::after { content: counter(num) '%'; }
@keyframes count-up { from { --num: 0; } to { --num: var(--target); } }
@media (prefers-reduced-motion: reduce) { .stat-countup { animation: none; --num: var(--target); } }
```

Keep the count-up element empty (the number is generated) and give it `role="img"` with `aria-label="65%"`; screen readers may skip generated content or announce every frame. More: [motion-design](motion-design.md).

## Speaker notes

Put notes in an `<aside class="notes">` inside each slide, the same markup reveal.js uses, so decks can move between the custom system and reveal.js. Write notes for every content slide.

```html
<section class="slide">
  <!-- slide content -->
  <aside class="notes">Explain the key metric here. Pause for questions.</aside>
</section>
```

```css
.notes { display: none; }
/* Press N (see the framework script) to show notes as an overlay while rehearsing */
.show-notes .slide.is-active .notes {
  display: block; position: absolute; inset: auto 0 0 0; max-height: 35%; overflow: auto;
  padding: 1.5rem 2rem; background: oklch(0.2 0 0 / 0.92); color: white; font-size: 1.25rem; line-height: 1.5;
}
```

For a real presenter view on a second screen, use reveal.js (press `S`).

## Framework

### Custom slide system

Uses the canvas above. Inactive slides are hidden with `inert`, so their links are not tabbable and screen readers only see the current slide.

```css
.slide { display: flex; opacity: 0; pointer-events: none; transition: opacity 0.4s ease; }
.slide.is-active { opacity: 1; pointer-events: auto; }
```

```js
let current = 0;
const slides = document.querySelectorAll('.slide');
function goTo(index) {
  current = Math.max(0, Math.min(index, slides.length - 1));
  slides.forEach((s, i) => { s.classList.toggle('is-active', i === current); s.inert = i !== current; });
  history.replaceState(null, '', '#' + (current + 1)); // deep-linkable
}
document.addEventListener('keydown', (e) => {
  if (['ArrowRight', 'PageDown', ' '].includes(e.key)) { e.preventDefault(); goTo(current + 1); }
  if (['ArrowLeft', 'PageUp'].includes(e.key)) goTo(current - 1);
  if (e.key.toLowerCase() === 'n') document.body.classList.toggle('show-notes');
});
goTo((parseInt(location.hash.slice(1), 10) || 1) - 1);
```

For reveal.js, load from a CDN and customize with CSS variables (`--r-heading-font`, `--r-main-color`, `--r-link-color`).

### Brand template

```css
.deck {
  --slide-bg: white; --slide-heading-color: var(--gray-900);
  --slide-text-color: var(--gray-600); --slide-accent: var(--brand-500);
  font-family: var(--font-body); /* headings use --font-heading */
}
.slide::after { content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 4px; background: var(--slide-accent); }
.slide-number { position: absolute; bottom: 1.5rem; right: 2rem; font-size: 0.875rem; color: var(--gray-500); font-variant-numeric: tabular-nums; }
.slide-logo { position: absolute; bottom: 1.5rem; left: 2rem; width: 80px; opacity: 0.3; }
```

## Quick reference

1. 16:9 with generous padding (4-6rem).
2. One idea per slide; split complex ones.
3. Headlines 3-4.5rem, max 8 words.
4. Body 1.25-1.5rem minimum (readable from the back of the room).
5. Brand colors consistently; max 3 colors per slide.
6. Build progressively; do not animate everything.
7. Simplify charts and highlight the key point.
8. Speaker notes on every content slide.
9. Closing slide: CTA + contact, kept up during Q&A.
10. Projectors wash out color; check on a large screen if possible.

## Review and export

1. **Render every slide** at 1920x1080 (step through `#1` to `#N` in a browser or headless renderer) and view each one. Check: no text overflowing or clipped by `overflow: hidden`, one idea per slide, headline readable at thumbnail size, consistent margins and slide-number position, brand colors correct.
2. **Contrast:** text on brand-color and image backgrounds meets 4.5:1 (3:1 for 24px+ text); projectors lower contrast further, so aim higher.
3. **PDF (custom system):** a print stylesheet that lays slides out one per page, with page size matching the canvas. Print with backgrounds enabled.

```css
@page { size: 1280px 720px; margin: 0; }
@media print {
  html, body { height: auto; overflow: visible; background: none; }
  .deck { position: static; }
  .slide { position: relative; left: 0; top: 0; transform: none; opacity: 1; break-after: page; }
}
```

For reveal.js, open with `?print-pdf` before printing.
