---
name: ai-traffic-tracking
description: When the user wants to track AI search traffic in GA4 or GSC. Also use when the user mentions "AI traffic," "ChatGPT referral," "Perplexity traffic," "AI Overviews," "GA4 AI sources," "AI search analytics," "track AI referrals," "AI search traffic," "Claude traffic," or "how to track AI traffic." For AI SEO strategy, use generative-engine-optimization.
metadata:
  version: 1.0.1
---

# Analytics: AI Traffic

Guides tracking of AI-driven search traffic in Google Analytics 4 and Google Search Console.

## Initial Assessment

**Project context:** Read the product marketing context when present. Without it, use available project material or user-provided facts and ask for missing information.

Identify which AI sources already send visits, whether GA4 and Search Console are in place, and which prompts or pages you want to track.

## Scope

- **AI search traffic**: Track in GA4 and GSC; separate AI sources from organic referral
- **Google AI Overviews**: AI summary box in Google search (formerly SGE)
- **AI-driven search**: Traffic from ChatGPT, Perplexity, Gemini, Claude, Copilot, etc.

## Why Track Separately

- AI traffic is growing but GA4 often groups it as Referral, Organic, or Direct
- AI visitors may have stronger intent and higher conversion
- Separating AI Overviews from organic helps assess AI impact

## GA4: AI-Driven Search

### Option 1: Exploration Report (Recommended)

1. **Explore** →**Free form**
2. **Dimensions**: `Session source` (or `Session source / medium`)
3. **Metrics**: Sessions, Engagement rate, Event count, etc.
4. **Filters**: Add filter →`Session source` **Matches regex** →use regex below
5. Configure table, save report

**Regex (common AI sources):**

```
chatgpt\.com|openai\.com|openai|perplexity\.ai|perplexity|doubao\.com|chat\.qwen\.ai|copilot\.microsoft\.com|copilot\.com|(business\.)?gemini\.google|chat\.deepseek\.com|deepseek\.com|poe\.com|anthropic\.com|claude\.ai|bard\.google\.com|edgeservices\.bing\.com
```

### Option 2: Custom Channel Group

1. **Admin** →**Data Display** →**Channel Groups**
2. Copy default group, name e.g. "Default and AI Chatbots"
3. Add channel "AI Chatbots": `Source` **Matches regex** (same regex)
4. **Important**: Place "AI Chatbots" above "Referral" so it matches first
5. Save and use in Traffic Acquisition

### Option 3: Custom Report

1. **Reports** →**Library** →Create Detail Report
2. Use Traffic Acquisition template
3. Add filter: `Session source` **Matches regex** (same regex)
4. Save and add to menu

## Common AI Source Domains

| Platform | GA4 Source examples |
|----------|---------------------|
| ChatGPT | chatgpt.com, openai |
| Perplexity | perplexity.ai, perplexity |
| Copilot | copilot.com, copilot.microsoft.com |
| Gemini | business.gemini.google, gemini.google |
| Claude | claude.ai, anthropic.com |
| Bing Chat | edgeservices.bing.com |

## Google AI Overviews

- **GA4 + URL fragment**: Some AI Overview clicks add URL fragments; can use GTM (partial coverage)
- **GSC**: For AI Overviews analysis in GSC (filter, limitations), see **google-search-console**

## Tracking AI Visibility Beyond Referrals

Referral traffic is the smallest part of the AI touch. Pair the GA4 setup above with these.

### What to Track

| Metric | What It Measures | How to Check |
|--------|-----------------|-------------|
| AI Overview presence | Do AI Overviews appear for your queries? | Manual check or Semrush/Ahrefs |
| Brand citation rate | How often you're cited in AI answers | AI visibility tools (below) |
| Share of AI voice | Your citations vs. competitors | Peec AI, Otterly, ZipTie |
| Citation sentiment | How AI describes your brand | Manual review + monitoring tools |
| Recommendation rate | Whether you're on the shortlist, not just cited | Prompt tracking + mention framing |
| Source attribution | Which of your pages get cited | Referral traffic from AI sources (GA4 setup above) |

### AI Visibility Monitoring Tools

| Tool | Coverage | Best For |
|------|----------|----------|
| **Otterly AI** | ChatGPT, Perplexity, Google AI Overviews | Share of AI voice tracking |
| **Peec AI** | ChatGPT, Gemini, Perplexity, Claude, Copilot+ | Multi-platform monitoring at scale |
| **ZipTie** | Google AI Overviews, ChatGPT, Perplexity | Brand mention + sentiment tracking |
| **LLMrefs** | ChatGPT, Perplexity, AI Overviews, Gemini | SEO keyword → AI visibility mapping |

### DIY Monitoring (No Tools)

Monthly manual check:
1. Pick your top 20 queries
2. Run each through ChatGPT, Perplexity, and Google
3. Record: Are you cited? Who is? What page?
4. Log in a spreadsheet, track month-over-month

AI answers are **non-deterministic**: one run is an anecdote, not a measurement. Run each query 3-5 times per platform and track the mention *rate* with its sample size ("cited 3/5, n=5"), comparing rates over time rather than single runs. Keep the list to prompts that would change revenue.

### The Attribution Blind Spot

Visible AI referral traffic undercounts the AI touch. In SimilarWeb data, only about 9% of post-recommendation visits arrived as visible AI referrals; most came through branded search, direct, or other channels, indistinguishable from ordinary organic visitors.

- **Self-reported attribution**: add a "how did you hear about us?" field with an AI option and a follow-up ("What did you type?") so buyers hand you real prompts to track. ChatGPT referral UTMs undercount, and AI Overview revenue can't be separated from organic in analytics, so this field is often the clearest signal.
- Segment branded search and direct trends alongside the AI referral report. See **attribution** for reconciling these sources.

### Search Console Expectations

Google is explicit that there is **no AI-specific Search Console reporting**. AI Overviews and AI Mode use core Search ranking, so the standard reports (Performance, Coverage, Core Web Vitals) remain what you measure Google with. Third-party tools are the only way to see cross-platform AI citation behavior.

For the query-filter workaround that estimates AI Overview visibility, see **google-search-console**.

## Checklist

- [ ] AI sources identified in GA4 (Session Source)
- [ ] AI traffic Exploration report created
- [ ] Channel group updated with AI above Referral (if used)
- [ ] Custom report added to Library (optional)
- [ ] GTM + URL fragment for AI Overviews (optional)
- [ ] GSC AI-oriented query filter (optional; see **google-search-console**)

## Output Format

- **GA4 setup**: Exploration, channel group, or custom report
- **Regex**: Adapted to user's observed sources

## Related Skills

- **generative-engine-optimization**: GEO strategy; AI traffic tracking measures GEO impact
- **attribution**: AI as an attribution blind spot; reconciling sources
- **traffic-analysis**: Traffic sources, attribution, UTM
- **analytics-tracking**: GA4 events and conversions
- **google-search-console**: GSC AI traffic analysis
- **robots-txt**: AI crawler allow/block strategy
