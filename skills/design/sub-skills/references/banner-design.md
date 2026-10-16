---
name: banner-design
description: "Design banners for web, advertising, and physical placements with readable messaging and format-appropriate composition."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: banner-design
---

# Banner Design

Website banners, email headers, event banners, and announcement bars for owned channels. Paid display/IAB ads: [ad-creative-design](ad-creative-design.md). Coded above-the-fold sections: [hero-section](hero-section.md). Full email templates: [email-design](email-design.md).

Read `DESIGN.md` for UI tokens and the project brand kit for approved brand primitives (see [design-context](design-context.md)); when absent, inspect the project's existing CSS variables or Tailwind theme. Banners are high-visibility touchpoints: follow brand guidelines strictly.

## Image-generation path

Prompt craft, cropping, and text-overlay fallback: [image-generation](image-generation.md).

1. Generate at the nearest supported ratio from the tables, then crop/resize to the exact size (for example 21:9, then 1440x600). Export web/email banners at 2x (2880x1200, 1200x400) and display at 1x for sharp retina rendering.
2. Web heroes crop differently per breakpoint: keep the subject centered with clear space for text, or generate a separate 4:5 mobile version.
3. For web and email, generate the visual without text and set headline + CTA as live HTML text (accessible, editable, visible when email images are blocked).
4. View the output: check spelling, legibility at displayed size, and that the text area is clean. Fix one issue per follow-up.

### Example prompts

- **Hero:** "Create a wide website hero banner for [brand]. [product/service] visual on the right, headline '[text]' on the left in [font-style]. [color] gradient background. CTA button '[action]'. Modern, bold layout."
- **Email header:** "Create a wide email header banner for [brand]. [campaign theme] with [color palette]. Logo centered at top, headline '[text]' below. Simple, clean design that renders in all email clients."
- **Event:** "Create a wide event banner for [event name]. [style] background with [decorative elements]. Event name '[text]' prominently displayed. Date '[date]' and location '[venue]' below. [mood/tone]."

## Sizes

Where the pixel ratio is not a standard generator ratio, use the nearest one and crop.

### Website

| Type | Dimensions | Ratio | Use |
|------|-----------|-------|-----|
| Hero (full width) | 1440 x 600 | 21:9 | Homepage, above the fold |
| Hero (tall) | 1440 x 800 | 16:9 | Full-viewport hero |
| Section banner | 1440 x 400 | 4:1 | Interior section divider |
| Sidebar | 300 x 250 or 300 x 600 | 5:4 / 9:16 | House promo (paid placements: [ad-creative-design](ad-creative-design.md)) |
| Notification bar | Full width x 48px | n/a (code) | Top-of-page announcement |
| Consent bar | Full width x 80px | n/a (code) | Bottom notification |

### Email

| Type | Dimensions | Ratio | Notes |
|------|-----------|-------|-------|
| Header | 600 x 200 | 3:1 (use 21:9, crop) | Standard width |
| Hero | 600 x 300 | 2:1 (use 16:9, crop) | Full-width hero |
| Compact banner | 600 x 150 | 4:1 | Promotional |

### Event / promotional

| Type | Dimensions | Ratio | Use |
|------|-----------|-------|-----|
| Event (wide) | 1200 x 400 | 3:1 (use 21:9, crop) | Event page header |
| Meetup | 1200 x 675 | 16:9 | Meetup.com cover |
| Eventbrite | 2160 x 1080 | 2:1 (use 16:9, crop) | Event cover |
| Conference | 1920 x 600 | 3.2:1 (use 4:1, crop) | Conference site hero |

## Hero composition

- **Split (content left, visual right):** grid `1fr 1fr`, min-height 600px, 80px padding, 60px gap. Content: eyebrow (14px uppercase, brand color), headline (`clamp(36px, 4vw, 56px)`, weight 800, `text-wrap: balance`), description (18px, muted), CTA group (flex, 16px gap).
- **Centered (text over background):** flex column centered, min-height 600px, 80px padding. Background image with gradient overlay for legibility. Headline `clamp(40px, 5vw, 72px)` white, max-width 800px.
- **Asymmetric:** grid `55% 45%`; content side padding 80px; visual side `clip-path: polygon(10% 0, 100% 0, 100% 100%, 0% 100%)`.
- **Full-bleed visual (minimal text):** background cover, min-height 80vh, `align-items: flex-end`. `::after` scrim 0 to 0.7 black from bottom. Content at z-index 2, max-width 600px, white text.

Best practices: full viewport width, 50-80vh tall; one headline, one CTA; content max-width 1200-1440px centered; stack and shrink headings on mobile; prefer CSS gradients and optimized images for load time.

## CTA placement and hierarchy

Primary + secondary pattern: flex container (`gap: 16px; flex-wrap: wrap`). Primary: solid brand-color fill, white text, `14px 28px` padding, 8px radius, shadow. Secondary: transparent, 1.5px neutral border, same size. Both `font-weight: 600`; hover with `translateY(-1px)` or fill.

| Banner | CTA placement |
|--------|---------------|
| Hero | Below headline + description, left-aligned |
| Centered | Centered below description |
| Sidebar | Bottom, full width |
| Notification bar | Inline with text, right side |
| Email | Large centered button |

## Animated banners

- **Parallax:** scroll container `perspective: 1px; height: 100vh; overflow-y: auto`; background layer `transform: translateZ(-1px) scale(2)` (scale = 1 + depth / perspective).
- **Animated gradient:** `background-size: 600% 600%`, animate `background-position` over 12s.
- **Floating shapes:** absolute circles at 0.08 opacity, each with its own translate/rotate keyframes (7-10s).
- **Text reveal:** words in `inline-block` spans, animate `translateY(100%)` to 0 with 0.1s stagger.
- **Typing:** `white-space: nowrap; width: 0`, animate width with `steps()`, blinking cursor via `border-right`.

Wrap all motion in `@media (prefers-reduced-motion: no-preference)` and keep the headline readable in the first frame. See [motion-design](motion-design.md).

## Responsive

- Use `clamp()` for min-height, padding, and font-size, for example `font-size: clamp(28px, 4vw, 64px)`.
- At 768px stack split grids to `1fr`, center text, and put the visual first with `order: -1`.
- Swap background images per breakpoint: mobile (default), tablet (768px), desktop (1200px).

## Promotional frameworks

- **Sale / discount:** red gradient (`135deg, #DC2626, #991B1B`), centered. Discount number `clamp(60px, 10vw, 120px)`, weight 900. Optional diagonal stripes via `repeating-linear-gradient(-45deg)` at 0.03 opacity.
- **Product launch:** dark (`#0F172A` to `#1E293B`), centered. Pill eyebrow badge (uppercase, 13px, brand color on translucent bg/border). Headline `clamp(36px, 5vw, 64px)` white. Spotlight glow `::after` with `radial-gradient` centered above.
- **Event countdown:** brand-color bg, centered. Units in a flex row (24px gap): number 48px/800, `tabular-nums`, dark translucent bg; label 12px uppercase; separators between units.
- **Announcement bar:** full width, brand-color bg, flex centered, `10px 20px` padding. Text 14px/500, links bold underlined. Close button absolute right.

### Seasonal themes

| Occasion | Colors | Elements | Mood |
|----------|--------|----------|------|
| Spring | Greens, pinks, yellows | Flowers, leaves, butterflies | Fresh, renewal |
| Summer | Blues, oranges, bright yellow | Sun, waves, palm trees | Energetic, warm |
| Fall | Oranges, reds, browns | Leaves, pumpkins | Cozy, harvest |
| Winter | Blues, whites, silvers | Snowflakes, frost, evergreen | Crisp, festive |
| Black Friday | Black, gold, red | Bold type, price tags | Urgency, luxury |
| New Year | Gold, black, champagne | Confetti, fireworks, sparkle | Celebration |
| Valentine's | Reds, pinks, rose gold | Hearts, flowers, soft gradients | Romantic, warm |

## Sidebar banners

Fixed width (usually 300px); 300x600 is the more visible format. Content fully visible without scrolling, clear separation from page content, strong contrast with the surroundings, headline + CTA only.

Pattern: 300x600px, flex column, brand gradient bg, `32px 24px` padding, white text. Logo top, visual center (`flex: 1`), headline 22px/700, body 14px at 0.85 opacity, CTA at bottom (`margin-top: auto`, white bg, brand-color text, centered).

## Email headers

Email HTML is severely constrained:

- Table-based layout, max 600px (design for 320px mobile), inline styles only, longhand CSS properties.
- Fonts: `Arial, Helvetica, sans-serif`. Web fonts render only in some clients (Apple Mail, iOS).
- Always set `background-color` as a fallback; Outlook ignores background images.
- Images: set `width`, `height`, `alt`, `display:block`. Many clients block images by default, so key copy must be live text.
- Structure: outer `<table>` with gradient bg, centered logo `<img>`, `<h1>` (28px bold white), `<p>` (16px white at 0.9 opacity), CTA as a nested table with white bg and brand-color text link.
- Test in an email-testing service (Litmus, Email on Acid) or real clients.

## Checklist

- [ ] Dimensions match the target placement (generated output cropped to exact size)
- [ ] Rendered output viewed: text spelled correctly and legible at display size
- [ ] Hierarchy: headline > description > CTA; CTA prominent and action-oriented
- [ ] Brand colors and fonts applied
- [ ] Text contrast 4.5:1 normal, 3:1 large (24px+, or 18.66px+ bold), measured over the busiest part of the image (add a scrim if needed)
- [ ] Scales from mobile to desktop
- [ ] Motion is smooth, subtle, and respects reduced-motion
- [ ] CSS gradients preferred over heavy images
- [ ] Email banners use table layout and inline styles
- [ ] Seasonal banners match the occasion's visual language
