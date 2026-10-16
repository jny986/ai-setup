---
name: graphic-design
description: "Compose graphics using purposeful hierarchy, typography, color, imagery, and delivery constraints."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: graphic-design
---

# Graphic Design

Core guidance for one-off visuals. Two output paths: AI image generation (default for social posts, posters, ads, rich visuals) or HTML/CSS/SVG code (editable, animated, or long/exact copy). Format-specific rules live in [social-media-graphic](social-media-graphic.md), [poster-design](poster-design.md), [thumbnail-design](thumbnail-design.md), [ad-creative-design](ad-creative-design.md), [banner-design](banner-design.md), [product-mockup](product-mockup.md), and [infographic](infographic.md).

Read `DESIGN.md` for UI tokens and the project brand kit for approved brand primitives (see [design-context](design-context.md)); when absent, inspect the project's existing CSS variables or Tailwind theme. Extract primary, secondary, accent colors, heading and body fonts, and style archetype.

## Brief analysis

| Intent | Approach | Key elements |
|--------|----------|--------------|
| Promotional | Bold, attention-grabbing | Large headline, CTA, product image |
| Informational | Clear hierarchy, readable | Structured content, icons, data |
| Emotional | Mood-driven, atmospheric | Photography, color mood, minimal text |
| Celebratory | Energetic, festive | Dynamic shapes, bright colors, confetti |
| Announcement | Clean, authoritative | Date/details prominent |
| Brand awareness | On-brand, memorable | Logo prominent, brand colors dominant |

Collect: headline, supporting text, product image or focal visual, CTA, brand elements, dimensions.

### Product image analysis

1. Extract 3-5 dominant colors.
2. Locate the subject and the negative space.
3. Judge mood: warm/cool, energetic/calm, luxurious/casual.
4. Pick a color strategy: harmonious (reuse image colors), contrasting (complements make it pop), or monochromatic (desaturate plus a brand-color overlay).

## AI image path

Use unless the output must be editable HTML, animated, or carry long/exact copy. Pipeline, reference images, aspect ratios, text limits, and the review checklist: [image-generation](image-generation.md). This section is the design layer.

Prompt template:

```text
Create a [style] [format] for [purpose].
Scene: [foreground, background, how elements are arranged]
Colors: [navy blue #1a2b4a background with coral #ff6b6b accents]
Typography: [large bold sans-serif headline "[TEXT]" in white, upper third]
Mood: [energetic, calm, professional, playful]
Exclude: [no borders, no clip art, no extra text]
```

With a product image, pass it as a reference:

> Place this product on a bold gradient background (#1a2b4a to #ff6b6b). Keep the product, its label and logo exactly as in the photo. Add a large headline "NEW ARRIVAL" in white bold sans-serif at the top. Add geometric accent shapes.

For non-native sizes, generate at the nearest ratio and crop to exact pixels, keeping text inside the central 80% (see [image-generation](image-generation.md)).

### Text-overlay fallback

After two failed text fixes, regenerate with no text and the upper third clear, then overlay the copy in code and render at exact size:

```html
<style>body{margin:0}</style>
<div class="canvas" style="width:1200px;height:628px;position:relative;background:url('visual.png') center/cover;">
  <h1 class="headline" style="position:absolute;left:64px;top:56px;max-width:60%;color:#fff;">NEW ARRIVAL</h1>
</div>
```

Render at exact canvas size (2x for retina), wait for web fonts, and confirm no text is clipped by the canvas. View the result.

## Composition

### Rule of thirds

Divide the canvas into a 3x3 grid. Put key elements on the four line intersections (33%/67%), not the center cell.

```css
/* Focal point on the upper-left intersection */
.focal-point {
  position: absolute;
  left: 33.33%;
  top: 33.33%;
  transform: translate(-50%, -50%);
}
```

### Golden ratio (1:1.618)

Size related elements by it: 48px headline, ~30px subheadline (48 / 1.618); 600px main area, ~370px accent area.

### Focal hierarchy

One primary focal point (largest, highest contrast), then secondary elements (medium), then tertiary details such as fine print, logos, decoration (smallest, lowest contrast).

### Reading patterns

- Z-pattern for text-light graphics: top-left, top-right, diagonal to bottom-left, bottom-right.
- F-pattern for information-dense layouts: scan across the top, then shorter lines lower down.

More layout theory: [layout-composition](layout-composition.md).

## Color

Start from the approved brand palette, or `DESIGN.md` when creating UI-adjacent graphics. Apply 60-30-10: 60% dominant, 30% secondary, 10% accent. Pair a primary with its complement for maximum contrast. Palette building: [color-palette](color-palette.md).

### Gradients

```css
/* Multi-stop */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Mesh-style (stacked radials) */
background:
  radial-gradient(at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
  radial-gradient(at 80% 20%, rgba(255, 119, 115, 0.3) 0%, transparent 50%),
  radial-gradient(at 50% 50%, rgb(76, 29, 149) 0%, rgb(15, 23, 42) 100%);

/* Conic */
background: conic-gradient(from 45deg, #12c2e9, #c471ed, #f64f59, #12c2e9);

/* Animated (web only) */
background: linear-gradient(270deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
background-size: 400% 400%;
animation: gradientShift 8s ease infinite;

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
```

### Color overlay on images

```css
.image-with-overlay { position: relative; }
.image-with-overlay::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.7), rgba(124, 58, 237, 0.7));
  mix-blend-mode: multiply;
}
```

More overlay and blend recipes: [image-treatment](image-treatment.md).

## Typography

Full guidance: [typography](typography.md).

```css
/* Display headline */
.headline {
  font-family: var(--font-heading);
  font-size: clamp(2.5rem, 8cqw, 5rem); /* cqw = % of .canvas width, not the viewport */
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -0.02em;
  text-wrap: balance;
}

/* Subheadline */
.subheadline {
  font-family: var(--font-body);
  font-size: clamp(1rem, 2.5cqw, 1.5rem);
  font-weight: 400;
  line-height: 1.4;
  opacity: 0.85;
}

/* Detail text: dates, fine print */
.detail {
  font-family: var(--font-body);
  font-size: 0.875rem;
  font-weight: 500;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}
```

Text effects:

- Gradient text: `background: linear-gradient(...)` + `background-clip: text` + `-webkit-text-fill-color: transparent`.
- Outlined text: `-webkit-text-stroke: 2px currentColor` + `-webkit-text-fill-color: transparent`.
- Glow: multi-layer `text-shadow` with rising blur and falling opacity.
- Depth: stacked 1px-offset `text-shadow` layers in progressively darker shades.

## Code output path

Self-contained HTML with embedded CSS, fixed-size canvas, layered structure. Render to PNG at exact size and view it before delivering.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=[HeadingFont]:wght@700;800&family=[BodyFont]:wght@400;500&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

    .canvas {
      width: [WIDTH]px;
      height: [HEIGHT]px;
      position: relative;
      overflow: hidden;
      container-type: inline-size; /* enables cqw units inside */
    }

    .background-layer { /* gradients, patterns, images */ }
    .content-layer { /* text, CTAs, key elements */ }
    .decoration-layer { /* shapes, accents, overlays */ }
  </style>
</head>
<body>
  <div class="canvas">
    <div class="background-layer">...</div>
    <div class="content-layer">...</div>
    <div class="decoration-layer">...</div>
  </div>
</body>
</html>
```

### Advanced CSS

```css
/* clip-path shapes */
.diagonal { clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%); }
.circle-reveal { clip-path: circle(40% at 50% 50%); }
.wave-bottom { clip-path: path('M0,200 C150,250 350,150 500,200 L500,0 L0,0 Z'); }

/* Glassmorphism */
.glass {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 16px;
}

/* Blend modes for image integration (or multiply, screen, soft-light) */
.image-overlay {
  background-image: url('product.jpg');
  background-size: cover;
  background-blend-mode: overlay;
  background-color: rgba(37, 99, 235, 0.5);
}
```

- SVG filters: inline `<svg>` with `<filter>` for noise (`feTurbulence` + `feColorMatrix` + `feBlend multiply`) and glow (`feGaussianBlur` + `feMerge`).
- Floating circles: absolutely positioned radial gradient with `filter: blur(40px)`.
- Grid/dot patterns: `linear-gradient` or `radial-gradient` background at low opacity, small `background-size`.
- Animation (web only): float (`translateY` 0 to -10px and back, 4s ease-in-out infinite), pulse glow (`box-shadow` intensity, 2-3s), shimmer (200% gradient, animate `background-position`).

## Style frameworks

Code-path starting points; for AI generation, translate the same cues into the prompt (style cues in [image-generation](image-generation.md)).

```css
/* Minimalist: single accent, whitespace, max 2 colors + neutrals */
.minimalist-canvas { background: #FAFAFA; padding: 60px; }
.minimalist-canvas .headline { font-size: 3rem; font-weight: 300; color: #171717; letter-spacing: -0.03em; }

/* Bold/Vibrant: saturated gradients, oversized type */
.bold-canvas { background: linear-gradient(135deg, #FF6B6B, #FFE66D); }
.bold-canvas .headline { font-size: 5rem; font-weight: 900; text-transform: uppercase; letter-spacing: -0.04em; }

/* Luxurious: dark ground, gold accents, serif */
.luxury-canvas { background: #0A0A0A; color: #F5F0E8; }
.luxury-canvas .headline { font-family: 'Playfair Display', serif; font-size: 3.5rem; font-weight: 400; letter-spacing: 0.05em; }
.luxury-canvas .accent { color: #D4AF37; border: 1px solid rgba(212, 175, 55, 0.3); }

/* Playful: bright colors, rounded shapes */
.playful-canvas { background: #FFF8F0; border-radius: 24px; }
.playful-canvas .headline { font-family: 'Fredoka', sans-serif; font-size: 3rem; color: #E03E3E; transform: rotate(-2deg); }

/* Corporate: blue/gray, structured grid */
.corporate-canvas { background: #FFFFFF; font-family: 'Inter', sans-serif; }
.corporate-canvas .headline { font-size: 2.5rem; font-weight: 700; color: #1E3A5F; }

/* Retro: warm palette #C84B31 #2D1B00 #F4E8C1 #ECDBBA, SVG halftone, distressed texture */
.retro-canvas { background: #F4E8C1; color: #2D1B00; }
.retro-canvas .headline { font-family: 'Playfair Display', serif; font-size: 4rem; font-weight: 900; }

/* Brutalist: B&W, raw borders, monospace, visible grid */
.brutalist-canvas { background: #FFFFFF; border: 4px solid #000000; }
.brutalist-canvas .headline {
  font-family: 'Space Mono', monospace; font-size: 4rem; font-weight: 700; text-transform: uppercase;
  color: #FFFFFF; mix-blend-mode: difference; /* white + difference = black on white, inverts over black blocks */
}
```

## Quality checklist

- [ ] Colors match the approved brand or UI palette
- [ ] Specified fonts used (loaded if web fonts)
- [ ] Clear hierarchy: the eye knows where to look first
- [ ] Contrast meets WCAG 2.x: 4.5:1 normal text, 3:1 large text (>=24px, or >=18.66px bold) and UI shapes such as CTA buttons
- [ ] Spacing not cramped; dimensions match the request
- [ ] Generated images: viewed, every word checked, cropped to exact pixels
- [ ] Code output: self-contained (fonts excepted), rendered and viewed
- [ ] Decoration enhances rather than distracts; style matches the archetype
- [ ] All copy accurate

## Tips

1. Get the background mood right before adding content.
2. Shapes at 0.05-0.15 opacity add depth without distraction.
3. Layer semi-transparent gradients for rich backgrounds.
4. Max 3 colors plus neutrals.
5. Headline at least 3x body size.
6. Whitespace is design.
7. Test at actual size, 100%.
8. Define colors once as CSS custom properties.
