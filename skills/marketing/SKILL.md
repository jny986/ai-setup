---
name: marketing
description: "Marketing playbooks for SaaS and software products. Use for any marketing, growth, or go-to-market task: copywriting and copy editing, CRO (landing pages, signup, onboarding, popups, paywalls), SEO (audits, AI search, schema, programmatic pages, site architecture), content and social, email, SMS and cold outreach, paid ads and ad creative, analytics, attribution and A/B tests, pricing and offers, launches, PR, events, partnerships, referrals and influencers, churn and retention, sales enablement, RevOps, prospecting, competitor and customer research, positioning and product marketing context, app store optimisation, and marketing images or video. Page and component builds hand off to the dev references."
argument-hint: "[guide] [task]"
license: MIT
metadata:
  version: "2.0"
  author: jny986
  author-url: https://jny986.com
  based_on: coreyhaines31/marketingskills@v2.11.27 (MIT), kostja94/marketing-skills (MIT), kostja94/pagina (MIT), kostja94/bricks (MIT)
---

A router over the marketing guides. Each guide lives at `<category>/[<group>/]<name>/GUIDE.md` in this skill's folder, with its own `references/` and `assets/` beside it. [references/name-table.md](references/name-table.md) lists every final name, its path, its source and the old names that alias to it.

## Steps

1. **Load product context.** Read `docs/marketing/product-marketing.md` if it exists. Guides refer to it as "the product marketing context"; if it's missing and the task depends on it, offer the `product-marketing` guide first.
2. **Pick the guide.**
   - Argument names a guide: resolve it through the name table first. An old name in the Aliases column becomes that row's final name. Use the table row with that name.
   - No argument and no task: show the tables below and ask what they're working on.
   - Otherwise: pick the row whose "Use when" fits the task. When two fit equally, ask once.
3. **Follow the guide.** Read `<path>/GUIDE.md` for the row's path and follow it as if it were the skill. Its relative links (`references/...`, `assets/...`) resolve against the guide's own folder.

When a guide hands off to another guide by name ("see cro", a **Related Skills** entry), that guide is the row of the same name here, resolved through steps 2 and 3.

A hand-off written as `dev/references/...` is a page or component build guide, not a marketing guide. The path resolves against the `skills/` folder, a sibling of this skill: read `skills/<path>/GUIDE.md` (`dev/references/pages` and `dev/references/components` are the indexes).

## Guides

### Analytics and measurement

| Guide | Path | Use when |
|---|---|---|
| `ab-testing` | `analytics/ab-testing` | Designing A/B tests or running an experimentation program |
| `attribution` | `analytics/attribution` | Which channels drive revenue, attribution models, MMM, incrementality, first-party attribution |
| `google-search-console` | `analytics/seo/google-search-console` | Search Console performance, indexing and API analysis |
| `seo-monitoring` | `analytics/seo/seo-monitoring` | SEO data system: benchmarks, article database, indexing, traffic, keywords, backlinks |
| `ai-traffic-tracking` | `analytics/sources/ai-traffic` | Tracking AI search traffic and AI visibility in GA4 and Search Console |
| `traffic-analysis` | `analytics/sources/traffic` | Traffic sources, dark traffic, UTM conventions, channel reporting |
| `analytics-tracking` | `analytics/tracking` | Tracking setup: GA4, GTM, events, tracking plans, conversion tracking |

### Channels: community, distribution, owned, partnerships, events

| Guide | Path | Use when |
|---|---|---|
| `community-building` | `channels/community/community-building` | Building a community (Discord, Slack, forum) or advocates |
| `community-forum` | `channels/community/community-forum` | Promoting via forums and communities (Hacker News, Reddit, Indie Hackers), inviting users to a community |
| `directory-submission` | `channels/community/directory-submission` | Submitting to startup, SaaS, AI or review directories for backlinks, with ready-to-paste copy |
| `product-hunt-launch` | `channels/community/product-hunt-launch` | Planning and running a Product Hunt launch |
| `aso` | `channels/distribution/aso` | App Store or Google Play listing optimisation |
| `distribution-channels` | `channels/distribution/distribution-channels` | Distribution via marketplaces, app stores and third-party platforms |
| `events` | `channels/events` | Webinars, conferences, sponsorships, speaking, field events |
| `email-marketing` | `channels/owned/email-marketing` | Lifecycle email sequences, drips, nurture and welcome flows |
| `employee-generated-content` | `channels/owned/employee-generated-content` | Employee-led content and advocacy |
| `sms` | `channels/owned/sms` | SMS, MMS or WhatsApp marketing |
| `affiliate-marketing` | `channels/partnerships/affiliate-marketing` | Affiliate program strategy, commissions, recruitment |
| `co-marketing` | `channels/partnerships/co-marketing` | Partner marketing and joint campaigns |
| `creator-program` | `channels/partnerships/creator-program` | Running a creator program |
| `education-program` | `channels/partnerships/education-program` | Student, teacher and education programs |
| `influencer-marketing` | `channels/partnerships/influencer-marketing` | Creator, influencer or ambassador partnerships |
| `public-relations` | `channels/partnerships/public-relations` | Press coverage, journalist pitches, media strategy |
| `referral-program` | `channels/partnerships/referral-program` | Referral programs, word of mouth, reviews |

### Content and copy

| Guide | Path | Use when |
|---|---|---|
| `article-content` | `content/article` | Writing article bodies: blog posts, guides, long-form pieces |
| `copy-editing` | `content/copy-editing` | Editing, proofreading or refreshing existing copy |
| `copywriting` | `content/copywriting` | Writing or rewriting page copy: headlines, value props, CTAs |
| `lead-magnets` | `content/lead-magnets` | Gated content, ebooks, checklists, templates for email capture |
| `podcast-marketing` | `content/podcast` | Podcast strategy, episodes, show notes and repurposing |
| `translation` | `content/translation` | Translating, transcreating or maintaining multilingual content |
| `video-marketing` | `content/video` | Video strategy and scripts, hooks, and producing video with AI tools or programmatic frameworks |
| `visual-content` | `content/visual-content` | Planning, generating or repurposing marketing images, social graphics, mockups, banners, OG images |

### Paid ads

| Guide | Path | Use when |
|---|---|---|
| `ad-creative` | `paid-ads/ad-creative` | Generating or iterating ad copy and creative at scale: static templates, hooks, video ad formats, creative strategy |
| `app-ads` | `paid-ads/formats/app-ads` | App install ads and user acquisition: Google App Campaigns, Apple Search Ads, CPI |
| `ctv-ads` | `paid-ads/formats/ctv-ads` | CTV, OTT and streaming TV ads |
| `directory-listing-ads` | `paid-ads/formats/directory-listing-ads` | Paid placements in directories and marketplaces (G2, Capterra, Shopify App Store) |
| `display-ads` | `paid-ads/formats/display-ads` | Display, banner and ad-network campaigns |
| `native-ads` | `paid-ads/formats/native-ads` | Native ads on Taboola, Outbrain and similar |
| `google-ads` | `paid-ads/platforms/google-ads` | Setting up or optimising Google Ads: Search, Performance Max, RSAs, Quality Score, PMF testing with ads |
| `linkedin-ads` | `paid-ads/platforms/linkedin-ads` | LinkedIn Ads: Campaign Manager, Lead Gen Forms, Sponsored Messaging, B2B and ABM |
| `meta-ads` | `paid-ads/platforms/meta-ads` | Meta (Facebook/Instagram) Ads: Advantage+, Pixel and CAPI, lookalikes, Andromeda, kill/scale rules |
| `reddit-ads` | `paid-ads/platforms/reddit-ads` | Reddit Ads: promoted posts, subreddit targeting, native creative |
| `tiktok-ads` | `paid-ads/platforms/tiktok-ads` | TikTok Ads: In-Feed, TopView, Spark Ads, vertical creative |
| `youtube-ads` | `paid-ads/platforms/youtube-ads` | YouTube video ads: TrueView, Bumper, Discovery, format selection |

### Social platforms

| Guide | Path | Use when |
|---|---|---|
| `social` | `platforms/social` | Social content, scheduling and listening on LinkedIn, X, Instagram, TikTok, Reddit, Pinterest, Medium, YouTube, GitHub, Grokipedia |

### Sales

| Guide | Path | Use when |
|---|---|---|
| `cold-email` | `sales/cold-email` | Cold outbound emails, follow-ups, sending setup, multichannel cadences |
| `prospecting` | `sales/prospecting` | Finding and qualifying prospects to build an outreach list |
| `revops` | `sales/revops` | Lead lifecycle, lead scoring, routing, marketing-to-sales handoff |
| `sales-enablement` | `sales/sales-enablement` | Sales decks, one-pagers, objection handling, demo scripts |

### SEO

| Guide | Path | Use when |
|---|---|---|
| `comparison-pages` | `seo/content/comparison-pages` | Strategy and content for comparison, "vs" and alternative pages |
| `competitor-research` | `seo/content/competitor-research` | Analysing or profiling competitors (keywords, content, backlinks, positioning) from names or URLs |
| `content-optimization` | `seo/content/content-optimization` | Optimising an article: length, headings, keyword placement, multimedia |
| `content-strategy` | `seo/content/content-strategy` | SEO content plans: topic clusters, pillar pages, editorial calendar, content prioritisation |
| `eeat-signals` | `seo/content/eeat-signals` | E-E-A-T, author and trust signals |
| `keyword-research` | `seo/content/keyword-research` | Keyword discovery, intent, clustering |
| `entity-seo` | `seo/entity-seo` | Entities, Knowledge Panel, @id and sameAs |
| `local-seo` | `seo/local` | Local search, Google Business Profile, NAP |
| `backlink-analysis` | `seo/off-page/backlink-analysis` | Analysing backlink profiles and link gaps |
| `link-building` | `seo/off-page/link-building` | Earning backlinks and outreach |
| `meta-description` | `seo/on-page/description` | Writing or auditing meta descriptions |
| `featured-snippet` | `seo/on-page/featured-snippet` | Winning featured snippets and position zero |
| `heading-structure` | `seo/on-page/heading` | H1-H6 structure and hierarchy |
| `image-optimization` | `seo/on-page/image-optimization` | Image SEO: alt text, formats, lazy loading, image sitemaps, OG images |
| `internal-links` | `seo/on-page/internal-links` | Internal linking and anchor text |
| `page-metadata` | `seo/on-page/metadata` | Sitewide metadata audit, implementation and release checks |
| `open-graph` | `seo/on-page/open-graph` | Open Graph tags and social previews |
| `schema-markup` | `seo/on-page/schema` | Schema markup, structured data, JSON-LD |
| `serp-features` | `seo/on-page/serp-features` | SERP features, rich results, zero-click patterns |
| `title-tag` | `seo/on-page/title` | Writing or auditing title tags |
| `twitter-cards` | `seo/on-page/twitter-cards` | Twitter/X card tags |
| `url-slug` | `seo/on-page/url-slug` | Creating or validating URL slugs for content pages |
| `url-structure` | `seo/on-page/url-structure` | Site-wide URL structure and hierarchy |
| `video-optimization` | `seo/on-page/video-optimization` | Video SEO: VideoObject, video sitemaps, key moments |
| `parasite-seo` | `seo/parasite-seo` | Ranking through third-party high-authority platforms |
| `programmatic-seo` | `seo/programmatic-seo` | Template-driven SEO pages at scale |
| `canonical-tag` | `seo/technical/canonical` | Canonical tags and duplicate content |
| `core-web-vitals` | `seo/technical/core-web-vitals` | LCP, INP, CLS and page speed |
| `site-crawlability` | `seo/technical/crawlability` | Crawlability, crawl budget, site structure for bots |
| `indexing` | `seo/technical/indexing` | Getting pages indexed; indexing problems |
| `indexnow` | `seo/technical/indexnow` | IndexNow instant URL submission |
| `mobile-friendly` | `seo/technical/mobile-friendly` | Mobile-friendliness and mobile-first indexing |
| `rendering-strategies` | `seo/technical/rendering-strategies` | SSR, SSG, CSR and rendering for SEO |
| `robots-txt` | `seo/technical/robots` | robots.txt rules and crawler access |
| `xml-sitemap` | `seo/technical/sitemap` | XML sitemaps: structure, submission, segmentation |

### Strategy: brand and content

| Guide | Path | Use when |
|---|---|---|
| `brand-monitoring` | `strategies/brand/brand-monitoring` | Tracking brand mentions, sentiment and reputation |
| `brand-protection` | `strategies/brand/brand-protection` | Trademarks, impersonation, brand abuse and takedowns |
| `brand-visual` | `strategies/brand/brand-visual` | Visual identity: typography, colours, design tokens, brand style guide |
| `branding` | `strategies/brand/branding` | Brand purpose, values, story, voice, narrative, brand guidelines |
| `content-marketing` | `strategies/brand/content-marketing` | Content types, formats, funnel mapping and repurposing across channels |
| `integrated-marketing` | `strategies/brand/integrated-marketing` | Coordinating channels with the PESO model and a consistent message |
| `marketing-psychology` | `strategies/brand/marketing-psychology` | Applying behavioural science, biases or mental models to marketing |
| `product-marketing` | `strategies/brand/product-marketing` | Creating or updating the product marketing context doc (positioning, ICP, audience) |
| `rebranding-strategy` | `strategies/brand/rebranding` | Rebrand execution: domain change, redirects, migration, announcement |

### Strategy: pricing, domain, localisation, paid and GEO

| Guide | Path | Use when |
|---|---|---|
| `domain-architecture` | `strategies/commercial/domain/domain-architecture` | Subdomain, subfolder or separate domain decisions |
| `domain-selection` | `strategies/commercial/domain/domain-selection` | Choosing a domain name and TLD |
| `multi-domain-brand-seo` | `strategies/commercial/domain/multi-domain-brand-seo` | SEO and brand when several domains coexist |
| `free-tools` | `strategies/commercial/free-tools` | Building a free tool (calculator, grader) for leads or SEO |
| `generative-engine-optimization` | `strategies/commercial/geo` | Getting cited by AI search and LLMs (AEO, GEO, llms.txt) |
| `localization-strategy` | `strategies/commercial/localization` | Market and locale selection, multilingual rollout, localisation architecture |
| `open-source-strategy` | `strategies/commercial/open-source` | Open source as a growth and commercialisation path |
| `paid-ads-strategy` | `strategies/commercial/paid-ads` | Paid campaigns: targeting, bidding, budgets, optimisation |
| `discount-marketing-strategy` | `strategies/commercial/pricing/discount-marketing` | Promotional pricing: annual, lifetime deals, seasonal, startup and referral discounts |
| `offers` | `strategies/commercial/pricing/offers` | Designing the offer itself: bonuses, guarantees, urgency, naming |
| `pricing-strategy` | `strategies/commercial/pricing/pricing-strategy` | Pricing, packaging, tiers, freemium or trials |

### Strategy: conversion

| Guide | Path | Use when |
|---|---|---|
| `conversion-optimization` | `strategies/conversion/conversion-optimization` | Improving conversions on a marketing page, form or funnel: page analysis, CRO process, experiment prioritisation |
| `onboarding` | `strategies/conversion/onboarding` | Post-signup activation, first-run experience, time to value |
| `paywalls` | `strategies/conversion/paywalls` | In-app paywalls, upgrade screens, feature gates, upsells |
| `popups` | `strategies/conversion/popups` | Popups, modals, slide-ins, exit intent, banners |
| `signup` | `strategies/conversion/signup` | Signup, registration or trial-start flows |

### Strategy: launch, growth and research

| Guide | Path | Use when |
|---|---|---|
| `cold-start-strategy` | `strategies/launch/cold-start` | Getting first users with zero traction (0 to 1) |
| `customer-research` | `strategies/launch/customer-research` | Interviews, surveys, reviews, transcripts, personas, JTBD, voice of customer |
| `growth-funnel` | `strategies/launch/growth-funnel` | AARRR growth funnel, bottlenecks, lifecycle actions |
| `gtm-strategy` | `strategies/launch/gtm` | A GTM strategy or a full 12-month marketing plan: GTM mode, ICP, market entry, repositioning, AARRR |
| `indie-hacker-strategy` | `strategies/launch/indie-hacker` | Indie hacker and bootstrapped founder growth, build in public |
| `marketing-ideas` | `strategies/launch/marketing-ideas` | Brainstorming growth ideas or tactics when stuck |
| `pmf-strategy` | `strategies/launch/pmf` | Validating or measuring product-market fit before scaling |
| `product-launch` | `strategies/launch/product-launch` | Product launches, feature announcements, changelogs and release notes, waitlists, site go-live |
| `research-sources` | `strategies/launch/research-sources` | Information sources for content ideas, competitor monitoring, industry tracking |
| `retention-strategy` | `strategies/launch/retention` | Churn, retention, cancel flows, save offers, dunning, failed payments |

### Strategy: operations

| Guide | Path | Use when |
|---|---|---|
| `marketing-council` | `strategies/operations/marketing-council` | Multiple expert perspectives or a simulated advisory board on a marketing question |
| `marketing-loops` | `strategies/operations/marketing-loops` | A recurring, agent-run marketing workflow on a cadence |

### Strategy: site structure and SEO audit

| Guide | Path | Use when |
|---|---|---|
| `seo-strategy` | `strategies/structure/seo` | Organic SEO strategy, workflow order and prioritisation |
| `seo-audit` | `strategies/structure/seo-audit` | Auditing or diagnosing technical and on-page SEO |
| `website-structure` | `strategies/structure/website-structure` | Which pages to build, page hierarchy, navigation and site structure |
