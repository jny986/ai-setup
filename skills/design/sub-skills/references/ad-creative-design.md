---
metadata:
  version: "1.0.0"
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: ad-creative-design
---

# Ad Creative Design

Paid creative: IAB display banners, Google Display/Performance Max assets, and paid social ads. Output is an image cropped to exact size, or HTML/CSS (optionally animated) when copy must be pixel-sharp at small sizes. Organic posts: [social-media-graphic](social-media-graphic.md). On-site and email banners: [banner-design](banner-design.md).

Tokens come from `.agents/design-context.md` (see [design-context](design-context.md)); with none, extend the project's existing CSS variables or Tailwind theme. Ads are often the first brand touchpoint: stay strictly on-brand.

## Image-generation path

Prompt craft, cropping, and text-overlay fallback: [image-generation](image-generation.md).

1. IAB sizes are not generator ratios. Generate at the nearest ratio from the size table, then crop/resize to exact size (for example 5:4 then 300x250).
2. **Small formats (728x90, 320x50, 160x600, 300x250):** downscaled AI text blurs and misspells. Generate the visual only ("no text"), set headline + CTA in HTML/CSS over it, and render at exact size. For multi-size sets, generate one master per ratio family and crop from it.
3. View every output at 100%: check spelling, offer details (prices, percentages, dates), CTA legibility, logo fidelity. Fix one issue per follow-up.

### Example prompts

- **Display:** "Create a [square/wide/tall] display ad. [product/service] visual on [background]. Headline '[text]' in [style]. CTA button '[action]' in [color]. Clean, conversion-focused layout."
- **Social:** "Create a square feed ad. [product] photo centered on [background color]. Short headline '[value prop]' above. CTA '[action]' button at bottom in [brand color]. Minimal text, bold imagery."
- **Retargeting leaderboard:** "Create an ultra-wide leaderboard ad background (8:1), no text; leave the center clear for copy." Then overlay in code: logo left, offer headline center, CTA pill right in the accent color.

## Sizes

### IAB display

| Name | Dimensions | Generate at, then crop |
|------|-----------|------------------------|
| Medium Rectangle | 300 x 250 | 5:4 |
| Large Rectangle | 336 x 280 | 5:4 |
| Leaderboard | 728 x 90 | 8:1 |
| Mobile Leaderboard | 320 x 50 | 8:1 |
| Large Mobile | 320 x 100 | 4:1 |
| Wide Skyscraper | 160 x 600 | 1:4 |
| Half Page | 300 x 600 | 9:16 |
| Billboard | 970 x 250 | 4:1 |
| Large Leaderboard | 970 x 90 | 8:1 |
| Square | 250 x 250 | 1:1 |

Export static ads at 2x (for example 600x500 for 300x250) only if the ad server accepts high-DPI assets; otherwise deliver exact size under the file-size cap.

### Social and platform

| Platform | Format | Dimensions |
|----------|--------|-----------|
| Meta feed | Single image | 1080 x 1350 (4:5, best on mobile) or 1080 x 1080 |
| Meta Stories/Reels | Full screen | 1080 x 1920 (9:16) |
| Google Responsive Display / PMax | Asset set | Landscape 1200 x 628, square 1200 x 1200, portrait 960 x 1200; logos 1200 x 1200 and 1200 x 300; 5MB max each |
| LinkedIn | Sponsored content | 1200 x 627 or 1080 x 1080 |
| X | Promoted | 1200 x 675 or 1080 x 1080 |

## Content hierarchy

Space is limited, so prioritize ruthlessly. Order: Attention (visual hook), Interest (value proposition), Desire (benefit), Action (CTA).

| Format | Elements, in priority order |
|--------|-----------------------------|
| Large (300x600, 970x250, 300x250) | Logo (small, top-left or top-center); hero visual; headline (5-8 words); optional one-line support; CTA |
| Medium (728x90, 320x100) | Logo (left, compact); headline (3-5 words); CTA (right). No room for support text or large visuals |
| Small (320x50, narrow 160x600 areas) | Logo or brand name as text; headline (2-4 words); CTA (text link or small button) |

### Copy limits

| Size | Headline | Body | CTA |
|------|----------|------|-----|
| 300x250 | 8 words | 12 words | 3 words |
| 728x90 | 5 words | none | 2 words |
| 160x600 | 6 words | 10 words | 2 words |
| 300x600 | 8 words | 15 words | 3 words |
| 320x50 | 4 words | none | 2 words |

### Headline formulas

1. Benefit-first: "Save 3 Hours Every Week"
2. Problem-solution: "Tired of [Problem]? Try [Product]"
3. Social proof: "Join 50,000+ [Users] Who..."
4. Urgency: "Last Day: 40% Off Everything"
5. Curiosity: "The [Tool] Top Companies Use for [Result]"
6. Numbers: "3x Faster [Task] Starting Today"

Only use claims (counts, multipliers) the advertiser can substantiate.

## CTA

The CTA is the most important element and must be unmissable.

Styles: **solid** (high-contrast fill + shadow), **outline** (transparent + border), **pill** (rounded + arrow). Properties: `padding: 10-12px 24-28px`, `font-weight: 700`, uppercase, hover `translateY(-1px)` with stronger shadow or background swap; pill uses `border-radius: 50px` with an `::after` arrow.

| Weak | Strong | Why |
|------|--------|-----|
| Submit | Get Started | Action-oriented |
| Click Here | Shop the Sale | Specific benefit |
| Learn More | See How It Works | Curiosity |
| Buy Now | Claim Your 20% Off | Value |
| Sign Up | Start Free Trial | Low commitment |
| Download | Get Your Free Guide | Ownership |

Placement: 300x250 bottom-center or bottom-right; 728x90 right, vertically centered; 160x600 bottom-center; 320x50 right. Keep at least 8px padding around the CTA; it should take 15-25% of ad width.

## Layouts by size

- **300x250:** flex column. Logo top (12px padding), visual (`flex: 1`), content bottom (16px padding, centered). Headline 18px/700.
- **728x90:** flex row, `align-items: center`, 20px gap. Logo left (28px high), headline (`flex: 1`, 20px/700), CTA right.
- **160x600:** flex column, centered text. Logo top, visual middle (`flex: 1`), headline 16px/700, body 12px, CTA bottom (`margin-top: auto`).
- **320x50:** flex row on brand-color bg. Text (`flex: 1`, 13px/700 white), CTA right (white bg, brand-color text, `6px 14px` padding).

Container for all sizes:

```css
.ad {
  position: relative;
  overflow: hidden;
  box-sizing: border-box; /* keeps the ad at exact IAB size */
  border: 1px solid #CCCCCC; /* required when the background is white or very light */
  border-radius: 0;
}
.ad .click-area { position: absolute; inset: 0; z-index: 100; cursor: pointer; }
```

## A/B variations

Produce at least two variations: version A is the primary design; version B changes one variable.

| Axis | A | B |
|------|---|---|
| Headline | Benefit-focused | Urgency-focused |
| CTA color | Brand primary | High-contrast accent |
| CTA copy | "Get Started" | "Try Free" |
| Layout | Image top, text bottom | Text left, image right |
| Background | Light/white | Dark/brand color |
| Visual | Product screenshot | Abstract/lifestyle |

Label each variation:

```html
<!-- VARIATION A: Benefit headline, primary CTA -->
<div class="ad variation-a">...</div>

<!-- VARIATION B: Urgency headline, accent CTA -->
<div class="ad variation-b">...</div>
```

## Platform requirements

Verify against the platform's current specs before delivery; these change.

### Google Display Network

- Max 150KB for static uploaded images and zipped HTML5 bundles.
- Animation stops within 30 seconds total, loops included.
- White or very light backgrounds need a visible border.
- HTML5 ads need `<meta name="ad.size" content="width=300,height=250">` in `<head>`.
- Click area covers the whole ad. No auto-playing audio.
- Responsive Display/PMax: avoid logos and text baked into images (Google overlays headlines); supply clean imagery.

### Meta

- The 20% text rule was retired in 2020 and is not enforced; still keep image text short, since the headline and primary text fields carry the copy.
- Primary text truncates near 125 characters; headline near 40.
- 9:16 safe zones (1080x1920): Stories keep text and logos out of the top and bottom ~14% (250px); Reels top ~14% and bottom ~35% (670px), ~6% from the sides.
- Square (1:1) and vertical (4:5) suit mobile feeds.

### LinkedIn

- Professional tone, no clickbait. Company logo visible.
- The platform skews blue; use a contrasting accent to stand out.

### Programmatic display

- Degrade gracefully (backup static image); load assets from relative paths or data URIs.
- Implement a click tag:

```html
<script>
var clickTag = "https://example.com";
</script>
<a href="javascript:void(window.open(window.clickTag))" style="position:absolute;inset:0;z-index:999;"></a>
<!-- Parent .ad must be position: relative. The ad server replaces clickTag; never hard-code a tracking URL. -->
```

## HTML5 animation

- **Staggered entry:** `fadeSlideIn` (opacity 0 to 1, translateY 10px to 0) with 0.2s delays for logo, visual, headline, CTA. Add a subtle `ctaPulse` (scale 1 to 1.03) after entry.
- **Multi-frame rotation:** frames absolutely positioned, shared `@keyframes frame` with opacity in/out, staggered by total duration / frame count. Max 3 frames over 10-15s.

Rules: 30s total including loops (for example a 10s sequence x 3); end on a static frame showing headline + CTA + logo; no fast flashing (accessibility). See [motion-design](motion-design.md).

## Checklist

- [ ] Dimensions exactly match the target size
- [ ] Output viewed at 100%: copy, prices, CTA spelled right and legible
- [ ] Hierarchy: visual > headline > CTA; CTA clearly clickable
- [ ] Copy within the limits above
- [ ] Brand colors and fonts applied
- [ ] Visible border on white/light display ads
- [ ] File size under the platform cap (aim under 150KB)
- [ ] Animation ends on a static frame with visible CTA
- [ ] At least 2 variations for A/B testing
- [ ] No text below 10px
- [ ] Contrast 4.5:1 normal text; 3:1 large text (24px+, or 18.66px+ bold) and CTA against its surroundings
