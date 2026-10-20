# Skills

| Name | Based on | Agent invokable | Version | Author | Description |
|------|----------|-----------------|---------|--------|-------------|
| [agents-review](skills/agents-review) | — | No | 1.0.0 | jny986 | Refactor an AGENTS.md or CLAUDE.md into a minimal root file plus linked docs, following progressive disclosure. |
| [claude-handoff](skills/claude-handoff) | [mattpocock/skills](https://github.com/mattpocock/skills) | No | 1.0.0 | jny986 | Hand the current conversation off to a fresh background agent that picks up the work immediately. |
| [codebase-design](skills/codebase-design) | [mattpocock/skills](https://github.com/mattpocock/skills) | Yes | 1.0.0 | jny986 | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or when another skill needs the deep-module vocabulary. |
| [design](skills/design) | [ArnavPuri/designskills](https://github.com/ArnavPuri/designskills), [CosmoBlk/email-design](https://github.com/CosmoBlk/email-design), [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill), [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Yes | 1.0.0 | jny986 | Router for visual design work. Use to capture product context in PRODUCT.md, document a visual system in DESIGN.md, create brand kits, plan a UI, improve task flows, consolidate UI patterns, design or build UI and graphics, implement visual references, adapt interfaces, generate variants, or audit and refine an interface. Sub-skills: product, shape, document, brandkit, audit, flow, systematize, refine; plus reference guides per surface. |
| [diagnosing-bugs](skills/diagnosing-bugs) | [mattpocock/skills](https://github.com/mattpocock/skills) | Yes | 1.0.1 | jny986 | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. |
| [docs](skills/docs) | [mattpocock/skills](https://github.com/mattpocock/skills) | Yes | 1.0.0 | jny986 | Sharpen ideas through grilling, maintain planning docs, synthesize specs, and draft dependency-linked tickets. Sub-skills: me, docs, spec, tickets. |
| [git](skills/git) | — | Yes | 1.0.0 | jny986 | Router for git and PR workflows. Use for any commit, push, pull request, branch wrap-up, diff review, or merge/rebase conflict task. Sub-skills: commit, create-pr, finalise, code-review, review-prs, resolving-merge-conflicts. |
| [handoff](skills/handoff) | [mattpocock/skills](https://github.com/mattpocock/skills) | No | 1.0.0 | jny986 | Compact the current conversation into a handoff document for another agent to pick up. |
| [implement](skills/implement) | [mattpocock/skills](https://github.com/mattpocock/skills) | Yes | 2.0.0 | jny986 | Implement features, changes, specs and tickets with automatic context and page/component workflow selection. |
| [improve-codebase-architecture](skills/improve-codebase-architecture) | [mattpocock/skills](https://github.com/mattpocock/skills) | No | 1.0.1 | jny986 | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| [loop-me](skills/loop-me) | [mattpocock/skills](https://github.com/mattpocock/skills) | No | 1.0.0 | jny986 | Grill me about specs for the workflows I want to build, within this workspace. |
| [marketing](skills/marketing) | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills), [kostja94/pagina](https://github.com/kostja94/pagina), [kostja94/bricks](https://github.com/kostja94/bricks) | Yes | 1.0.0 | jny986 | Marketing playbooks for SaaS and software products. Use for any marketing, growth, or go-to-market task: copywriting and copy editing, CRO (landing pages, signup, onboarding, popups, paywalls), SEO (audits, AI search, schema, programmatic pages, site architecture), content and social, email, SMS and cold outreach, paid ads and ad creative, analytics, attribution and A/B tests, pricing and offers, launches, PR, events, partnerships, referrals and influencers, churn and retention, sales enablement, RevOps, prospecting, competitor and customer research, positioning and product marketing context, app store optimisation, and marketing images or video. Page and component builds hand off to the implement router’s build guides. |
| [prototype](skills/prototype) | [mattpocock/skills](https://github.com/mattpocock/skills) | Yes | 1.0.0 | jny986 | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should look like. |
| [research](skills/research) | [mattpocock/skills](https://github.com/mattpocock/skills) | Yes | 1.0.0 | jny986 | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent. |
| [security](skills/security) | [getsentry/skills](https://github.com/getsentry/skills), [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills), [affaan-m/ECC](https://github.com/affaan-m/ECC) | Yes | 1.0.0 | jny986 | Router for security work. Use to review code for vulnerabilities, build a feature securely, harden Docker, CI/CD, cloud or dependencies, or gate a release. Sub-skills: review-code, build-securely, harden-deployment, release-gate. |
| [setup](skills/setup) | [mattpocock/skills](https://github.com/mattpocock/skills) | Yes | 1.0.1 | jny986 | Set up a project to use jny986/ai-setup skills. Use to prepare AGENTS.md or CLAUDE.md, configure engineering workflows, migrate domain glossaries, or check project readiness. |
| [tdd](skills/tdd) | [mattpocock/skills](https://github.com/mattpocock/skills) | Yes | 1.0.1 | jny986 | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. |
| [teach](skills/teach) | [mattpocock/skills](https://github.com/mattpocock/skills) | No | 1.0.0 | jny986 | Teach the user a new skill or concept, within this workspace. |
| [to-questionnaire](skills/to-questionnaire) | [mattpocock/skills](https://github.com/mattpocock/skills) | No | 1.0.0 | jny986 | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. |
| [triage](skills/triage) | [mattpocock/skills](https://github.com/mattpocock/skills) | No | 1.0.1 | jny986 | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs. |
| [wait-what](skills/wait-what) | [mattpocock/skills](https://github.com/mattpocock/skills) | No | 1.0.1 | jny986 | Stop. That last message did not land: re-pitch it. |
| [wayfinder](skills/wayfinder) | [mattpocock/skills](https://github.com/mattpocock/skills) | No | 1.0.0 | jny986 | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear. |
| [what-to-use](skills/what-to-use) | [mattpocock/skills](https://github.com/mattpocock/skills) | No | 1.0.1 | jny986 | Ask which skill or flow fits your situation. A router over every skill in this repo, and any other skill available. |
| [wizard](skills/wizard) | [mattpocock/skills](https://github.com/mattpocock/skills) | Yes | 1.0.0 | jny986 | Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, or running a one-off migration or cutover. Don't invoke this for steps the agent can perform itself. |
| [writing-beats](skills/writing-beats) | [mattpocock/skills](https://github.com/mattpocock/skills) | No | 1.0.0 | jny986 | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it. |
| [writing-for-agents](skills/writing-for-agents) | [mattpocock/skills](https://github.com/mattpocock/skills) | Yes | 1.0.0 | jny986 | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md. |
| [writing-fragments](skills/writing-fragments) | [mattpocock/skills](https://github.com/mattpocock/skills) | No | 1.0.0 | jny986 | Writing, explore: mine raw fragments, no structure yet. |
| [writing-shape](skills/writing-shape) | [mattpocock/skills](https://github.com/mattpocock/skills) | No | 1.0.0 | jny986 | Writing, exploit: shape raw material into an article, paragraph by paragraph. |

<!-- marketing-sub-skills:start -->
## Marketing sub-skills

- **analytics** (5)
  - [ab-testing](skills/marketing/sub-skills/analytics/ab-testing.md) (v1.0.0, —): Designing A/B tests or running an experimentation program
  - [analytics-tracking](skills/marketing/sub-skills/analytics/tracking.md) (v1.3.1, —): Tracking setup: GA4, GTM, events, tracking plans, conversion tracking
  - [attribution](skills/marketing/sub-skills/analytics/attribution.md) (v1.0.0, —): Which channels drive revenue, attribution models, MMM, incrementality, first-party attribution
  - [seo-analytics](skills/marketing/sub-skills/analytics/seo.md) (v1.0.0, —): Search Console analysis and API; SEO data system: benchmarks, article database, indexing, traffic, keywords, backlinks
  - [traffic-analysis](skills/marketing/sub-skills/analytics/traffic.md) (v1.2.0, —): Traffic sources, dark traffic, UTM conventions, channel reporting, AI search traffic in GA4
- **channels** (17)
  - **community** (4)
    - [community-building](skills/marketing/sub-skills/channels/community/community-building.md) (v1.0.0, —): Building a community (Discord, Slack, forum) or advocates
    - [community-forum](skills/marketing/sub-skills/channels/community/community-forum.md) (v1.1.1, —): Promoting via forums and communities (Hacker News, Reddit, Indie Hackers), inviting users to a community
    - [directory-submission](skills/marketing/sub-skills/channels/community/directory-submission.md) (v1.2.0, —): Submitting to startup, SaaS, AI or review directories for backlinks, with ready-to-paste copy
    - [product-hunt-launch](skills/marketing/sub-skills/channels/community/product-hunt-launch.md) (v1.1.0, —): Planning and running a Product Hunt launch
  - **distribution** (2)
    - [aso](skills/marketing/sub-skills/channels/distribution/aso.md) (v1.0.0, —): App Store or Google Play listing optimisation
    - [distribution-channels](skills/marketing/sub-skills/channels/distribution/distribution-channels.md) (v1.1.1, —): Distribution via marketplaces, app stores and third-party platforms
  - **events** (1)
    - [events](skills/marketing/sub-skills/channels/events/events.md) (v1.0.0, —): Webinars, conferences, sponsorships, speaking, field events
  - **owned** (3)
    - [email-marketing](skills/marketing/sub-skills/channels/owned/email-marketing.md) (v1.0.1, —): Lifecycle email sequences, drips, nurture and welcome flows
    - [employee-generated-content](skills/marketing/sub-skills/channels/owned/employee-generated-content.md) (v1.0.1, —): Employee-led content and advocacy
    - [sms](skills/marketing/sub-skills/channels/owned/sms.md) (v1.0.0, —): SMS, MMS or WhatsApp marketing
  - **partnerships** (7)
    - [affiliate-marketing](skills/marketing/sub-skills/channels/partnerships/affiliate-marketing.md) (v1.0.1, —): Affiliate program strategy, commissions, recruitment
    - [co-marketing](skills/marketing/sub-skills/channels/partnerships/co-marketing.md) (v1.0.0, —): Partner marketing and joint campaigns
    - [creator-program](skills/marketing/sub-skills/channels/partnerships/creator-program.md) (v1.1.1, —): Running a creator program
    - [education-program](skills/marketing/sub-skills/channels/partnerships/education-program.md) (v1.0.1, —): Student, teacher and education programs
    - [influencer-marketing](skills/marketing/sub-skills/channels/partnerships/influencer-marketing.md) (v1.0.1, —): Creator, influencer or ambassador partnerships
    - [public-relations](skills/marketing/sub-skills/channels/partnerships/public-relations.md) (v1.1.0, —): Press coverage, journalist pitches, media strategy
    - [referral-program](skills/marketing/sub-skills/channels/partnerships/referral-program.md) (v1.0.1, —): Referral programs, word of mouth, reviews
- **content** (8)
  - [article-content](skills/marketing/sub-skills/content/article.md) (v1.1.1, —): Writing article bodies: blog posts, sub-skills, long-form pieces
  - [copy-editing](skills/marketing/sub-skills/content/copy-editing.md) (v1.0.0, jny986): Editing, proofreading or refreshing existing copy
  - [copywriting](skills/marketing/sub-skills/content/copywriting.md) (v1.2.0, —): Writing or rewriting page copy: headlines, value props, CTAs
  - [lead-magnets](skills/marketing/sub-skills/content/lead-magnets.md) (v1.0.0, jny986): Gated content, ebooks, checklists, templates for email capture
  - [podcast-marketing](skills/marketing/sub-skills/content/podcast.md) (v1.0.1, —): Podcast strategy, episodes, show notes and repurposing
  - [translation](skills/marketing/sub-skills/content/translation.md) (v2.0.0, —): Translating, transcreating or maintaining multilingual content
  - [video-marketing](skills/marketing/sub-skills/content/video.md) (v1.0.1, —): Video strategy and scripts, hooks, and producing video with AI tools or programmatic frameworks
  - [visual-content](skills/marketing/sub-skills/content/visual-content.md) (v1.0.1, —): Planning, generating or repurposing marketing images, social graphics, mockups, banners, OG images
- **paid-ads** (12)
  - **formats** (5)
    - [app-ads](skills/marketing/sub-skills/paid-ads/formats/app-ads.md) (v1.0.1, —): App install ads and user acquisition: Google App Campaigns, Apple Search Ads, CPI
    - [ctv-ads](skills/marketing/sub-skills/paid-ads/formats/ctv-ads.md) (v1.0.1, —): CTV, OTT and streaming TV ads
    - [directory-listing-ads](skills/marketing/sub-skills/paid-ads/formats/directory-listing-ads.md) (v1.0.1, —): Paid placements in directories and marketplaces (G2, Capterra, Shopify App Store)
    - [display-ads](skills/marketing/sub-skills/paid-ads/formats/display-ads.md) (v1.0.1, —): Display, banner and ad-network campaigns
    - [native-ads](skills/marketing/sub-skills/paid-ads/formats/native-ads.md) (v1.0.1, —): Native ads on Taboola, Outbrain and similar
  - **platforms** (6)
    - [google-ads](skills/marketing/sub-skills/paid-ads/platforms/google-ads.md) (v1.4.1, —): Setting up or optimising Google Ads: Search, Performance Max, RSAs, Quality Score, PMF testing with ads
    - [linkedin-ads](skills/marketing/sub-skills/paid-ads/platforms/linkedin-ads.md) (v1.2.0, —): LinkedIn Ads: Campaign Manager, Lead Gen Forms, Sponsored Messaging, B2B and ABM
    - [meta-ads](skills/marketing/sub-skills/paid-ads/platforms/meta-ads.md) (v1.1.1, —): Meta (Facebook/Instagram) Ads: Advantage+, Pixel and CAPI, lookalikes, Andromeda, kill/scale rules
    - [reddit-ads](skills/marketing/sub-skills/paid-ads/platforms/reddit-ads.md) (v1.0.1, —): Reddit Ads: promoted posts, subreddit targeting, native creative
    - [tiktok-ads](skills/marketing/sub-skills/paid-ads/platforms/tiktok-ads.md) (v1.0.1, —): TikTok Ads: In-Feed, TopView, Spark Ads, vertical creative
    - [youtube-ads](skills/marketing/sub-skills/paid-ads/platforms/youtube-ads.md) (v1.0.1, —): YouTube video ads: TrueView, Bumper, Discovery, format selection
  - [ad-creative](skills/marketing/sub-skills/paid-ads/ad-creative.md) (v1.0.0, jny986): Generating or iterating ad copy and creative at scale: static templates, hooks, video ad formats, creative strategy
- **platforms** (1)
  - [social](skills/marketing/sub-skills/platforms/social.md) (v1.0.0, jny986): Social content, scheduling and listening on LinkedIn, X, Instagram, TikTok, Reddit, Pinterest, Medium, YouTube, GitHub, Grokipedia
- **sales** (4)
  - [cold-email](skills/marketing/sub-skills/sales/cold-email.md) (v1.0.0, —): Cold outbound emails, follow-ups, sending setup, multichannel cadences
  - [prospecting](skills/marketing/sub-skills/sales/prospecting.md) (v1.0.0, —): Finding and qualifying prospects to build an outreach list
  - [revops](skills/marketing/sub-skills/sales/revops.md) (v1.0.0, —): Lead lifecycle, lead scoring, routing, marketing-to-sales handoff
  - [sales-enablement](skills/marketing/sub-skills/sales/sales-enablement.md) (v1.0.0, —): Sales decks, one-pagers, objection handling, demo scripts
- **seo** (35)
  - **content** (6)
    - [comparison-pages](skills/marketing/sub-skills/seo/content/comparison-pages.md) (v1.0.0, —): Strategy and content for comparison, "vs" and alternative pages
    - [competitor-research](skills/marketing/sub-skills/seo/content/competitor-research.md) (v1.2.1, —): Analysing or profiling competitors (keywords, content, backlinks, positioning) from names or URLs
    - [content-optimization](skills/marketing/sub-skills/seo/content/content-optimization.md) (v1.2.1, —): Optimising an article: length, headings, keyword placement, multimedia
    - [content-strategy](skills/marketing/sub-skills/seo/content/content-strategy.md) (v1.1.1, —): SEO content plans: topic clusters, pillar pages, editorial calendar, content prioritisation
    - [eeat-signals](skills/marketing/sub-skills/seo/content/eeat-signals.md) (v1.0.1, —): E-E-A-T, author and trust signals
    - [keyword-research](skills/marketing/sub-skills/seo/content/keyword-research.md) (v1.3.1, —): Keyword discovery, intent, clustering
  - **off-page** (2)
    - [backlink-analysis](skills/marketing/sub-skills/seo/off-page/backlink-analysis.md) (v1.0.1, —): Analysing backlink profiles and link gaps
    - [link-building](skills/marketing/sub-skills/seo/off-page/link-building.md) (v1.0.1, —): Earning backlinks and outreach
  - **on-page** (14)
    - [featured-snippet](skills/marketing/sub-skills/seo/on-page/featured-snippet.md) (v1.0.1, —): Winning featured snippets and position zero
    - [heading-structure](skills/marketing/sub-skills/seo/on-page/heading.md) (v2.0.0, —): H1-H6 structure and hierarchy
    - [image-optimization](skills/marketing/sub-skills/seo/on-page/image-optimization.md) (v1.2.1, —): Image SEO: alt text, formats, lazy loading, image sitemaps, OG images
    - [internal-links](skills/marketing/sub-skills/seo/on-page/internal-links.md) (v1.0.1, —): Internal linking and anchor text
    - [meta-description](skills/marketing/sub-skills/seo/on-page/description.md) (v2.0.0, —): Writing or auditing meta descriptions
    - [open-graph](skills/marketing/sub-skills/seo/on-page/open-graph.md) (v2.0.0, —): Open Graph tags and social previews
    - [page-metadata](skills/marketing/sub-skills/seo/on-page/metadata.md) (v2.0.0, —): Sitewide metadata audit, implementation and release checks
    - [schema-markup](skills/marketing/sub-skills/seo/on-page/schema.md) (v1.5.0, —): Schema markup, structured data, JSON-LD
    - [serp-features](skills/marketing/sub-skills/seo/on-page/serp-features.md) (v1.1.0, —): SERP features, rich results, zero-click patterns
    - [title-tag](skills/marketing/sub-skills/seo/on-page/title.md) (v2.0.0, —): Writing or auditing title tags
    - [twitter-cards](skills/marketing/sub-skills/seo/on-page/twitter-cards.md) (v2.0.0, —): Twitter/X card tags
    - [url-slug](skills/marketing/sub-skills/seo/on-page/url-slug.md) (v1.0.1, —): Creating or validating URL slugs for content pages
    - [url-structure](skills/marketing/sub-skills/seo/on-page/url-structure.md) (v1.1.0, —): Site-wide URL structure and hierarchy
    - [video-optimization](skills/marketing/sub-skills/seo/on-page/video-optimization.md) (v1.0.1, —): Video SEO: VideoObject, video sitemaps, key moments
  - **technical** (9)
    - [canonical-tag](skills/marketing/sub-skills/seo/technical/canonical.md) (v1.0.1, —): Canonical tags and duplicate content
    - [core-web-vitals](skills/marketing/sub-skills/seo/technical/core-web-vitals.md) (v1.0.2, —): LCP, INP, CLS and page speed
    - [indexing](skills/marketing/sub-skills/seo/technical/indexing.md) (v1.0.1, —): Getting pages indexed; indexing problems
    - [indexnow](skills/marketing/sub-skills/seo/technical/indexnow.md) (v1.0.1, —): IndexNow instant URL submission
    - [mobile-friendly](skills/marketing/sub-skills/seo/technical/mobile-friendly.md) (v1.1.2, —): Mobile-friendliness and mobile-first indexing
    - [rendering-strategies](skills/marketing/sub-skills/seo/technical/rendering-strategies.md) (v1.0.2, —): SSR, SSG, CSR and rendering for SEO
    - [robots-txt](skills/marketing/sub-skills/seo/technical/robots.md) (v1.2.0, —): robots.txt rules and crawler access
    - [site-crawlability](skills/marketing/sub-skills/seo/technical/crawlability.md) (v1.2.1, —): Crawlability, crawl budget, site structure for bots
    - [xml-sitemap](skills/marketing/sub-skills/seo/technical/sitemap.md) (v1.1.0, —): XML sitemaps: structure, submission, segmentation
  - [entity-seo](skills/marketing/sub-skills/seo/entity-seo.md) (v1.0.1, —): Entities, Knowledge Panel, @id and sameAs
  - [local-seo](skills/marketing/sub-skills/seo/local.md) (v1.0.1, —): Local search, Google Business Profile, NAP
  - [parasite-seo](skills/marketing/sub-skills/seo/parasite-seo.md) (v1.1.0, —): Ranking through third-party high-authority platforms
  - [programmatic-seo](skills/marketing/sub-skills/seo/programmatic-seo.md) (v1.4.1, —): Template-driven SEO pages at scale
- **strategies** (40)
  - **brand** (9)
    - [brand-monitoring](skills/marketing/sub-skills/strategies/brand/brand-monitoring.md) (v1.0.1, —): Tracking brand mentions, sentiment and reputation
    - [brand-protection](skills/marketing/sub-skills/strategies/brand/brand-protection.md) (v1.0.1, —): Trademarks, impersonation, brand abuse and takedowns
    - [brand-visual](skills/marketing/sub-skills/strategies/brand/brand-visual.md) (v1.4.0, —): Visual identity: typography, colours, design tokens, brand style guide
    - [branding](skills/marketing/sub-skills/strategies/brand/branding.md) (v1.2.0, —): Brand purpose, values, story, voice, narrative, brand guidelines
    - [content-marketing](skills/marketing/sub-skills/strategies/brand/content-marketing.md) (v1.2.1, —): Content types, formats, funnel mapping and repurposing across channels
    - [integrated-marketing](skills/marketing/sub-skills/strategies/brand/integrated-marketing.md) (v1.1.1, —): Coordinating channels with the PESO model and a consistent message
    - [marketing-psychology](skills/marketing/sub-skills/strategies/brand/marketing-psychology.md) (v1.0.0, jny986): Applying behavioural science, biases or mental models to marketing
    - [product-marketing](skills/marketing/sub-skills/strategies/brand/product-marketing.md) (v1.0.0, jny986): Creating or updating the product marketing context doc (positioning, ICP, audience)
    - [rebranding-strategy](skills/marketing/sub-skills/strategies/brand/rebranding.md) (v1.0.1, —): Rebrand execution: domain change, redirects, migration, announcement
  - **commercial** (11)
    - **domain** (3)
      - [domain-architecture](skills/marketing/sub-skills/strategies/commercial/domain/domain-architecture.md) (v1.0.1, —): Subdomain, subfolder or separate domain decisions
      - [domain-selection](skills/marketing/sub-skills/strategies/commercial/domain/domain-selection.md) (v1.0.1, —): Choosing a domain name and TLD
      - [multi-domain-brand-seo](skills/marketing/sub-skills/strategies/commercial/domain/multi-domain-brand-seo.md) (v1.0.1, —): SEO and brand when several domains coexist
    - **pricing** (3)
      - [discount-marketing-strategy](skills/marketing/sub-skills/strategies/commercial/pricing/discount-marketing.md) (v1.1.1, —): Promotional pricing: annual, lifetime deals, seasonal, startup and referral discounts
      - [offers](skills/marketing/sub-skills/strategies/commercial/pricing/offers.md) (v1.0.0, jny986): Designing the offer itself: bonuses, guarantees, urgency, naming
      - [pricing-strategy](skills/marketing/sub-skills/strategies/commercial/pricing/pricing-strategy.md) (v1.0.1, —): Pricing, packaging, tiers, freemium or trials
    - [free-tools](skills/marketing/sub-skills/strategies/commercial/free-tools.md) (v1.0.0, jny986): Building a free tool (calculator, grader) for leads or SEO
    - [generative-engine-optimization](skills/marketing/sub-skills/strategies/commercial/geo.md) (v1.4.0, —): Getting cited by AI search and LLMs (AEO, GEO, llms.txt)
    - [localization-strategy](skills/marketing/sub-skills/strategies/commercial/localization.md) (v2.0.0, —): Market and locale selection, multilingual rollout, localisation architecture
    - [open-source-strategy](skills/marketing/sub-skills/strategies/commercial/open-source.md) (v1.0.1, —): Open source as a growth and commercialisation path
    - [paid-ads-strategy](skills/marketing/sub-skills/strategies/commercial/paid-ads.md) (v1.7.0, —): Paid campaigns: targeting, bidding, budgets, optimisation
  - **conversion** (5)
    - [conversion-optimization](skills/marketing/sub-skills/strategies/conversion/conversion-optimization.md) (v1.1.1, —): Improving conversions on a marketing page, form or funnel: page analysis, CRO process, experiment prioritisation
    - [onboarding](skills/marketing/sub-skills/strategies/conversion/onboarding.md) (v1.0.0, —): Post-signup activation, first-run experience, time to value
    - [paywalls](skills/marketing/sub-skills/strategies/conversion/paywalls.md) (v1.0.0, —): In-app paywalls, upgrade screens, feature gates, upsells
    - [popups](skills/marketing/sub-skills/strategies/conversion/popups.md) (v1.0.0, —): Popups, modals, slide-ins, exit intent, banners
    - [signup](skills/marketing/sub-skills/strategies/conversion/signup.md) (v1.0.0, —): Signup, registration or trial-start flows
  - **launch** (10)
    - [cold-start-strategy](skills/marketing/sub-skills/strategies/launch/cold-start.md) (v1.3.0, —): Getting first users with zero traction (0 to 1)
    - [customer-research](skills/marketing/sub-skills/strategies/launch/customer-research.md) (v1.0.0, —): Interviews, surveys, reviews, transcripts, personas, JTBD, voice of customer
    - [growth-funnel](skills/marketing/sub-skills/strategies/launch/growth-funnel.md) (v1.1.1, —): AARRR growth funnel, bottlenecks, lifecycle actions
    - [gtm-strategy](skills/marketing/sub-skills/strategies/launch/gtm.md) (v1.2.0, —): A GTM strategy or a full 12-month marketing plan: GTM mode, ICP, market entry, repositioning, AARRR
    - [indie-hacker-strategy](skills/marketing/sub-skills/strategies/launch/indie-hacker.md) (v1.1.1, —): Indie hacker and bootstrapped founder growth, build in public
    - [marketing-ideas](skills/marketing/sub-skills/strategies/launch/marketing-ideas.md) (v1.0.0, —): Brainstorming growth ideas or tactics when stuck
    - [pmf-strategy](skills/marketing/sub-skills/strategies/launch/pmf.md) (v1.1.1, —): Validating or measuring product-market fit before scaling
    - [product-launch](skills/marketing/sub-skills/strategies/launch/product-launch.md) (v1.2.0, —): Product launches, feature announcements, changelogs and release notes, waitlists, site go-live
    - [research-sources](skills/marketing/sub-skills/strategies/launch/research-sources.md) (v1.1.1, —): Information sources for content ideas, competitor monitoring, industry tracking
    - [retention-strategy](skills/marketing/sub-skills/strategies/launch/retention.md) (v1.1.1, —): Churn, retention, cancel flows, save offers, dunning, failed payments
  - **operations** (2)
    - [marketing-council](skills/marketing/sub-skills/strategies/operations/marketing-council.md) (v1.0.0, —): Multiple expert perspectives or a simulated advisory board on a marketing question
    - [marketing-loops](skills/marketing/sub-skills/strategies/operations/marketing-loops.md) (v1.0.0, —): A recurring, agent-run marketing workflow on a cadence
  - **structure** (3)
    - [seo-audit](skills/marketing/sub-skills/strategies/structure/seo-audit.md) (v1.1.0, —): Auditing or diagnosing technical and on-page SEO
    - [seo-strategy](skills/marketing/sub-skills/strategies/structure/seo.md) (v1.3.0, —): Organic SEO strategy, workflow order and prioritisation
    - [website-structure](skills/marketing/sub-skills/strategies/structure/website-structure.md) (v1.5.0, —): Which pages to build, page hierarchy, navigation and site structure
<!-- marketing-sub-skills:end -->

<!-- git-sub-skills:start -->
## Git sub-skills

- [code-review](skills/git/sub-skills/code-review.md) (v1.0.0, jny986): Review changes since a commit, branch, tag or merge-base, against repo standards, the spec and security
- [commit](skills/git/sub-skills/commit.md) (v1.0.0, jny986): Commit and push the current work, on the branch its ticket calls for
- [create-pr](skills/git/sub-skills/create-pr.md) (v1.0.0, jny986): Open a GitHub PR from the current branch (commits and pushes first if needed)
- [finalise](skills/git/sub-skills/finalise.md) (v1.0.0, jny986): The user explicitly asks to finalise a branch whose dev work is done: review, fix findings, then open the PR
- [resolving-merge-conflicts](skills/git/sub-skills/resolving-merge-conflicts.md) (v1.0.0, jny986): A merge or rebase is in progress with conflicts
- [review-prs](skills/git/sub-skills/review-prs.md) (v1.0.0, jny986): Review the open PRs awaiting the user's review, asking continue or skip for each
<!-- git-sub-skills:end -->

<!-- security-sub-skills:start -->
## Security sub-skills

- [build-securely](skills/security/sub-skills/build-securely.md) (v1.0.0, jny986): Design or write a feature that handles input, auth, data, external calls, LLMs or personal data
- [harden-deployment](skills/security/sub-skills/harden-deployment.md) (v1.0.0, jny986): Secure Dockerfiles, CI/CD, cloud, secrets or dependencies
- [release-gate](skills/security/sub-skills/release-gate.md) (v1.0.0, jny986): Final check before merging or deploying
- [review-code](skills/security/sub-skills/review-code.md) (v1.0.0, jny986): Audit existing code or a diff for vulnerabilities
<!-- security-sub-skills:end -->

<!-- design-sub-skills:start -->
## Design sub-skills

- [audit](skills/design/sub-skills/audit.md) (v1.0.0, jny986): Audit an existing website or app interface: UX, visual design, accessibility, performance, responsive behavior, and implementation
- [brandkit](skills/design/sub-skills/brandkit.md) (v1.0.0, jny986): Create a project brand kit: written identity guide, HTML specimen, or presentation image
- [document](skills/design/sub-skills/document.md) (v1.0.0, jny986): Document the current UI system or seed an approved direction in `DESIGN.md`
- [flow](skills/design/sub-skills/flow.md) (v1.0.0, jny986): Design or improve a task journey: steps, forms, onboarding, interface copy, feedback, and recovery
- [product](skills/design/sub-skills/product.md) (v1.0.0, jny986): Capture or update confirmed product facts, users, jobs, and constraints in `PRODUCT.md`
- [refine](skills/design/sub-skills/refine.md) (v1.0.0, jny986): Improve an existing interface's hierarchy, density, typography, color, layout, motion, or final finish
- [shape](skills/design/sub-skills/shape.md) (v1.0.0, jny986): Plan a UI surface or feature before implementation: task, hierarchy, interactions, states, and direction
- [systematize](skills/design/sub-skills/systematize.md) (v1.0.0, jny986): Consolidate repeated UI patterns into shared tokens and components, migrate consumers, and verify parity
<!-- design-sub-skills:end -->

<!-- implement-sub-skills:start -->
## Implement sub-skills

- [component](skills/implement/sub-skills/component.md) (v1.0.0, jny986): Build or change a bounded interface component or composition and its behavior
- [page](skills/implement/sub-skills/page.md) (v1.0.0, jny986): Build or change page-level hierarchy, routing, content, data, metadata, or states
- [spec](skills/implement/sub-skills/spec.md) (v1.0.0, jny986): Complete a spec, coordinating its ticket graph when tickets exist
- [ticket](skills/implement/sub-skills/ticket.md) (v1.0.0, jny986): Resolve and implement one ticket against its acceptance criteria and parent-spec constraints
<!-- implement-sub-skills:end -->

<!-- docs-sub-skills:start -->
## Docs sub-skills

- [docs](skills/docs/sub-skills/docs.md) (v1.0.0, jny986): Interview while maintaining a plan, terminology, and decisions
- [me](skills/docs/sub-skills/me.md) (v1.0.0, jny986): Interview and stress-test an idea without writing documents
- [spec](skills/docs/sub-skills/spec.md) (v1.0.0, jny986): Synthesize existing context into a spec for the configured tracker
- [tickets](skills/docs/sub-skills/tickets.md) (v1.0.0, jny986): Break a plan, spec, or conversation into dependency-linked tickets
<!-- docs-sub-skills:end -->
