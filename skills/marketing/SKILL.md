---
name: marketing
description: "Marketing playbooks for SaaS and software products. Use for any marketing, growth, or go-to-market task: copywriting and copy editing, CRO (landing pages, signup, onboarding, popups, paywalls), SEO (audits, AI search, schema, programmatic pages, site architecture), content and social, email, SMS and cold outreach, paid ads and ad creative, analytics, attribution and A/B tests, pricing and offers, launches, PR, events, partnerships, referrals and influencers, churn and retention, sales enablement, RevOps, prospecting, competitor and customer research, positioning and product marketing context, app store optimisation, and marketing images or video."
argument-hint: "[guide] [task]"
license: MIT
metadata:
  version: "1.0"
  author: jny986
  author-url: https://jny986.com
  based_on: coreyhaines31/marketingskills@v2.11.27 (MIT)
---

A router over the marketing guides. A guide lives at either a flat `<name>/GUIDE.md` or a nested `<category>/[<group>/]<name>/GUIDE.md` in this skill's folder, with its own `references/` and `assets/` beside it. Guides are moving from flat to nested one category at a time; [references/name-table.md](references/name-table.md) lists every final name, its nested path and the old names that alias to it.

## Steps

1. **Load product context.** Read `docs/marketing/product-marketing.md` if it exists. Guides refer to it as "the product marketing context"; if it's missing and the task depends on it, offer the `product-marketing` guide first.
2. **Pick the guide.**
   - Argument names a guide: first resolve it through the name table. An old name in the Aliases column becomes that row's final name.
     - The guide table has a row with the final name: use it.
     - It doesn't yet (its category hasn't moved): use the row of its alias, the flat guide it replaces. If it has no alias, pick by "Use when" below.
   - No argument and no task: show the table below and ask what they're working on.
   - Otherwise: pick the row whose "Use when" fits the task. When two fit equally, ask once.
3. **Follow the guide.** Read `<path>/GUIDE.md`, where `<path>` is the second code span in its table row, or the name itself when the row has none (a flat guide). Follow it as if it were the skill. Its relative links (`references/…`, `assets/…`) resolve against the guide's own folder.

When a guide hands off to another skill by name ("see cro", a **Related Skills** entry, "hand off to copywriting"), that skill is the guide of the same name here, resolved through steps 2 and 3.

## Guides

| Guide | Use when |
|---|---|
| **Foundations** | |
| `product-marketing` `strategies/brand/product-marketing` | Creating or updating the product marketing context doc (positioning, ICP, audience) |
| `marketing-psychology` `strategies/brand/marketing-psychology` | Applying behavioural science, biases or mental models to marketing |
| **Strategy and planning** | |
| **Copy and creative** | |
| `copywriting` | Writing or rewriting page copy: headlines, value props, CTAs |
| `copy-editing` | Editing, proofreading or refreshing existing copy |
| `image` | Generating or optimising marketing images, mockups, banners, OG images |
| `video` | Producing video with AI tools or programmatic frameworks |
| **Conversion (CRO)** | |
| `ab-testing` | Designing A/B tests or running an experimentation program |
| **Brand and commercial strategy** | |
| `branding` `strategies/brand/branding` | Brand purpose, values, story, voice, narrative, brand guidelines |
| `brand-visual` `strategies/brand/brand-visual` | Visual identity: typography, colours, design tokens, brand style guide |
| `brand-monitoring` `strategies/brand/brand-monitoring` | Tracking brand mentions, sentiment and reputation |
| `brand-protection` `strategies/brand/brand-protection` | Trademarks, impersonation, brand abuse and takedowns |
| `integrated-marketing` `strategies/brand/integrated-marketing` | Coordinating channels with the PESO model and a consistent message |
| `rebranding-strategy` `strategies/brand/rebranding` | Rebrand execution: domain change, redirects, migration, announcement |
| `content-marketing` `strategies/brand/content-marketing` | Content types, formats, funnel mapping and repurposing across channels |
| `domain-selection` `strategies/commercial/domain/domain-selection` | Choosing a domain name and TLD |
| `domain-architecture` `strategies/commercial/domain/domain-architecture` | Subdomain, subfolder or separate domain decisions |
| `multi-domain-brand-seo` `strategies/commercial/domain/multi-domain-brand-seo` | SEO and brand when several domains coexist |
| `localization-strategy` `strategies/commercial/localization` | Market and locale selection, multilingual rollout, localisation architecture |
| `open-source-strategy` `strategies/commercial/open-source` | Open source as a growth and commercialisation path |
| `discount-marketing-strategy` `strategies/commercial/pricing/discount-marketing` | Promotional pricing: annual, lifetime deals, seasonal, startup and referral discounts |
| **Pricing and revenue** | |
| `pricing-strategy` `strategies/commercial/pricing/pricing-strategy` | Pricing, packaging, tiers, freemium or trials |
| `offers` `strategies/commercial/pricing/offers` | Designing the offer itself: bonuses, guarantees, urgency, naming |
| `revops` | Lead lifecycle, lead scoring, routing, marketing-to-sales handoff |
| `sales-enablement` | Sales decks, one-pagers, objection handling, demo scripts |
| **SEO and discoverability** | |
| `generative-engine-optimization` `strategies/commercial/geo` | Getting cited by AI search and LLMs (AEO, GEO, llms.txt) |
| `directory-submissions` | Submitting to startup, SaaS, AI or review directories for backlinks |
| `aso` | App Store or Google Play listing optimisation |
| `free-tools` `strategies/commercial/free-tools` | Building a free tool (calculator, grader) for leads or SEO |
| **SEO (nested)** | |
| `competitor-research` `seo/content/competitor-research` | Analysing or profiling competitors (keywords, content, backlinks, positioning) from names or URLs |
| `comparison-pages` `seo/content/comparison-pages` | Strategy and content for comparison, "vs" and alternative pages |
| `content-strategy` `seo/content/content-strategy` | SEO content plans: topic clusters, pillar pages, editorial calendar, content prioritisation |
| `content-optimization` `seo/content/content-optimization` | Optimising an article: length, headings, keyword placement, multimedia |
| `eeat-signals` `seo/content/eeat-signals` | E-E-A-T, author and trust signals |
| `keyword-research` `seo/content/keyword-research` | Keyword discovery, intent, clustering |
| `entity-seo` `seo/entity-seo` | Entities, Knowledge Panel, @id and sameAs |
| `local-seo` `seo/local` | Local search, Google Business Profile, NAP |
| `backlink-analysis` `seo/off-page/backlink-analysis` | Analysing backlink profiles and link gaps |
| `link-building` `seo/off-page/link-building` | Earning backlinks and outreach |
| `meta-description` `seo/on-page/description` | Writing or auditing meta descriptions |
| `featured-snippet` `seo/on-page/featured-snippet` | Winning featured snippets and position zero |
| `heading-structure` `seo/on-page/heading` | H1-H6 structure and hierarchy |
| `image-optimization` `seo/on-page/image-optimization` | Image SEO: alt text, formats, lazy loading, image sitemaps, OG images |
| `internal-links` `seo/on-page/internal-links` | Internal linking and anchor text |
| `page-metadata` `seo/on-page/metadata` | Sitewide metadata audit, implementation and release checks |
| `open-graph` `seo/on-page/open-graph` | Open Graph tags and social previews |
| `schema-markup` `seo/on-page/schema` | Schema markup, structured data, JSON-LD |
| `serp-features` `seo/on-page/serp-features` | SERP features, rich results, zero-click patterns |
| `title-tag` `seo/on-page/title` | Writing or auditing title tags |
| `twitter-cards` `seo/on-page/twitter-cards` | Twitter/X card tags |
| `url-structure` `seo/on-page/url-structure` | Site-wide URL structure and hierarchy |
| `url-slug` `seo/on-page/url-slug` | Creating or validating URL slugs for content pages |
| `video-optimization` `seo/on-page/video-optimization` | Video SEO: VideoObject, video sitemaps, key moments |
| `parasite-seo` `seo/parasite-seo` | Ranking through third-party high-authority platforms |
| `programmatic-seo` `seo/programmatic-seo` | Template-driven SEO pages at scale |
| `canonical-tag` `seo/technical/canonical` | Canonical tags and duplicate content |
| `core-web-vitals` `seo/technical/core-web-vitals` | LCP, INP, CLS and page speed |
| `site-crawlability` `seo/technical/crawlability` | Crawlability, crawl budget, site structure for bots |
| `indexing` `seo/technical/indexing` | Getting pages indexed; indexing problems |
| `indexnow` `seo/technical/indexnow` | IndexNow instant URL submission |
| `mobile-friendly` `seo/technical/mobile-friendly` | Mobile-friendliness and mobile-first indexing |
| `rendering-strategies` `seo/technical/rendering-strategies` | SSR, SSG, CSR and rendering for SEO |
| `robots-txt` `seo/technical/robots` | robots.txt rules and crawler access |
| `xml-sitemap` `seo/technical/sitemap` | XML sitemaps: structure, submission, segmentation |
| **Strategies (nested)** | |
| `conversion-optimization` `strategies/conversion/conversion-optimization` | Improving conversions on a marketing page, form or funnel: page analysis, CRO process, experiment prioritisation |
| `signup` `strategies/conversion/signup` | Signup, registration or trial-start flows |
| `onboarding` `strategies/conversion/onboarding` | Post-signup activation, first-run experience, time to value |
| `popups` `strategies/conversion/popups` | Popups, modals, slide-ins, exit intent, banners |
| `paywalls` `strategies/conversion/paywalls` | In-app paywalls, upgrade screens, feature gates, upsells |
| `gtm-strategy` `strategies/launch/gtm` | A GTM strategy or a full 12-month marketing plan: GTM mode, ICP, market entry, repositioning, AARRR |
| `product-launch` `strategies/launch/product-launch` | Product launches, feature announcements, changelogs and release notes, waitlists, site go-live |
| `retention-strategy` `strategies/launch/retention` | Churn, retention, cancel flows, save offers, dunning, failed payments |
| `customer-research` `strategies/launch/customer-research` | Interviews, surveys, reviews, transcripts, personas, JTBD, voice of customer |
| `marketing-ideas` `strategies/launch/marketing-ideas` | Brainstorming growth ideas or tactics when stuck |
| `cold-start-strategy` `strategies/launch/cold-start` | Getting first users with zero traction (0 to 1) |
| `growth-funnel` `strategies/launch/growth-funnel` | AARRR growth funnel, bottlenecks, lifecycle actions |
| `indie-hacker-strategy` `strategies/launch/indie-hacker` | Indie hacker and bootstrapped founder growth, build in public |
| `pmf-strategy` `strategies/launch/pmf` | Validating or measuring product-market fit before scaling |
| `research-sources` `strategies/launch/research-sources` | Information sources for content ideas, competitor monitoring, industry tracking |
| `marketing-council` `strategies/operations/marketing-council` | Multiple expert perspectives or a simulated advisory board on a marketing question |
| `marketing-loops` `strategies/operations/marketing-loops` | A recurring, agent-run marketing workflow on a cadence |
| `seo-strategy` `strategies/structure/seo` | Organic SEO strategy, workflow order and prioritisation |
| `seo-audit` `strategies/structure/seo-audit` | Auditing or diagnosing technical and on-page SEO |
| `website-structure` `strategies/structure/website-structure` | Which pages to build, page hierarchy, navigation and site structure |
| **Channels** | |
| `emails` | Lifecycle email sequences, drips, nurture and welcome flows |
| `cold-email` | Cold outbound emails, follow-ups, sending setup, multichannel cadences |
| `prospecting` | Finding and qualifying prospects to build an outreach list |
| `sms` | SMS, MMS or WhatsApp marketing |
| `social` | Social content, scheduling and listening on LinkedIn, X, Instagram, TikTok |
| `paid-ads-strategy` `strategies/commercial/paid-ads` | Paid campaigns: targeting, bidding, budgets, optimisation |
| `ad-creative` | Generating or iterating ad copy and creative at scale |
| `community-marketing` | Building a community (Discord, Slack, forum) or advocates |
| `influencer-marketing` | Creator, influencer or ambassador partnerships |
| `co-marketing` | Partner marketing and joint campaigns |
| `referrals` | Referral or affiliate programs, word of mouth |
| `public-relations` | Press coverage, journalist pitches, media strategy |
| `events` | Webinars, conferences, sponsorships, speaking, field events |
| `lead-magnets` | Gated content, ebooks, checklists, templates for email capture |
| **Measurement** | |
| `analytics` | Tracking setup: GA4, GTM, events, UTMs, conversion tracking |
| `attribution` | Which channels drive revenue, attribution models, MMM, incrementality |
