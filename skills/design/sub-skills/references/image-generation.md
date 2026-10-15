---
metadata:
  version: "1.0.0"
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: image-generation
---

# Image Generation

Tool-agnostic craft for AI-generated images: prompts, references, refinement, aspect ratios, text limits, review. Other graphics references ([graphic-design](graphic-design.md), [social-media-graphic](social-media-graphic.md), [thumbnail-design](thumbnail-design.md), [product-mockup](product-mockup.md), [poster-design](poster-design.md), [ad-creative-design](ad-creative-design.md), [banner-design](banner-design.md), [infographic](infographic.md)) add format rules on top of this and link here instead of repeating it.

Tokens come from `.agents/design-context.md` (see [design-context](design-context.md)); with none, extend the project's existing CSS variables or Tailwind theme. Pull hex colors, style archetype, and type description into the prompt. Say when output is not brand-matched.

## Generation modes

| Mode | Use when | Input |
|------|----------|-------|
| Text-to-image | Creating from scratch: posters, graphics, illustrations | Prompt |
| Image edit | Product shots, mockups, style transfer, adding elements | Reference image + prompt |
| Multi-turn | Iterative refinement, variations | Chat/session with history |
| Batch | Large sets (social sets, ad variants) | Many prompts, one shared style block |

## Prompt structure

```text
[FORMAT] + [SUBJECT] + [STYLE] + [COMPOSITION] + [COLOR] + [TYPOGRAPHY] + [MOOD] + [EXCLUDE]
```

Example, product social post:

> Create a square social media graphic for a premium headphone launch.
> The headphones are centered on a deep navy (#0d1b2a) to electric blue (#00b4d8) diagonal gradient background.
> Bold white sans-serif text "HEAR EVERYTHING" spans the top third.
> Small coral (#ff6b6b) subtext "Available March 20" below.
> Subtle geometric triangles in the background at 10% opacity.
> Clean, modern, premium feel. No borders, no clip art.

Principles:

1. Describe scenes, not keywords: "A sneaker floating above a reflective surface with dramatic side lighting" beats "sneaker, cool, modern".
2. Give hex codes for every brand color.
3. Describe spatial layout: "headline in upper third, product centered, CTA lower right".
4. Name the style: flat vector, 3D render, watercolor, photorealistic, minimalist Swiss.
5. Give type instructions: style, size relationship, color, position.
6. State exclusions: no watermarks, no beveled effects, no clip art.
7. Never put pixel sizes in the prompt and expect them honored; set the aspect ratio (below).

### Style cues

| Style | Prompt additions |
|-------|-----------------|
| Minimalist | generous whitespace, single accent color, clean sans-serif, no decorative elements |
| Bold/Vibrant | saturated colors, large impactful typography, geometric shapes, high contrast |
| Luxurious | dark background, gold or champagne accents, serif typography, subtle texture |
| Playful | bright palette, rounded shapes, hand-drawn feel, casual handwriting font |
| Corporate | structured grid, blue tones, clean hierarchy, balanced composition |
| Retro | halftone dots, muted vintage palette, serif headlines, film grain |
| Brutalist | raw, high-contrast black and white, unconventional layout, oversized type |

## Reference images

- Pass logos, product photos, faces, and style references as images instead of describing them; tools reproduce references far more faithfully than descriptions.
- Say what to preserve: "keep the product's shape, colors, label text, and logo exactly as in the reference".
- Label each reference's role when passing several: product, logo, style reference.
- Reference limits vary by tool; check before sending a large set.
- Do not invent likenesses of real people. With a real person's photo, say "keep this person's face and identity unchanged".

Edit example, product photo to graphic:

> Transform this product photo into a premium social media graphic. Place the product on a gradient background (#1a1a2e to #16213e). Add bold white headline "JUST DROPPED" above and price "$299" in coral (#e94560) below. Keep the product exactly as in the photo. Modern, clean, high-end. Square format.

## Multi-turn refinement

- Change one thing per turn and say what must stay: "Keep the layout and text exactly as is. Make the background warmer, sunset tones."
- Text fix: `Change "EVERYTHNG" to "EVERYTHING". Change nothing else.`
- Later turns drift: if the image degrades after 3-4 turns, restart with a consolidated prompt and the best version as a reference.
- Keep every version; compare against the previous one.

## Aspect ratios and exact sizes

Tools output a fixed set of ratios (commonly 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9, some also 4:1 and 8:1); check the tool's list. For any other target (300x250, 1200x628, A4):

1. Generate at the nearest supported ratio, at the highest resolution offered (2K for screen, 4K for print or large placements).
2. Center-crop and resize to exact pixels in any image editor or script.
3. Tell the model to keep text and key subjects inside the area that survives the crop ("keep all text within the central 80%").
4. Generate extreme ratios (8:1, 1:4) natively; cropping a square master to them keeps too little.
5. For several sizes from one master, crop each with a focal point so the subject stays in frame, then view each export.

| Use case | Ratio | Final size | Notes |
|----------|-------|-----------|-------|
| Instagram feed portrait | 4:5 | 1080x1350 | Grid preview crops to a 3:4 center |
| Instagram feed square | 1:1 | 1080x1080 | Keep text ~100px from edges |
| Story / Reels / TikTok | 9:16 | 1080x1920 | Safe zones in [social-media-graphic](social-media-graphic.md) |
| X post | 16:9 | 1600x900 | Text must read at small preview size |
| LinkedIn post | 1:1 or 4:5 | 1200x1200 / 1080x1350 | Link previews ~1.91:1 (1200x627): generate 16:9 and crop |
| Facebook / Open Graph link image | 16:9, crop | 1200x630 | |
| Pinterest pin | 2:3 | 1000x1500 | |
| YouTube thumbnail | 16:9 | 1280x720 | Must read at 168x94; avoid bottom-right |
| Leaderboard banner | 8:1 | 728x90 | Minimal text, strong CTA |
| Medium rectangle ad | 5:4, crop | 300x250 | |
| Poster / flyer | 2:3 or 3:4 | print size | Bleed and DPI in [poster-design](poster-design.md) |

## Text rendering limits

Text is the most common failure.

- Put exact copy in double quotes: `headline "HEAR EVERYTHING"`.
- Keep rendered text to a headline, a subline, and a CTA. Put paragraphs, legal copy, and prices that change in an HTML/CSS overlay.
- Spell out unusual words and brand names; say "spelled exactly as written".
- Models cannot see platform UI: state safe zones in the prompt.
- Small text, numbers, charts, and logos come out wrong most often. Prefer a code overlay or a real logo file composited in code.
- After two failed text fixes, regenerate with "no text, leave the upper third clear" and add the copy in code (see [graphic-design](graphic-design.md)).

## Review checklist

View every generated file at full size and at the size it will be seen (thumbnail, feed card). Never deliver an unviewed image.

- [ ] Text legible and spelled exactly as briefed
- [ ] Colors match the brand context
- [ ] One clear focal point and visual hierarchy
- [ ] Sufficient text/background contrast
- [ ] No artifacts, extra fingers, warped logos, or distorted products
- [ ] Aspect ratio and exact pixel size match the placement
- [ ] Reference product/logo/face unchanged versus the source
- [ ] Style matches the brief

If a check fails, refine one change per turn. Report which checks were verified and any compromise (for example, "text added as overlay after repeated misspellings"). Some tools embed an invisible provenance watermark in output; disclose AI generation where a platform or client requires it.
