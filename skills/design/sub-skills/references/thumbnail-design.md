---
metadata:
  version: "1.0.0"
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: thumbnail-design
---

# Thumbnail Design

YouTube thumbnails, video/podcast/course covers, article headers, and Open Graph (link-preview) images, optimized for small-size readability and clicks. For feed posts see [social-media-graphic](social-media-graphic.md); for paid ads [ad-creative-design](ad-creative-design.md).

Tokens come from `.agents/design-context.md` (see [design-context](design-context.md)); with none, extend the project's existing CSS variables or Tailwind theme. Thumbnails favor readability and impact over strict brand rules, but brand colors build channel recognition.

## AI image path

Pipeline, references, text limits, review: [image-generation](image-generation.md). Prompt craft and overlay fallback: [graphic-design](graphic-design.md).

1. Generate at the ratio in the format table, then crop (for example 16:9 to 1280x720).
2. Real people: pass their photo as a reference and say "keep this person's face and identity unchanged". Do not invent likenesses of real people.
3. View at full size, then shrink to 168x94 and view again. Text must stay readable and the face expression visible. Fix one issue per follow-up turn.

Example prompts:

- YouTube: "Create a YouTube thumbnail (16:9). [subject] on the left side with [expression/pose]. Bold text '[title]' in [color] with dark outline on the right. [background style]. High contrast, readable at small size."
- Article header: "Create a landscape article header image. Abstract [color palette] gradient background. Title '[headline]' in bold white sans-serif, centered. Subtle geometric shapes. Clean, editorial feel."
- OG image: "Create a landscape Open Graph image for [brand/site]. Keep all text inside the central 80%. Logo top-left, title '[text]' large and centered, tagline below in lighter weight. [brand color] gradient background. Professional, shareable."

## Formats

| Format | Size | Ratio | Generate at | Notes |
|--------|------|-------|-------------|-------|
| YouTube thumbnail | 1280 x 720 | 16:9 | 16:9 | Min 640px wide; JPG/PNG under 2 MB; must read at 168x94 |
| YouTube Shorts cover | 1080 x 1920 | 9:16 | 9:16 | Shelf shows a center crop; keep text mid-frame |
| Article header / hero | 1200 x 630 | 1.91:1 | 16:9, crop | Blog header |
| OG image | 1200 x 630 | 1.91:1 | 16:9, crop | Link previews on FB, LinkedIn, Slack, X |
| X large-image card | 1200 x 628 | ~1.91:1 | 16:9, crop | X can crop toward 2:1; keep margins |
| Podcast cover | 3000 x 3000 | 1:1 | 1:1 (highest res) | Apple: 1400-3000px square, JPG/PNG, RGB |
| Course thumbnail | 1280 x 720 (Udemy min 750 x 422) | 16:9 | 16:9 | Udemy, Skillshare |
| Vimeo thumbnail | 1280 x 720 | 16:9 | 16:9 | Same as YouTube |

## Composition

- **3-second rule:** the topic must be clear at a glance.
- **Small-size readability:** thumbnails display as small as 168x94. Max 5-7 words; font size at least 60px at 1280x720 (~8px at sidebar size); bold or black weights only; always high contrast; no small details.
- **Three-element maximum:** (1) face or focal image, (2) bold text of 2-5 words, (3) one supporting element (icon, arrow, emoji, product). More is clutter.

## Click frameworks

### Curiosity gap

Show enough to intrigue, not enough to satisfy.

```text
- Left: expressive face (surprise, shock, excitement)
- Right: bold text with ONE missing piece
- Example: "I tried [PRODUCT] for 30 days..." with a shocked face
- Use "?" or "..." to open loops
```

### Before/after

```css
.before-after { display: grid; grid-template-columns: 1fr 1fr; height: 100%; position: relative; }
.before {
  background: #E5E7EB; /* muted, desaturated */
  filter: grayscale(30%);
  display: flex; align-items: center; justify-content: center;
}
.after {
  background: linear-gradient(135deg, var(--primary), var(--accent));
  display: flex; align-items: center; justify-content: center;
}
.divider-arrow {
  position: absolute; left: 50%; top: 50%;
  transform: translate(-50%, -50%);
  font-size: 64px; z-index: 10; /* large right-pointing arrow */
}
```

### Numbers/lists

"7 Tips", "$10K", "100 Days".

```text
- Giant number: 120-200px, bold, gradient or accent color
- Supporting text: 36-48px beside or below
- Background: clean gradient, not busy
- Optional topic icon
```

### Reaction/emotion

Expressive faces are the strongest thumbnail element. This is a widely held practice, not a measured guarantee.

```text
- Face: ~60% of frame, left or right
- Emotion: surprise, excitement, disbelief, joy
- 2-3 words of text on the opposite side
- Colored border or glow behind the face to separate it from the background
```

### Versus

```css
.versus { display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; height: 100%; }
.vs-badge {
  font-size: 72px; font-weight: 900; color: var(--accent);
  text-shadow: 0 0 30px rgba(var(--accent-rgb), 0.5); z-index: 2;
}
.side-a { background: linear-gradient(135deg, #1a1a2e, #16213e); }
.side-b { background: linear-gradient(135deg, #2d1b00, #462300); }
```

## Text treatment

Type fundamentals: [typography](typography.md).

```css
.thumb-text {
  font-family: 'Inter', 'Arial Black', sans-serif;
  font-size: 80px;
  font-weight: 900;
  color: #FFFFFF;
  text-transform: uppercase;
  line-height: 0.95;
  letter-spacing: -0.02em;

  /* Stroke plus shadow keeps text readable over any background */
  -webkit-text-stroke: 3px rgba(0, 0, 0, 0.8);
  paint-order: stroke fill;
  text-shadow: 4px 4px 0 rgba(0, 0, 0, 0.9), 0 0 20px rgba(0, 0, 0, 0.5);
}

.thumb-text .highlight { color: var(--accent); -webkit-text-stroke-color: rgba(0, 0, 0, 0.9); }
```

Text backgrounds:

```css
/* Solid pill */
.text-pill { display: inline-block; background: var(--primary); padding: 8px 24px; border-radius: 8px; font-weight: 800; font-size: 48px; }

/* Angled bar */
.text-bar { display: inline-block; background: var(--accent); padding: 8px 20px; transform: skewX(-5deg); }
.text-bar span { display: inline-block; transform: skewX(5deg); /* counter-skew keeps text straight */ }

/* Blurred backdrop */
.text-backdrop { background: rgba(0, 0, 0, 0.6); backdrop-filter: blur(8px); padding: 12px 24px; border-radius: 8px; }
```

## Faces and emoji

Face cutout with glow:

```css
.face-container { position: relative; z-index: 2; }
.face-container img {
  height: 100%;
  object-fit: contain;
  object-position: bottom;
  filter: drop-shadow(0 0 30px rgba(var(--primary-rgb), 0.6)); /* remove the background beforehand */
}
.face-container::before {
  content: '';
  position: absolute; width: 80%; height: 80%; top: 10%; left: 10%;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(var(--primary-rgb), 0.4), transparent 70%);
  z-index: -1;
}
```

With no face, use an oversized emoji as the anchor:

```css
.emoji-accent {
  font-size: 120px;
  position: absolute;
  transform: rotate(-10deg);
  filter: drop-shadow(4px 4px 0 rgba(0,0,0,0.3));
}
```

## Color

Associations are conventions, not rules. Palette theory: [color-palette](color-palette.md).

| Color | Association | Fits |
|-------|-------------|------|
| Red (#EF4444) | Urgency, excitement | Breaking news, warnings, hot takes |
| Yellow (#EAB308) | Attention, energy | Tips, positive content, highlights |
| Blue (#3B82F6) | Trust, calm | Tutorials, education, tech |
| Green (#22C55E) | Growth, money | Finance, results |
| Orange (#F97316) | Energy, warmth | Creative, DIY, food |
| Purple (#8B5CF6) | Premium, mystery | Luxury, deep dives |
| Black (#000000) | Power, sophistication | Dramatic reveals, premium |
| White (#FFFFFF) | Clean, modern | Minimalist channels |

Pairings that pop: yellow text on dark blue; white on deep red or purple; black on bright yellow; cyan accent on dark; red accent on charcoal.

## YouTube specifics

At ~168x94 in the sidebar, only bold high-contrast text reads, faces must be large enough to show expression, details vanish, and the color scheme must stand apart from neighbors.

YouTube overlays a duration badge bottom-right, a red watch-progress bar along the bottom edge on watched videos, and hover icons (Watch Later, queue) top-right. Keep critical content out of all three.

```css
/* Approximate duration-badge zone: avoid content here */
.youtube-safe { position: absolute; bottom: 0; right: 0; width: 120px; height: 40px; }
```

Channel consistency: one background color or gradient per series, same font treatment, a recurring layout (face left plus text right, or reverse), and a brand color as signature (border or text highlight).

## Article header and OG image

OG requirements:

- 1200 x 630; declare with `og:image:width` and `og:image:height`.
- Keep under 1 MB for fast loading (platform caps are higher, around 5-8 MB).
- Absolute HTTPS URL in `og:image`; `twitter:card` = `summary_large_image` for X.
- Text readable scaled to ~600x315.
- No text in the outer 10% margins.

```css
.article-header {
  width: 1200px; height: 630px; position: relative;
  display: flex; align-items: center; padding: 60px 80px;
  background: linear-gradient(135deg, #0F172A, #1E293B);
  overflow: hidden;
}
.article-header .title {
  font-family: var(--font-heading); font-size: 56px; font-weight: 800;
  color: #F8FAFC; line-height: 1.15; max-width: 700px; text-wrap: balance;
}
.article-header .meta {
  display: flex; align-items: center; gap: 12px; margin-top: 24px;
  font-size: 18px; color: rgba(248, 250, 252, 0.7);
}
.article-header .brand { position: absolute; bottom: 40px; right: 60px; font-size: 20px; font-weight: 700; color: var(--primary); }
.article-header::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 6px;
  background: linear-gradient(90deg, var(--primary), var(--accent));
}
```

## Code output

Self-contained HTML with a fixed-size canvas; set body margin 0 for export, render at the exact size, then run the same full-size and 168x94 checks as for AI output.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@700;800;900&display=swap" rel="stylesheet">
  <style>
    body { margin: 0; }
    .thumbnail {
      width: 1280px;
      height: 720px;
      position: relative;
      overflow: hidden;
      /* design styles */
    }
  </style>
</head>
<body>
  <div class="thumbnail">
    <!-- content -->
  </div>
</body>
</html>
```

## Quality checklist

- [ ] Viewed at full size and shrunk to 168x94: text spelled right and readable
- [ ] Max 5-7 words
- [ ] 3 or fewer visual elements
- [ ] High-contrast text (stroke plus shadow)
- [ ] Clear focal point that communicates the topic
- [ ] Bottom-right, bottom edge, and top-right clear (duration badge, progress bar, hover icons)
- [ ] Colors distinct from platform UI (avoid pure white and YouTube red)
- [ ] Consistent with other thumbnails in the series
- [ ] Emotional hook: face, number, or curiosity element
- [ ] Design-context colors and fonts applied where appropriate
