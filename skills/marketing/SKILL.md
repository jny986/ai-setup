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
| `product-marketing` | Creating or updating the product marketing context doc (positioning, ICP, audience) |
| `customer-research` | Interviews, surveys, reviews, transcripts, personas, JTBD, voice of customer |
| `competitor-profiling` | Researching and profiling competitors from their URLs |
| `marketing-psychology` | Applying behavioural science, biases or mental models to marketing |
| **Strategy and planning** | |
| `marketing-plan` | A full marketing, growth or GTM plan |
| `marketing-ideas` | Brainstorming growth ideas or tactics when stuck |
| `marketing-council` | Multiple expert perspectives or a simulated advisory board on a marketing question |
| `marketing-loops` | A recurring, agent-run marketing workflow on a cadence |
| `content-strategy` | Deciding what content to create, topic clusters, editorial calendar |
| `launch` | Product launches, feature announcements, changelogs and release notes, Product Hunt, waitlists, site go-live |
| **Copy and creative** | |
| `copywriting` | Writing or rewriting page copy: headlines, value props, CTAs |
| `copy-editing` | Editing, proofreading or refreshing existing copy |
| `image` | Generating or optimising marketing images, mockups, banners, OG images |
| `video` | Producing video with AI tools or programmatic frameworks |
| **Conversion (CRO)** | |
| `cro` | Improving conversions on a marketing page or form |
| `signup` | Signup, registration or trial-start flows |
| `onboarding` | Post-signup activation, first-run experience, time to value |
| `popups` | Popups, modals, slide-ins, exit intent, banners |
| `paywalls` | In-app paywalls, upgrade screens, feature gates, upsells |
| `ab-testing` | Designing A/B tests or running an experimentation program |
| **Pricing and revenue** | |
| `pricing` | Pricing, packaging, tiers, freemium or trials |
| `offers` | Designing the offer itself: bonuses, guarantees, urgency, naming |
| `churn-prevention` | Churn, cancel flows, save offers, dunning, failed payments |
| `revops` | Lead lifecycle, lead scoring, routing, marketing-to-sales handoff |
| `sales-enablement` | Sales decks, one-pagers, objection handling, demo scripts |
| **SEO and discoverability** | |
| `seo-audit` | Auditing or diagnosing technical and on-page SEO |
| `ai-seo` | Getting cited by AI search and LLMs (AEO, GEO, llms.txt) |
| `schema` | Schema markup, structured data, JSON-LD |
| `programmatic-seo` | Template-driven SEO pages at scale |
| `site-architecture` | Page hierarchy, navigation, URLs, internal linking, sitemaps |
| `competitors` | Comparison, "vs" and alternative pages |
| `directory-submissions` | Submitting to startup, SaaS, AI or review directories for backlinks |
| `aso` | App Store or Google Play listing optimisation |
| `free-tools` | Building a free tool (calculator, grader) for leads or SEO |
| **Channels** | |
| `emails` | Lifecycle email sequences, drips, nurture and welcome flows |
| `cold-email` | Cold outbound emails, follow-ups, sending setup, multichannel cadences |
| `prospecting` | Finding and qualifying prospects to build an outreach list |
| `sms` | SMS, MMS or WhatsApp marketing |
| `social` | Social content, scheduling and listening on LinkedIn, X, Instagram, TikTok |
| `ads` | Paid campaigns: targeting, bidding, budgets, optimisation |
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
