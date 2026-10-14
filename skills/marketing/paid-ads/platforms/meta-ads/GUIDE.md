---
name: meta-ads
description: When the user wants to set up, optimize, or manage Meta (Facebook/Instagram) Ads. Also use when the user mentions "Meta Ads," "Facebook Ads," "Instagram Ads," "Meta Pixel," "Conversions API," "Advantage+," "lookalike audience," or "Meta retargeting." For landing pages, use dev/references/pages/marketing/landing-page.
metadata:
  version: 1.1.1
---

# Paid Ads: Meta Ads

Guides Meta (Facebook/Instagram) Ads setup, campaign structure, audience targeting, and creative optimization. Meta excels at demand generation and visual products; use when creating demand or when creative assets are strong.

## Campaign Structure

**Hierarchy**: Campaign → Ad Set → Ad (3 levels)

**Principle**: One objective per campaign. Multiple campaigns for the same objective split budget and data, slowing the algorithm's learning phase. Consolidate by objective; focus on clean structure and data-led decisions.

```
Account
├── Campaign: Prospecting
│   ├── Ad Set: Lookalike 1%
│   └── Ad Set: Broad (Advantage+)
├── Campaign: Retargeting
└── Campaign: Testing
```

**Naming**: `META_[Objective]_[Audience]_[Offer]_[Date]` (e.g., `META_Conv_Lookalike-Customers_FreeTrial_2024Q1`)

## Advantage+ & Automation

| Feature | Use |
|---------|-----|
| **Advantage+ Shopping Campaigns** | E-commerce; automatic audience discovery |
| **Dynamic Ads** | Product catalog; auto-generated creative |
| **Automatic Placements** | Let Meta optimize across Feed, Stories, Reels |
| **Advantage+ Audience** | Broad targeting; algorithm finds converters |

Provide diverse creative assets to enable multiple ad formats; algorithm performs better with variety.

## Campaign Objectives

| Objective | Use when |
|-----------|----------|
| Awareness | Reach; brand recall |
| Traffic | Clicks to site |
| Conversions | Leads; sales; app installs |
| Engagement | Video views; post engagement |

## Audience Targeting

| Type | Best for |
|------|----------|
| **Lookalikes** | Base on best customers (by LTV), not all customers |
| **Interest/behavior** | Broad; let algorithm optimize |
| **Advantage+** | Automated; fewer manual controls |
| **Retargeting** | Website visitors; engagers; custom audiences |

**Exclusions**: Existing customers; recent converters (7–14d).

## Creative Best Practices

- **Image**: Clear product; before/after; human faces; text &lt;20%
- **Video (15–30s)**: Hook 0–3s; problem 3–8s; solution 8–20s; CTA 20–30s
- **Placements**: Feed (FB/IG); Stories/Reels; vertical for Stories
- **Volume**: 3–5 ad variants per ad set for testing

## Optimization

- **Learning phase**: 50+ conversions per ad set per week to exit; avoid frequent changes during learning
- **CBO vs ABO**: Campaign Budget Optimization consolidates spend; use when scaling
- **Frequency**: &lt;3 to avoid fatigue
- **Creative refresh**: Plan continuous testing; creative fatigue is a main lever—refresh when performance drops

## Tracking

- **Meta Pixel** + **Conversions API**: Server-side for better attribution
- **Events API**: App events; server-to-server

## Pre-Launch Checklist

- [ ] Pixel installed; Conversions API configured
- [ ] Conversion events firing correctly
- [ ] Landing page mobile-friendly; fast load
- [ ] 3+ ad creatives per ad set
- [ ] Audience exclusions set

## Operating Playbooks

| Task | Load |
|------|------|
| When to kill, graduate or scale an ad; fatigue bands; testing structure; lead forms; Advantage+ transition; partnership ads; rolling reach | [meta-decision-system.md](references/meta-decision-system.md) |
| Andromeda-era creative volume, creative as targeting, identity keywords, AI variants, native-looking ads | [meta-andromeda-playbook.md](references/meta-andromeda-playbook.md) |
| Choosing which creative format to make next (S-F tier taxonomy) | [meta-creative-formats](../../ad-creative/references/meta-creative-formats.md) |

### Audience knowledge: creative vs targeting

After Meta's Andromeda update, put 80%+ of audience knowledge into creative (headlines, hooks, visuals, examples) and 20% into targeting filters. Target broadly and let specific creative do the targeting; interest-stacking now actively hurts. Prefer Advantage+ or broad targeting with several creatives that each speak to a different segment.

### Retargeting

- Segment by funnel stage: top (blog readers, video viewers), middle (pricing/feature visitors), bottom (cart abandoners, trial users).
- Windows: hot 1-7 days, warm 7-30 days at 3-5x/week, cold 30-90 days at 1-2x/week.
- Retarget with different offers, not the same one: the top reason people didn't buy is that the offer wasn't right for them.
- Run four ad types together: objection-handling, proof testimonial carousel, other-offers CBO, value-first audit or assessment.

### Landing page alignment

Run 20-40 headlines as ad variations, then mirror the winning headline verbatim in the landing page H1, subheadline and lead-in. Expect a 15-20% minimum lift in landing-page conversion. Keep at least three split tests running across ad creative, landing page, offer or post-conversion flow.

### Scaling

- Raise budgets about 20% at a time (never 30%+ in one move) and wait 3-5 days between increases.
- Judge scaling headroom on blended ROAS and net cash flow, not per-ad-set ROAS; find the break-even ROAS/CPA ceiling and scale toward it.

### Conflicts with ours (kostja wording above wins)

- **Interest/behaviour targeting:** the table above lists it as broad and algorithm-optimised. Ours says interest-stacking now hurts post-Andromeda and recommends broad targeting with differentiated creative.
- **Frequency:** the guide above says keep frequency under 3. Ours uses bands by campaign type (warning at 3.0-3.5 for scaling-campaign ads; account-wide wall at 3.5).

## Related Skills

- **paid-ads-strategy**: Channel selection; creative frameworks; budget allocation
- **dev/references/pages/marketing/landing-page**: LP for paid traffic
- **analytics-tracking**: Conversion tracking; ROAS
