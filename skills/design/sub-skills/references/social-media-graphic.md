---
metadata:
  version: "1.0.0"
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: social-media-graphic
---

# Social Media Graphic

Organic feed graphics (posts, stories, carousels, covers) sized for Instagram, X, LinkedIn, Facebook, Pinterest, TikTok, with platform safe zones. For paid ads see [ad-creative-design](ad-creative-design.md); for website/email banners [banner-design](banner-design.md); for YouTube thumbnails and OG images [thumbnail-design](thumbnail-design.md).

Tokens come from `.agents/design-context.md` (see [design-context](design-context.md)); with none, extend the project's existing CSS variables or Tailwind theme. Social graphics must be strongly on-brand: consistency builds recognition.

Default output is an AI-generated image cropped to exact platform pixels. Use HTML/CSS for multi-slide carousels with shared templates or copy-heavy posts.

## AI image path

Pipeline, references, text limits, review: [image-generation](image-generation.md). Prompt craft and overlay fallback: [graphic-design](graphic-design.md).

1. Generate at the ratio in the table below; crop to exact pixels.
2. State the safe zone in the prompt ("keep all text in the middle 70% vertically"); the model cannot see platform UI.
3. View the output: spelling, legibility at phone-feed size, safe zones. Fix one issue per follow-up turn.

| Target | Generate at | Crop to |
|--------|-------------|---------|
| IG/FB/LinkedIn square | 1:1 | 1080x1080 |
| IG/FB/LinkedIn portrait | 4:5 | 1080x1350 |
| IG feed 3:4 | 3:4 | 1080x1440 |
| Story / Reel / TikTok cover | 9:16 | 1080x1920 |
| X in-feed | 16:9 | 1200x675 |
| Link card / FB / LinkedIn landscape (1.91:1) | 16:9 | 1200x628 |
| X header (3:1) | 21:9 | 1500x500 |
| LinkedIn personal banner | 4:1 | 1584x396 |
| LinkedIn company cover (~5.9:1) | 8:1 | 1128x191 |
| Facebook page cover | 21:9 | 1640x624 (2x of 820x312) |
| Pinterest pin | 2:3 | 1000x1500 |

Example prompts:

- Instagram post: "Create a square Instagram post graphic for [brand]. [product] centered on [color] gradient. Bold [font-style] text '[headline]'. Clean, modern aesthetic."
- Instagram story: "Create a vertical story graphic for [brand]. [product/subject] as the focal point with [color scheme] background. Text '[headline]' in the upper-middle, CTA '[action]' above the lower fifth; leave the top and bottom 15% free of text. Trendy, editorial style."
- LinkedIn post: "Create a professional landscape LinkedIn post graphic for [brand]. [topic/statistic] visualized with [chart type or icon]. Headline '[text]' in [font-style]. Corporate blue tones, clean data-driven layout."

## Platform dimensions

Platform specs change; confirm against current platform docs.

### Instagram

| Format | Size | Ratio | Use |
|--------|------|-------|-----|
| Feed square | 1080 x 1080 | 1:1 | Standard |
| Feed portrait | 1080 x 1350 | 4:5 | Maximum feed real estate |
| Feed 3:4 | 1080 x 1440 | 3:4 | Matches the 3:4 profile grid (since 2025) |
| Feed landscape | 1080 x 566 | 1.91:1 | Panoramic |
| Story / Reel cover | 1080 x 1920 | 9:16 | Full-screen vertical |
| Carousel slide | 1080 x 1080 or 1080 x 1350 | 1:1 / 4:5 | All slides use the first slide's ratio |
| Profile picture | 320 x 320 | 1:1 | Circular crop |

### X

| Format | Size | Ratio | Use |
|--------|------|-------|-----|
| In-feed image | 1200 x 675 | 16:9 | Standard |
| Header | 1500 x 500 | 3:1 | Profile header |
| Card image | 1200 x 628 | 1.91:1 | Link preview |

### LinkedIn

| Format | Size | Ratio | Use |
|--------|------|-------|-----|
| Feed post | 1200 x 627 | 1.91:1 | Standard |
| Feed square | 1200 x 1200 | 1:1 | Square |
| Feed portrait | 1080 x 1350 | 4:5 | More mobile real estate |
| Personal banner | 1584 x 396 | 4:1 | Profile background |
| Company cover | 1128 x 191 | ~5.9:1 | Company page |
| Article/newsletter cover | 1920 x 1080 | 16:9 | Article header |

### Facebook

| Format | Size | Ratio | Use |
|--------|------|-------|-----|
| Feed post | 1080 x 1350 or 1200 x 630 | 4:5 / 1.91:1 | 4:5 wins on mobile; 1.91:1 for link shares |
| Cover photo | 820 x 312 (upload 1640 x 624) | 2.63:1 | Mobile shows a 640 x 360 crop |
| Event cover | 1920 x 1005 | 1.91:1 | Event banner |
| Story | 1080 x 1920 | 9:16 | Story |

### Pinterest

| Format | Size | Ratio | Use |
|--------|------|-------|-----|
| Standard pin | 1000 x 1500 | 2:3 | Optimal engagement |
| Long pin | 1000 x 2100 | 1:2.1 | Feed crops pins taller than 2:3; put the hook in the top 1500px |
| Square pin | 1000 x 1000 | 1:1 | Alternative |

### TikTok

| Format | Size | Ratio | Use |
|--------|------|-------|-----|
| Video cover | 1080 x 1920 | 9:16 | Profile grid shows a ~3:4 center crop |

## Safe zones

UI overlaps content on every platform. Keep critical text and visuals inside these zones.

Instagram feed post (1080 x 1080 / 1080 x 1350):

```text
Safe zone: 60px padding on all sides
Profile grid shows a 3:4 center crop: on 1:1 keep key content in the central 810px width;
on 4:5 the grid trims ~34px from each side
```

Instagram / Facebook story (1080 x 1920):

```text
Top safe: 250px (~14%: progress bar, profile, close)
Bottom safe: 250px (~14%: reply bar, CTA sticker)
Left/right safe: 60px
Content zone: 960w x 1420h centered
```

Reels / TikTok cover (1080 x 1920):

```text
Top: ~220px clear   Bottom: ~420px clear (caption, audio, CTA)
Right: ~130px clear (like/comment/share rail)
Keep the headline in the center band; it also survives the 3:4 grid crop
```

X (1200 x 675):

```text
Safe zone: 40px padding all sides
Center text; edges may crop on mobile
Key content in center 1120 x 595
```

LinkedIn (1200 x 627):

```text
Safe zone: 50px padding all sides
Avoid bottom-left: engagement buttons overlap
Center the main message
```

Facebook cover (820 x 312):

```text
Desktop shows 820 x 312; mobile shows full height but crops the sides (~555px of 820 visible)
Mobile safe zone: center ~555 x 312
Profile photo can overlap the bottom-left; keep text centered
```

Pinterest pin (1000 x 1500):

```text
Keep ~80px clear top and bottom (Save button and icons overlay the corners)
Logo/branding: small, bottom-center or top-left
Headline readable at ~236px feed width
```

## Platform style

- **Instagram:** clean editorial layouts, generous whitespace; muted palette plus one pop color; consistent carousel templates; sans-serif; photo-forward with text on 60-80% opacity backgrounds; 12-16px radius on inner elements.
- **X:** bold, high-contrast (dark mode common); large text, viewed small; data visualizations and charts perform well; minimal decoration.
- **LinkedIn:** professional; blue tones blend in; clean data and insights; headshot plus quote for thought leadership; subtle gradients.
- **Facebook:** warm, approachable; photo-centric with overlay text; event and community layouts; covers work with little or no text (the old 20% text rule was retired in 2020); authentic over polished in groups.
- **Pinterest:** vertical; text over lifestyle imagery; step-by-step and numbered list pins; warm aspirational palettes; bold text readable small.
- **TikTok:** bold, energetic, trend-driven; high contrast for small screens; casual type; the cover must convey the content in under 1 second.

## Templates

### Quote post (Instagram 1080x1080)

```html
<div class="canvas" style="width:1080px;height:1080px;position:relative;overflow:hidden;
  background:linear-gradient(135deg, var(--primary), var(--secondary));
  display:flex;align-items:center;justify-content:center;padding:80px;">

  <div style="text-align:center;">
    <div style="font-size:72px;line-height:1.1;margin-bottom:8px;opacity:0.3;
      font-family:Georgia,serif;">"</div>
    <p style="font-family:var(--font-heading);font-size:42px;font-weight:700;
      color:#fff;line-height:1.3;text-wrap:balance;">
      The quote text goes here, keep it under 120 characters for readability.
    </p>
    <div style="margin-top:40px;display:flex;align-items:center;justify-content:center;gap:12px;">
      <div style="width:40px;height:2px;background:rgba(255,255,255,0.5);"></div>
      <span style="font-family:var(--font-body);font-size:18px;color:rgba(255,255,255,0.8);
        text-transform:uppercase;letter-spacing:0.1em;">Author Name</span>
      <div style="width:40px;height:2px;background:rgba(255,255,255,0.5);"></div>
    </div>
  </div>
</div>
```

### Announcement (LinkedIn 1200x627)

```text
- Left 60%: headline (bold, 48px) + body (20px) + CTA badge
- Right 40%: visual (icon, illustration, or abstract shape)
- Top bar: brand-color accent line (4px)
- Bottom: logo + URL, small
- Background: white or very light neutral
```

### Tip carousel (Instagram 1080x1080)

```text
Slide 1 (cover):
- Bold headline: "5 Tips for [Topic]"
- Subtext: "Swipe to learn more"
- Gradient or image background; logo bottom-center

Slides 2-6 (content):
- Tip number: large, semi-transparent background numeral ("01")
- Tip headline: 32px bold
- Tip description: 20px, 2-3 lines max
- Same background on all slides; progress dots at bottom

Slide 7 (CTA):
- "Found this helpful?" + follow CTA + handle
- Share/save prompt; logo
```

### Before/after (Instagram 1080x1350)

```text
- Top half: "Before" label + image/state
- Divider: thin line or diagonal cut with label
- Bottom half: "After" label + image/state
- Equal halves
- Muted/gray for before, vibrant for after
```

### Data/stat post (X 1200x675)

```text
- Large number: 72-96px, bold, gradient or accent color
- Context line: 24px below the number
- Supporting text: 18px, 2 lines max
- Source attribution: 14px, bottom-right
- Background: clean gradient or subtle pattern
- Brand mark: small, bottom-left
```

## Carousel system

Keep header bar, padding, accent, and progress indicator identical across slides.

```css
:root {
  --slide-bg: #0F172A;
  --slide-text: #F8FAFC;
  --slide-accent: #6366F1;
  --slide-padding: 80px;
  --slide-radius: 0; /* edge-to-edge */
}

.slide-header {
  position: absolute; top: 0; left: 0; right: 0;
  height: 4px; background: var(--slide-accent);
}

.progress-dots {
  position: absolute; bottom: 40px; left: 50%; transform: translateX(-50%);
  display: flex; gap: 8px;
}
.progress-dots .dot { width: 8px; height: 8px; border-radius: 50%; background: rgba(255,255,255,0.3); }
.progress-dots .dot.active { background: var(--slide-accent); width: 24px; border-radius: 4px; }

/* Swipe hint on first slide */
.swipe-hint {
  position: absolute; right: 40px; top: 50%; transform: translateY(-50%);
  font-size: 14px; letter-spacing: 0.1em; text-transform: uppercase;
  writing-mode: vertical-rl; opacity: 0.6;
}
```

## Engagement rules

- Headlines: max 6 words per line; max 3 lines per text block.
- Minimum font size: 24px Instagram, 20px X/LinkedIn.
- Contrast: white on dark overlay or dark on light overlay; never mid-tone on mid-tone. Ratios in [graphic-design](graphic-design.md).
- Attention: asymmetric layouts; one bold color on a muted palette; oversized numbers or single words as anchors; negative space framing the message; diagonals for movement; an 8-12px inset frame.
- CTAs: Instagram "Save this for later", "Share to your story"; X "Reply with your take", "Bookmark this thread"; LinkedIn "Agree? Share your perspective below", "Follow for more insights"; Pinterest "Save this pin", "Click through for the full guide".

## Code output path

For carousels or copy-heavy posts, output a self-contained HTML file with:

1. Exact `width` and `height` on the canvas element
2. Web fonts loaded via `<link>`
3. All colors from design-context, as CSS custom properties
4. Comments marking editable sections (text, colors, images)

Render at the exact canvas size with body margin 0 and view the result as you would an AI output.

## Quality checklist

- [ ] Dimensions exactly match the target platform
- [ ] Text inside safe zones
- [ ] Font size readable at the platform's display size
- [ ] Brand colors and fonts applied consistently
- [ ] Clear hierarchy, one focal point
- [ ] Not text-heavy; social is visual-first
- [ ] CTA included where appropriate
- [ ] Output viewed: every word spelled correctly, legible at phone size
- [ ] Code output self-contained except fonts
