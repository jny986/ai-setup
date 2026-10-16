---
name: design-critique
description: "Review rendered interfaces or static designs and report evidence-based findings, user impact, and concrete recommendations."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: ArnavPuri/designskills, pbakaus/impeccable
  based_on_version: main(c787301), main(2f98774)
  based_on_skill: design-critique, critique
---

# Design Critique

Evaluate an existing design and give evidence-based, actionable recommendations. Apply fixes when requested. Use [audit](../audit.md) for a combined interface and implementation audit; this reference also covers static images and design frames.

Read `DESIGN.md` for UI tokens and the project brand kit for approved brand primitives (see [design-context](design-context.md)); when absent, inspect the project's existing CSS variables or Tailwind theme. Judge brand consistency against the brand kit and UI consistency against `DESIGN.md`; when neither exists, state the context limits affecting the review. Know the project's purpose, audience, and the one action the design should drive.

Look at the rendered result before judging visual quality. When the artifact cannot be rendered or viewed, limit claims to what the available source proves and state the missing visual evidence.

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
3. Assign severity by user impact and write the report. Score only when the user requests it or supplies a rubric.
4. After fixes are applied, re-render and compare before and after.

### Static images

Posters, ads, social graphics, and generated images have no DOM: skip keyboard and performance checks, estimate contrast by sampling pixel colors and applying the WCAG formula, and judge the image at its real display size (for example a thumbnail downscaled to 320px wide). To fix a generated image, give concrete edit instructions for the image-generation tool rather than CSS. See [image-generation](image-generation.md).

## Visual hierarchy

- [ ] **Primary focal point:** one clear element draws attention first
- [ ] **Secondary elements:** a clear 2nd and 3rd level of importance
- [ ] **Size contrast:** size supports importance alongside position, weight, and grouping
- [ ] **Color contrast:** the primary CTA uses the strongest color; secondary elements recede
- [ ] **Weight contrast:** headings feel heavier than body
- [ ] **Whitespace:** the most important element has the most room
- [ ] **Reading flow:** the composition and content establish a useful sequence for this task

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
- [ ] **Roles:** brand, surface, text, action, and status roles are coherent; additional colors have a clear purpose
- [ ] **Contrast:** text meets WCAG AA (4.5:1 normal; 3:1 for 24px+ or 18.66px+ bold). Use the checker's color-contrast results; for text over images or gradients, measure the worst spot
- [ ] **Semantic consistency:** status meanings agree across the interface and with its domain conventions
- [ ] **Dark mode:** colors adapted, not just inverted
- [ ] **Color-only information:** none

```css
/* Before: ~2.3:1 on white, fails AA */
.muted-text { color: #aaa; }

/* After: 4.74:1 on white, passes AA (documented muted text color) */
.muted-text { color: #737373; }

/* Link indistinguishable from text: underline + color */
a { color: var(--brand-500); text-decoration: underline; text-underline-offset: 2px; }
```

See [color-palette](color-palette.md).

## Typography

- [ ] **Families:** each family has a useful, consistent role
- [ ] **Size scale:** repeated roles are consistent; differences carry information
- [ ] **Weights:** role differences are distinguishable in the actual face
- [ ] **Line height:** body 1.5-1.75, headings 1.1-1.3
- [ ] **Line length:** body 45-75 characters
- [ ] **Consistency:** same element types share styles
- [ ] **Text wrap:** headings use `text-wrap: balance`
- [ ] **Responsive:** text stays readable and hierarchy holds across widths and user text settings

```css
/* Line length too long: constrain prose */
.content .prose { max-width: 65ch; }

/* Arbitrary sizes: adopt a modular scale */
:root {
  --type-ratio: 1.25; /* documented type ratio */
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
- [ ] **Animation:** effects have a purpose and fit the measured rendering budget; see [motion-design](motion-design.md)
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

## Usability and cognitive load

For interactive artifacts, walk the actual task and record the step or state that produces friction. Select the relevant lenses:

| Lens | Evidence to seek |
|---|---|
| System status | Does feedback reflect the actual operation, progress, outcome, and current location? |
| Domain language | Do labels and information order match the user's task and established terminology? |
| Control and recovery | Can users go back, cancel, undo when safe, and recover without losing valid work? |
| Consistency | Do equivalent actions and controls behave consistently across screens and platforms? |
| Error prevention | Are prerequisites, constraints, and consequential outcomes visible before commitment? |
| Recognition and memory | Is needed context present at the decision, or must users recall another screen or hidden information? |
| Efficiency | Can frequent users repeat work efficiently while newcomers can discover required actions? |
| Grouping and relevance | Are related decisions grouped and secondary detail disclosed where useful? |
| Error explanation | Does failure feedback identify the problem and a truthful next step? |
| Help | Is guidance available at the point of need without blocking normal work? |

Assess complexity against the actual domain, audience, and task. Option counts alone do not prove overload. Look for observed ambiguity, unnecessary context switching, repeated entry, or a failure to find the next action. Use [flow](../flow.md) to implement journey changes and [refine](../refine.md) for visual improvements.

## Severity and report

Use the P0–P3 scale from [audit](../audit.md): P0 blocks the primary task; P1 causes major difficulty or a material accessibility barrier; P2 adds friction with a workable path; P3 is low-impact finish. For a static artifact, assess its intended communication outcome. Assign severity from demonstrated impact, rather than counting stylistic rule violations.

Each finding names the location or state, observed evidence, user impact, and a concrete recommendation. Include code when it makes an implementation fix clearer; use layout or image-edit instructions for non-code artifacts. Merge symptoms with a shared cause and order findings by impact, then useful implementation sequence.

A compact report can contain:

```text
Target and intended outcome: [artifact, audience, task]
Evidence and scope: [renders, states, widths, interactions, checks]
What works: [supported strengths, when useful]
Findings:
  [P1] [problem] — [location]; [evidence]; [impact]; [recommendation]
Fix order: [priority changes and dependencies]
Limits: [unavailable context, untested states, uncertain claims]
```

A diagnosis is complete when supported findings and verification limits are actionable. It does not require code changes. If scoring is requested, agree or state the rubric and anchor ratings in evidence; distinguish subjective visual judgment from measured behavior and accessibility results.

## Verification after requested fixes

Re-render affected states at comparable widths, themes, content, and input settings. Compare before and after, recheck the specific reported failures, and inspect related consumers when shared styles or components changed. Report which findings were resolved and which remain open; a clean automated scan alone does not establish usability or visual quality. For finish work, use [polish](polish.md).
