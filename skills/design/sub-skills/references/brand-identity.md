---
name: brand-identity
description: "Create or extend a brand identity through logos, color, typography, imagery, and production assets."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: brand-identity
---

# Brand Identity

A complete visual identity: logo mark and variations (SVG), color roles, fonts, patterns, favicons/app icons, avatars, and a guidelines page. For only a palette see [color-palette](color-palette.md); only fonts, [typography](typography.md); UI tokens and components, [design-system](design-system.md).

Read `DESIGN.md` for UI tokens and the project brand kit for approved brand primitives (see [design-context](design-context.md)); when absent, inspect the project's existing CSS variables or Tailwind theme. When refreshing an existing brand, change only what the user wants changed.

Start by defining the brand's industry, audience, and 3-5 personality adjectives. Generate full shade scales with [color-palette](color-palette.md); the `--brand-100` ... `--brand-500` variables below are that shared scale.

## Logo principles

1. **Simplicity:** recognizable at 16x16px. Strip every element that adds no meaning.
2. **Memorability:** one distinctive feature, not three.
3. **Scalability:** favicon to billboard; avoid thin strokes that vanish when small.
4. **Versatility:** works on light, dark, and photographic backgrounds.
5. **Timelessness:** avoid trends (current gradients, specific illustration styles); flat geometric forms endure.

### SVG and CSS techniques

Use simple geometric SVG marks (48x48 viewBox, rounded rect + inner shape). For CSS-only marks: `display: grid; place-items: center` on a colored rounded square, with an `::after` pseudo-element for the inner shape.

Ship final logos as SVG with text converted to paths or shapes; never depend on a web font or `<text>` inside a logo file. Image generation is useful for concept directions and moodboards, but it produces raster images with unreliable lettering: redraw the chosen direction as clean SVG. See [image-generation](image-generation.md).

## Logo variations

Every brand needs at least four forms:

1. **Primary (lockup):** icon + wordmark side by side (`flex`, `gap: 0.75rem`); icon 40px, wordmark in the heading font at 1.25rem/700.
2. **Secondary (stacked):** icon above wordmark (`flex-direction: column; text-align: center`).
3. **Icon mark:** symbol only, for favicons, app icons, avatars.
4. **Wordmark only:** text-only for inline use.

Responsive pattern: full logo by default; swap to icon-only at `max-width: 480px`.

## Color system

A brand color system is more than a palette.

| Role | Count | Purpose |
|------|-------|---------|
| Primary | 1 | Main brand color; CTAs, key UI |
| Secondary | 1 | Supporting, complementary accent |
| Neutral | 1 scale | Text, borders, backgrounds |
| Semantic | 4 | Success, warning, error, info |
| Surface | 2-3 | Background layers |

```css
:root {
  /* Brand */
  --color-primary: oklch(0.55 0.15 250);
  --color-primary-light: oklch(0.70 0.10 250);
  --color-primary-dark: oklch(0.40 0.15 250);

  --color-secondary: oklch(0.60 0.18 330);
  --color-secondary-light: oklch(0.75 0.12 330);

  /* Surfaces (semantic names shared with design-system) */
  --bg-primary: oklch(0.99 0.005 250);
  --bg-secondary: oklch(0.97 0.005 250);
  --bg-raised: oklch(1.00 0 0);

  /* Text */
  --text-primary: oklch(0.20 0.02 250);
  --text-secondary: oklch(0.50 0.01 250);  /* ~5.8:1 on bg-primary */
  --text-inverse: oklch(0.97 0.005 250);
}
```

Record approved brand colors in the brand kit using precise values and verify each text/background pair for contrast. Preserve the implemented UI color notation in `DESIGN.md`.

## Typography

| Personality | Font style | Examples |
|-------------|-----------|----------|
| Traditional | Serif | Playfair Display, Lora |
| Modern / clean | Neo-grotesque / geometric sans | Inter, DM Sans, Manrope |
| Friendly / warm | Rounded sans | Nunito, Quicksand |
| Technical | Monospace or grotesk | JetBrains Mono, Space Grotesk |
| Luxury | Thin serif/sans | Cormorant, Outfit |
| Playful | Display or handwritten | Bricolage Grotesque, Caveat |

```css
:root {
  --font-heading: 'Playfair Display', Georgia, 'Times New Roman', serif;
  --font-body: 'Inter', system-ui, -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace;
}
```

Always include system fallbacks, with the generic family last.

## Patterns and textures

```css
/* Dot grid */
.brand-pattern-dots {
  background-image: radial-gradient(circle, var(--brand-200) 1px, transparent 1px);
  background-size: 24px 24px;
}

/* Diagonal lines */
.brand-pattern-lines {
  background-image: repeating-linear-gradient(
    45deg, transparent, transparent 10px, var(--brand-100) 10px, var(--brand-100) 11px);
}

/* Grid */
.brand-pattern-grid {
  background-image:
    linear-gradient(var(--brand-100) 1px, transparent 1px),
    linear-gradient(90deg, var(--brand-100) 1px, transparent 1px);
  background-size: 32px 32px;
}

/* Noise texture */
.brand-texture { position: relative; }
.brand-texture::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.05'/%3E%3C/svg%3E");
  pointer-events: none;
}
```

## Clear space and minimum size

Clear zone equals the height of the logo mark (or a reference letter such as the "x" in the wordmark) on all sides.

```css
.logo-container { padding: var(--logo-clearzone, 2rem); }
.logo-primary { min-width: 120px; }   /* never render the full lockup smaller */
.logo-icon-mark { min-width: 24px; }  /* icon-only floor; favicons are the 16px exception */
```

Document these usage rules:

1. Do not rotate the logo.
2. Do not change colors outside the approved set.
3. Do not stretch or distort.
4. Do not place on busy backgrounds without a container.
5. Keep minimum clear space equal to the mark height.

## Guidelines document

Sections:

1. **Brand story:** mission, vision, values (one paragraph each).
2. **Logo:** all variations, clear zone, minimum sizes, misuse examples.
3. **Color:** primary, secondary, semantic palettes with hex/oklch/rgb.
4. **Typography:** families, scale, pairing rules.
5. **Imagery:** photography, illustration, icon style.
6. **Voice and tone:** writing guidelines.
7. **Patterns and textures:** background treatments.
8. **Application examples:** how it comes together.

Structure as semantic sections (`<section id="logo">`, `<section id="colors">`, ...) in a `<main class="brand-guide">`. Show logos in specimen blocks (light and dark variants, `display: grid; place-items: center; min-height: 200px`) and color swatches in an auto-fit grid (`minmax(160px, 1fr)`).

## Favicons and app icons

| Format | Size | Usage |
|--------|------|-------|
| ICO | 32x32 | Legacy browser tab |
| PNG | 180x180 | Apple touch icon (no transparency) |
| PNG | 192x192 | Android home screen |
| PNG | 512x512 | Android splash, PWA |
| SVG | any | Modern browsers, scalable |

```html
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png"><!-- 180x180, no transparency -->
<link rel="manifest" href="/site.webmanifest">
```

SVG favicon with dark-mode support:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <style>
    rect { fill: #4f46e5; }
    @media (prefers-color-scheme: dark) {
      rect { fill: #818cf8; }
    }
  </style>
  <rect width="32" height="32" rx="6"/>
  <!-- Letterform as a path, not <text>: fonts render differently per OS -->
  <path d="M11 8h6a4 4 0 0 1 0 8h-6zm0 8h7a4 4 0 0 1 0 8h-7z" fill="none" stroke="white" stroke-width="3" stroke-linejoin="round"/>
</svg>
```

Use the brand Primary hex (and Primary Light for dark mode) instead of the example colors. See [icon-design](icon-design.md).

```json
{
  "name": "Brand Name",
  "short_name": "Brand",
  "icons": [
    { "src": "/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icon-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ],
  "theme_color": "#4f46e5",
  "background_color": "#ffffff"
}
```

## Social avatars

1. Use the icon mark, not the full logo, for square/circular avatars.
2. Pad the mark so it never touches the circular crop.
3. Use the primary brand color as background.

```css
.social-avatar {
  width: 400px; height: 400px;
  background: var(--brand-500);
  display: grid; place-items: center;
  border-radius: 50%; /* preview of the circular crop */
}
.social-avatar .logo-mark { width: 55%; height: 55%; color: white; } /* ~22.5% padding per side */
```

| Platform | Upload size |
|----------|------------|
| X | 400x400 |
| LinkedIn | 400x400 |
| Instagram | 320x320 |
| GitHub | 500x500 |
| Slack | 512x512 |

## Applications

- **Business card:** 3.5x2in, flex column, `justify-content: space-between`. Name in the display font 14pt/700, title 9pt uppercase in brand color, contact 8pt gray.
- **Email signature:** table-based; logo mark (48px) with a brand-color `border-right`, name/title/contact stacked in the adjacent cell. Arial, inline styles only. See [email-design](email-design.md).

## Proof sheet

Render one sheet and view it before delivering: every logo variation on light, dark, and brand-color backgrounds; the icon mark at 16, 32, 48, and 180px; the favicon in a mock browser tab; the avatar inside a circle crop. Check that the mark is still recognizable at 16px, no strokes vanish, contrast holds on every background, and nothing touches the circular crop.

When the brand is final, record its identity and assets in the brand kit. Update affected UI tokens and rules in `DESIGN.md`, or document an intentional difference. Show the changes for review.

## Checklist

1. Define personality (3-5 adjectives).
2. Choose primary and secondary colors.
3. Select the font pairing.
4. Design the mark and all four variations.
5. Define clear zone and minimum sizes.
6. Generate the full color system (shades, semantics, neutrals).
7. Create patterns/textures.
8. Build favicons and app icons.
9. Create the social avatar.
10. Document everything in a guidelines page.
11. Render a proof sheet, inspect it, and save approved brand identity to the brand kit and affected UI rules to `DESIGN.md`.
