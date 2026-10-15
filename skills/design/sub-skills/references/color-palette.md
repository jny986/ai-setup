---
metadata:
  version: "1.0.0"
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: color-palette
---

# Color Palette

Accessible, production-ready color systems from any starting point: OKLCH shade scales, tinted neutrals, semantic colors, contrast, dark remaps, gradients, CSS and Tailwind output.

Tokens come from `.agents/design-context.md` (see [design-context](design-context.md)); with none, extend the project's existing CSS variables or Tailwind theme. If the context has a Color System, its hex values are the source of truth: extend, do not replace. Variable naming is defined in design-context; token layering in [design-system](design-system.md). Full dark themes (elevation, images, toggles): [dark-mode](dark-mode.md).

## Color theory

Generate in OKLCH. Its lightness channel is perceptually even, so a fixed L step looks the same at every hue (in HSL, yellow at `hsl(60 100% 50%)` is far lighter than blue at `hsl(240 100% 50%)`). Use HSL only if a legacy tool forces it. High-chroma OKLCH can fall outside sRGB: when converting to hex, reduce chroma and keep L and H.

| Harmony | Angles from base | Feel |
|---------|------------------|------|
| Complementary | 180 | High contrast, energetic |
| Analogous | +/-30 | Harmonious, natural |
| Triadic | 120, 240 | Vibrant, balanced |
| Split-complementary | 150, 210 | Contrast with less tension |
| Tetradic | 90, 180, 270 | Rich, needs careful balance |

```css
:root {
  --brand-hue: 250;
  --brand-chroma: 0.15;
  --brand-l: 0.55;

  --color-primary:     oklch(var(--brand-l) var(--brand-chroma) var(--brand-hue));
  --color-complement:  oklch(var(--brand-l) var(--brand-chroma) calc(var(--brand-hue) + 180));
  --color-analogous-1: oklch(var(--brand-l) var(--brand-chroma) calc(var(--brand-hue) + 30));
  --color-analogous-2: oklch(var(--brand-l) var(--brand-chroma) calc(var(--brand-hue) - 30));
  --color-triadic-1:   oklch(var(--brand-l) var(--brand-chroma) calc(var(--brand-hue) + 120));
  --color-triadic-2:   oklch(var(--brand-l) var(--brand-chroma) calc(var(--brand-hue) + 240));
}
```

## Shade scale (50-950)

Eleven steps: vary lightness, hold hue, reduce chroma slightly at the extremes.

| Token | L | Use |
|-------|---|-----|
| 50 | 0.97 | Tinted background |
| 100 | 0.93 | Hover background |
| 200 | 0.87 | Active background |
| 300 | 0.78 | Borders |
| 400 | 0.68 | Placeholder text |
| 500 | 0.55 | Base, primary actions |
| 600 | 0.48 | Hover on primary |
| 700 | 0.40 | Active on primary |
| 800 | 0.32 | Headings on light |
| 900 | 0.24 | Body text on light |
| 950 | 0.16 | High-contrast text |

```css
:root {
  --brand-hue: 250;
  --brand-chroma: 0.15;

  --brand-50:  oklch(0.97 calc(var(--brand-chroma) * 0.3) var(--brand-hue));
  --brand-100: oklch(0.93 calc(var(--brand-chroma) * 0.4) var(--brand-hue));
  --brand-200: oklch(0.87 calc(var(--brand-chroma) * 0.5) var(--brand-hue));
  --brand-300: oklch(0.78 calc(var(--brand-chroma) * 0.7) var(--brand-hue));
  --brand-400: oklch(0.68 calc(var(--brand-chroma) * 0.85) var(--brand-hue));
  --brand-500: oklch(0.55 var(--brand-chroma) var(--brand-hue));
  --brand-600: oklch(0.48 var(--brand-chroma) var(--brand-hue));
  --brand-700: oklch(0.40 var(--brand-chroma) var(--brand-hue));
  --brand-800: oklch(0.32 calc(var(--brand-chroma) * 0.9) var(--brand-hue));
  --brand-900: oklch(0.24 calc(var(--brand-chroma) * 0.8) var(--brand-hue));
  --brand-950: oklch(0.16 calc(var(--brand-chroma) * 0.7) var(--brand-hue));
}
```

## Semantic colors

| Role | Hue | Note |
|------|-----|------|
| Success | 145 | Green |
| Warning | 85 | Amber |
| Error | 25 | Red |
| Info | 230 | Blue |

```css
:root {
  --success-50:  oklch(0.97 0.04 145);
  --success-400: oklch(0.68 0.15 145);  /* dark-mode foreground */
  --success-500: oklch(0.55 0.16 145);
  --success-700: oklch(0.40 0.14 145);

  --warning-50:  oklch(0.97 0.04 85);
  --warning-400: oklch(0.72 0.15 85);
  --warning-500: oklch(0.60 0.16 85);   /* about 4:1 on white: dark text ON it; 700 for warning TEXT */
  --warning-700: oklch(0.45 0.14 85);

  --error-50:  oklch(0.97 0.04 25);
  --error-400: oklch(0.68 0.16 25);
  --error-500: oklch(0.55 0.18 25);
  --error-700: oklch(0.40 0.16 25);

  --info-50:  oklch(0.97 0.04 230);
  --info-400: oklch(0.68 0.12 230);
  --info-500: oklch(0.55 0.14 230);
  --info-700: oklch(0.40 0.12 230);
}
```

Generate a full 50-950 scale for a semantic hue only when needed (alerts, badges, charts); 50/400/500/700 covers most UI.

## Neutral scale

Tint neutrals slightly with the brand hue.

```css
:root {
  --neutral-hue: var(--brand-hue);
  --neutral-chroma: 0.01;

  --gray-50:  oklch(0.98 var(--neutral-chroma) var(--neutral-hue));
  --gray-100: oklch(0.96 var(--neutral-chroma) var(--neutral-hue));
  --gray-200: oklch(0.90 var(--neutral-chroma) var(--neutral-hue));
  --gray-300: oklch(0.83 var(--neutral-chroma) var(--neutral-hue));
  --gray-400: oklch(0.71 var(--neutral-chroma) var(--neutral-hue));
  --gray-500: oklch(0.55 var(--neutral-chroma) var(--neutral-hue));
  --gray-600: oklch(0.45 var(--neutral-chroma) var(--neutral-hue));
  --gray-700: oklch(0.37 var(--neutral-chroma) var(--neutral-hue));
  --gray-800: oklch(0.27 var(--neutral-chroma) var(--neutral-hue));
  --gray-900: oklch(0.20 var(--neutral-chroma) var(--neutral-hue));
  --gray-950: oklch(0.13 var(--neutral-chroma) var(--neutral-hue));
}
```

## WCAG 2.2 contrast

| Level | Normal text | Large text (24px+, or 18.66px+ bold) | Non-text UI (icons, borders, focus rings, chart marks) |
|-------|-------------|------------------------------------|-------------------------------------------------------|
| AA | 4.5:1 | 3:1 | 3:1 against adjacent colors (SC 1.4.11) |
| AAA | 7:1 | 4.5:1 | none |

Ratio = `(L1 + 0.05) / (L2 + 0.05)` with L1 the lighter and L2 the darker relative luminance (`0.2126 R + 0.7152 G + 0.0722 B` on linearized sRGB). Do not round up: 4.49:1 fails. APCA (Lc) is a draft candidate for WCAG 3: a useful second opinion, especially in dark mode, never the compliance standard.

Rules:

- Body text on light: 900 or 950. On dark: 50 or 100.
- Primary buttons: white on 500+ usually passes (L 0.55 blue is about 4.9:1), but yellows, ambers and cyans at L 0.55-0.65 often fail. Use dark text on those. Always measure.
- Disabled: 400 on light. Exempt from WCAG but keep distinguishable.
- Links: distinguish from surrounding text by more than color. Underline, or give 3:1 against surrounding text plus a non-color cue on hover and focus.

Lightness shortcut for near-neutrals: relative luminance is roughly L cubed, so 4.5:1 needs an L gap of about 0.42-0.45 or more (more mid-range). Use it to pick candidates, then measure.

```text
text L 0.20 | bg L 0.97 | gap 0.77 -> ~16.6:1, passes AAA
text L 0.55 | bg L 0.97 | gap 0.42 -> ~4.5:1, borderline AA; safe for large text
text L 0.57 | bg L 0.97 | gap 0.40 -> ~4.1:1, fails AA for normal text
```

Measure on sRGB hex, not by eye: contexts store hex while browsers render OKLCH. Use any WCAG contrast calculator. Compute each step's contrast on white and black, mark it AA (4.5:1), large/UI (3:1) or fail, and for failures propose the nearest passing shade (same hue and chroma, adjusted lightness). Also check every real pairing you ship (text on `--bg-*`, button label on `--interactive-*`, dark-mode pairs), not only white and black.

## Dark mode remap

Do not invert the scale. Remap semantic tokens (same names as the light layer):

```css
[data-theme="dark"] {
  --bg-primary:   var(--gray-950);
  --bg-secondary: var(--gray-900);
  --bg-tertiary:  var(--gray-800);

  --text-primary:   var(--gray-50);
  --text-secondary: var(--gray-300);
  --text-tertiary:  var(--gray-400);

  --surface:       var(--gray-900);
  --surface-hover: var(--gray-800);

  --border-default: var(--gray-700);

  --interactive-primary: var(--brand-400);

  --color-success: var(--success-400);
  --color-warning: var(--warning-400);
  --color-error:   var(--error-400);
}
```

- Reduce contrast slightly: gray-50 on gray-950, not pure white on pure black.
- Reduce chroma slightly: saturated colors glow on dark.
- Elevation uses lighter surfaces, the opposite of light-mode shadows.

## Color by industry

| Industry | Primary colors | Why |
|----------|----------------|-----|
| Finance | Navy, dark blue, green | Trust, stability, growth |
| Health | Blue, teal, white | Calm, cleanliness |
| Food | Red, orange, yellow | Appetite, warmth |
| Tech / SaaS | Blue, violet, cyan | Reliability, innovation |
| Luxury | Black, gold, deep purple | Elegance, exclusivity |
| Eco | Green, earth tones | Nature, sustainability |
| Education | Blue, orange, green | Trust, enthusiasm |
| Creative | Bold primaries, neons | Energy, expression |

These are conventions to start from, not rules.

## Gradients

- Under 60 degrees of hue rotation: subtle. 90-180 degrees: vibrant.
- Writing stops in `oklch()` does not make the gradient interpolate in OKLCH. Without a hint, browsers use Oklab for modern colors and sRGB for hex, rgb and hsl stops; both cut straight through the color space and can pass through gray between distant hues. Add `in oklch` (and `longer hue` for rainbow sweeps).
- Alternatively add a mid stop with a slight chroma boost to avoid the gray dead zone.

```css
.gradient-subtle {
  background: linear-gradient(135deg in oklch, oklch(0.55 0.15 250), oklch(0.55 0.15 280));
}

.gradient-vibrant {
  background: linear-gradient(
    135deg in oklch,
    oklch(0.65 0.20 280),
    oklch(0.60 0.22 330),
    oklch(0.65 0.20 20)
  );
}

.gradient-mesh {
  background:
    radial-gradient(at 0% 0%, oklch(0.70 0.15 280) 0%, transparent 50%),
    radial-gradient(at 100% 0%, oklch(0.70 0.15 200) 0%, transparent 50%),
    radial-gradient(at 100% 100%, oklch(0.70 0.15 330) 0%, transparent 50%),
    oklch(0.97 0.01 250);
}
```

## Tailwind output

Tailwind v4 (CSS-first): put the scale in `@theme`; it generates `bg-brand-500`, `text-brand-900`, etc.

```css
@import "tailwindcss";
@theme {
  --color-brand-50:  oklch(0.97 0.045 250);
  --color-brand-500: oklch(0.55 0.15 250);
  --color-brand-900: oklch(0.24 0.12 250);
  /* every step 50-950, plus success/warning/error/info */
}
```

Tailwind v3:

```js
// tailwind.config.js
const brand = {
  50:  'oklch(0.97 0.045 250)',
  100: 'oklch(0.93 0.06 250)',
  200: 'oklch(0.87 0.075 250)',
  300: 'oklch(0.78 0.105 250)',
  400: 'oklch(0.68 0.1275 250)',
  500: 'oklch(0.55 0.15 250)',
  600: 'oklch(0.48 0.15 250)',
  700: 'oklch(0.40 0.15 250)',
  800: 'oklch(0.32 0.135 250)',
  900: 'oklch(0.24 0.12 250)',
  950: 'oklch(0.16 0.105 250)',
};

module.exports = {
  theme: {
    extend: {
      colors: {
        brand,
        success: { /* same pattern, hue 145 */ },
        warning: { /* same pattern, hue 85 */ },
        error:   { /* same pattern, hue 25 */ },
        info:    { /* same pattern, hue 230 */ },
      },
    },
  },
};
```

## Token layering

Primitives (`--brand-*`, `--gray-*`, status scales) feed semantic tokens, which feed components. Dark mode and theming remap only the semantic layer. Full layering: [design-system](design-system.md).

```css
:root {
  --color-primary:       var(--brand-500);
  --interactive-primary: var(--brand-500);
  --color-error:         var(--error-500);
  --bg-primary:          var(--gray-50);
  --text-primary:        var(--gray-900);
  --border-default:      var(--gray-200);
}

.btn-primary {
  background: var(--interactive-primary);
  color: white; /* verify >= 4.5:1 against brand-500 */
}
```

## Verifying and saving

Render a swatch sheet (HTML) showing each scale as labeled swatches (token, hex, contrast on white and black) plus sample text and button pairings in light and dark. View it at actual size. Check that steps are evenly spaced, none is muddy or neon, and neutrals read as neutral.

To write back to `.agents/design-context.md`, update only changed Color System rows, show a before/after diff and ask first. Mapping:

| Context role | Take from |
|--------------|-----------|
| Primary | `--brand-500` (600 if 500 fails 4.5:1 with white text) |
| Primary Light / Dark | `--brand-400` / `--brand-700` |
| Secondary / Accent | 500 step of that hue |
| Neutral 50 / 100 / 200 / 500 / 800 / 900 | matching `--gray-*` |
| Success / Warning / Error | `--success-500` / `--warning-500` / `--error-500` (text uses 700) |

## Palette from a single hex

1. Convert the brand hex to OKLCH and take its hue.
2. Generate 50-950 with the lightness map.
3. Generate tinted neutrals and pick semantic hues.
4. Measure contrast and fix failures.
5. Build the dark remap.
6. Export CSS variables or Tailwind config, then render the swatch sheet.
