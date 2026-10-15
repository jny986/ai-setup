---
metadata:
  version: "1.0.0"
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: typography
---

# Typography

Type scales, font pairing, heading hierarchy, readable body text, fluid sizing, variable fonts and font loading for web and UI.

Tokens come from `.agents/design-context.md` (see [design-context](design-context.md)); with none, extend the project's existing CSS variables or Tailwind theme. Use the context's fonts, base size, scale ratio and weights unless the user is changing them. The default scale in design-context (12/14/16/18/20/24/30/36/48/60/72) is Tailwind's hand-tuned scale, not a strict 1.25 progression. If the project already uses it, keep it; for new work generate a true modular scale from the saved ratio and say which you used. Token layering: [design-system](design-system.md).

## Type scale ratio

| Ratio | Name | Value | Best for |
|-------|------|-------|----------|
| Minor second | Tight | 1.067 | Dense data UIs, dashboards |
| Major second | Compact | 1.125 | Apps, tools |
| Minor third | Default | 1.200 | General web, blogs, marketing |
| Major third | Relaxed | 1.250 | Editorial, magazines |
| Perfect fourth | Bold | 1.333 | Marketing, landing pages |
| Augmented fourth | Impact | 1.414 | Bold headlines, creative sites |
| Perfect fifth | Drama | 1.500 | High-impact heroes |
| Golden ratio | Grand | 1.618 | Art, luxury, editorial |

`size(n) = base x ratio^n`. Each step is the previous times the ratio, so changing `--type-ratio` updates the whole scale. Comments below are for 1.25; recompute for other ratios. Keep functional text (captions, labels) at 12px or larger.

```css
:root {
  --type-ratio: 1.25;
  --type-base: 1rem;

  --text-xs:   max(0.75rem, calc(var(--text-sm) / var(--type-ratio))); /* 10.24px, floored to 12px */
  --text-sm:   calc(var(--type-base) / var(--type-ratio));  /* 12.8px */
  --text-base: var(--type-base);                             /* 16px */
  --text-lg:   calc(var(--text-base) * var(--type-ratio));   /* 20px */
  --text-xl:   calc(var(--text-lg) * var(--type-ratio));     /* 25px */
  --text-2xl:  calc(var(--text-xl) * var(--type-ratio));     /* 31.25px */
  --text-3xl:  calc(var(--text-2xl) * var(--type-ratio));    /* 39px */
  --text-4xl:  calc(var(--text-3xl) * var(--type-ratio));    /* 48.8px */
  --text-5xl:  calc(var(--text-4xl) * var(--type-ratio));    /* 61px */
}
```

## Font pairing

Strategies:

1. Serif headings + sans body: classic editorial.
2. Geometric sans headings + humanist sans body: modern but warm.
3. Slab serif headings + sans body: bold, confident.
4. Mono headings + sans body: technical, developer-oriented.
5. One family, different weights (700+ headings, 400 body): safest.

Avoid:

- Two fonts of the same category with similar proportions (two geometric sans).
- More than 2 typefaces per page (3 if one is monospace for code).
- Decorative or display fonts for body text.

### Pairings

| Group | Heading + body | Note |
|-------|----------------|------|
| Editorial | Playfair Display + Source Sans 3 | Elegant serif, clean sans. Magazines, blogs |
| Editorial | Lora + Inter | Warm transitional serif, neutral sans. Very readable |
| Editorial | Fraunces + Commissioner | Variable soft serif with personality, low-contrast humanist sans |
| Modern / SaaS | Inter + Inter | Single family: 700 headings, 400 body. Versatile |
| Modern / SaaS | DM Sans + DM Sans | Geometric, slightly more personality than Inter |
| Modern / SaaS | Manrope + Source Sans 3 | Semi-condensed grotesque + humanist. Friendly tech |
| Bold / marketing | Space Grotesk + DM Sans (or General Sans, Fontshare, self-host) | Techy and bold |
| Bold / marketing | Bricolage Grotesque + Inter | Quirky variable sans + reliable body. Playful but professional |
| Bold / marketing | Cabinet Grotesk + Satoshi (Fontshare, self-host) | Modern geometric pair, premium startup feel |
| Specialized | JetBrains Mono + Inter | Developer tools, docs |
| Specialized | Instrument Serif + Instrument Sans | Designed together. Instrument Serif is display-weight only: headings, not body |
| Specialized | Sora + Newsreader | Geometric sans headings, readable serif body. Inverted classic |

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@700;800&display=swap" rel="stylesheet">
```

```css
:root {
  --font-heading: 'Playfair Display', Georgia, serif;
  --font-body: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
}
```

## Heading hierarchy

Defaults for ratio 1.25, base 16px:

```css
h1 {
  font-family: var(--font-heading);
  font-size: var(--text-5xl);   /* ~61px */
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.025em;
  margin-bottom: 0.5em;
}

h2 {
  font-family: var(--font-heading);
  font-size: var(--text-4xl);   /* ~49px */
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.02em;
  margin-bottom: 0.5em;
}

h3 {
  font-family: var(--font-heading);
  font-size: var(--text-3xl);   /* ~39px */
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.015em;
  margin-bottom: 0.5em;
}

h4 { font-size: var(--text-2xl); font-weight: 600; line-height: 1.25; letter-spacing: -0.01em; } /* ~31px */
h5 { font-size: var(--text-xl); font-weight: 600; line-height: 1.3; }                           /* ~25px */

h6 {
  font-size: var(--text-lg);    /* ~20px */
  font-weight: 600;
  line-height: 1.4;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

- Negative letter-spacing on large headings (-0.01em to -0.03em); tighter line-height (1.1-1.3) than body.
- Never skip levels (h1 to h3) to get a smaller size. Levels are document structure for screen readers; decouple looks with classes (`<h2 class="h4">`).

## Body text

- Size: 16px minimum, 18px preferred for long-form.
- Line height: 1.5 for UI, 1.6-1.75 for long-form.
- Line length: 45-75 characters (65ch ideal).
- Paragraph spacing: 1em-1.5em.

```css
body {
  font-family: var(--font-body);
  font-size: 1.125rem;        /* 18px */
  line-height: 1.65;
  color: var(--text-primary, var(--gray-900));
  -webkit-font-smoothing: antialiased;  /* macOS only; harmless elsewhere */
  text-rendering: optimizeLegibility;
}

.prose {
  max-width: 65ch;
  margin-inline: auto;
}

.prose > * + * { margin-top: 1em; }
.prose p + p { margin-top: 1.25em; }
```

## Fluid typography with clamp()

```text
clamp(min, preferred, max)
slope     = (maxSize - minSize) / (maxViewport - minViewport)   e.g. (24 - 20) / (1280 - 360) = 0.004348
preferred = (slope * 100)vw + (minSize - slope * minViewport) / 16 rem
          = 0.4348vw + 1.152rem  ->  clamp(1.25rem, 0.4348vw + 1.152rem, 1.5rem)
```

Always keep a `rem` term in the preferred value. Pure `vw` sizes do not grow with browser zoom and fail WCAG 1.4.4 (Resize Text).

This scale replaces the static one above (use one or the other). Maxes approximate a 1.25-1.33 progression at desktop widths; mins stay close to the mobile static scale.

```css
:root {
  --text-base: clamp(1rem, 0.5vw + 0.875rem, 1.125rem);
  --text-lg:   clamp(1.125rem, 0.75vw + 0.9rem, 1.35rem);
  --text-xl:   clamp(1.25rem, 1vw + 0.95rem, 1.75rem);
  --text-2xl:  clamp(1.5rem, 1.5vw + 1rem, 2.25rem);
  --text-3xl:  clamp(1.875rem, 2vw + 1.1rem, 3rem);
  --text-4xl:  clamp(2.25rem, 3vw + 1rem, 4rem);
  --text-5xl:  clamp(2.75rem, 4vw + 1rem, 5.5rem);
}

.hero-title {
  font-size: clamp(2.5rem, 5vw + 1rem, 6rem);
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -0.03em;
  text-wrap: balance;
}
```

## Text effects

Use brand tokens for gradients (a stock purple gradient is a generic tell).

```css
.gradient-text {
  background: linear-gradient(135deg, var(--brand-500), var(--brand-700));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.outlined-text {
  -webkit-text-stroke: 2px currentColor;
  -webkit-text-fill-color: transparent;
  font-weight: 800;
  font-size: 5rem;
}

.text-shadow-soft { text-shadow: 0 2px 4px rgba(0,0,0,0.1); }
.text-shadow-hard { text-shadow: 3px 3px 0 rgba(0,0,0,0.15); }
.text-over-image  { text-shadow: 0 2px 16px rgba(0,0,0,0.5); }
.text-backdrop    { background: rgba(0,0,0,0.5); backdrop-filter: blur(4px); padding: 0.5em 1em; border-radius: 0.25em; }
```

Gradient, outlined and image-backed text must still meet contrast: measure the lightest part of the gradient or photo behind the text. Keep outlined text to display sizes.

## Variable fonts

| Axis | CSS property | Typical range |
|------|--------------|---------------|
| wght | `font-weight` | 100-900 |
| wdth | `font-stretch` | 75%-125% |
| slnt | `font-style: oblique Xdeg` | -12 to 0 |
| ital | `font-style: italic` | 0 or 1 |
| opsz | `font-optical-sizing: auto` | varies (Inter 14-32) |

```css
@font-face {
  font-family: 'Inter Variable';
  src: url('/fonts/InterVariable.woff2') format('woff2');
  font-weight: 100 900;
  font-display: swap;
}

.heading {
  font-family: 'Inter Variable', sans-serif;
  font-weight: 750;
  font-optical-sizing: auto;
}

/* Only works if the font has a wdth axis (Roboto Flex, Mona Sans; Inter has none) */
.heading-wide { font-stretch: 110%; }
```

Prefer `font-weight`, `font-stretch`, `font-style` and `font-optical-sizing` over `font-variation-settings`, which overrides all axes at once and does not inherit per axis. Check a font's axes on its Google Fonts page before using them.

## Letter-spacing

| Context | letter-spacing |
|---------|----------------|
| Large headings (3rem+) | -0.02 to -0.03em |
| Small headings | -0.01em |
| Body | normal |
| All caps | +0.05 to +0.1em |
| Small / caption | +0.01 to +0.02em |
| Monospace | normal |

```css
.caps-label {
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: var(--text-sm);
  font-weight: 600;
}
```

## Font loading

Pick one: Google Fonts CDN (preconnect plus the stylesheet above) or self-hosting (better for performance and privacy/GDPR). When self-hosting, preload only the 1-2 files needed above the fold.

```html
<link rel="preload" as="font" type="font/woff2" href="/fonts/inter-var.woff2" crossorigin>
```

```css
@font-face {
  font-family: 'Inter';
  src: url('/fonts/inter-var.woff2') format('woff2');
  font-weight: 100 900;
  font-display: swap;
}
```

| `font-display` | Behavior | Use |
|----------------|----------|-----|
| swap | Fallback immediately, swap when loaded | Body text, most cases |
| optional | Brief block, may skip the custom font | Non-critical decorative fonts |
| fallback | Short block, short swap period | Balance of swap and optional |
| block | Invisible text up to 3s | Icon fonts only |

System fallback stack:

```css
:root {
  --font-system: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI',
                 Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
}
```

Prevent layout shift by matching fallback metrics. The values below are for Inter over Arial; for other fonts generate them with a metrics tool (Fontaine, Capsize) or let the framework do it (`next/font` does automatically).

```css
@font-face {
  font-family: 'Inter Fallback';
  src: local('Arial');
  size-adjust: 107%;
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
}

body { font-family: 'Inter', 'Inter Fallback', sans-serif; }
```

### Licensing

- Google Fonts: open source (almost all SIL OFL 1.1, a few Apache 2.0). Free for commercial use, embedding and self-hosting.
- Fontshare (Satoshi, General Sans, Cabinet Grotesk): free for commercial use under the ITF Free Font License but not on Google Fonts. Download and self-host.
- Commercial foundry fonts need a web license, often priced by pageviews. Never self-host a font file pulled from a design tool or OS without confirming the license.

## Checklist

1. Scale ratio fits the project; max 2 typefaces (3 with mono).
2. Body 16-18px, line-height 1.5-1.75, line length 45-75 characters.
3. `clamp()` for fluid sizing, with a `rem` term.
4. Negative letter-spacing on large headings, positive on uppercase.
5. Critical fonts preloaded, `font-display: swap`, system fallback with metric overrides.
6. `text-wrap: balance` on headings, `text-wrap: pretty` on paragraphs.

## Verifying

Render a type specimen with the real fonts: h1-h6, a body paragraph (about 3 lines at real width), caption, label, code, and a long unbroken heading. View it at 375px and 1280px wide. Check that fonts actually loaded (not fallback), each level is a clear step from the next, body line length is 45-75 characters, and no heading is wider than the viewport.

To write back to `.agents/design-context.md`, update only changed Typography fields (as full font stacks), show the diff and ask first.
