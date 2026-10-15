---
metadata:
  version: "1.0.0"
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: product-mockup
---

# Product Mockup

Presenting a product or UI itself. For a marketing graphic that merely includes a product, see [graphic-design](graphic-design.md), [social-media-graphic](social-media-graphic.md), or [ad-creative-design](ad-creative-design.md).

Tokens come from `.agents/design-context.md` (see [design-context](design-context.md)); with none, extend the project's existing CSS variables or Tailwind theme. Match the mockup's stage and background to the brand style.

## Choosing a path

- **AI image tool, for physical products:** product photo plus prompt gives a photoreal staged scene, packaging, or lifestyle shot.
- **HTML/CSS, for app and web screenshots:** image models redraw UI and alter text, icons, and layout, so wrap real screenshots in CSS device frames and render to PNG. For a photoreal device scene, generate the scene with a blank screen, then composite the real screenshot in code.

## AI path

Pipeline, references, ratios, review: [image-generation](image-generation.md). Prompt craft and text-overlay fallback: [graphic-design](graphic-design.md).

1. Pass the product photo as a reference and say "keep the product's shape, colors, label text, and logo exactly as in the reference".
2. Ratio: 1:1 or 4:5 for e-commerce and social; 16:9 or 3:2 for web heroes. Crop to exact pixels afterward.
3. Compare the output with the source photo: label text, logo, proportions, color, and part count must match. AI "improvements" to the product are defects. Fix one issue per follow-up turn.
4. Marketplace main images (for example Amazon) usually require a pure white #FFFFFF background, the product filling ~85% of the frame, and at least 1000px on the longest side (1600+ for zoom). Check the marketplace's current rules.

Example prompts:

- Product photo: "Place this [product] on a [background description]. Professional product photography style. [lighting]. [additional elements]."
- Device mockup: "Create a [device type] mockup showing [app/website screenshot]. [angle/perspective] view on a [surface/background]. Soft shadows, [lighting style]. Clean, realistic presentation."
- Packaging mockup: "Create a product packaging mockup for [brand]. [box/bottle/bag] with [label design description] on a [background]. Studio lighting, [additional props]. Premium, shelf-ready look."

## Mockup types

| Type | Best for | Technique |
|------|----------|-----------|
| Device frame | App/web screenshots | CSS device shells |
| Lifestyle/context | Product in environment | Background + shadows |
| 3D perspective | Dynamic presentation | CSS perspective/transform |
| Before/after | Transformations | Split comparison |
| Feature callout | Highlighting features | Lines + labels |
| Packaging | Physical boxes | CSS 3D box |
| Multi-device | Responsive showcase | Multiple frames |
| Screenshot frame | Clean screenshot display | Window chrome + shadow |

## Device frames

Fit screenshots by matching the screen's aspect ratio; never stretch them.

### Phone

```css
.phone-mockup {
  position: relative; width: 280px; height: 572px; background: #1a1a1a;
  border-radius: 40px; padding: 12px;
  box-shadow: 0 0 0 2px #333, 0 0 0 4px #1a1a1a, 0 20px 60px rgba(0,0,0,0.4);
}
.phone-mockup .screen { width: 100%; height: 100%; border-radius: 30px; overflow: hidden; background: #fff; position: relative; }
.phone-mockup .dynamic-island {
  position: absolute; top: 10px; left: 50%; transform: translateX(-50%);
  width: 100px; height: 28px; background: #000; border-radius: 20px; z-index: 10;
}
.phone-mockup .screen img { width: 100%; height: 100%; object-fit: cover; border-radius: 30px; }
```

### Laptop

```css
.laptop-mockup { position: relative; width: 680px; }
.laptop-screen { background: #222; border-radius: 12px 12px 0 0; padding: 16px 16px 0; position: relative; }
.laptop-screen .screen { width: 100%; aspect-ratio: 16/10; background: #fff; border-radius: 4px 4px 0 0; overflow: hidden; }
.laptop-screen::before { content: ''; position: absolute; top: 6px; left: 50%; transform: translateX(-50%); width: 6px; height: 6px; background: #444; border-radius: 50%; }
.laptop-base { height: 14px; background: linear-gradient(180deg, #ccc 0%, #aaa 100%); border-radius: 0 0 8px 8px; }
```

### Browser window

```css
.browser-mockup { width: 800px; border-radius: 8px; overflow: hidden; box-shadow: 0 20px 60px rgba(0,0,0,0.3); }
.browser-chrome { background: #E5E7EB; padding: 10px 16px; display: flex; align-items: center; gap: 8px; }
.browser-dots { display: flex; gap: 6px; }
.browser-dots span { width: 10px; height: 10px; border-radius: 50%; }
.browser-dots span:nth-child(1) { background: #EF4444; }
.browser-dots span:nth-child(2) { background: #F59E0B; }
.browser-dots span:nth-child(3) { background: #22C55E; }
.browser-url { flex: 1; background: #fff; border-radius: 4px; padding: 4px 12px; font-size: 12px; color: #666; }
.browser-content { background: #fff; width: 100%; aspect-ratio: 16/10; overflow: hidden; }
```

## 3D perspective

### Tilted view

```css
.tilt-container { perspective: 1200px; display: flex; justify-content: center; align-items: center; padding: 80px; }
.tilt-device { transform: rotateX(12deg) rotateY(-8deg) rotateZ(2deg); transform-style: preserve-3d; transition: transform 0.4s ease; }
.tilt-device:hover { transform: rotateX(5deg) rotateY(-3deg) rotateZ(0deg); }
```

### Floating

```css
.float-device {
  transform: rotateY(-15deg) rotateX(5deg) translateZ(20px);
  transform-style: preserve-3d; animation: gentleFloat 6s ease-in-out infinite;
}
@keyframes gentleFloat {
  0%, 100% { transform: rotateY(-15deg) rotateX(5deg) translateZ(20px) translateY(0); }
  50% { transform: rotateY(-15deg) rotateX(5deg) translateZ(20px) translateY(-12px); }
}
@media (prefers-reduced-motion: reduce) { .float-device { animation: none; } }
```

### Stacked multi-device

```css
.device-stack { position: relative; perspective: 1200px; width: 800px; height: 600px; }
.device-stack .phone  { position: absolute; right: 10%; bottom: 5%; z-index: 3; transform: rotateY(-5deg) translateZ(40px); }
.device-stack .laptop { position: absolute; left: 5%; top: 10%; z-index: 1; transform: rotateY(5deg); }
.device-stack .tablet { position: absolute; right: 25%; top: 5%; z-index: 2; transform: rotateY(-3deg) translateZ(20px) scale(0.8); }
```

### Fan layout

```css
.fan-layout { display: flex; align-items: flex-end; justify-content: center; perspective: 1500px; }
.fan-layout .screen:nth-child(1) { transform: rotateY(25deg) translateX(-30px); }
.fan-layout .screen:nth-child(2) { transform: rotateY(0deg) translateZ(30px); z-index: 2; }
.fan-layout .screen:nth-child(3) { transform: rotateY(-25deg) translateX(30px); }
```

## Stages and backgrounds

```css
/* Gradient stage */
.product-stage {
  display: flex; align-items: center; justify-content: center; min-height: 600px; padding: 80px;
  background: radial-gradient(ellipse at 50% 120%, rgba(var(--primary-rgb), 0.15) 0%, transparent 60%),
              linear-gradient(180deg, #0F172A 0%, #1E293B 100%);
}

/* Desk/surface scene */
.desk-scene {
  position: relative; background: linear-gradient(180deg, #F8FAFC 0%, #E2E8F0 100%);
  min-height: 600px; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 40px;
}
.desk-scene::before {
  content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 40%;
  background: linear-gradient(180deg, #E2E8F0, #CBD5E1);
}
.desk-scene .device { position: relative; z-index: 2; filter: drop-shadow(0 20px 40px rgba(0,0,0,0.15)); }
```

`--primary-rgb` is a space- or comma-separated channel triplet you define alongside the brand color (see [design-context](design-context.md)).

## Before/after

```css
/* Slider-style: .after is clipped to the left half */
.comparison { position: relative; width: 800px; aspect-ratio: 16/9; overflow: hidden; border-radius: 12px; box-shadow: 0 20px 60px rgba(0,0,0,0.2); }
.comparison .before, .comparison .after { position: absolute; inset: 0; }
.comparison .before { z-index: 1; filter: grayscale(50%) brightness(0.9); }
.comparison .after  { z-index: 2; clip-path: inset(0 50% 0 0); }
.comparison .divider { position: absolute; left: 50%; top: 0; bottom: 0; width: 3px; background: #fff; z-index: 3; }

/* Side-by-side */
.side-by-side { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; align-items: start; }
.side-by-side .label { font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 12px; }
```

## Feature callouts

```css
.feature-showcase { position: relative; display: flex; align-items: center; justify-content: center; padding: 80px; }
.callout { position: absolute; display: flex; align-items: center; gap: 8px; }
.callout .dot { width: 12px; height: 12px; border-radius: 50%; background: var(--accent); box-shadow: 0 0 0 4px rgba(var(--accent-rgb), 0.2); flex-shrink: 0; }
.callout .line { width: 60px; height: 1px; background: rgba(255,255,255,0.3); flex-shrink: 0; }
.callout .text { font-size: 13px; font-weight: 500; background: rgba(0,0,0,0.4); backdrop-filter: blur(8px); padding: 6px 12px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.1); white-space: nowrap; }

/* Numbered list */
.feature-list { display: flex; flex-direction: column; gap: 20px; }
.feature-item { display: flex; align-items: flex-start; gap: 16px; }
.feature-number { width: 32px; height: 32px; border-radius: 50%; background: var(--primary); color: #fff; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 700; flex-shrink: 0; }
```

## Packaging (3D box)

Wrap `.product-box` in a parent with `perspective: 1000px`. Box is 200w x 280h x 60d, centered on z=0.

```css
.product-box { width: 200px; height: 280px; position: relative; transform-style: preserve-3d; transform: rotateX(-12deg) rotateY(-25deg); /* negative X tilt shows the top face */ }
.box-front { position: absolute; width: 200px; height: 280px; background: var(--primary); transform: translateZ(30px); display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 24px; border-radius: 4px; }
.box-side { position: absolute; left: 0; top: 0; width: 60px; height: 280px; background: color-mix(in srgb, var(--primary) 80%, black); transform: rotateY(90deg) translateZ(170px); /* 170 = width - depth/2 */ }
.box-top { position: absolute; left: 0; top: 0; width: 200px; height: 60px; background: color-mix(in srgb, var(--primary) 90%, white); transform: rotateX(90deg) translateZ(30px); /* 30 = depth/2 */ }
```

## Screenshot presentation

```css
/* Clean window frame */
.screenshot-frame { border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.05), 0 20px 60px rgba(0,0,0,0.15); background: #fff; }
.screenshot-frame .chrome { height: 36px; background: linear-gradient(180deg, #F9FAFB, #F3F4F6); display: flex; align-items: center; padding: 0 12px; gap: 6px; border-bottom: 1px solid #E5E7EB; }
.screenshot-frame .chrome .dot { width: 10px; height: 10px; border-radius: 50%; background: #D1D5DB; }
.screenshot-frame img { width: 100%; display: block; }

/* Rotated collage */
.screenshot-collage { display: flex; padding: 40px; justify-content: center; }
.screenshot-collage .shot:nth-child(1) { transform: rotate(-5deg); z-index: 1; }
.screenshot-collage .shot:nth-child(2) { transform: rotate(0deg) translateY(-10px); z-index: 2; }
.screenshot-collage .shot:nth-child(3) { transform: rotate(5deg); z-index: 1; }
.screenshot-collage .shot { border-radius: 8px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.2); border: 4px solid #fff; }
```

## Quality checklist

- [ ] Frames realistic: proportions, shadows, details
- [ ] Shadows soft and directional, not uniform
- [ ] 3D transforms use sensible perspective depth
- [ ] Screenshot content visible, real, unaltered, and unstretched
- [ ] Stage uses brand colors
- [ ] Multiple devices scaled relative to each other
- [ ] Composition draws the eye to the product
- [ ] AI output compared against the source photo: label, logo, shape unchanged
- [ ] Code output rendered to PNG at exact size and viewed; self-contained HTML/CSS
