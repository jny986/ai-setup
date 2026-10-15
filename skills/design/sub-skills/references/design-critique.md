---
metadata:
  version: "1.0.0"
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: design-critique
---

# Design Critique

Evaluate an existing design and give specific, actionable fixes with code.

Tokens come from `.agents/design-context.md` (see [design-context](design-context.md)); with none, extend the project's existing CSS variables or Tailwind theme. "On-brand" is judged against that file, not taste; without it, say the Consistency and Aesthetics scores were judged without brand context. Know the project's purpose, audience, and the one action the design should drive.

Never critique from source code alone: look at the rendered result first.

## Look at the artifact first

| Artifact | How to look at it |
|----------|-------------------|
| HTML file, dev server, or URL | Render it and view at 100% |
| Image (screenshot, generated image, poster) | View the file; zoom or crop to inspect small details |
| Design-tool frame | Export it as an image (plus the token/variable list if available) |
| React/Vue component | Render it in the dev server or Storybook, then treat it as a URL |

For web artifacts:

1. View the first viewport at mobile (about 375px), tablet (about 768px), and desktop (about 1440px) widths, then scroll the full page at mobile and desktop. If the design supports dark mode, view it too.
2. Run an accessibility checker if one is available (axe, Lighthouse, or the browser's built-in audit) and record rule ids and counts.
3. Inspect computed styles for the sets of font sizes, families, text colors, and spacing values in use, which is the evidence for consistency. Check for horizontal overflow, tap targets under 24px, images without alt text, unlabeled form controls, skipped heading levels, missing `lang` or viewport meta, and animation with no `prefers-reduced-motion` rule.

Treat automated numbers as evidence, not verdicts: a contrast "failure" on a disabled control or decorative text may be fine; say so explicitly.

### Procedure

Same order every time, so critiques are comparable:

1. Look at the desktop first viewport for about 5 seconds' worth of attention. Write down what you noticed first, second, and third, and what the page is asking you to do. That is the hierarchy evidence.
2. Walk the review areas below using the renders plus any tool output. Every finding cites evidence: an image region, a measured value, or a checker rule id.
3. Assign severity, score, and write the report.
4. After fixes are applied, re-render and compare before and after.

### Static images

Posters, ads, social graphics, and generated images have no DOM: skip keyboard and performance checks, estimate contrast by sampling pixel colors and applying the WCAG formula, and judge the image at its real display size (for example a thumbnail downscaled to 320px wide). To fix a generated image, give concrete edit instructions for the image-generation tool rather than CSS. See [image-generation](image-generation.md).

## Visual hierarchy

- [ ] **Primary focal point:** one clear element draws attention first
- [ ] **Secondary elements:** a clear 2nd and 3rd level of importance
- [ ] **Size contrast:** the most important element is largest, with enough difference between levels
- [ ] **Color contrast:** the primary CTA uses the strongest color; secondary elements recede
- [ ] **Weight contrast:** headings feel heavier than body
- [ ] **Whitespace:** the most important element has the most room
- [ ] **Reading flow:** F-pattern for content, Z-pattern for landing pages

```css
/* Before: flat hierarchy */
.heading { font-size: 1.5rem; color: #333; }
.subheading { font-size: 1.25rem; color: #333; }
.body { font-size: 1rem; color: #333; }

/* After: clear hierarchy */
.heading { font-size: 2.5rem; font-weight: 800; color: var(--gray-900); letter-spacing: -0.02em; }
.subheading { font-size: 1.25rem; font-weight: 500; color: var(--gray-500); }
.body { font-size: 1rem; font-weight: 400; color: var(--gray-700); line-height: 1.65; }
```

## Color usage

- [ ] **Cohesion:** all colors come from one family/system
- [ ] **Meaning:** each color serves a purpose (brand, semantic, decorative)
- [ ] **Count:** 1-2 brand + 4 semantic + neutrals
- [ ] **Contrast:** text meets WCAG AA (4.5:1 normal; 3:1 for 24px+ or 18.66px+ bold). Use the checker's color-contrast results; for text over images or gradients, measure the worst spot
- [ ] **Semantic consistency:** red is always error, green always success
- [ ] **Dark mode:** colors adapted, not just inverted
- [ ] **Color-only information:** none

```css
/* Before: ~2.3:1 on white, fails AA */
.muted-text { color: #aaa; }

/* After: 4.74:1 on white, passes AA (design-context Neutral 500) */
.muted-text { color: #737373; }

/* Link indistinguishable from text: underline + color */
a { color: var(--brand-500); text-decoration: underline; text-underline-offset: 2px; }
```

See [color-palette](color-palette.md).

## Typography

- [ ] **Font count:** max 2 typefaces (3 with monospace)
- [ ] **Size scale:** consistent ratio, not arbitrary. Roughly 5-8 distinct sizes in use; 12+ means no scale
- [ ] **Weights:** 2-3 in use (400, 600, 700 works)
- [ ] **Line height:** body 1.5-1.75, headings 1.1-1.3
- [ ] **Line length:** body 45-75 characters
- [ ] **Consistency:** same element types share styles
- [ ] **Text wrap:** headings use `text-wrap: balance`
- [ ] **Responsive:** text scales on mobile

```css
/* Line length too long: constrain prose */
.content .prose { max-width: 65ch; }

/* Arbitrary sizes: adopt a modular scale */
:root {
  --type-ratio: 1.25; /* design-context Scale Ratio */
  --text-base: 1rem;
  --text-lg: calc(var(--text-base) * var(--type-ratio));
  --text-xl: calc(var(--text-lg) * var(--type-ratio));
}
```

See [typography](typography.md).

## Spacing and alignment

- [ ] **Consistent gaps** between similar elements
- [ ] **Spacing scale** on a 4px or 8px base
- [ ] **Alignment:** elements on a grid; left edges line up
- [ ] **Proximity:** related items closer than unrelated ones
- [ ] **Padding balance** within components
- [ ] **Vertical rhythm** is consistent
- [ ] **Edge consistency:** page margins match across sections

```css
/* Before: random pixel values */
.card { padding: 17px; margin-bottom: 23px; }
.section { padding: 45px 30px; }

/* After: scale tokens */
.card { padding: var(--space-5); margin-bottom: var(--space-6); }
.section { padding: var(--space-12) var(--space-8); }

/* Misaligned elements: consistent container */
.container { max-width: 1200px; margin-inline: auto; padding-inline: var(--space-6); }
```

See [layout-composition](layout-composition.md).

## Accessibility

Contrast:

- [ ] Normal text 4.5:1; large text (24px+, or 18.66px+ bold) 3:1
- [ ] UI components (borders, icons) 3:1 against adjacent colors
- [ ] Focus indicators 3:1 against adjacent background

Keyboard:

- [ ] All interactive elements focusable, in visual order
- [ ] Focus indicator visible with sufficient contrast
- [ ] No keyboard traps
- [ ] Skip-to-content link exists

Screen reader:

- [ ] Meaningful alt text (or `alt=""` if decorative)
- [ ] Form inputs have associated labels
- [ ] Icon-only buttons have `aria-label`
- [ ] Headings form a logical outline (no skipped levels)
- [ ] Dynamic changes are announced (aria-live)

```css
/* Never remove focus without a replacement */
*:focus { outline: none; } /* before: do not do this */

*:focus-visible { outline: 2px solid var(--brand-500); outline-offset: 2px; } /* after */

.skip-link {
  position: absolute; top: -100%; left: 0;
  padding: 0.5rem 1rem; background: var(--brand-500); color: white; z-index: 9999;
}
.skip-link:focus { top: 0; }
```

```html
<a href="#main-content" class="skip-link">Skip to main content</a>
```

## Responsive behavior

- [ ] **Mobile layout** stacks sensibly
- [ ] **Touch targets** at least 24x24px (WCAG 2.2 AA, SC 2.5.8); 44x44px recommended on mobile
- [ ] **Text** at least 16px on mobile (no zoom needed)
- [ ] **No horizontal overflow**
- [ ] **Images** resize (`max-width: 100%`)
- [ ] **Navigation** is accessible and usable on mobile
- [ ] **Breakpoints** transition smoothly

```css
/* Fixed width overflows: flexible with a max */
.card { width: 100%; max-width: 400px; }

/* Small touch target: larger hit area, same visual icon (with box-sizing: border-box) */
.icon-button { min-width: 44px; min-height: 44px; display: inline-grid; place-items: center; }

img { max-width: 100%; height: auto; }
```

See [mobile-ui-design](mobile-ui-design.md).

## Performance

- [ ] **Font loading:** `font-display: swap`; critical fonts preloaded
- [ ] **Image formats:** AVIF/WebP with fallbacks; `srcset` + `sizes` so phones skip desktop images
- [ ] **Image sizing:** not 4000px for a 400px display
- [ ] **Animation:** only `transform` and `opacity`
- [ ] **CSS:** no redundant or overriding styles
- [ ] **Layout shifts:** dimensions reserved for images and embeds
- [ ] **Shadows/blurs:** no heavy effects on frequently painted elements
- [ ] **LCP:** no lazy-loaded images in the first viewport

```css
/* Before: triggers layout */
.card:hover { margin-top: -5px; }
/* After: composited */
.card:hover { transform: translateY(-5px); }

/* Layout shift: put intrinsic size in HTML (<img width="1600" height="900">), then: */
img { max-width: 100%; height: auto; }
```

## Severity and recommendation format

Assign exactly one severity per issue.

| Severity | Criteria | Examples |
|----------|----------|----------|
| Critical | Blocks the core task, or fails WCAG A/AA on core content | Body text 2.3:1, CTA invisible on mobile, keyboard trap, horizontal scroll on mobile, unlabeled form fields |
| High | Core task works but is noticeably harder, or the design undermines its main goal | No clear primary CTA, competing focal points, off-brand colors/fonts, tap targets under 24px |
| Medium | Visible polish problem most users feel but can work around | 10+ font sizes, off-grid spacing, inconsistent radii, weak secondary hierarchy |
| Low | Refinement a designer would notice | Heading widows, loose letter-spacing, minor alignment drift |

Order fixes by severity, then by impact divided by effort within a severity.

Recommendation format:

```text
### [Severity] Issue: [What's wrong]
**Category**: Hierarchy | Color | Typography | Spacing | Accessibility | Responsive | Performance
**Evidence**: [image region, measured value, or checker rule id]
**Problem**: [1-2 sentences: what's wrong and why it matters]
**Fix**: [Specific CSS/HTML using the project's tokens]
**Impact**: [What improves]
```

Example:

```text
### [High] Issue: Hero headline, subtitle, and CTA compete for attention
**Category**: Hierarchy
**Evidence**: desktop first viewport -- headline 28px/600, subtitle 24px/600, CTA is a gray outline button
**Problem**: Nothing reads first, and the only action looks secondary.
**Fix**: .hero-headline { font-size: clamp(2.5rem, 5vw + 1rem, 5rem); font-weight: 800; }
         .hero-subtitle { font-size: var(--text-xl); color: var(--text-secondary); max-width: 50ch; }
         .hero-cta { background: var(--interactive-primary); color: white; }
**Impact**: Headline -> value prop -> CTA reads in order within 3 seconds.
```

## Before/after verification

A critique is not done until the fixes are checked on the rendered page.

1. For each fix, show the current CSS (before) and improved CSS (after) and say what changed and why. Use existing tokens (`--space-*`, `--text-*`, `--bg-*`, `--text-primary`, `--interactive-primary`, `--radius-*`, `--shadow-*`); never introduce new hard-coded values.
2. If you applied the fixes, re-render at the same widths and compare before and after side by side.
3. Confirm every Critical and High issue is resolved (checker violations gone, no overflow, targets at least 24px) and nothing regressed at the other widths or in dark mode. Re-score only after this check.

## Scoring

Rate 1-10 per category:

| Category | Weight | Evaluate |
|----------|--------|----------|
| Hierarchy | 25% | Clear focal points, scannable, directed flow (hierarchy review, 5-second test) |
| Consistency | 25% | Spacing scale, color system, type system, brand match (color, typography, spacing reviews) |
| Aesthetics | 25% | Color harmony, whitespace, polish, fit to style archetype |
| Usability | 25% | Accessibility, responsiveness, clarity, performance (accessibility, responsive, performance reviews, checker output) |

Overall is the weighted average, rounded to one decimal. Caps keep scores honest: any open Critical issue caps its category at 4 and the overall at 6; any open High issue caps its category at 7. Aesthetics must cite at least one concrete observation, not just "looks modern."

| Score | Meaning |
|-------|---------|
| 1-2 | Fundamentally broken; major rework |
| 3-4 | Significant issues in multiple areas |
| 5-6 | Functional but unpolished |
| 7-8 | Good; minor refinements would elevate it |
| 9-10 | Excellent; professional quality |

### Report template

```text
## Design Critique Report

### Overall Score: X/10

| Category    | Score | Notes         |
|-------------|-------|---------------|
| Hierarchy   | X/10  | [brief note]  |
| Consistency | X/10  | [brief note]  |
| Aesthetics  | X/10  | [brief note]  |
| Usability   | X/10  | [brief note]  |

### Top 3 Strengths
1. [What's working well]
2. [What's working well]
3. [What's working well]

### Issues by Severity
| # | Severity | Category | Issue | Evidence |
|---|----------|----------|-------|----------|
| 1 | Critical | ...      | ...   | ...      |

### Fixes (in priority order, with code, in the recommendation format)

### Quick Wins (under 5 min each)
- [Small change, big impact]
```

## Process summary

0. Render the artifact and look before reading code.
1. Read design context and understand goals.
2. Hierarchy: is there a clear 1-2-3 priority?
3. Color: cohesive, accessible, purposeful?
4. Typography: consistent scale, good line length, readable?
5. Spacing: systematic, aligned, consistent?
6. Accessibility: contrast, focus, labels, keyboard?
7. Responsive: mobile stacking, touch targets, overflow?
8. Performance: efficient animation, sized images, loaded fonts?
9. Always give specific fixes with code, never just description.
10. Score, assign severity, apply caps, rank fixes.
11. Re-render after fixes and confirm Critical/High issues are gone.
