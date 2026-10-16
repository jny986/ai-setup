---
name: image-treatment
description: "Apply image treatments and responsive delivery through filters, masks, overlays, cropping, and export workflows."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: image-treatment
---

# Image Treatment

Treat existing images in code: filters, blend modes, duotone, masks, overlays, collages, SVG filters, responsive delivery. To create new images see [image-generation](image-generation.md). For treatments that must be baked into the file (social images, email, OG images), apply them in an image editor or script instead of CSS.

Read `DESIGN.md` for UI tokens and the project brand kit for approved brand primitives (see [design-context](design-context.md)); when absent, inspect the project's existing CSS variables or Tailwind theme. Duotone and overlay colors should come from the color system. Examples use `--brand-*` variables. Identify the mood first: editorial, product, marketing, artistic.

## CSS filters

| Filter | Range | Effect |
|--------|-------|--------|
| brightness() | 0-2+ | Darken (< 1) or lighten (> 1) |
| contrast() | 0-2+ | Reduce (< 1) or boost (> 1) |
| saturate() | 0-3+ | Desaturate (0) or vivid (> 1) |
| grayscale() | 0-1 | Remove color |
| sepia() | 0-1 | Warm vintage tone |
| hue-rotate() | 0-360deg | Shift all hues |
| blur() | 0-20px+ | Gaussian blur |

Presets:

```css
.filter-vintage  { filter: sepia(0.3) contrast(1.1) brightness(1.05) saturate(0.9); }
.filter-cool     { filter: saturate(0.85) contrast(1.1) brightness(1.02) hue-rotate(-10deg); }
.filter-bw       { filter: grayscale(1) contrast(1.4) brightness(1.05); }
.filter-dreamy   { filter: brightness(1.1) contrast(0.9) saturate(1.2) blur(0.5px); }
.filter-faded    { filter: contrast(0.85) brightness(1.1) saturate(0.7); }
.filter-moody    { filter: brightness(0.85) contrast(1.2) saturate(0.8); }
.filter-vivid    { filter: contrast(1.15) saturate(1.4) brightness(1.02); }
```

Hover reveal:

```css
.image-card img { filter: grayscale(0.8) brightness(0.9); transition: filter 0.4s ease; }
.image-card:hover img { filter: grayscale(0) brightness(1); }
```

## Blend modes

| Mode | Effect | Use |
|------|--------|-----|
| multiply | Darkens (white disappears) | Color tints, knocking out white backgrounds |
| screen | Lightens (black disappears) | Glow effects |
| overlay | Boosts contrast | Color overlays |
| soft-light | Subtle overlay | Gentle tinting |
| color | Applies hue/saturation, keeps luminosity | Tinting photos |
| luminosity | Brightness from the layer, hue/saturation from below | Recoloring textures |

```css
.image-container { position: relative; }
.image-container::after {
  content: ''; position: absolute; inset: 0;
  background: var(--brand-500); mix-blend-mode: multiply; opacity: 0.6;
}
```

## Duotone

Maps lights to one color and darks to another.

### CSS-only

Grayscale image multiplied onto the highlight color (white to highlight, black to black), then the shadow color lightens the darks. The highlight must be lighter than the shadow in every RGB channel.

```css
.duotone { position: relative; isolation: isolate; background: #e2b94c; /* highlight */ }
.duotone img { display: block; width: 100%; filter: grayscale(1) contrast(1.2); mix-blend-mode: multiply; }
.duotone::after {
  content: ''; position: absolute; inset: 0; pointer-events: none;
  background: #1a1a2e; /* shadow */ mix-blend-mode: lighten;
}
```

### SVG filter (exact mapping, any element)

`tableValues` are each channel of shadow to highlight in 0-1 (hex / 255): `#1a1a2e` to `#e2b94c`.

```html
<svg width="0" height="0" aria-hidden="true" style="position:absolute">
  <filter id="duotone-gold" color-interpolation-filters="sRGB">
    <feColorMatrix type="matrix" values="0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0 0 0 1 0"/>
    <feComponentTransfer>
      <feFuncR type="table" tableValues="0.102 0.886"/>
      <feFuncG type="table" tableValues="0.102 0.725"/>
      <feFuncB type="table" tableValues="0.180 0.298"/>
    </feComponentTransfer>
  </filter>
</svg>
<img src="photo.jpg" alt="..." style="filter: url(#duotone-gold)">
```

### Pairs

| Shadow | Highlight | Feel |
|--------|-----------|------|
| #1a1a2e | #e2b94c | Luxury, gold on navy |
| #0d1b2a | #3498db | Tech, cool blue |
| #2d1b4e | #ff6b6b | Creative, bold |
| #1b3a2a | #a7f3d0 | Natural, green |

## Masking

```css
.clip-circle   { clip-path: circle(50%); }
.clip-rounded  { clip-path: inset(0 round 1rem); }
.clip-diagonal { clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%); }
.clip-hexagon  { clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); }

/* Gradient fades */
.image-fade-bottom {
  mask-image: linear-gradient(to bottom, black 60%, transparent 100%);
  -webkit-mask-image: linear-gradient(to bottom, black 60%, transparent 100%);
}
.image-vignette {
  mask-image: radial-gradient(ellipse 70% 70% at center, black 50%, transparent 100%);
  -webkit-mask-image: radial-gradient(ellipse 70% 70% at center, black 50%, transparent 100%);
}
```

Text-shaped mask:

```css
.image-text-mask {
  background-image: url('photo.jpg'); background-size: cover;
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text; font-size: 8rem; font-weight: 900;
  color: transparent; /* fallback if background-clip: text is unsupported */
}
```

Display-size decorative text only. The photo under the letters must give 3:1 contrast with the page background, and the element keeps real text for screen readers.

## Background images

```css
.hero-bg { background: url('hero.jpg') center/cover no-repeat; min-height: 80vh; }

.parallax-section {
  background: url('bg.jpg') center/cover no-repeat;
  background-attachment: fixed;
  min-height: 60vh;
}
@media (hover: none), (prefers-reduced-motion: reduce) {
  .parallax-section { background-attachment: scroll; } /* iOS ignores fixed; parallax can trigger vestibular issues */
}

/* Layered: overlay, pattern, photo */
.layered-bg {
  background:
    linear-gradient(to bottom, rgba(0,0,0,0.4), rgba(0,0,0,0.7)),
    url('pattern.svg') repeat center / 64px 64px,
    url('photo.jpg') no-repeat center / cover;
}
```

## Overlays

Gradient overlay for text legibility:

```css
.image-overlay-gradient { position: relative; }
.image-overlay-gradient::after {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.3) 40%, transparent 100%);
}
.image-overlay-gradient .content { position: relative; z-index: 1; color: white; }
```

Text over images must meet WCAG contrast (4.5:1, or 3:1 for >=24px / >=18.66px bold) against the lightest pixels behind it. Check the region under the text in the rendered result, not the image average; strengthen the overlay until it passes.

Hover reveal:

```css
.card-image { position: relative; overflow: hidden; }
.card-image .overlay {
  position: absolute; inset: 0;
  background: rgb(0 0 0 / 0.85); /* or oklch(from var(--brand-500) l c h / 0.85) where relative color syntax is supported */
  display: grid; place-items: center; opacity: 0; transition: opacity 0.3s ease;
}
.card-image:hover .overlay, .card-image:focus-within .overlay { opacity: 1; }
```

## Grids and collages

```css
/* Masonry-style: columns flow top-to-bottom, so reading order runs down each column */
.image-grid-masonry { columns: 3; column-gap: 1rem; }
.image-grid-masonry img { display: block; width: 100%; margin-bottom: 1rem; border-radius: 0.5rem; break-inside: avoid; }
@media (max-width: 768px) { .image-grid-masonry { columns: 2; } }
@media (max-width: 480px) { .image-grid-masonry { columns: 1; } }

/* Grid collage */
.image-collage {
  display: grid; grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(3, 200px); gap: 0.5rem;
}
.image-collage img:nth-child(1) { grid-column: 1 / 3; grid-row: 1 / 3; }
.image-collage img { width: 100%; height: 100%; object-fit: cover; border-radius: 0.5rem; }
```

## Responsive delivery

### Resolution switching

`w` descriptors list each file's real pixel width; `sizes` says how wide the image is displayed so the browser can choose before layout. Without `sizes` it assumes `100vw`.

```html
<img src="card-800.jpg"
     srcset="card-400.jpg 400w, card-800.jpg 800w, card-1200.jpg 1200w, card-1600.jpg 1600w"
     sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 400px"
     alt="Team reviewing designs at a whiteboard" width="800" height="600"
     loading="lazy" decoding="async">
```

### Art direction and formats

Browsers take the first matching `<source>`: order by media query, then by format (AVIF before WebP). `width` and `height` on `<source>` handle a different aspect ratio per breakpoint.

```html
<picture>
  <source media="(max-width: 640px)" type="image/avif"
          srcset="hero-mobile-640.avif 640w, hero-mobile-1280.avif 1280w" sizes="100vw" width="1280" height="1600">
  <source media="(max-width: 640px)" type="image/webp"
          srcset="hero-mobile-640.webp 640w, hero-mobile-1280.webp 1280w" sizes="100vw" width="1280" height="1600">
  <source type="image/avif" srcset="hero-1600.avif 1600w, hero-2400.avif 2400w" sizes="100vw">
  <source type="image/webp" srcset="hero-1600.webp 1600w, hero-2400.webp 2400w" sizes="100vw">
  <img src="hero-1600.jpg" alt="Describe what the hero shows" width="1600" height="900"
       fetchpriority="high" decoding="async">
</picture>
```

Rules:

1. Always set `width` and `height` (intrinsic aspect ratio) to prevent layout shift; CSS can still make it fluid with `width: 100%; height: auto`.
2. `loading="lazy"` for below-the-fold images. Never lazy-load the LCP/hero image: leave it eager and add `fetchpriority="high"`.
3. `decoding="async"` so decode does not block rendering.
4. Formats: AVIF, then WebP, then JPEG fallback in `<img src>`. PNG/SVG only for transparency or sharp edges. Start at quality ~50-65 for AVIF, ~75-80 for WebP.
5. `alt` states the image's purpose; decorative images use `alt=""`.

### Variants

Export each hero at 640, 1280, 1600, and 2400px wide in WebP (quality ~78), AVIF (~55), and JPEG (~82, progressive), from the highest-resolution source, with any image tool.

## SVG filters and effects

```css
/* Frosted glass */
.frosted-glass { backdrop-filter: blur(12px) saturate(180%); background: rgba(255,255,255,0.7); }
@supports not (backdrop-filter: blur(1px)) { .frosted-glass { background: rgba(255,255,255,0.92); } } /* keep text readable */

/* Shape-following shadow */
.shaped-shadow { filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2)); }
```

Noise/grain (apply with `.grain { filter: url(#noise); }`):

```html
<svg width="0" height="0" aria-hidden="true" style="position:absolute">
  <filter id="noise">
    <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/>
    <feColorMatrix type="saturate" values="0"/>
    <feBlend in="SourceGraphic" mode="multiply"/>
  </filter>
</svg>
```

## Object-fit

| Value | Behavior |
|-------|----------|
| cover | Fills container, crops excess (most common) |
| contain | Fits entirely, may leave empty space |
| fill | Stretches (distorts) |
| scale-down | Like contain, never scales up |

```css
.card-image { width: 100%; height: 200px; object-fit: cover; object-position: center; }
.portrait   { object-fit: cover; object-position: center top; }
.thumbnail  { aspect-ratio: 1; object-fit: cover; border-radius: 0.75rem; }
```

## Review

Render at desktop, mobile (375px wide), and dark mode, and view each. Check:

- [ ] Faces and products not cropped by `object-fit` or `clip-path` at any width
- [ ] Text over images passes contrast at its worst spot
- [ ] Duotone and filters look on-brand, not muddy
- [ ] Nothing breaks where a blend mode or filter is unsupported
- [ ] The intended `srcset` candidate loads (`img.currentSrc`) and the hero is not lazy-loaded
- [ ] `background-attachment: fixed` disabled on touch devices
