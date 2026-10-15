---
name: marketing
description: "Marketing playbooks for SaaS and software products. Use for any marketing, growth, or go-to-market task: copywriting and copy editing, CRO (landing pages, signup, onboarding, popups, paywalls), SEO (audits, AI search, schema, programmatic pages, site architecture), content and social, email, SMS and cold outreach, paid ads and ad creative, analytics, attribution and A/B tests, pricing and offers, launches, PR, events, partnerships, referrals and influencers, churn and retention, sales enablement, RevOps, prospecting, competitor and customer research, positioning and product marketing context, app store optimisation, and marketing images or video. Page and component builds hand off to the dev references."
argument-hint: "[guide] [task]"
license: MIT
metadata:
  version: "2.0"
  author: jny986
  author-url: https://jny986.com
---

A router over the marketing guides. Each guide is a file at `references/<category>/[<group>/]<name>.md` in this skill's folder. Its supporting `references/` and `assets/` folders sit beside it, shared with the other guides in the same folder. [references/name-table.md](references/name-table.md) lists every final name, its path, its source and the old names that alias to it.

## Steps

1. **Load product context.** Read `docs/marketing/product-marketing.md` if it exists. Guides refer to it as "the product marketing context"; if it's missing and the task depends on it, offer the `product-marketing` guide first.
2. **Pick the guide.**
   - Argument names a guide: resolve it through the name table first. An old name in the Aliases column becomes that row's final name. Use the table row with that name.
   - No argument and no task: show the tables below and ask what they're working on.
   - Otherwise: pick the row whose "Use when" fits the task. When two fit equally, ask once.
3. **Follow the guide.** Read the guide file at the row's path and follow it as if it were the skill. Its relative links (`references/...`, `assets/...`) resolve against the guide file's own folder.

When a guide hands off to another guide by name ("see cro", a **Related Skills** entry), that guide is the row of the same name here, resolved through steps 2 and 3.

A hand-off written as `dev/references/...` is a page or component build guide, not a marketing guide. The path resolves against the `skills/` folder, a sibling of this skill: read `skills/<path>/GUIDE.md` (`dev/references/pages` and `dev/references/components` are the indexes).

## Guides

### Analytics and measurement

| Guide | Path | Use when |
|---|---|---|
| `ab-testing` | `references/analytics/ab-testing.md` | Designing A/B tests or running an experimentation program |
| `attribution` | `references/analytics/attribution.md` | Which channels drive revenue, attribution models, MMM, incrementality, first-party attribution |
| `seo-analytics` | `references/analytics/seo.md` | Search Console analysis and API; SEO data system: benchmarks, article database, indexing, traffic, keywords, backlinks |
| `traffic-analysis` | `references/analytics/traffic.md` | Traffic sources, dark traffic, UTM conventions, channel reporting, AI search traffic in GA4 |
| `analytics-tracking` | `references/analytics/tracking.md` | Tracking setup: GA4, GTM, events, tracking plans, conversion tracking |

### Channels: community, distribution, owned, partnerships, events

| Guide | Path | Use when |
|---|---|---|
| `community-building` | `references/channels/community/community-building.md` | Building a community (Discord, Slack, forum) or advocates |
| `community-forum` | `references/channels/community/community-forum.md` | Promoting via forums and communities (Hacker News, Reddit, Indie Hackers), inviting users to a community |
| `directory-submission` | `references/channels/community/directory-submission.md` | Submitting to startup, SaaS, AI or review directories for backlinks, with ready-to-paste copy |
| `product-hunt-launch` | `references/channels/community/product-hunt-launch.md` | Planning and running a Product Hunt launch |
| `aso` | `references/channels/distribution/aso.md` | App Store or Google Play listing optimisation |
| `distribution-channels` | `references/channels/distribution/distribution-channels.md` | Distribution via marketplaces, app stores and third-party platforms |
| `events` | `references/channels/events/events.md` | Webinars, conferences, sponsorships, speaking, field events |
| `email-marketing` | `references/channels/owned/email-marketing.md` | Lifecycle email sequences, drips, nurture and welcome flows |
| `employee-generated-content` | `references/channels/owned/employee-generated-content.md` | Employee-led content and advocacy |
| `sms` | `references/channels/owned/sms.md` | SMS, MMS or WhatsApp marketing |
| `affiliate-marketing` | `references/channels/partnerships/affiliate-marketing.md` | Affiliate program strategy, commissions, recruitment |
| `co-marketing` | `references/channels/partnerships/co-marketing.md` | Partner marketing and joint campaigns |
| `creator-program` | `references/channels/partnerships/creator-program.md` | Running a creator program |
| `education-program` | `references/channels/partnerships/education-program.md` | Student, teacher and education programs |
| `influencer-marketing` | `references/channels/partnerships/influencer-marketing.md` | Creator, influencer or ambassador partnerships |
| `public-relations` | `references/channels/partnerships/public-relations.md` | Press coverage, journalist pitches, media strategy |
| `referral-program` | `references/channels/partnerships/referral-program.md` | Referral programs, word of mouth, reviews |

### Content and copy

| Guide | Path | Use when |
|---|---|---|
| `article-content` | `references/content/article.md` | Writing article bodies: blog posts, guides, long-form pieces |
| `copy-editing` | `references/content/copy-editing.md` | Editing, proofreading or refreshing existing copy |
| `copywriting` | `references/content/copywriting.md` | Writing or rewriting page copy: headlines, value props, CTAs |
| `lead-magnets` | `references/content/lead-magnets.md` | Gated content, ebooks, checklists, templates for email capture |
| `podcast-marketing` | `references/content/podcast.md` | Podcast strategy, episodes, show notes and repurposing |
| `translation` | `references/content/translation.md` | Translating, transcreating or maintaining multilingual content |
| `video-marketing` | `references/content/video.md` | Video strategy and scripts, hooks, and producing video with AI tools or programmatic frameworks |
| `visual-content` | `references/content/visual-content.md` | Planning, generating or repurposing marketing images, social graphics, mockups, banners, OG images |

### Paid ads

| Guide | Path | Use when |
|---|---|---|
| `ad-creative` | `references/paid-ads/ad-creative.md` | Generating or iterating ad copy and creative at scale: static templates, hooks, video ad formats, creative strategy |
| `app-ads` | `references/paid-ads/formats/app-ads.md` | App install ads and user acquisition: Google App Campaigns, Apple Search Ads, CPI |
| `ctv-ads` | `references/paid-ads/formats/ctv-ads.md` | CTV, OTT and streaming TV ads |
| `directory-listing-ads` | `references/paid-ads/formats/directory-listing-ads.md` | Paid placements in directories and marketplaces (G2, Capterra, Shopify App Store) |
| `display-ads` | `references/paid-ads/formats/display-ads.md` | Display, banner and ad-network campaigns |
| `native-ads` | `references/paid-ads/formats/native-ads.md` | Native ads on Taboola, Outbrain and similar |
| `google-ads` | `references/paid-ads/platforms/google-ads.md` | Setting up or optimising Google Ads: Search, Performance Max, RSAs, Quality Score, PMF testing with ads |
| `linkedin-ads` | `references/paid-ads/platforms/linkedin-ads.md` | LinkedIn Ads: Campaign Manager, Lead Gen Forms, Sponsored Messaging, B2B and ABM |
| `meta-ads` | `references/paid-ads/platforms/meta-ads.md` | Meta (Facebook/Instagram) Ads: Advantage+, Pixel and CAPI, lookalikes, Andromeda, kill/scale rules |
| `reddit-ads` | `references/paid-ads/platforms/reddit-ads.md` | Reddit Ads: promoted posts, subreddit targeting, native creative |
| `tiktok-ads` | `references/paid-ads/platforms/tiktok-ads.md` | TikTok Ads: In-Feed, TopView, Spark Ads, vertical creative |
| `youtube-ads` | `references/paid-ads/platforms/youtube-ads.md` | YouTube video ads: TrueView, Bumper, Discovery, format selection |

### Social platforms

| Guide | Path | Use when |
|---|---|---|
| `social` | `references/platforms/social.md` | Social content, scheduling and listening on LinkedIn, X, Instagram, TikTok, Reddit, Pinterest, Medium, YouTube, GitHub, Grokipedia |

### Sales

| Guide | Path | Use when |
|---|---|---|
| `cold-email` | `references/sales/cold-email.md` | Cold outbound emails, follow-ups, sending setup, multichannel cadences |
| `prospecting` | `references/sales/prospecting.md` | Finding and qualifying prospects to build an outreach list |
| `revops` | `references/sales/revops.md` | Lead lifecycle, lead scoring, routing, marketing-to-sales handoff |
| `sales-enablement` | `references/sales/sales-enablement.md` | Sales decks, one-pagers, objection handling, demo scripts |

### SEO

| Guide | Path | Use when |
|---|---|---|
| `comparison-pages` | `references/seo/content/comparison-pages.md` | Strategy and content for comparison, "vs" and alternative pages |
| `competitor-research` | `references/seo/content/competitor-research.md` | Analysing or profiling competitors (keywords, content, backlinks, positioning) from names or URLs |
| `content-optimization` | `references/seo/content/content-optimization.md` | Optimising an article: length, headings, keyword placement, multimedia |
| `content-strategy` | `references/seo/content/content-strategy.md` | SEO content plans: topic clusters, pillar pages, editorial calendar, content prioritisation |
| `eeat-signals` | `references/seo/content/eeat-signals.md` | E-E-A-T, author and trust signals |
| `keyword-research` | `references/seo/content/keyword-research.md` | Keyword discovery, intent, clustering |
| `entity-seo` | `references/seo/entity-seo.md` | Entities, Knowledge Panel, @id and sameAs |
| `local-seo` | `references/seo/local.md` | Local search, Google Business Profile, NAP |
| `backlink-analysis` | `references/seo/off-page/backlink-analysis.md` | Analysing backlink profiles and link gaps |
| `link-building` | `references/seo/off-page/link-building.md` | Earning backlinks and outreach |
| `meta-description` | `references/seo/on-page/description.md` | Writing or auditing meta descriptions |
| `featured-snippet` | `references/seo/on-page/featured-snippet.md` | Winning featured snippets and position zero |
| `heading-structure` | `references/seo/on-page/heading.md` | H1-H6 structure and hierarchy |
| `image-optimization` | `references/seo/on-page/image-optimization.md` | Image SEO: alt text, formats, lazy loading, image sitemaps, OG images |
| `internal-links` | `references/seo/on-page/internal-links.md` | Internal linking and anchor text |
| `page-metadata` | `references/seo/on-page/metadata.md` | Sitewide metadata audit, implementation and release checks |
| `open-graph` | `references/seo/on-page/open-graph.md` | Open Graph tags and social previews |
| `schema-markup` | `references/seo/on-page/schema.md` | Schema markup, structured data, JSON-LD |
| `serp-features` | `references/seo/on-page/serp-features.md` | SERP features, rich results, zero-click patterns |
| `title-tag` | `references/seo/on-page/title.md` | Writing or auditing title tags |
| `twitter-cards` | `references/seo/on-page/twitter-cards.md` | Twitter/X card tags |
| `url-slug` | `references/seo/on-page/url-slug.md` | Creating or validating URL slugs for content pages |
| `url-structure` | `references/seo/on-page/url-structure.md` | Site-wide URL structure and hierarchy |
| `video-optimization` | `references/seo/on-page/video-optimization.md` | Video SEO: VideoObject, video sitemaps, key moments |
| `parasite-seo` | `references/seo/parasite-seo.md` | Ranking through third-party high-authority platforms |
| `programmatic-seo` | `references/seo/programmatic-seo.md` | Template-driven SEO pages at scale |
| `canonical-tag` | `references/seo/technical/canonical.md` | Canonical tags and duplicate content |
| `core-web-vitals` | `references/seo/technical/core-web-vitals.md` | LCP, INP, CLS and page speed |
| `site-crawlability` | `references/seo/technical/crawlability.md` | Crawlability, crawl budget, site structure for bots |
| `indexing` | `references/seo/technical/indexing.md` | Getting pages indexed; indexing problems |
| `indexnow` | `references/seo/technical/indexnow.md` | IndexNow instant URL submission |
| `mobile-friendly` | `references/seo/technical/mobile-friendly.md` | Mobile-friendliness and mobile-first indexing |
| `rendering-strategies` | `references/seo/technical/rendering-strategies.md` | SSR, SSG, CSR and rendering for SEO |
| `robots-txt` | `references/seo/technical/robots.md` | robots.txt rules and crawler access |
| `xml-sitemap` | `references/seo/technical/sitemap.md` | XML sitemaps: structure, submission, segmentation |

### Strategy: brand and content

| Guide | Path | Use when |
|---|---|---|
| `brand-monitoring` | `references/strategies/brand/brand-monitoring.md` | Tracking brand mentions, sentiment and reputation |
| `brand-protection` | `references/strategies/brand/brand-protection.md` | Trademarks, impersonation, brand abuse and takedowns |
| `brand-visual` | `references/strategies/brand/brand-visual.md` | Visual identity: typography, colours, design tokens, brand style guide |
| `branding` | `references/strategies/brand/branding.md` | Brand purpose, values, story, voice, narrative, brand guidelines |
| `content-marketing` | `references/strategies/brand/content-marketing.md` | Content types, formats, funnel mapping and repurposing across channels |
| `integrated-marketing` | `references/strategies/brand/integrated-marketing.md` | Coordinating channels with the PESO model and a consistent message |
| `marketing-psychology` | `references/strategies/brand/marketing-psychology.md` | Applying behavioural science, biases or mental models to marketing |
| `product-marketing` | `references/strategies/brand/product-marketing.md` | Creating or updating the product marketing context doc (positioning, ICP, audience) |
| `rebranding-strategy` | `references/strategies/brand/rebranding.md` | Rebrand execution: domain change, redirects, migration, announcement |

### Strategy: pricing, domain, localisation, paid and GEO

| Guide | Path | Use when |
|---|---|---|
| `domain-architecture` | `references/strategies/commercial/domain/domain-architecture.md` | Subdomain, subfolder or separate domain decisions |
| `domain-selection` | `references/strategies/commercial/domain/domain-selection.md` | Choosing a domain name and TLD |
| `multi-domain-brand-seo` | `references/strategies/commercial/domain/multi-domain-brand-seo.md` | SEO and brand when several domains coexist |
| `free-tools` | `references/strategies/commercial/free-tools.md` | Building a free tool (calculator, grader) for leads or SEO |
| `generative-engine-optimization` | `references/strategies/commercial/geo.md` | Getting cited by AI search and LLMs (AEO, GEO, llms.txt) |
| `localization-strategy` | `references/strategies/commercial/localization.md` | Market and locale selection, multilingual rollout, localisation architecture |
| `open-source-strategy` | `references/strategies/commercial/open-source.md` | Open source as a growth and commercialisation path |
| `paid-ads-strategy` | `references/strategies/commercial/paid-ads.md` | Paid campaigns: targeting, bidding, budgets, optimisation |
| `discount-marketing-strategy` | `references/strategies/commercial/pricing/discount-marketing.md` | Promotional pricing: annual, lifetime deals, seasonal, startup and referral discounts |
| `offers` | `references/strategies/commercial/pricing/offers.md` | Designing the offer itself: bonuses, guarantees, urgency, naming |
| `pricing-strategy` | `references/strategies/commercial/pricing/pricing-strategy.md` | Pricing, packaging, tiers, freemium or trials |

### Strategy: conversion

| Guide | Path | Use when |
|---|---|---|
| `conversion-optimization` | `references/strategies/conversion/conversion-optimization.md` | Improving conversions on a marketing page, form or funnel: page analysis, CRO process, experiment prioritisation |
| `onboarding` | `references/strategies/conversion/onboarding.md` | Post-signup activation, first-run experience, time to value |
| `paywalls` | `references/strategies/conversion/paywalls.md` | In-app paywalls, upgrade screens, feature gates, upsells |
| `popups` | `references/strategies/conversion/popups.md` | Popups, modals, slide-ins, exit intent, banners |
| `signup` | `references/strategies/conversion/signup.md` | Signup, registration or trial-start flows |

### Strategy: launch, growth and research

| Guide | Path | Use when |
|---|---|---|
| `cold-start-strategy` | `references/strategies/launch/cold-start.md` | Getting first users with zero traction (0 to 1) |
| `customer-research` | `references/strategies/launch/customer-research.md` | Interviews, surveys, reviews, transcripts, personas, JTBD, voice of customer |
| `growth-funnel` | `references/strategies/launch/growth-funnel.md` | AARRR growth funnel, bottlenecks, lifecycle actions |
| `gtm-strategy` | `references/strategies/launch/gtm.md` | A GTM strategy or a full 12-month marketing plan: GTM mode, ICP, market entry, repositioning, AARRR |
| `indie-hacker-strategy` | `references/strategies/launch/indie-hacker.md` | Indie hacker and bootstrapped founder growth, build in public |
| `marketing-ideas` | `references/strategies/launch/marketing-ideas.md` | Brainstorming growth ideas or tactics when stuck |
| `pmf-strategy` | `references/strategies/launch/pmf.md` | Validating or measuring product-market fit before scaling |
| `product-launch` | `references/strategies/launch/product-launch.md` | Product launches, feature announcements, changelogs and release notes, waitlists, site go-live |
| `research-sources` | `references/strategies/launch/research-sources.md` | Information sources for content ideas, competitor monitoring, industry tracking |
| `retention-strategy` | `references/strategies/launch/retention.md` | Churn, retention, cancel flows, save offers, dunning, failed payments |

### Strategy: operations

| Guide | Path | Use when |
|---|---|---|
| `marketing-council` | `references/strategies/operations/marketing-council.md` | Multiple expert perspectives or a simulated advisory board on a marketing question |
| `marketing-loops` | `references/strategies/operations/marketing-loops.md` | A recurring, agent-run marketing workflow on a cadence |

### Strategy: site structure and SEO audit

| Guide | Path | Use when |
|---|---|---|
| `seo-strategy` | `references/strategies/structure/seo.md` | Organic SEO strategy, workflow order and prioritisation |
| `seo-audit` | `references/strategies/structure/seo-audit.md` | Auditing or diagnosing technical and on-page SEO |
| `website-structure` | `references/strategies/structure/website-structure.md` | Which pages to build, page hierarchy, navigation and site structure |
