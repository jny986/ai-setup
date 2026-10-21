---
name: content-strategy
description: When the user wants to plan content for SEO, create content calendar, or build topic clusters. Also use when the user mentions "content strategy," "content plan," "topic clusters," "pillar content," "pillar page," "cluster articles," "editorial calendar," "content hub," "content planning," "content clusters," "topic cluster strategy," "content strategy for SEO," or "content calendar." For editorial mix, use content-marketing.
metadata:
  version: 1.0.0
  based_on_repo: kostja94/marketing-skills, coreyhaines31/marketingskills
  based_on_version: v1.0.0(8dd89c5), v2.13.0(e85f3cb)
  based_on_skill: content-strategy, content-strategy
---

# SEO Content: Content Strategy

Guides content strategy for SEO: topic clusters, pillar pages, cluster articles, and editorial planning. For content marketing across all channels (blog, email, social, video), see **content-marketing**. For translation workflow and multilingual content, see **translation**.

## Initial Assessment

**Project context:** Read the product marketing context when present and load only what is relevant to this task. Otherwise use available project material or user-provided facts and ask for missing information.

Identify:
1. **Keywords**: From keyword research — see **keyword-research** for discovery and clustering
2. **Existing content**: What already exists
3. **Resources**: Content capacity, tools
4. **Goals**: Traffic, conversions, authority

**Product-Led SEO**: Do SEO around product/users, not around industry/search engines. See **seo-strategy** for Product-Led SEO principle, products suited for SEO, and workflow order.

## Topic Clusters

Topic clusters organize content by **topic** rather than isolated keywords. A **pillar page** covers a broad core topic; **cluster articles** cover subtopics; all connect via internal links. This signals topical authority to search engines and AI systems.

### Structure

```
Pillar page (broad topic, 2,000-5,000+ words)
    <-> internal links
Cluster 1 (subtopic, 800-2,500 words)
Cluster 2 (subtopic)
...
Cluster 6-12 (subtopics)
    <-> cluster to cluster links
```

### Pillar Page

| Attribute | Guideline |
|-----------|-----------|
| **Length** | 2,000-5,000+ words; comprehensive guide |
| **Keyword** | Broad head term with search volume |
| **Role** | Hub; links to all cluster articles; targets primary topic |
| **Conversion** | Link to product/feature pages where relevant |

### Cluster Articles

| Attribute | Guideline |
|-----------|-----------|
| **Count** | 6-12 articles per pillar (minimum 6 for authority) |
| **Length** | 800-2,500 words each; focused on one subtopic |
| **Keyword** | Long-tail, specific intent per article |
| **Links** | Each cluster links to pillar; pillar links back; related clusters link to each other |

### Internal Linking Model

| Link type | Purpose |
|-----------|---------|
| **Pillar to Cluster** | Hub distributes authority; users discover subtopics |
| **Cluster to Pillar** | Signals relationship; passes equity to hub |
| **Cluster to Cluster** | Related subtopics; strengthens topical coverage |

### Structure and Content Equally Important

**Framework and body quality both matter**: TOC, chapter logic, and content depth are all essential for SEO and UX. Weak structure undermines strong writing; weak writing undermines strong structure. Plan both from the start.

### Why Topic Clusters Work

- **Topical authority**: Rank for multiple variations; comprehensive coverage signals expertise
- **Avoid cannibalization**: One page per topic/keyword; no competing pages
- **Better internal linking**: Clear logic; crawlers understand structure
- **AI citations**: Clustered content gets ~42% more AI citations than standalone
- **Traffic**: ~30% more organic traffic; rankings hold ~2.5x longer

### Implementation Steps

1. **Choose 3-7 core topics** -> business relevance, search demand, competitive opportunity
2. **Map subtopics** -> People Also Ask, competitor analysis, keyword tools
3. **Content audit** -> Identify existing pages that can become pillar or cluster; find gaps
4. **Build clusters first** (optional) -> Cluster pages often rank first; add pillar after
5. **Create pillar** -> Comprehensive guide; link to all clusters
6. **Establish links** -> Pillar <-> cluster; cluster <-> cluster
7. **Update quarterly** -> Maintain freshness and authority

### Example

- **Pillar**: "SEO Guide" (targets "SEO")
- **Clusters**: "Technical SEO," "On-Page SEO," "Link Building," "Content SEO," "Local SEO," "E-E-A-T"

## Content Types

| Type | Use | SEO Fit |
|------|-----|---------|
| **How-to guides** | Informational intent; high share potential | High -> matches search intent |
| **Comparisons** | Commercial intent; "X vs Y" | High |
| **List posts** | "Top 10," "Best X" | High |
| **Glossaries** | Definition queries; internal link hub | High |
| **Tools/calculators** | Linkable assets; engagement | High |
| **Case studies** | Proof; conversion support | Medium -> supports conversion |
| **Funding / PR** | Funding rounds, acquisitions | Low -> brand/PR, not search-driven |
| **Product updates** | Feature launches, release notes | Low -> internal audience |
| **News / Trending** | Industry news, hot topics | Medium -> quick spikes, short shelf life |

### Evergreen vs Timely Content Mix

- **Evergreen** (70-75%): Pillar guides, how-tos, comparisons, glossaries. Drives long-term traffic, backlinks, authority. Refresh every 6-12 months.
- **Timely** (25-30%): Seasonal, trending, news. Generates quick traffic, shows topical relevance. Link timely pieces into evergreen pillars.
- **Balance**: Too much evergreen = blog feels stale; too much timely = irregular traffic, constant content churn.

## Editorial Calendar

- Map keywords to content pieces
- Prioritize by opportunity (volume -> intent -> feasibility)
- Schedule by capacity
- Include update schedule for existing content

## Information-Gain Gate

Before committing to a searchable piece, read the current top results for its query and write one sentence on what yours will add that none of them have: original data, a real product example, a working tool or template, a clearer answer, a stronger opinion. If you can't write that sentence, don't write the piece; it will be the eleventh copy of the same article, and neither Google nor AI assistants have a reason to prefer it.

## Additional Searchable Formats

- **Use-case content**: formula `[persona] + [use-case]` targets long-tail keywords ("Project management for designers", "Task tracking for developers").
- **Template libraries**: high-intent keywords plus product adoption ("marketing plan template"); provide standalone value and show how the product enhances the template.

## Identifying Pillars

1. **Product-led**: What problems does your product solve?
2. **Audience-led**: What does your ICP need to learn?
3. **Search-led**: What topics have volume in your space?
4. **Competitor-led**: What are competitors ranking for?

### Pillar Criteria

Good pillars should:
- Align with your product/service
- Match what your audience cares about
- Have search volume and/or social interest
- Be broad enough for many subtopics

## Keyword Research by Buyer Stage

Map topics to the buyer's journey using proven keyword modifiers:

### Awareness Stage
Modifiers: "what is," "how to," "guide to," "introduction to"

Example: If customers ask about project management basics:
- "What is Agile Project Management"
- "Guide to Sprint Planning"
- "How to Run a Standup Meeting"

### Consideration Stage
Modifiers: "best," "top," "vs," "alternatives," "comparison"

Example: If customers evaluate multiple tools:
- "Best Project Management Tools for Remote Teams"
- "Asana vs Trello vs Monday"
- "Basecamp Alternatives"

### Decision Stage
Modifiers: "pricing," "reviews," "demo," "trial," "buy"

Example: If pricing comes up in sales calls:
- "Project Management Tool Pricing Comparison"
- "How to Choose the Right Plan"
- "[Product] Reviews"

### Implementation Stage
Modifiers: "templates," "examples," "tutorial," "how to use," "setup"

Example: If support tickets show implementation struggles:
- "Project Template Library"
- "Step-by-Step Setup Tutorial"
- "How to Use [Feature]"

## Content Ideation Sources

### 1. Keyword Data

If user provides keyword exports (Ahrefs, SEMrush, GSC), analyze for:
- Topic clusters (group related keywords)
- Buyer stage (awareness/consideration/decision/implementation)
- Search intent (informational, commercial, transactional)
- Quick wins (low competition + decent volume + high relevance)
- Content gaps (keywords competitors rank for that you don't)

Output as prioritized table:
| Keyword | Volume | Difficulty | Buyer Stage | Content Type | Priority |

### 2. Call Transcripts

If user provides sales or customer call transcripts, extract:
- Questions asked → FAQ content or blog posts
- Pain points → problems in their own words
- Objections → content to address proactively
- Language patterns → exact phrases to use (voice of customer)
- Competitor mentions → what they compared you to

Output content ideas with supporting quotes.

### 3. Survey Responses

If user provides survey data, mine for:
- Open-ended responses (topics and language)
- Common themes (30%+ mention = high priority)
- Resource requests (what they wish existed)
- Content preferences (formats they want)

### 4. Forum Research

Use web search to find content ideas:

**Reddit:** `site:reddit.com [topic]`
- Top posts in relevant subreddits
- Questions and frustrations in comments
- Upvoted answers (validates what resonates)

**Quora:** `site:quora.com [topic]`
- Most-followed questions
- Highly upvoted answers

**Other:** Indie Hackers, Hacker News, Product Hunt, industry Slack/Discord

Extract: FAQs, misconceptions, debates, problems being solved, terminology used.

### 5. Competitor Analysis

Use web search to analyze competitor content:

**Find their content:** `site:competitor.com/blog`

**Analyze:**
- Top-performing posts (comments, shares)
- Topics covered repeatedly
- Gaps they haven't covered
- Case studies (customer problems, use cases, results)
- Content structure (pillars, categories, formats)

**Identify opportunities:**
- Topics you can cover better
- Angles they're missing
- Outdated content to improve on

### 6. Sales and Support Input

Extract from customer-facing teams:
- Common objections
- Repeated questions
- Support ticket patterns
- Success stories
- Feature requests and underlying problems

## Prioritizing Content Ideas

Score each idea on four factors:

### 1. Customer Impact (40%)
- How frequently did this topic come up in research?
- What percentage of customers face this challenge?
- How emotionally charged was this pain point?
- What's the potential LTV of customers with this need?

### 2. Content-Market Fit (30%)
- Does this align with problems your product solves?
- Can you offer unique insights from customer research?
- Do you have customer stories to support this?
- Will this naturally lead to product interest?

### 3. Search Potential (20%)
- What's the monthly search volume?
- How competitive is this topic?
- Are there related long-tail opportunities?
- Is search interest growing or declining?

### 4. Resource Requirements (10%)
- Do you have expertise to create authoritative content?
- What additional research is needed?
- What assets (graphics, data, examples) will you need?

### Scoring Template

| Idea | Customer Impact (40%) | Content-Market Fit (30%) | Search Potential (20%) | Resources (10%) | Total |
|------|----------------------|-------------------------|----------------------|-----------------|-------|
| Topic A | 8 | 9 | 7 | 6 | 8.0 |
| Topic B | 6 | 7 | 9 | 8 | 7.1 |

Score 1-10 per factor, multiply by the weight, sum for the total. Rank the list; make the top-scoring pieces first.

## Link-Earning Formats

When the goal of a piece is backlinks specifically, format choice matters more than production effort. Foundation Inc.'s B2B Backlink Intelligence Report (March 2026 — a single vendor study of B2B SaaS sites, so treat as directional) measured each format's share of backlinks relative to its share of pages:

| Format | Backlinks vs. page share |
|---|---|
| Statistics / data roundups | **4.25x** |
| Glossary / definition pages | 1.47x |
| Interactive tools / calculators (see **free-tools**) | 1.38x |
| How-to / tutorials | 1.36x |
| Original research / reports | 0.80x |
| Ultimate guides | 0.77x |
| Thought leadership | 0.74x |
| Templates / frameworks | 0.68x |

The counterintuitive read: **curating statistics earns ~5x the links of producing original research.** Writers link to whatever makes citation easiest — a maintained stat-roundup page is citation infrastructure, while original research often gets cited *via* the roundups that aggregate it. Implications: (1) publish a stats page for your category and keep it fresh — it's cheap and compounds, and citable one-line stats are also what LLMs lift, making it an AI-visibility play (see **generative-engine-optimization**); (2) when you do run original research, pair it with your own stat-roundup page that presents the findings as citable one-liners, so you capture the links your data generates. The formats at the bottom aren't dead — guides, templates, and thought leadership earn their keep on rankings, conversions, and brand. Judge each piece by the job it's for, and don't expect links from formats that don't earn them.

To get those assets in front of the people who link, and to point their authority at the pages that need it, see **link-building**.

## Output Format

- **Topic cluster** map (pillar + 6-12 clusters)
- **Content calendar** (topics, keywords, deadlines)
- **Internal linking** plan
- **Update plan** for existing content
- **Priority table**: keyword, volume, difficulty, buyer stage, content type, score (see Prioritizing Content Ideas)

## Headless CMS

Choosing, modelling and wiring a headless CMS for marketing content: [references/headless-cms.md](references/headless-cms.md).

## Related Skills

- **content-marketing**: Content types, formats, channels, repurposing; SEO content is one channel
- **translation**: Multilingual content; translation workflow, glossary; avoid thin translations
- **seo-strategy**: SEO workflow order, Product-Led SEO, audit approach; use when planning SEO from scratch
- **website-structure**: Plan which pages to build; structure informs content clusters and pillar placement
- **keyword-research**: Keywords drive content plan
- **programmatic-seo**: Programmatic SEO for scaling pages with template + data; complements topic clusters
- **content-optimization**: Word count, H2 keywords, keyword density, multimedia, lists -> on-page content optimization
- **internal-links**: Clusters need internal linking
- **link-building**: Content strategy creates linkable assets; earning links to the content and the pages it supports
- **heading-structure**: Content structure uses headings
- **generative-engine-optimization**: Optimizing content for AI search and LLM citations
- **seo-audit**: Technical SEO and on-page optimization
- **free-tools**: Interactive tools and calculators as link-earning assets
- **copywriting**: Writing individual content pieces
- **competitor-research**: Competitor content gaps for topic mapping
