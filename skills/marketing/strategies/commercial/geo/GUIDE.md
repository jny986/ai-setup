---
name: generative-engine-optimization
description: When the user wants to optimize for AI search visibility (ChatGPT, Claude, Perplexity, AI Overviews). Also use when the user mentions "GEO," "AEO," "generative engine optimization," "AI search visibility," "LLM optimization," "GitHub GEO," "Grokipedia," "optimize for ChatGPT," "AI Overviews," "Bing Copilot," "Yandex AI," "Perplexity optimization," "GEO strategy," or "AI search optimization." For third-party publishing strategy (which platforms to use), use parasite-seo. For GitHub repos, README, and Awesome lists, use social (GitHub reference). For Medium.com only, use social (Medium reference). For Grokipedia edits, use social (Grokipedia reference). For traditional Google SERP strategy, use seo-strategy.
metadata:
  version: 1.4.0
  based_on_repo: kostja94/marketing-skills, coreyhaines31/marketingskills
  based_on_version: v1.0.0(8dd89c5), v2.11.29(c7d7dfb)
  based_on_skill: generative-engine-optimization, ai-seo
---

# Strategies: GEO (Generative Engine Optimization)

Guides GEO/AEO strategy for AI search visibility. GEO optimizes content for ChatGPT, Claude, Perplexity, and AI search summaries (Google AI Overviews, Bing Copilot, Yandex Search with AI)—getting cited in AI-generated answers rather than ranking in traditional SERPs. See **serp-features** for AI search as SERP features; **featured-snippet** for snippet optimization that overlaps with AI Overviews.

## Scope

- **GEO** = Generative Engine Optimization
- **AEO** = Answer Engine Optimization
- **LLMO** = Large Language Model Optimization
- **AIO** = Artificial Intelligence Optimization

All refer to the same goal: visibility in AI assistant responses.

## GEO vs. SEO

| Dimension | SEO | GEO |
|-----------|-----|-----|
| **Goal** | Rankings in search results | Citations in AI answers |
| **User path** | Click → visit → convert | Answer in-place; may not visit |
| **Content** | Full page optimization | Clear, citable paragraphs |
| **Metrics** | Clicks, traffic | Citations, brand mentions |
| **Platforms** | Google, Bing, Yandex (organic) | AI Overviews, Copilot, Yandex AI, ChatGPT, Perplexity |

**Both matter**: Create content that ranks and gets cited. AI search summaries (AI Overviews, Copilot, Yandex AI) are **SERP features**—see **serp-features**. When SERP features cause **zero-click** (user gets answer without clicking), citation becomes the primary value; optimize for being cited, not just ranked.

## AI Search Platforms (SERP Features + Standalone)

| Platform | Type | Source Selection | Optimization Focus |
|----------|------|------------------|---------------------|
| **Google AI Overviews** | SERP feature | Top 10–12 organic; Gemini; favors older domains (49% over 15 yrs) | Traditional SEO; structured data; citable blocks |
| **Bing Copilot Search** | SERP feature | Bing index; GPT-4; 9.81% domain overlap with Google; favors younger domains (18.85%); LinkedIn signals for B2B | Bing optimization; LinkedIn presence; structured content |
| **Yandex Search with AI / Neuro** | SERP feature | Real-time Yandex search; YandexGPT; Russia-focused | Yandex indexing; Russian content; cited sources |
| **Perplexity** | Standalone | 200B+ URL index; independent crawl; favors recency, semantic alignment | Content freshness; semantic markup; mid-tier site opportunity |
| **ChatGPT (web search)** | Standalone | GPTbot; high-authority, frequently updated, LLM-friendly; favors older domains (45.8%) | Backlinks; structured data; authority signals |

**Citation behavior**: AI Overview citations 20–35% higher CTR than equivalent organic. Copilot: shortest responses, fewest links (~3.13/response). Perplexity: prominent URL citations, high trackability. [Geneo](https://geneo.app/blog/chatgpt-vs-perplexity-vs-google-ai-overview-geo-comparison/), [GEO AIO](https://geoaiomarketing.com/how-bing-copilot-selects-sources-compared-to-perplexity/)

**Platform traffic context**: Among standalone AI tools, ChatGPT captures ~60%+ of independent Gen AI traffic, Gemini ~20%+, while Claude, Perplexity, and Grok each account for ~2-4%+. These tools reach users directly. SERP features (AI Overviews, Copilot) reach users through existing search flows rather than as independent destinations. Prioritize optimization effort proportionally.

## How GEO Works (RAG & Search Supply)

GEO operates through **RAG (Retrieval-Augmented Generation)**—AI tools retrieve content first, then generate answers. The retrieval supply type varies by platform and determines which content surfaces for citation.

### Retrieval Supply Types

| Type | Description | Platforms |
|------|------------|-----------|
| **Self-built index** | Platform maintains its own crawl and search index | Perplexity (200B+ URL index, PerplexityBot); ChatGPT (OAI-SearchBot index) |
| **Bound search engine** | Platform uses a fixed first-party search API | Copilot (Bing); Google AI Overviews / AI Mode (Google Search + query fan-out) |
| **Third-party API** | Platform contracts a third-party search API | Claude for Government (Brave Search API); smaller AI tools using Tavily, Exa, You.com |
| **Hybrid** | Combination of self-built + external API | ChatGPT (OAI-SearchBot + possible search partners); Claude Web Search (supplier not publicly disclosed) |

### Platform Retrieval & Implications

| Platform | Primary Supply | Strategic Implication |
|----------|---------------|----------------------|
| **Google AI Overviews / AI Mode** | Google Search (query fan-out) | Strong traditional SEO + structured data is the most reliable path |
| **Bing Copilot** | Bing index | Requires Bing indexing; LinkedIn signals for B2B visibility |
| **ChatGPT (web search)** | OAI-SearchBot + partners | High-authority, frequently updated content favored; backlinks matter |
| **Perplexity** | Proprietary crawl | Content freshness; semantic alignment; mid-tier sites have opportunity |
| **Claude (web search)** | Not publicly disclosed | Focus on general crawlability and clear structured content |

**Third-party search APIs** (Tavily, Exa, You.com, Brave Search API) feed smaller AI tools and custom agents. Content that is crawlable and indexed via standard web search reaches these APIs through their supply indexes. **Core model training** (long, costly, not widely actionable): focus on RAG optimization.

## AI Crawlers & Discovery

AI crawlers fall into three categories with different implications for content strategy:

| Type | Purpose | Examples | Implication |
|------|---------|---------|-------------|
| **Training crawlers** | Gather data for model training | GPTBot, ClaudeBot, Google-Extended, Meta crawlers | Blocking via robots.txt prevents training data use; **does not** affect real-time search/retrieval by the same provider |
| **Index/RAG crawlers** | Build search index for retrieval | OAI-SearchBot, PerplexityBot, Claude-SearchBot, Bytespider (Cohere), AppleBot | **Must allow** for RAG-based AI citation; critical for GEO |
| **Real-time crawlers** | Fetch content on-demand at query time | ChatGPT-User (opt-in via web search) | Content must be accessible without a login; paywalls may block citation |

**Content discovery**: "Push" submissions for general web content are primarily supported through Bing IndexNow. Google's Indexing API is limited to JobPosting and BroadcastEvent pages only (not general content). OpenAI, Anthropic, Perplexity, xAI, Meta, and DeepSeek do **not** offer public submission portals—their crawlers discover content through standard crawl and sitemaps only.

AI crawlers generally do **not** execute JavaScript—critical content must be in initial HTML. See **rendering-strategies** for SSR, SSG, CSR; **site-crawlability** for AI crawler optimization; **robots-txt** for allow/block decisions. [Vercel/MERJ study](https://vercel.com/blog/the-rise-of-the-ai-crawler) (2024)

## Content Best Practices

| Practice | Purpose |
|----------|---------|
| **Direct-answer format** | Answer specific questions in clear paragraphs |
| **Entity signals** | Clear brand, product, author identity; see **entity-seo** |
| **Citable paragraphs** | Each block understandable on its own |
| **Distribution** | Website, **YouTube** (Google prioritizes YouTube in search; ~78% of social media citations in AI Overviews come from YouTube + Reddit), forums, Reddit—thoughtful comments can outrank blog posts |

### Article-Level GEO

For blog posts and articles, structure content for AI citation. Studies find content with TL;DR, structured formats, and clear answers is cited substantially more by AI engines.

| Element | Guideline |
|---------|-----------|
| **TL;DR or Key Takeaways** | Choose one: **TL;DR** = 50–100 word bold summary paragraph; **Key Takeaways** = 5–7 bullet points; placed after intro |
| **QAE pattern** | Question (H2) → Answer (2 sentences) → Evidence (data, examples, lists) |
| **Answer-first** | Direct answer in first 40–60 words after each H2 |
| **Answer blocks** | 100–200 words per section; direct answer + context + evidence + nuance |
| **Structured formats** | Lists, tables, numbered steps increase citation rate |

See **article-content** for content creation; `dev/references/pages/content/article` for page structure.

## Parasite SEO & High-Authority Platforms

**Parasite SEO** = Placing content on high-authority platforms to leverage their domain strength for rankings and AI citation. See **parasite-seo** for full strategy.

**GitHub**: Tier 2 technical authority; very high AI citation. See **social** (GitHub reference) for repos, README, Pages, gists, awesome lists.

**YouTube**: Google prioritizes YouTube in search; YouTube citations in AI Overviews surged 25.21%. Long-form instructional and visual-demo videos dominate. See **social** (YouTube reference) for channel and video optimization; **video-optimization** for website-embedded video SEO.

**Grokipedia**: xAI's AI encyclopedia; ChatGPT, Perplexity, Copilot cite it. See **social** (Grokipedia reference) for adding recommendations or links. Contribute genuinely useful content; avoid manipulative placement (Google Site Reputation Abuse policy).

> **Source conflicts (kostja wins, ours flagged):** the AI Search Platforms and Retrieval tables above say Claude's search supplier is not publicly disclosed (Brave only for Claude for Government) and treat `Google-Extended` as a training crawler. The AI Search Landscape table and [references/platform-ranking-factors.md](references/platform-ranking-factors.md) below state that Claude uses Brave Search and that `Google-Extended` also controls Gemini grounding. Treat the latter as unconfirmed.

## Reference Routing

Start with this skill's core workflow. Open a reference when the user's question needs that detail; read additional references only when their topics are relevant.

| User questions | Local reference |
|---|---|
| Why can an agent not read our site? Are bot access, discovery files, or HTML blocking it? | [Agent readiness](references/agent-readiness.md) |
| Why are we cited but absent from the shortlist? Can our own buyer's guide help competitors? How should we measure recommendations? | [Citations vs. recommendations](references/citations-vs-recommendations.md) |
| How should we structure a definition, comparison, or FAQ? What makes an answer block useful on its own? | [Content patterns](references/content-patterns.md) |
| How does the approach differ for product pages, docs, local businesses, or ecommerce? Which content type should we improve? | [Content types](references/content-types.md) |
| Did an engine change which page formats it cites? Should we still invest in listicles or comparison pages? How do we separate a shift from noisy measurements? | [Format volatility](references/format-volatility.md) |
| Should we publish LinkedIn posts, articles, or company-page content? What makes that content discoverable and citable? | [LinkedIn citations](references/linkedin-ai-citations.md) |
| What belongs in an OKF bundle? Is it an established AI-search requirement or an emerging experiment? | [Open Knowledge Format](references/okf.md) |
| Where should we start for a particular AI engine? Which search and training crawlers should we distinguish? | [Platform ranking factors](references/platform-ranking-factors.md) |
| Why does AI describe our positioning incorrectly? How can third-party consensus reinforce a specific use case? | [Positioning and consensus](references/positioning-and-consensus.md) |
| How should a video's title, captions, chapters, or description support citations? What should we check before publishing? | [YouTube citations](references/youtube-ai-citations.md) |

Read these bundled files from this guide's folder; do not substitute a remote repository URL for a local reference. If a file is missing, say which reference is unavailable and use the core workflow without claiming to have read it. For time-sensitive statistics, platform behavior, or tool claims in any reference, check the source date and current primary documentation before making a recommendation.

## Before Starting (AI Visibility Context)

Gather this context (ask if not provided):

### 1. Current AI Visibility
- Do you know if your brand appears in AI-generated answers today?
- Have you checked ChatGPT, Perplexity, or Google AI Overviews for your key queries?
- What queries matter most to your business?

### 2. Content & Domain
- What type of content do you produce? (Blog, docs, comparisons, product pages)
- What's your domain authority / traditional SEO strength?
- Do you have existing structured data (schema markup)?

### 3. Goals
- Get cited as a source in AI answers?
- Appear in Google AI Overviews for specific queries?
- Compete with specific brands already getting cited?
- Optimize existing content or create new AI-optimized content?

### 4. Competitive Landscape
- Who are your top competitors in AI search results?
- Are they being cited where you're not?
- Do you have Wikipedia coverage or a presence on review sites?

## How AI Search Works

### The AI Search Landscape

| Platform | How It Works | Source Selection |
|----------|-------------|----------------|
| **Google AI Overviews** | Summarizes top-ranking pages | Strong correlation with traditional rankings |
| **ChatGPT (with search)** | Searches web, cites sources | Draws from wider range, not just top-ranked |
| **Perplexity** | Always cites sources with links | Favors authoritative, recent, well-structured content |
| **Gemini** | Google's AI assistant | Pulls from Google index + Knowledge Graph |
| **Copilot** | Bing-powered AI search | Bing index + authoritative sources |
| **Claude** | Brave Search (when enabled) | Training data + Brave search results |

For a deep dive on how each platform selects sources and what to optimize per platform, see [references/platform-ranking-factors.md](references/platform-ranking-factors.md).

### Key Difference from Traditional SEO

Traditional SEO gets you ranked. AI SEO gets you **cited**.

In traditional search, you need to rank on page 1. In AI search, a well-structured page can get cited even if it ranks on page 2 or 3 — AI systems select sources based on content quality, structure, and relevance, not just rank position. Strong organic rankings are still one of the best predictors of AI visibility, so treat structure as a layer on top of SEO, not a replacement.

**Critical stats** (they drift; re-check before quoting to a client, and distrust vendor stats with no source or date):
- AI Overviews appeared on ~45% of the keywords BrightEdge tracks, and position-one desktop CTR fell ~58% when one was present (Ahrefs, Dec 2025 data). Both are sample-specific, so don't forecast a site's traffic loss from them
- Adding statistics and citations raised visibility by roughly 30–40% in the original GEO study (Aggarwal et al., 2023)

### Google's Official Stance vs. Multi-Platform Reality

**Google's position** ([AI features optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)):
> "The best practices for SEO continue to be relevant because our generative AI features on Google Search are rooted in our core Search ranking and quality systems."

Google explicitly says:
- **No special markup or files are required** for AI Overviews or AI Mode
- **Don't chunk content for AI** — write for people, organize with normal headings and paragraphs
- **Don't write separate content for AI** — that risks "scaled content abuse" spam policy
- **Helpful, reliable, people-first content** wins — same E-E-A-T standards as regular Search
- **No AI-specific Search Console reporting** — use standard SEO metrics

**Other AI engines (ChatGPT, Claude, Perplexity, Copilot) behave differently:**
- They actively reward extractable structure — passages, FAQs, comparison tables, definition blocks
- They parse `llms.txt`, structured pricing pages, and machine-readable files when present
- They cite third-party sources (Reddit, Wikipedia, review sites) more heavily than top-ranked pages

**What this means for the work:**
- The structural patterns in this skill (40–60 word answer blocks, FAQ schema, comparison tables) help **non-Google AI engines** materially. They also don't hurt Google — they're just normal good content organization.
- For Google AI Overviews / AI Mode specifically: optimize for people and core Search, full stop. Strong E-E-A-T, original information, semantic HTML, clean indexability.
- For ChatGPT/Claude/Perplexity: layer on the extractable structure + llms.txt + machine-readable files.

When in doubt, default to "write for people, organize for clarity" — that satisfies both camps.

### Query Fan-Out (Google AI Search)

Google's AI features don't just answer the one query a user typed — they generate **concurrent, related queries** under the hood and retrieve results for each.

Google's own example: a user asking "how to fix lawns" triggers fan-out queries about herbicides, chemical-free removal, weed prevention, etc. The AI synthesizes across all of them.

**Implications:**
- Single-page-per-keyword targeting is less effective. Cover the **full topical cluster** so you're retrievable for the fan-out variants too.
- Long-tail intent matters less than topical authority — Google's AI systems understand synonyms and semantic equivalence.
- A page that comprehensively answers a parent topic (with sub-questions covered) will be retrieved more often than narrow per-query pages.

**Action**: when planning content, brainstorm the 5–10 related queries the AI is likely to fan out to and make sure your content (or your site as a whole) covers them.

ChatGPT fans out too — and you can extract its *literal* background queries for your niche via DevTools (method in [references/format-volatility.md](references/format-volatility.md)). Post-5.6, ChatGPT's fan-outs shifted away from "best/vs/top" modifiers toward `site:` and "official" searches — use the extraction to see where your category's fan-outs stand today.

## AI Visibility Audit

Before optimizing, assess your current AI search presence.

### Step 1: Check AI Answers for Your Key Queries

Test 10-20 of your most important queries across platforms:

| Query | Google AI Overview | ChatGPT | Perplexity | You Cited? | Competitors Cited? |
|-------|:-----------------:|:-------:|:----------:|:----------:|:-----------------:|
| [query 1] | Yes/No | Yes/No | Yes/No | Yes/No | [who] |
| [query 2] | Yes/No | Yes/No | Yes/No | Yes/No | [who] |

**Query types to test**, spread across buyer awareness stages and written the way people actually type into a chat box:
- Problem-aware: "How do I [problem your product solves]?"
- Solution-aware: "What is [your product category]?" / "Best [category] for [use case]"
- Product-aware: "[Your brand] vs [competitor]" / "Is [your brand] good for [use case]?"
- Most aware: "[Your brand] pricing" / "Does [your brand] integrate with [tool]?"

Keep the list to prompts that would change revenue. A citation for a glossary question ("what is gross profit?") rarely sells anything. Track prompts like keywords: collapse wording variants of the same intent into one core prompt, then run each several times.

### Step 2: Analyze Citation Patterns

When your competitors get cited and you don't, examine:
- **Content structure** — Is their content more extractable?
- **Authority signals** — Do they have more citations, stats, expert quotes?
- **Freshness** — Is their content more recently updated?
- **Schema markup** — Do they have structured data you're missing?
- **Third-party presence** — Are they cited via Wikipedia, Reddit, review sites?

**Turn findings into work.** If an assistant states something wrong or vague about you, the page that should state that fact isn't saying it plainly; fix that page first. If you're absent, the sources it cites for the prompt are your target list for PR, review sites, and directories.

### Step 3: Content Extractability Check

For each priority page, verify:

| Check | Pass/Fail |
|-------|-----------|
| Clear definition in first paragraph? | |
| Self-contained answer blocks (work without surrounding context)? | |
| Statistics with sources cited? | |
| Comparison tables for "[X] vs [Y]" queries? | |
| FAQ section with natural-language questions? | |
| Schema markup (FAQ, HowTo, Article, Product)? | |
| Expert attribution (author name, credentials)? | |
| Recently updated (within 6 months)? | |
| Heading structure matches query patterns? | |
| AI crawler policy matches discovery and training goals? | |

### Step 4: AI Bot Access Check

Audit AI user agents by purpose. Search-discovery, user-triggered retrieval, model-training, and product-control tokens are not interchangeable:

- **Search discovery:** `OAI-SearchBot` (ChatGPT), `PerplexityBot`, `Claude-SearchBot`, and the conventional search crawlers that feed an answer product
- **User-triggered retrieval:** `ChatGPT-User`, `Claude-User`, and `Perplexity-User`; vendor handling can differ from automatic crawlers, so verify the current documentation
- **Potential model training:** `GPTBot` and `ClaudeBot`
- **Google product control:** `Google-Extended` controls certain Gemini training and grounding uses of content Google already crawls; it does not affect Google Search inclusion or ranking

Check each relevant user-agent group and any WAF or CDN rules separately. A publisher can allow search discovery while disallowing model-development crawlers; do not infer that blocking a training crawler necessarily blocks citations.

See [references/platform-ranking-factors.md](references/platform-ranking-factors.md) for the full robots.txt configuration.

## Optimization Strategy

### The Three Pillars

```
1. Structure (make it extractable)
2. Authority (make it citable)
3. Presence (be where AI looks)
```

### Pillar 1: Structure — Make Content Extractable

AI systems extract passages, not pages. Every key claim should work as a standalone statement.

**Content block patterns:**
- **Definition blocks** for "What is X?" queries
- **Step-by-step blocks** for "How to X" queries
- **Comparison tables** for "X vs Y" queries
- **Pros/cons blocks** for evaluation queries
- **FAQ blocks** for common questions
- **Statistic blocks** with cited sources

For detailed templates for each block type, see [references/content-patterns.md](references/content-patterns.md).

**Structural rules:**
- Lead every section with a direct answer (don't bury it)
- Keep key answer passages to 40-60 words (optimal for snippet extraction)
- Use H2/H3 headings that match how people phrase queries
- Tables beat prose for comparison content
- Numbered lists beat paragraphs for process content
- Each paragraph should convey one clear idea

### Pillar 2: Authority — Make Content Citable

AI systems prefer sources they can trust. Build citation-worthiness.

**The Princeton GEO research** (KDD 2024, studied across Perplexity.ai) ranked 9 optimization methods:

| Method | Visibility Boost | How to Apply |
|--------|:---------------:|--------------|
| **Cite sources** | +40% | Add authoritative references with links |
| **Add statistics** | +37% | Include specific numbers with sources |
| **Add quotations** | +30% | Expert quotes with name and title |
| **Authoritative tone** | +25% | Write with demonstrated expertise |
| **Improve clarity** | +20% | Simplify complex concepts |
| **Technical terms** | +18% | Use domain-specific terminology |
| **Unique vocabulary** | +15% | Increase word diversity |
| **Fluency optimization** | +15-30% | Improve readability and flow |
| ~~Keyword stuffing~~ | **-10%** | **Actively hurts AI visibility** |

**Best combination:** Fluency + Statistics = maximum boost. Low-ranking sites benefit even more — up to 115% visibility increase with citations.

**Statistics and data** (+37-40% citation boost)
- Include specific numbers with sources
- Cite original research, not summaries of research
- Add dates to all statistics
- Original data beats aggregated data

**Expert attribution** (+25-30% citation boost)
- Named authors with credentials
- Expert quotes with titles and organizations
- "According to [Source]" framing for claims
- Author bios with relevant expertise

**Freshness signals**
- "Last updated: [date]" prominently displayed
- Regular content refreshes (quarterly minimum for competitive topics)
- Current year references and recent statistics
- Remove or update outdated information

**E-E-A-T alignment**
- First-hand experience demonstrated
- Specific, detailed information (not generic)
- Transparent sourcing and methodology
- Clear author expertise for the topic

### Pillar 3: Presence — Be Where AI Looks

AI systems don't just cite your website — they cite where you appear.

**Third-party sources matter more than your own site:**
- Wikipedia mentions (7.8% of all ChatGPT citations)
- Reddit discussions (volatile: ~1.8% of ChatGPT citations historically, but nearly wiped from ChatGPT by Aug 2026 retrieval changes — still retrieved elsewhere; see the volatility section in [references/agent-readiness.md](references/agent-readiness.md))
- Industry publications and guest posts
- LinkedIn — among the most-cited domains for professional queries, but which surface gets cited depends on the engine (ChatGPT now favors posts over articles; Gemini barely cites LinkedIn). Front-load the target phrase, since a post's first words become its URL slug. See [references/linkedin-ai-citations.md](references/linkedin-ai-citations.md)
- Review sites (G2, Capterra, TrustRadius for B2B SaaS)
- YouTube (frequently cited by Google AI Overviews)
- Podcasts (episodes get transcribed, show notes published — both get crawled and cited)
- Quora answers

**Actions:**
- Ensure your Wikipedia page is accurate and current
- Participate authentically in Reddit communities — but as one surface in a portfolio, never the whole strategy (citation mixes shift overnight with retrieval updates)
- Get featured in industry roundups and comparison articles
- Make every third-party profile (G2, Capterra, Gartner, Crunchbase, LinkedIn) describe you with the same segment and positioning as your About page; models look for consensus. For repositioning, mergers, and head terms, see [references/positioning-and-consensus.md](references/positioning-and-consensus.md)
- Create YouTube content for key how-to queries — models don't watch the video, they read the text layer around it; see [references/youtube-ai-citations.md](references/youtube-ai-citations.md) for the full anatomy (transcript, captions, chapters, description, pinned comment)
- Guest on podcasts in your category (prep with the podcast guest prep in **public-relations**)
- Answer relevant Quora questions with depth

### Machine-Readable Files for AI Agents

> **Google's stance**: not required for AI Overviews or AI Mode. Their guide explicitly says you don't need new markup, AI files, or markdown to appear in generative AI search.
>
> **Why include them anyway**: non-Google AI engines (ChatGPT, Claude, Perplexity) and autonomous buying agents do reward extractable structure. The files below help with those engines without harming Google.

AI agents aren't just answering questions — they're becoming buyers. When an AI agent evaluates tools on behalf of a user, it needs structured, parseable information. If your pricing is locked in a JavaScript-rendered page or a "contact sales" wall, agents will skip you and recommend competitors whose information they can actually read.

**Audit this layer first**: [references/agent-readiness.md](references/agent-readiness.md) — the access/discovery/parseability checklist, free scoring tools (`npx is-agentic`, Frase's checker), Markdown content negotiation + `Link` headers, `llms-full.txt`, and the emerging agent-*actionable* layer (WebMCP).

Add these machine-readable files to your site root:

**`/pricing.md` or `/pricing.txt`** — Structured pricing data for AI agents

```markdown
# Pricing — [Your Product Name]

## Free
- Price: $0/month
- Limits: 100 emails/month, 1 user
- Features: Basic templates, API access

## Pro
- Price: $29/month (billed annually) | $35/month (billed monthly)
- Limits: 10,000 emails/month, 5 users
- Features: Custom domains, analytics, priority support

## Enterprise
- Price: Custom — contact sales@example.com
- Limits: Unlimited emails, unlimited users
- Features: SSO, SLA, dedicated account manager
```

**Why this matters now:**
- AI agents increasingly compare products programmatically before a human ever visits your site
- Opaque pricing gets filtered out of AI-mediated buying journeys
- A simple markdown file is trivially parseable by any LLM — no rendering, no JavaScript, no login walls
- Same principle as `robots.txt` (for crawlers), `llms.txt` (for AI context), and `AGENTS.md` (for agent capabilities)

**Best practices:**
- Use consistent units (monthly vs. annual, per-seat vs. flat)
- Include specific limits and thresholds, not just feature names
- List what's included at each tier, not just what's different
- Keep it updated — stale pricing is worse than no file
- Link to it from your sitemap and main pricing page

**`/llms.txt`** — Context file for AI systems (see [llmstxt.org](https://llmstxt.org))

If you don't have one yet, add an `llms.txt` that gives AI systems a quick overview of what your product does, who it's for, and links to key pages (including your pricing).

**`/okf/` — Open Knowledge Format bundle (Google-backed, v0.1)**

Google [introduced OKF](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) in June 2026 — a markdown spec for representing site content as a directory of cross-linked files with YAML frontmatter, agent-readable without scraping. Built primarily for data-team catalog metadata; the site-readable-by-agents repurposing was popularized by Suganthan Mohanadasan. No confirmed AI-search ranking signal today — treat it as protocol-layer registration like early schema.org. **For the full breakdown, implementation paths (free generator, WordPress plugin, by-hand), hosting guidance, and when to skip, see [references/okf.md](references/okf.md).**

### Schema Markup for AI

Structured data helps AI systems understand your content. Key schemas:

| Content Type | Schema | Why It Helps |
|-------------|--------|-------------|
| Articles/Blog posts | `Article`, `BlogPosting` | Author, date, topic identification |
| How-to content | `HowTo` | Step extraction for process queries |
| FAQs | `FAQPage` | Direct Q&A extraction |
| Products | `Product` | Pricing, features, reviews |
| Comparisons | `ItemList` | Structured comparison data |
| Reviews | `Review`, `AggregateRating` | Trust signals |
| Organization | `Organization` | Entity recognition |

Content with proper schema shows 30-40% higher AI visibility on non-Google AI engines. **Google's note**: structured data is "not required for generative AI search" but is recommended for overall SEO strategy. For implementation, use **schema-markup**.

## Agentic Experiences

Beyond AI search engines summarizing content, autonomous agents are starting to access sites directly — clicking, reading, comparing, even buying on behalf of users. Google's guide flags this as an emerging category to plan for.

**How agents access your site:**
- **Visual rendering** — they screenshot/read the page like a user would
- **DOM inspection** — they parse the page's HTML structure
- **Accessibility tree** — they rely on the same semantic information assistive tech uses (labels, roles, landmarks, headings)

**What to do:**
- **Render meaningful content without heavy JS gymnastics** — if the page is blank until 4 frameworks finish loading, agents see blank
- **Semantic HTML** — use `<main>`, `<nav>`, `<article>`, `<button>`, proper heading hierarchy, `alt` text on images
- **Clean accessibility tree** — every interactive element labelled; ARIA used correctly (or not at all when native HTML suffices)
- **Stable selectors / predictable layouts** — agents struggle with sites that re-render every interaction
- **Visible pricing, specs, contact info** — anything an agent would need to make a buying recommendation should be on a public, indexable page (this is where `/pricing.md` and similar files help)

**Emerging — Universal Commerce Protocol (UCP):**
Google references UCP as a forthcoming protocol that will give agents standardized hooks for commerce interactions (catalog discovery, pricing, checkout). Watch for adoption; for now, the structural recommendations above are the precursor.

For ecom and local business specifically, Google highlights:
- **Merchant Center feeds** + **Google Business Profile** for product/service visibility in AI Search
- **Business Agent** for conversational customer engagement (where applicable)

## Content Types That Get Cited Most

Not all content is equally citable — and the format mix is **volatile**. The long-standing baseline had comparison articles (~33%) and listicles (~10%) among the top citation earners, but **ChatGPT 5.6 (Aug 2026) demoted the exploited formats: listicle citations fell −50.5% and comparison-page citations −32.1%, while `site:` and "official" retrieval surged** — a shift toward primary sources and owned pages. Format strategy is now per-platform (comparisons still work on Google AIO/Gemini/Perplexity). See [references/format-volatility.md](references/format-volatility.md) for the shift data, the per-platform format table, and the ChatGPT fan-out extraction diagnostic.

**Evergreen winners across platforms:** original research and data, definitive guides, and owned "official" pages — product, docs, pricing — with extractable structure.

**Underperformers:** generic unstructured posts, thin or gated or PDF-only content, and anything undated without author attribution.

**Citation ≠ recommendation.** Getting cited means your content was useful to consult; getting *recommended* — onto the buyer's actual shortlist — is governed by web-wide consensus (reviews, forums, analysts, press) and is largely independent of your own content. Self-promotional "best [category]" listicles can even backfire for emerging brands: in one 100-query B2B study, 69% of the AI Overview citations that self-promotional listicles earned came in answers that recommended competitors instead of the publishing brand. See [references/citations-vs-recommendations.md](references/citations-vs-recommendations.md) for the visibility ladder (retrieved → cited → mentioned → recommended), stage-dependent buyer's-guide strategy, what earns recommendations, and the attribution blind spot.

## What NOT to Do

Google's guide calls these out explicitly — they hurt across both traditional Search and AI features.

1. **Write separate content "for AI"**. Same content should serve people and AI. Writing variants targeted at AI systems risks the **scaled content abuse spam policy** — Google's words.
2. **Chunk pages into AI-bait fragments**. Google's guide is direct: *"Don't break your content into tiny pieces for AI to better understand it."* Use normal paragraph + heading structure.
3. **Generate at scale for ranking manipulation**. AI-generated content is fine *if* it meets Search Essentials and spam policies. Mass-producing thin variations does not.
4. **Pursue inauthentic mentions**. Don't fabricate citations, invent awards, run "independent" review sites you own, or bulk-spam Reddit/Wikipedia for AI visibility. Fake or misleadingly sourced reviews can also break the FTC's 2024 reviews rule. Real participation only.
5. **Treat every AI user agent as the same control**. `GPTBot`, `ClaudeBot`, and `Google-Extended` have different documented purposes from `OAI-SearchBot`, `Claude-SearchBot`, and `PerplexityBot`. Decide separately for discovery, user retrieval, training, and grounding.
6. **Hide your main content behind JS that doesn't render**. Both core Search and AI agents need to see your content; JS-only rendering loses both audiences.
7. **Skip E-E-A-T fundamentals**. Author identity, first-hand experience, expertise signals, transparent sourcing — Google's guide leans heavily on these for AI features.

## AI SEO by Content Type

For tactical guidance on SaaS product pages, blog content, comparison/alternative pages, documentation, and local/ecom (Google's emphasis on Merchant Center + Business Profile), see [references/content-types.md](references/content-types.md).

## Tools

- GEO tracking and optimization tools for measuring AI citation and visibility

## Key Insight

ChatGPT traffic converts at significantly higher rates than Google search—studies report 2x to 9x uplift depending on industry. AI tool users often have clearer intent, but results vary by vertical.

## Output Format

- **Content structure** for AI citation
- **Entity** optimization; see **entity-seo**
- **Distribution** strategy
- **Measurement** approach

## Related Skills

- **site-crawlability**: AI crawler optimization; URL/redirect management
- **rendering-strategies**: SSR, SSG, CSR; content in initial HTML for AI crawlers
- **robots-txt**: AI crawler allow/block (GPTBot, ClaudeBot, PerplexityBot)
- **parasite-seo**: Parasite SEO strategy; high-authority platforms for GEO
- **social** (GitHub reference): GitHub for GEO; repos, README; Tier 2 technical authority
- **social** (YouTube reference): YouTube optimization; GEO distribution; Google prioritizes YouTube
- **serp-features**: **Strongly related**—AI Overviews, Bing Copilot, Yandex AI; platform comparison
- **featured-snippet**: Snippet optimization; overlaps with AI Overviews
- **entity-seo**: Entity signals; Organization, Person schema; GEO citation
- **article-content**: Article body creation; TL;DR, Key Takeaways, QAE pattern
- `dev/references/pages/content/article`: Article page structure; schema; layout
- `dev/references/pages/content/faq`: FAQ structure for GEO; citable Q&A blocks; content in initial HTML
- `dev/references/components/content/howto-section`: HowTo step sections; citable ordered procedures; HowTo JSON-LD
- **ai-traffic-tracking**: AI referral and citation measurement
- **seo-audit**: Traditional technical and on-page SEO audits
- **schema-markup**: Structured data that helps AI understand your content
- **content-strategy**: Planning what content to create
- **comparison-pages**: Comparison pages that get cited
- **programmatic-seo**: SEO pages at scale
- **copywriting**: Content that is both human-readable and AI-extractable
- **lead-magnets**: Packaging an owned course or content library as an installable agent skill (different from public-site AI visibility)
