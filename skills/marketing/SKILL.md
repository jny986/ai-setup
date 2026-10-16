---
name: marketing
description: "Marketing playbooks for SaaS and software products. Use for any marketing, growth, or go-to-market task: copywriting and copy editing, CRO (landing pages, signup, onboarding, popups, paywalls), SEO (audits, AI search, schema, programmatic pages, site architecture), content and social, email, SMS and cold outreach, paid ads and ad creative, analytics, attribution and A/B tests, pricing and offers, launches, PR, events, partnerships, referrals and influencers, churn and retention, sales enablement, RevOps, prospecting, competitor and customer research, positioning and product marketing context, app store optimisation, and marketing images or video. Page and component builds hand off to the implement router’s build guides."
argument-hint: "[sub-skill] [task]"
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

A router over the marketing sub-skills. Each sub-skill is a file at `sub-skills/<category>/[<group>/]<name>.md` in this skill's folder. Its supporting `references/` and `assets/` folders sit beside it, shared with the other sub-skills in the same folder. [sub-skills/name-table.md](sub-skills/name-table.md) lists every final name, its path, its source and the old names that alias to it.

## Steps

1. **Load product context.** Read `docs/marketing/product-marketing.md` if it exists. Sub-skills refer to it as "the product marketing context"; if it's missing and the task depends on it, offer the `product-marketing` sub-skill first.
2. **Pick the sub-skill.**
   - Argument names a sub-skill: resolve it through the name table first. An old name in the Aliases column becomes that row's final name. Use the table row with that name.
   - No argument and no task: show the tables below and ask what they're working on.
   - Otherwise: pick the row whose "Use when" fits the task. When two fit equally, ask once.
3. **Follow the sub-skill.** Read the sub-skill file at the row's path and follow it as if it were the skill. Its relative links (`references/...`, `assets/...`) resolve against the sub-skill file's own folder.

When a sub-skill hands off to another sub-skill by name ("see cro", a **Related Skills** entry), that sub-skill is the row of the same name here, resolved through steps 2 and 3.

A hand-off written as `implement/sub-skills/references/...` is a page or component build guide, not a marketing sub-skill. The path resolves against the `skills/` folder, a sibling of this skill: read `skills/<path>/GUIDE.md` (`implement/sub-skills/references/pages.md` and `implement/sub-skills/references/components.md` are the indexes).

## Sub-skills

### Analytics and measurement

| Sub-skill | Path | Use when |
|---|---|---|
| `ab-testing` | `sub-skills/analytics/ab-testing.md` | Designing A/B tests or running an experimentation program |
| `attribution` | `sub-skills/analytics/attribution.md` | Which channels drive revenue, attribution models, MMM, incrementality, first-party attribution |
| `seo-analytics` | `sub-skills/analytics/seo.md` | Search Console analysis and API; SEO data system: benchmarks, article database, indexing, traffic, keywords, backlinks |
| `traffic-analysis` | `sub-skills/analytics/traffic.md` | Traffic sources, dark traffic, UTM conventions, channel reporting, AI search traffic in GA4 |
| `analytics-tracking` | `sub-skills/analytics/tracking.md` | Tracking setup: GA4, GTM, events, tracking plans, conversion tracking |

### Channels: community, distribution, owned, partnerships, events

| Sub-skill | Path | Use when |
|---|---|---|
| `community-building` | `sub-skills/channels/community/community-building.md` | Building a community (Discord, Slack, forum) or advocates |
| `community-forum` | `sub-skills/channels/community/community-forum.md` | Promoting via forums and communities (Hacker News, Reddit, Indie Hackers), inviting users to a community |
| `directory-submission` | `sub-skills/channels/community/directory-submission.md` | Submitting to startup, SaaS, AI or review directories for backlinks, with ready-to-paste copy |
| `product-hunt-launch` | `sub-skills/channels/community/product-hunt-launch.md` | Planning and running a Product Hunt launch |
| `aso` | `sub-skills/channels/distribution/aso.md` | App Store or Google Play listing optimisation |
| `distribution-channels` | `sub-skills/channels/distribution/distribution-channels.md` | Distribution via marketplaces, app stores and third-party platforms |
| `events` | `sub-skills/channels/events/events.md` | Webinars, conferences, sponsorships, speaking, field events |
| `email-marketing` | `sub-skills/channels/owned/email-marketing.md` | Lifecycle email sequences, drips, nurture and welcome flows |
| `employee-generated-content` | `sub-skills/channels/owned/employee-generated-content.md` | Employee-led content and advocacy |
| `sms` | `sub-skills/channels/owned/sms.md` | SMS, MMS or WhatsApp marketing |
| `affiliate-marketing` | `sub-skills/channels/partnerships/affiliate-marketing.md` | Affiliate program strategy, commissions, recruitment |
| `co-marketing` | `sub-skills/channels/partnerships/co-marketing.md` | Partner marketing and joint campaigns |
| `creator-program` | `sub-skills/channels/partnerships/creator-program.md` | Running a creator program |
| `education-program` | `sub-skills/channels/partnerships/education-program.md` | Student, teacher and education programs |
| `influencer-marketing` | `sub-skills/channels/partnerships/influencer-marketing.md` | Creator, influencer or ambassador partnerships |
| `public-relations` | `sub-skills/channels/partnerships/public-relations.md` | Press coverage, journalist pitches, media strategy |
| `referral-program` | `sub-skills/channels/partnerships/referral-program.md` | Referral programs, word of mouth, reviews |

### Content and copy

| Sub-skill | Path | Use when |
|---|---|---|
| `article-content` | `sub-skills/content/article.md` | Writing article bodies: blog posts, sub-skills, long-form pieces |
| `copy-editing` | `sub-skills/content/copy-editing.md` | Editing, proofreading or refreshing existing copy |
| `copywriting` | `sub-skills/content/copywriting.md` | Writing or rewriting page copy: headlines, value props, CTAs |
| `lead-magnets` | `sub-skills/content/lead-magnets.md` | Gated content, ebooks, checklists, templates for email capture |
| `podcast-marketing` | `sub-skills/content/podcast.md` | Podcast strategy, episodes, show notes and repurposing |
| `translation` | `sub-skills/content/translation.md` | Translating, transcreating or maintaining multilingual content |
| `video-marketing` | `sub-skills/content/video.md` | Video strategy and scripts, hooks, and producing video with AI tools or programmatic frameworks |
| `visual-content` | `sub-skills/content/visual-content.md` | Planning, generating or repurposing marketing images, social graphics, mockups, banners, OG images |

### Paid ads

| Sub-skill | Path | Use when |
|---|---|---|
| `ad-creative` | `sub-skills/paid-ads/ad-creative.md` | Generating or iterating ad copy and creative at scale: static templates, hooks, video ad formats, creative strategy |
| `app-ads` | `sub-skills/paid-ads/formats/app-ads.md` | App install ads and user acquisition: Google App Campaigns, Apple Search Ads, CPI |
| `ctv-ads` | `sub-skills/paid-ads/formats/ctv-ads.md` | CTV, OTT and streaming TV ads |
| `directory-listing-ads` | `sub-skills/paid-ads/formats/directory-listing-ads.md` | Paid placements in directories and marketplaces (G2, Capterra, Shopify App Store) |
| `display-ads` | `sub-skills/paid-ads/formats/display-ads.md` | Display, banner and ad-network campaigns |
| `native-ads` | `sub-skills/paid-ads/formats/native-ads.md` | Native ads on Taboola, Outbrain and similar |
| `google-ads` | `sub-skills/paid-ads/platforms/google-ads.md` | Setting up or optimising Google Ads: Search, Performance Max, RSAs, Quality Score, PMF testing with ads |
| `linkedin-ads` | `sub-skills/paid-ads/platforms/linkedin-ads.md` | LinkedIn Ads: Campaign Manager, Lead Gen Forms, Sponsored Messaging, B2B and ABM |
| `meta-ads` | `sub-skills/paid-ads/platforms/meta-ads.md` | Meta (Facebook/Instagram) Ads: Advantage+, Pixel and CAPI, lookalikes, Andromeda, kill/scale rules |
| `reddit-ads` | `sub-skills/paid-ads/platforms/reddit-ads.md` | Reddit Ads: promoted posts, subreddit targeting, native creative |
| `tiktok-ads` | `sub-skills/paid-ads/platforms/tiktok-ads.md` | TikTok Ads: In-Feed, TopView, Spark Ads, vertical creative |
| `youtube-ads` | `sub-skills/paid-ads/platforms/youtube-ads.md` | YouTube video ads: TrueView, Bumper, Discovery, format selection |

### Social platforms

| Sub-skill | Path | Use when |
|---|---|---|
| `social` | `sub-skills/platforms/social.md` | Social content, scheduling and listening on LinkedIn, X, Instagram, TikTok, Reddit, Pinterest, Medium, YouTube, GitHub, Grokipedia |

### Sales

| Sub-skill | Path | Use when |
|---|---|---|
| `cold-email` | `sub-skills/sales/cold-email.md` | Cold outbound emails, follow-ups, sending setup, multichannel cadences |
| `prospecting` | `sub-skills/sales/prospecting.md` | Finding and qualifying prospects to build an outreach list |
| `revops` | `sub-skills/sales/revops.md` | Lead lifecycle, lead scoring, routing, marketing-to-sales handoff |
| `sales-enablement` | `sub-skills/sales/sales-enablement.md` | Sales decks, one-pagers, objection handling, demo scripts |

### SEO

| Sub-skill | Path | Use when |
|---|---|---|
| `comparison-pages` | `sub-skills/seo/content/comparison-pages.md` | Strategy and content for comparison, "vs" and alternative pages |
| `competitor-research` | `sub-skills/seo/content/competitor-research.md` | Analysing or profiling competitors (keywords, content, backlinks, positioning) from names or URLs |
| `content-optimization` | `sub-skills/seo/content/content-optimization.md` | Optimising an article: length, headings, keyword placement, multimedia |
| `content-strategy` | `sub-skills/seo/content/content-strategy.md` | SEO content plans: topic clusters, pillar pages, editorial calendar, content prioritisation |
| `eeat-signals` | `sub-skills/seo/content/eeat-signals.md` | E-E-A-T, author and trust signals |
| `keyword-research` | `sub-skills/seo/content/keyword-research.md` | Keyword discovery, intent, clustering |
| `entity-seo` | `sub-skills/seo/entity-seo.md` | Entities, Knowledge Panel, @id and sameAs |
| `local-seo` | `sub-skills/seo/local.md` | Local search, Google Business Profile, NAP |
| `backlink-analysis` | `sub-skills/seo/off-page/backlink-analysis.md` | Analysing backlink profiles and link gaps |
| `link-building` | `sub-skills/seo/off-page/link-building.md` | Earning backlinks and outreach |
| `meta-description` | `sub-skills/seo/on-page/description.md` | Writing or auditing meta descriptions |
| `featured-snippet` | `sub-skills/seo/on-page/featured-snippet.md` | Winning featured snippets and position zero |
| `heading-structure` | `sub-skills/seo/on-page/heading.md` | H1-H6 structure and hierarchy |
| `image-optimization` | `sub-skills/seo/on-page/image-optimization.md` | Image SEO: alt text, formats, lazy loading, image sitemaps, OG images |
| `internal-links` | `sub-skills/seo/on-page/internal-links.md` | Internal linking and anchor text |
| `page-metadata` | `sub-skills/seo/on-page/metadata.md` | Sitewide metadata audit, implementation and release checks |
| `open-graph` | `sub-skills/seo/on-page/open-graph.md` | Open Graph tags and social previews |
| `schema-markup` | `sub-skills/seo/on-page/schema.md` | Schema markup, structured data, JSON-LD |
| `serp-features` | `sub-skills/seo/on-page/serp-features.md` | SERP features, rich results, zero-click patterns |
| `title-tag` | `sub-skills/seo/on-page/title.md` | Writing or auditing title tags |
| `twitter-cards` | `sub-skills/seo/on-page/twitter-cards.md` | Twitter/X card tags |
| `url-slug` | `sub-skills/seo/on-page/url-slug.md` | Creating or validating URL slugs for content pages |
| `url-structure` | `sub-skills/seo/on-page/url-structure.md` | Site-wide URL structure and hierarchy |
| `video-optimization` | `sub-skills/seo/on-page/video-optimization.md` | Video SEO: VideoObject, video sitemaps, key moments |
| `parasite-seo` | `sub-skills/seo/parasite-seo.md` | Ranking through third-party high-authority platforms |
| `programmatic-seo` | `sub-skills/seo/programmatic-seo.md` | Template-driven SEO pages at scale |
| `canonical-tag` | `sub-skills/seo/technical/canonical.md` | Canonical tags and duplicate content |
| `core-web-vitals` | `sub-skills/seo/technical/core-web-vitals.md` | LCP, INP, CLS and page speed |
| `site-crawlability` | `sub-skills/seo/technical/crawlability.md` | Crawlability, crawl budget, site structure for bots |
| `indexing` | `sub-skills/seo/technical/indexing.md` | Getting pages indexed; indexing problems |
| `indexnow` | `sub-skills/seo/technical/indexnow.md` | IndexNow instant URL submission |
| `mobile-friendly` | `sub-skills/seo/technical/mobile-friendly.md` | Mobile-friendliness and mobile-first indexing |
| `rendering-strategies` | `sub-skills/seo/technical/rendering-strategies.md` | SSR, SSG, CSR and rendering for SEO |
| `robots-txt` | `sub-skills/seo/technical/robots.md` | robots.txt rules and crawler access |
| `xml-sitemap` | `sub-skills/seo/technical/sitemap.md` | XML sitemaps: structure, submission, segmentation |

### Strategy: brand and content

| Sub-skill | Path | Use when |
|---|---|---|
| `brand-monitoring` | `sub-skills/strategies/brand/brand-monitoring.md` | Tracking brand mentions, sentiment and reputation |
| `brand-protection` | `sub-skills/strategies/brand/brand-protection.md` | Trademarks, impersonation, brand abuse and takedowns |
| `brand-visual` | `sub-skills/strategies/brand/brand-visual.md` | Visual identity: typography, colours, design tokens, brand style guide |
| `branding` | `sub-skills/strategies/brand/branding.md` | Brand purpose, values, story, voice, narrative, brand guidelines |
| `content-marketing` | `sub-skills/strategies/brand/content-marketing.md` | Content types, formats, funnel mapping and repurposing across channels |
| `integrated-marketing` | `sub-skills/strategies/brand/integrated-marketing.md` | Coordinating channels with the PESO model and a consistent message |
| `marketing-psychology` | `sub-skills/strategies/brand/marketing-psychology.md` | Applying behavioural science, biases or mental models to marketing |
| `product-marketing` | `sub-skills/strategies/brand/product-marketing.md` | Creating or updating the product marketing context doc (positioning, ICP, audience) |
| `rebranding-strategy` | `sub-skills/strategies/brand/rebranding.md` | Rebrand execution: domain change, redirects, migration, announcement |

### Strategy: pricing, domain, localisation, paid and GEO

| Sub-skill | Path | Use when |
|---|---|---|
| `domain-architecture` | `sub-skills/strategies/commercial/domain/domain-architecture.md` | Subdomain, subfolder or separate domain decisions |
| `domain-selection` | `sub-skills/strategies/commercial/domain/domain-selection.md` | Choosing a domain name and TLD |
| `multi-domain-brand-seo` | `sub-skills/strategies/commercial/domain/multi-domain-brand-seo.md` | SEO and brand when several domains coexist |
| `free-tools` | `sub-skills/strategies/commercial/free-tools.md` | Building a free tool (calculator, grader) for leads or SEO |
| `generative-engine-optimization` | `sub-skills/strategies/commercial/geo.md` | Getting cited by AI search and LLMs (AEO, GEO, llms.txt) |
| `localization-strategy` | `sub-skills/strategies/commercial/localization.md` | Market and locale selection, multilingual rollout, localisation architecture |
| `open-source-strategy` | `sub-skills/strategies/commercial/open-source.md` | Open source as a growth and commercialisation path |
| `paid-ads-strategy` | `sub-skills/strategies/commercial/paid-ads.md` | Paid campaigns: targeting, bidding, budgets, optimisation |
| `discount-marketing-strategy` | `sub-skills/strategies/commercial/pricing/discount-marketing.md` | Promotional pricing: annual, lifetime deals, seasonal, startup and referral discounts |
| `offers` | `sub-skills/strategies/commercial/pricing/offers.md` | Designing the offer itself: bonuses, guarantees, urgency, naming |
| `pricing-strategy` | `sub-skills/strategies/commercial/pricing/pricing-strategy.md` | Pricing, packaging, tiers, freemium or trials |

### Strategy: conversion

| Sub-skill | Path | Use when |
|---|---|---|
| `conversion-optimization` | `sub-skills/strategies/conversion/conversion-optimization.md` | Improving conversions on a marketing page, form or funnel: page analysis, CRO process, experiment prioritisation |
| `onboarding` | `sub-skills/strategies/conversion/onboarding.md` | Post-signup activation, first-run experience, time to value |
| `paywalls` | `sub-skills/strategies/conversion/paywalls.md` | In-app paywalls, upgrade screens, feature gates, upsells |
| `popups` | `sub-skills/strategies/conversion/popups.md` | Popups, modals, slide-ins, exit intent, banners |
| `signup` | `sub-skills/strategies/conversion/signup.md` | Signup, registration or trial-start flows |

### Strategy: launch, growth and research

| Sub-skill | Path | Use when |
|---|---|---|
| `cold-start-strategy` | `sub-skills/strategies/launch/cold-start.md` | Getting first users with zero traction (0 to 1) |
| `customer-research` | `sub-skills/strategies/launch/customer-research.md` | Interviews, surveys, reviews, transcripts, personas, JTBD, voice of customer |
| `growth-funnel` | `sub-skills/strategies/launch/growth-funnel.md` | AARRR growth funnel, bottlenecks, lifecycle actions |
| `gtm-strategy` | `sub-skills/strategies/launch/gtm.md` | A GTM strategy or a full 12-month marketing plan: GTM mode, ICP, market entry, repositioning, AARRR |
| `indie-hacker-strategy` | `sub-skills/strategies/launch/indie-hacker.md` | Indie hacker and bootstrapped founder growth, build in public |
| `marketing-ideas` | `sub-skills/strategies/launch/marketing-ideas.md` | Brainstorming growth ideas or tactics when stuck |
| `pmf-strategy` | `sub-skills/strategies/launch/pmf.md` | Validating or measuring product-market fit before scaling |
| `product-launch` | `sub-skills/strategies/launch/product-launch.md` | Product launches, feature announcements, changelogs and release notes, waitlists, site go-live |
| `research-sources` | `sub-skills/strategies/launch/research-sources.md` | Information sources for content ideas, competitor monitoring, industry tracking |
| `retention-strategy` | `sub-skills/strategies/launch/retention.md` | Churn, retention, cancel flows, save offers, dunning, failed payments |

### Strategy: operations

| Sub-skill | Path | Use when |
|---|---|---|
| `marketing-council` | `sub-skills/strategies/operations/marketing-council.md` | Multiple expert perspectives or a simulated advisory board on a marketing question |
| `marketing-loops` | `sub-skills/strategies/operations/marketing-loops.md` | A recurring, agent-run marketing workflow on a cadence |

### Strategy: site structure and SEO audit

| Sub-skill | Path | Use when |
|---|---|---|
| `seo-strategy` | `sub-skills/strategies/structure/seo.md` | Organic SEO strategy, workflow order and prioritisation |
| `seo-audit` | `sub-skills/strategies/structure/seo-audit.md` | Auditing or diagnosing technical and on-page SEO |
| `website-structure` | `sub-skills/strategies/structure/website-structure.md` | Which pages to build, page hierarchy, navigation and site structure |
