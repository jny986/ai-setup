---
name: visual-content
description: When the user wants to plan, create, or repurpose visual content (images, infographics, social post images) across channels. Also use when the user mentions "content images," "social media images," "infographic," "visual content," "post image," "image specs," "visual repurposing," "content visuals," or "image for social post." For Pinterest, use pinterest-posts.
metadata:
  version: 1.0.1
---

# Content: Visual Content

Guides visual content planning and creation across website, social media, email, and other channels. Images are needed not just for websites—social posts, infographics, and repurposed content all require visuals. Visual-first planning in content calendars improves engagement; cross-channel consistency and repurposing maximize ROI.

## Scope

- **When to use images**: By content type and format
- **Specs by context**: Website vs social vs email
- **Platform image specs**: X, LinkedIn, Pinterest, Instagram, Facebook, YouTube
- **Repurposing**: One visual → multiple formats and channels
- **Visual-first planning**: Content calendar with image planning

## Initial Assessment

**Project context:** Read the product marketing context when present. Without it, use available project material or user-provided facts and ask for missing information.

Identify:
1. **Context**: Article, social post, infographic, email, landing page
2. **Channels**: Which platforms will use this visual
3. **Repurposing**: Will this visual be adapted for other formats?

For image production, also gather (ask if not provided):

### 1. Image Goal
- What type of image? (Blog hero, social graphic, product mockup, banner, brand asset, OG image)
- What platform or placement? (Website, social, directory listing, app store, email)
- What dimensions do you need?

### 2. Production Approach
- Do you have existing brand assets? (Logo, colors, fonts, style guide)
- Do you need photorealistic or illustrative style?
- Is this a one-off or a template for repeated use?

### 3. Technical Context
- Do you have API keys for any image tools? (Gemini, Replicate/Flux, Ideogram)
- Budget constraints? (Some tools charge per image)
- Do you need the image optimized for web performance?

## 1. When to Use Images

| Content Type | Visual Need | Notes |
|--------------|-------------|-------|
| **Article / Blog** | Hero image, in-article images, screenshots | See **image-optimization** for web (alt, WebP, LCP) |
| **Social post** | Single image, carousel, or link preview | Platform-specific specs below |
| **Infographic** | Primary format; data visualization | Repurpose to social (cropped), blog (full) |
| **Case study** | Customer photo, results chart, logo | Repurpose to LinkedIn carousel, blog |
| **Product update** | Screenshot, feature graphic | Changelog, email, social |
| **Email** | Header image, inline graphics | Keep lightweight; many clients block images |
| **Landing page** | Hero, trust badges, screenshots | See **hero-generator**, **image-optimization** |

## 2. Website vs Social vs Email

| Context | Priority | Skill |
|---------|----------|-------|
| **Website** | Alt text, WebP, LCP, responsive, lazy loading | **image-optimization** |
| **Social posts** | Platform dimensions, aspect ratio, file size | **Platform skills** (X, LinkedIn, Pinterest, etc.) |
| **OG / Twitter Cards** | 1200×630, 1200×675 for link previews | **open-graph**, **twitter-cards** |
| **Email** | Inline-friendly; avoid heavy images; alt for blocked | **email-marketing** |

## 3. Platform Image Specs (Social)

| Platform | Post Image | Stories / Reels | Profile | Notes |
|----------|------------|-----------------|---------|-------|
| **X (Twitter)** | 1200×675 (16:9), 800×800 | — | 400×400 | See **social** (X reference) |
| **LinkedIn** | 1200×627, 1200×1200; carousel up to 20 | — | 400×400 | See **social** (LinkedIn reference); vertical preferred on mobile |
| **Pinterest** | 1000×1500 (2:3) | — | 165×165 | Alt text ~25% more impressions; see **social** (Pinterest reference) |
| **Instagram** | 1080×1350 (4:5), 1080×1080 | 1080×1920 (9:16) | 320×320 | 4:5 outperforms square on feed |
| **Facebook** | 1200×630, 1080×1080 | 1080×1920 | 320×320 | |
| **YouTube** | Thumbnail 1280×720 | — | 800×800 | |

**General**: 1080px width works across most platforms; vertical (4:5, 9:16) outperforms square on mobile-first feeds. Keep critical elements (logo, text) in safe center—platforms may crop.

## 4. Visual Repurposing

**Principle**: One core visual → multiple crops/formats → multiple channels.

| Core Visual | Adaptations | Channels |
|-------------|-------------|----------|
| **Infographic** | Full (blog), cropped sections (Instagram, LinkedIn carousel), square (X) | Blog, LinkedIn, Instagram, X |
| **Case study graphic** | Hero (blog), single slide (LinkedIn), story (Instagram) | Blog, LinkedIn, Instagram |
| **Product screenshot** | Hero (landing), post (X, LinkedIn), email header | Website, social, email |
| **Quote graphic** | Square (X, LinkedIn), 4:5 (Instagram) | X, LinkedIn, Instagram |

**Workflow**: Design at largest needed size; export platform-specific crops. Use consistent colors, fonts, logo placement (see **brand-visual**).

## 5. Visual-First Content Planning

- **Plan images in content calendar**: Don't add visuals as afterthought; visuals drive engagement
- **Batch by theme**: Create visuals for a topic cluster or campaign together for consistency
- **Repurposing column**: In calendar, note which core piece becomes which visual format for which channel
- **Asset library**: Organize by campaign/theme; tag for reuse

## 6. Format-Specific Notes

### Infographics

- **Dimensions**: 800–1200px width; height varies by content
- **Export**: PNG for web; PDF for download
- **Repurpose**: Slice into 3–5 slides for LinkedIn carousel; single stat for X/Instagram

### Social Post Images

- **Text overlay**: Keep minimal; many platforms deprecate text-heavy images
- **Branding**: Logo in corner; consistent with **brand-visual**
- **Alt text**: Add for LinkedIn, Pinterest, X (accessibility + Pinterest SEO); see **image-optimization** for alt best practices

### Article / Blog Images

- **Hero**: Often LCP candidate; optimize per **image-optimization**
- **In-article**: Support narrative; alt text, captions per **image-optimization**
- **Screenshots**: Annotate when helpful; keep file size low

## 7. Producing the Image

Tools, models and workflows for creating the asset.

### Choosing Your Approach

Pick the right tool for the job:

| Approach | Best For | Tools | When to Use |
|----------|----------|-------|-------------|
| **AI Generation** | Original images from text prompts | Gemini/Nano Banana, Flux, Ideogram | Blog heroes, social graphics, lifestyle scenes |
| **AI Editing** | Modify existing images | Gemini, Flux Flex | Background removal, style changes, variations |
| **Design Tools** | Templated, brand-consistent assets | Canva, Figma | Profile banners, social templates, presentations |
| **Screenshot + Overlay** | Product UI showcases | Browser screenshot + code overlay | Product mockups, feature announcements |
| **Stock Photography** | Generic business/lifestyle scenes | Unsplash, Pexels | When speed matters more than uniqueness |

### AI Image Generation

#### Model Comparison

| Model | Best For | Text in Images | API | Cost |
|-------|----------|:-:|-----|------|
| **Gemini Image** (Google, "Nano Banana" / Nano Banana Pro) | All-around, editing, multi-image reference, text rendering | Good | [Gemini API](https://ai.google.dev/gemini-api/docs/image-generation) | Check [pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| **Flux** (Black Forest Labs — Pro 1.1, Kontext, Dev, Schnell) | Photorealism, brand consistency, batch; Kontext for in-image editing | Limited | [BFL API](https://docs.bfl.ai/), Replicate, fal.ai | Check [pricing](https://docs.bfl.ai/quick_start/pricing) |
| **Ideogram 3.0** | Typography, branded graphics, accurate text rendering | Best | [Ideogram API](https://developer.ideogram.ai/) | Check [pricing](https://about.ideogram.ai/api-pricing) |
| **ChatGPT Images 2.0 / GPT Image** (OpenAI) | General purpose, ChatGPT integration, native editing | Good | [OpenAI API](https://platform.openai.com/docs/guides/image-generation) | Check [pricing](https://platform.openai.com/docs/pricing) |
| **Midjourney v7** | Artistic, high-aesthetic, art-directed visuals | Improved | No official API; Discord + Web | Subscription-based |
| **Recraft V3** | Vector + brand-consistent illustrations, design assets | Strong | [Recraft API](https://www.recraft.ai/docs) | Per-credit |
| **Stable Diffusion 3.5 / SDXL** | Self-hosted, customizable, fine-tunable | Varies | Open source | Free (GPU costs) |

**Note:** DALL-E 3 is fully deprecated. OpenAI's current image models are the GPT Image family. `gpt-image-1` retires on 23 Oct 2026 and `gpt-image-1-mini` and `gpt-image-1.5` on 1 Dec 2026; OpenAI's recommended replacements are `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare` (check OpenAI's deprecations page for the current list).

#### When to Use Which

```
Need text/headlines in the image?
├── Yes → Ideogram 3.0 (best), Gemini (good), GPT Image / ChatGPT Images (decent)
└── No ↓

Need product/brand consistency across many images?
├── Yes → Flux (multi-image reference), Gemini Nano Banana Pro, Recraft V3
└── No ↓

Need to edit an existing image (in-place)?
├── Yes → Gemini (native editing), Flux Kontext, ChatGPT Images
└── No ↓

Need vector / illustrative brand assets?
├── Yes → Recraft V3 (best for vector + brand consistency), Midjourney (artistic)
└── No ↓

Need highest visual quality / art direction?
├── Yes → Flux Pro 1.1, Midjourney v7
└── No ↓

Need volume at low cost?
└── Flux Schnell, Gemini Flash, Stable Diffusion (self-hosted)
```

#### Prompting Basics

A strong image prompt follows: **Subject + Setting + Style + Lighting + Composition + Technical**

```
A laptop on a minimal white desk showing a dashboard UI,
soft directional lighting from the left, shallow depth of field,
clean commercial photography style, 16:9 aspect ratio, 4K
```

Before writing a prompt for a specific model, or when a prompt underperforms, read [references/ai-image-prompting.md](references/ai-image-prompting.md): style, lighting and composition keywords, model-specific tips, common prompt mistakes, and batch and cost workflows.

### Design Tools

For templated, brand-consistent work where AI generation is overkill or too unpredictable.

#### Canva

Best for non-designers who need polished output fast.

- **Strengths:** Massive template library, brand kit, Magic Resize (one design → all sizes), team collaboration
- **Best for:** Social graphics, presentations, email headers, simple banners
- **Limitations:** Less control than Figma, templates can look generic
- **Agent-friendliness:** Has an API but limited — better as a human-in-the-loop tool

#### Figma

Best for teams with design systems or pixel-perfect needs.

- **Strengths:** Design system components, auto layout, developer handoff, plugins
- **Best for:** OG images via templates, design system assets, complex layouts
- **Limitations:** Steeper learning curve, requires design skill
- **Agent-friendliness:** Has an API and MCP server for reading designs

#### When to Use Design Tools vs. AI Generation

| Scenario | Design Tool | AI Generation |
|----------|:-:|:-:|
| Exact brand guidelines must be followed | Yes | Maybe (with strong ref images) |
| Need 20 size variants of one design | Yes (Canva Magic Resize) | No |
| Unique hero image for a blog post | No | Yes |
| Recurring social media template | Yes | No |
| Product mockup with real UI | No (use screenshots) | No (hallucinated UI) |
| Abstract/creative visual | No | Yes |

### Marketing Image Workflows

#### Blog & Article Hero Images

The image at the top of every post. Sets tone, improves shareability, required for OG/social previews.

1. **Define the concept** — what visual metaphor represents the topic?
2. **Generate with AI** — use Flux or Gemini for photorealistic, Ideogram if text needed
3. **Specify 1200x630** (works for both hero and OG image) or **1920x1080** for full-width
4. **Optimize** — compress to <200KB, serve as WebP with JPEG fallback

**Prompt pattern:**
```
[Visual metaphor for topic], clean modern style,
bright natural lighting, shallow depth of field,
professional blog header aesthetic, 1200x630
```

#### Social Media Graphics

Platform-specific images for organic posts.

| Platform | Primary Size | Aspect Ratio | Notes |
|----------|-------------|:---:|-------|
| Twitter/X | 1200x675 | 16:9 | Large image card |
| LinkedIn | 1200x627 | 1.91:1 | Feed image |
| Instagram Feed | 1080x1350 | 4:5 | Outperforms square; 1080x1080 (1:1) also works |
| Instagram Stories | 1080x1920 | 9:16 | Full screen vertical |
| Facebook | 1200x630 | 1.91:1 | Link share image |

**Workflow:**
1. Create the hero concept at highest resolution needed
2. Use Canva Magic Resize or manual crop for platform variants
3. Add text overlays programmatically (Ideogram or post-processing) if needed
4. Export at platform-specific dimensions

#### Product Mockups & Screenshots

Showcase your product UI in context with real screenshots; AI models hallucinate UI.

1. **Capture real screenshots** of your product at 2x resolution
2. **Frame in device mockups** — use browser frame, laptop, or phone templates
3. **Add context** — callout arrows, feature labels, before/after comparisons
4. **Annotate with code** — Hyperframes or HTML/CSS for programmatic overlays

**Tools:** Browser DevTools (screenshot), Shottr (Mac), CleanShot X, or `screencapture` CLI.

#### Profile & Listing Banners

Banners for profiles, directory listings, and marketplace pages. Often the first visual impression.

| Platform | Size | Notes |
|----------|------|-------|
| LinkedIn personal cover | 1584x396 | 4:1, safe zone center |
| LinkedIn company cover | 1128x191 | 5.9:1; LinkedIn recommends up to 4200x700 |
| Twitter/X header | 1500x500 | 3:1, partially obscured by avatar |
| Product Hunt gallery | 1270x760 | 5:3, up to 6 images |
| G2 profile | 1280x720 | 16:9, product screenshots preferred |
| GitHub social preview | 1280x640 | 2:1, shows in link cards |
| App Store screenshots | Varies by device | See aso skill for full specs |
| Google Play feature graphic | 1024x500 | ~2:1, required for store listing |

**Best practices:**
- **Keep text minimal** — banners are seen at small sizes on mobile
- **Center critical content** — edges get cropped differently per device
- **Show the product** — real UI screenshots outperform abstract graphics on directory listings
- **Update seasonally** — stale banners signal an inactive product

**Workflow:**
1. Pick the platform(s) and note exact dimensions
2. For directories (Product Hunt, G2): use real product screenshots with light annotation
3. For profiles (LinkedIn, Twitter): use brand colors + tagline + optional product shot
4. Generate with Canva/Figma templates or Ideogram (if text-heavy)
5. Test at actual display size — zoom out to check readability

#### Brand Assets

Logos, icons, and illustrations. AI generation has limits here.

| Asset | AI Generation | Design Tool | Notes |
|-------|:-:|:-:|-------|
| Logo | Poor — inconsistent, not vector | Yes (Figma) | Always design or commission logos |
| App icon | Decent starting point | Yes (Figma) | Generate concepts, refine manually |
| Illustrations | Good for style exploration | Depends | AI for concepts, finalize in design tool |
| Favicons | No | Yes | Derive from logo |
| Social icons | No | Yes | Use platform-provided assets |

### Image Optimization and OG Images

Formats, compression, lazy loading, alt text and dynamic OG images live in **image-optimization**. Meta tags for link previews live in **open-graph** and **twitter-cards**.

## Output Format

- **Visual plan** (what images for what content)
- **Specs** by context (platform dimensions, format)
- **Repurposing** map (one visual → multiple outputs)
- **References** to platform skills and image-optimization

> **Source conflicts (kostja wins, ours flagged):** our social size table led with 1080x1080 for the Instagram feed. kostja says 4:5 (1080x1350) outperforms square, so the table above uses 4:5 and keeps square as an option.

## Related Skills

### Content & Strategy

- **content-marketing**: Content types, formats, repurposing; visual content is part of content mix
- **content-strategy**: SEO topic clusters; article visuals
- **copywriting**: Copy pairs with visuals; headlines for image posts

### Platform (Image Specs)

- **social** (X reference): X post image specs
- **social** (LinkedIn reference): LinkedIn image specs
- **social** (Pinterest reference): Pinterest Pin dimensions, alt text
- **social** (Reddit reference): Reddit image post context

### Website & SEO

- **image-optimization**: Web images (alt, captions, WebP, LCP, responsive); central skill for image SEO
- **open-graph, twitter-cards**: Link preview images
- **hero-generator**: Hero section visuals

### Other

- **brand-visual**: Typography, colors, imagery tone; visual consistency
- **video-marketing**: Video thumbnails; video as visual format
- **video-optimization**: Video SEO; VideoObject; video sitemap; YouTube prioritization

### Production

- **ad-creative**: Paid ad image creative, platform-specific ad specs, scaled ad production
- **video-marketing**: AI video production and programmatic video
- **social**: What to post and content strategy
- **conversion-optimization**: Image placement and conversion on landing pages
- **aso**: App store screenshot specs and optimization
- **directory-submission**: Product Hunt gallery images and directory listing visuals
