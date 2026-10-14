---
name: video-marketing
description: When the user wants to plan video marketing, create video scripts, or optimize for short-form or long-form video. Also use when the user mentions "video marketing," "video script," "short-form video," "long-form video," "TikTok script," "Reels script," "YouTube script," "video hook," or "video content strategy." For on-site video SEO, use video-optimization.
metadata:
  version: 1.0.1
  based_on_repo: kostja94/marketing-skills, coreyhaines31/marketingskills
  based_on_version: v1.0.0(8dd89c5), v2.11.27(28e4a81)
  based_on_skill: video-marketing, video
---

# Content: Video Marketing

Guides video marketing strategy and script creation for short-form and long-form content. Short-form commands ~82% of internet traffic with 2.5× more engagement than long-form; 71% of viewers decide within 3 seconds whether to continue. Use this skill when planning video content, writing scripts, or optimizing for platforms.

## Initial Assessment

**Project context:** Read the product marketing context when present. Without it, use available project material or user-provided facts and ask for missing information.

Identify:
1. **Format**: Short-form (TikTok, Reels, Shorts) vs long-form (YouTube, webinar)
2. **Goal**: Awareness, consideration, conversion, education
3. **Platform**: TikTok, Instagram Reels, YouTube Shorts, YouTube long-form

For production work, also gather (ask if not provided):

### 1. Video Goal
- What type of video? (Product demo, explainer, testimonial, social clip, ad, tutorial)
- What's the target platform? (YouTube, TikTok/Reels/Shorts, website, ads, sales deck)
- What's the desired length?

### 2. Production Approach
- Do you need a human presenter? (AI avatar vs. voiceover vs. screen recording)
- Do you have existing footage or assets? (Screenshots, logos, product UI)
- Do you need generated footage? (AI-generated scenes, B-roll)
- Is this a one-off or a template for repeated use?

### 3. Technical Context
- What's your tech stack? (Node.js, Python, etc.)
- Do you have API keys for any video tools?
- Budget constraints? (Some tools charge per minute of video)

## Short-Form vs Long-Form

| Format | Length | Use | Platforms |
|--------|--------|-----|-----------|
| **Short-form** | 15–60 sec | Hooks, tips, UGC-style; 90% watch daily | TikTok, Reels, Shorts |
| **Long-form** | 3–15+ min | Deep dives; tutorials; Gen Z discovers via short, engages with long | YouTube |

**Optimal short-form length**: 31–60 seconds for higher completion rates.

## Critical First 3 Seconds

71% of viewers decide within 3 seconds whether to continue. Hook types:

| Hook Type | Example |
|-----------|---------|
| **Story-driven** | "Three months ago, I had zero subscribers..." |
| **Contrarian** | "Everyone says X. Here's why they're wrong." |
| **Question** | "Why do 90% of startups fail at this?" |
| **Result-focused** | "I went from 0 to 10K in 30 days. Here's how." |

## Script Structure (Short-Form)

**Hook (0–3 sec)** → **Problem (3–15 sec)** → **Solution (15–45 sec)** → **CTA (final 5 sec)**

Achieves 70%+ completion for algorithmic boost. Frameworks: Hook-Value-CTA, AIDA, PAS, BAB.

## Platform-Specific Hooks

| Platform | Hook Length | Notes |
|----------|-------------|-------|
| **TikTok** | 2 seconds | High energy; 4,000-char captions for SEO |
| **Instagram Reels** | 3 seconds | Polished aesthetics; penalizes TikTok watermarks |
| **YouTube Shorts** | 3–5 seconds | Searchable titles; keyword-rich descriptions |

## UGC-Style Content

- **Authenticity > polish**: UGC-style generates 50%+ of engagement
- **Trust**: 86% of consumers trust brands publishing UGC more than polished ads

## Long-Form Script Structure

- **Hook** (0–30 sec): Promise; why watch
- **Intro** (30–60 sec): Context; what you'll cover
- **Body**: Sections with clear transitions
- **CTA**: Subscribe; link; next step
- **Outro**: Recap; repeat CTA

## Choosing Your Approach

Pick the right tool for the job:

| Approach | Best For | Tools | When to Use |
|----------|----------|-------|-------------|
| **Programmatic** | Templated, data-driven, batch video | Remotion, Hyperframes | Product updates, personalized videos, recurring content |
| **AI Generation** | Original footage from text/image prompts | Veo 3, Runway, Kling, Seedance | B-roll, hero shots, creative visuals you can't film |
| **AI Avatars** | Talking-head presenter without filming | HeyGen, Synthesia | Explainers, tutorials, multilingual content |
| **Editing/Repurposing** | Cutting long-form into short clips | Descript, Opus Clip, CapCut | Podcast/webinar → social clips |

## Programmatic Video

Build videos with code. Best for repeatable, templated, or data-driven video at scale.

### Hyperframes (HTML/CSS — recommended for agents)

Open-source, Apache 2.0, from HeyGen. Uses plain HTML/CSS/JS — no framework DSL to learn. LLM-native: AI models generate better HTML than React components.

```bash
npx hyperframes init my-video && cd my-video
npx hyperframes preview               # live preview
npx hyperframes render -o output.mp4  # render index.html
```

**Key concept:** A composition is one HTML file. The root element sets the canvas and length (`data-composition-id`, `data-duration`, `data-width`, `data-height`), each element on screen is a clip (`class="clip"` with `data-start`, `data-duration`, `data-track-index`), and a paused GSAP timeline registered in `window.__timelines` drives the animation. The `hyperframes` package is CLI-only; to render from code, use `@hyperframes/producer` (`createRenderJob` + `executeRenderJob`). Full syntax and a working example: [Hyperframes integration guide](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/hyperframes.md).

**Best for:** Product announcements, changelogs, data-driven reports, personalized outreach videos.

**Why agents prefer it:** Plain HTML/CSS means any coding agent can write a composition without learning a framework. Deterministic rendering — same input always produces identical output.

### Remotion (React)

Mature open-source framework. More powerful than Hyperframes but requires React knowledge.

```bash
npx create-video@latest
```

**Key concept:** React components are frames. Props drive content. Render locally or via Remotion Lambda (AWS) for scale.

```tsx
export const ProductDemo: React.FC<{ title: string; features: string[] }> = ({
  title, features
}) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{ background: "#000", color: "#fff" }}>
      <h1>{title}</h1>
      {features.map((f, i) => (
        <Sequence from={i * 30} key={i}>
          <p>{f}</p>
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
```

**Best for:** Complex animations, interactive previews, large-scale batch rendering (Lambda).

### When to Pick Which

| Factor | Hyperframes | Remotion |
|--------|-------------|----------|
| Agent compatibility | Better (plain HTML) | Good (React) |
| Animation complexity | GSAP timelines (plus CSS) | Advanced (Spring, interpolate) |
| Batch rendering | Local | Lambda (AWS) for scale |
| Learning curve | Minimal | Moderate (React + Remotion API) |
| License | Apache 2.0 | Company license for commercial use |

## AI Video Generation

Generate original footage from text or image prompts. Use for B-roll, hero visuals, and scenes you can't practically film.

### Model Comparison

| Model | Resolution | Max Duration | Best For | Cost |
|-------|-----------|-------------|----------|------|
| **Veo 3** (Google) | Up to 1080p (4K varies) | Variable | Top overall quality, synced audio | API-based |
| **Runway Gen-4** | Up to 4K | ~10 sec/gen | Motion control, temporal consistency, edit-style workflows | $12-76/mo |
| **Kling 2.5/3.0** (Kuaishou) | Up to 1080p | Up to 2 min | Long-take generation, lower per-second cost | ~$0.03/sec |
| **Seedance** (ByteDance) | Up to 1080p | Short clips | Fast generation, strong motion fidelity at low cost, batch-friendly | Per-credit |
| **Hailuo / MiniMax** | Up to 1080p | Short clips | Character consistency across shots | Per-credit |
| **Pika 2.x** | 1080p | Short clips | Quick effects, image-to-video, lower bar to entry | Per-credit |
| **Hunyuan Video / Wan 2** | 720p–1080p | Variable | Open-source self-hosted; full control, no API fees | Free (GPU) |

**Quick picks**:
- **Highest quality + audio**: Veo 3
- **Batch / volume / cost**: Kling, Seedance
- **Character consistency across multiple shots**: Hailuo
- **Self-hosted, brand-controlled**: Hunyuan Video or Wan 2 (open weights)
- **Storyboard → video workflow**: Runway, LTX Studio
- **Image-to-video from a still you already have**: Kling, Pika, Runway

### Prompting for Video Models

Good video prompts specify: **subject + action + camera + style + mood**

```
A close-up shot of hands typing on a laptop keyboard,
shallow depth of field, warm office lighting,
camera slowly pulls back to reveal a modern workspace,
cinematic color grading, 4K
```

Before writing a prompt for a specific model, or when a prompt underperforms, read [references/ai-video-prompting.md](references/ai-video-prompting.md): camera vocabulary, style keywords, model-specific tips, common prompt mistakes, aspect ratios, and cost tactics.

### When to Use AI Generation vs. Stock

| Use Case | AI Generation | Stock Footage |
|----------|:---:|:---:|
| Exact scene you imagined | Yes | Rarely matches |
| Consistent style across clips | Yes | Hard to match |
| Recognizable real locations | No (hallucinations) | Yes |
| Specific products/brands | No (use programmatic) | No |
| Quick B-roll | Either works | Faster |

## AI Avatars

Create talking-head videos without filming. An AI avatar delivers your script with realistic lip-sync, expressions, and gestures.

### HeyGen (recommended — has MCP server)

Best lip-sync and micro-expressions. 230+ avatars, 140+ languages.

**Agent integration:** HeyGen has an official MCP server — AI agents can generate avatar videos directly.

| Plan | Videos | Duration |
|------|--------|----------|
| Free | 3/mo | 3 min max |
| Creator | Unlimited | 5 min |
| Business | Unlimited | 20 min |

Check [heygen.com/pricing](https://www.heygen.com/pricing) for current prices.

**Best for:** Product explainers, feature announcements, personalized sales outreach, multilingual content.

**Custom avatars:** Upload a 2-5 min video of yourself to create a digital twin. Looks and sounds like you, generates videos from text scripts.

### Synthesia

Full-body avatars with expressive body language. Built-in script generation from URLs/docs.

**Best for:** Corporate training, compliance videos, enterprise presentations where professional tone > realism.

### When to Use Avatars vs. Other Approaches

| Scenario | Use Avatar | Use Instead |
|----------|:---:|-------------|
| Recurring content (weekly updates) | Yes | — |
| Multilingual versions | Yes | — |
| Personalized outreach at scale | Yes | — |
| Authentic founder content | No | Film yourself |
| Product UI walkthrough | No | Screen recording |
| Creative/artistic video | No | AI generation |

## Editing & Repurposing Tools

Turn existing content into multiple video formats.

| Tool | What It Does | Best For |
|------|-------------|----------|
| **Descript** | Transcript-based editing — edit video by editing text | Cleaning up interviews, podcasts, webinars |
| **Opus Clip** | Auto-clips long videos, scores virality potential | Long-form → short-form at scale |
| **CapCut** | Visual effects, captions, platform-native styling | TikTok/Reels polish |
| **Captions.ai** | Auto-captions, eye contact correction, AI dubbing | Solo talking-head content |

### Repurposing Workflow

```
Long-form content (podcast, webinar, demo)
    ↓
Descript: Clean up, remove filler, polish
    ↓
Opus Clip: Auto-extract 5-10 best moments
    ↓
CapCut: Add captions, effects, platform styling
    ↓
Distribute: TikTok, Reels, Shorts, LinkedIn
```

### Reverse-Engineer a Viral Edit

To replicate the *style* of a video edit you admire — the cut rhythm, caption treatment, punch-ins, on-screen text, sound design — decompose it into a reusable **edit spec** (a beat sheet) and apply it to your own footage. Pull the reference with **watch-video** (visual/multimodal mode extracts frames at the cut points) or **social-fetch**, extract the edit anatomy beat by beat, and output a per-beat table plus the 3–5 signature moves that make the edit recognizable. Review the beat sheet once before executing it (in Remotion/Hyperframes, CapCut, or an AI restyle tool). Copies the editing grammar, never the reference's footage/script/music. Full method: [references/edit-anatomy.md](references/edit-anatomy.md).

## Video Production Workflows

### Product Demo Video

1. **Script** the key features and value props (use copywriting skill)
2. **Screen record** the product flow
3. **Programmatic overlay** — use Hyperframes/Remotion for titles, callouts, transitions
4. **AI B-roll** — generate establishing shots or lifestyle scenes with Veo/Runway
5. **Voiceover** — record yourself or use AI avatar for narration
6. **Export** at platform-appropriate specs

**Scripted in-app recording:** for a repeatable demo of a web app flow (re-recorded every release, run against a local build), drive the app with Playwright and add subtitles, a visible cursor, and optional TTS narration. See [references/product-demo-recording.md](references/product-demo-recording.md) for the workflow, step modes, and local-app gotchas.

### Explainer Video

1. **Script** the problem → solution → CTA arc
2. **Choose presenter** — AI avatar (HeyGen) or voiceover + visuals
3. **Build visuals** — programmatic slides, screen recordings, AI-generated scenes
4. **Add captions** — always, for accessibility and engagement
5. **Export** — landscape for YouTube/website, vertical for social

### Batch Social Clips

1. **Create master template** in Hyperframes/Remotion
2. **Feed data** — product features, testimonials, stats
3. **Render batch** — one template, many variations
4. **Add platform-specific captions** via CapCut or Captions.ai
5. **Schedule** across platforms

## Agent-Native Video Pipeline

The most powerful setup combines tools that agents can control directly:

```
Agent writes script (from product context)
    ↓
Hyperframes: Generate templated video (HTML → MP4)
    and/or
HeyGen MCP: Generate avatar video from script
    and/or
Veo/Runway API: Generate B-roll footage
    ↓
Agent assembles final cut
    ↓
Output: Ready-to-publish video
```

**What makes this agent-native:**
- Hyperframes uses HTML — any coding agent can generate it
- HeyGen MCP server — agents call it directly
- Video model APIs — standard HTTP requests
- No manual editing step required

## Common Mistakes

1. **Uncanny valley avatars** — if avatar quality matters, invest in HeyGen Creator+ tier
2. **No captions** — 80%+ of short-form video is watched without sound
3. **Over-producing** — authentic often outperforms polished, especially on TikTok

## Tool Integrations

| Tool | Type | MCP | Guide |
|------|------|:---:|-------|
| **HeyGen** | AI avatars | Yes | [heygen.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/heygen.md) |
| **Hyperframes** | Programmatic video | - | [hyperframes.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/hyperframes.md) |
| **Remotion** | Programmatic video | - | [remotion.dev](https://www.remotion.dev/docs) |
| **Runway** | AI generation | - | [runwayml.com/docs](https://docs.dev.runwayml.com) |

## Output Format

- **Format** (short vs long) recommendation
- **Hook** options (2–3 variants)
- **Script** (timestamped if long-form)
- **CTA** placement
- **Platform** optimization notes

> **Source conflicts (kostja wins, ours flagged):** our copy says 85% of social video is watched without sound. kostja says 80%+ (TikTok reference). Used kostja's figure above.

## Related Skills

- **social** (TikTok reference): TikTok caption, video specs, script
- **tiktok-ads**: TikTok ad creative
- **content-marketing**: Video as content format; repurposing
- **social** (YouTube reference): YouTube SEO, description, thumbnail (platform skill)
- **video-optimization**: Website video SEO; VideoObject; video sitemap; Google prioritizes YouTube
- **social**: Video content strategy, hooks and what to post
- **ad-creative**: Paid video ad creative and iteration
- **copywriting**: Video scripts and messaging
- **marketing-psychology**: Hooks and persuasion in video
