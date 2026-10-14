---
name: affiliate-marketing
description: When the user wants to plan, implement, or optimize affiliate marketing strategy. Also use when the user mentions "affiliate marketing," "affiliate program strategy," "CPS model," "affiliate recruitment," "commission structure," "affiliate partners," "affiliate network," "affiliate tracking," "affiliate commission," or "partner marketing." Also use when the user mentions "affiliate program design," "cookie duration," "recurring commissions," "super affiliates," "buyout clause," "affiliate reconciliation," "affiliate incrementality," "Rewardful," "Tolt," "PartnerStack," or "partner program." For customer referral programs, use referral-program. For affiliate page, use `dev/references/pages/marketing/program`.
metadata:
  version: 1.0.1
  based_on_repo: kostja94/marketing-skills, coreyhaines31/marketingskills
  based_on_version: v1.0.0(8dd89c5), v2.11.29(c7d7dfb)
  based_on_skill: affiliate-marketing, referrals
---

# Channels: Affiliate

Guides affiliate marketing strategy for AI/SaaS products. Affiliate marketing uses a CPS (Cost Per Sale) model—pay only when sales occur. ROI typically 5:1 to 10:1; CAC 40%–50% lower than paid ads.

## Initial Assessment

**Project context:** Read the product marketing context when present and load only what is relevant to this task. Otherwise use available project material or user-provided facts and ask for missing information.

Identify:
1. **Product type**: SaaS, AI tool, subscription
2. **Commission model**: Pay-per-sale, pay-per-lead, pay-per-click
3. **Target affiliates**: Content creators, publishers, coupon sites

## Referral vs. Affiliate

Customer referral rewards existing customers, usually with one-time or limited rewards: higher trust, lower volume. Affiliate reaches audiences you don't have, often non-customers, on an ongoing commission: higher volume, variable trust, and it suits higher-ticket products that justify commissions. For customer referral design see **referral-program**; both can run together.

## Commission Models

| Model | Use | Typical Rate |
|-------|-----|--------------|
| **Pay-per-sale** | Most common; pay on conversion | 10%–20% |
| **Pay-per-lead** | Lead gen (signup, form fill) | $5–50/lead |
| **Pay-per-click** | Rare; risk of abuse | $0.01–10.50/click |

For SaaS: Prefer pay-per-sale or pay-per-lead. Recurring commissions for subscriptions.

## Key Terms

| Term | Definition |
|------|------------|
| **Cookie duration** | Attribution window (typically 30–90 days) |
| **Recurring commission** | Ongoing % from subscription renewals |
| **Sub-affiliate** | Affiliates who recruit other affiliates |
| **Performance bonus** | Extra reward when affiliate hits sales targets |
| **Attribution** | Linking sale to correct affiliate |

## Promotion Channels

- **Content creators**: Bloggers, YouTubers, podcasters, social influencers
- **Publishers**: Media, niche sites, email newsletters
- **Coupon/cashback**: Price-sensitive users; see **discount-marketing-strategy** for code strategy
- **Professional affiliates**: Agencies managing multiple programs
- **Communities**: Facebook Groups, Discord, Reddit, forums
- **Existing customers**: Word-of-mouth via referral rewards

## Setup Options

*Product and website examples are illustrative only. No affiliation, partnership, or endorsement implied.*

| Approach | Use |
|----------|-----|
| **Self-build** | Forms (e.g. Google Forms); quick, low budget |
| **Third-party** | Affiliate tracking platforms (e.g. Rewardful, Tapfiliate) for AI/SaaS |

Submit program to affiliate program directories after launch for discoverability.

## Recruitment Strategies

1. **Dedicated landing page**: Clear commission, payout terms, cookie duration, signup flow; link in nav/footer.
2. **Partner personas**: Define 5+ personas (bloggers, YouTubers, newsletter owners, community admins); list audience fit and motivations.
3. **Target high-influence types**: SEO content owners ranking for your keywords; reviewers/listicle sites; media buyers.
4. **Reverse research**: Find affiliates promoting competitors; they may promote you too.
5. **Unconventional outreach**: Competitor backlink analysis; creative outreach beyond cold email and networks.

Expect a small fraction of partners to drive most sales—quality over vanity metrics.

## Program Design & Operations

- **Commission structures, cookie windows, recruitment and outreach template, enablement, tools, fraud prevention**: [references/affiliate-programs.md](references/affiliate-programs.md)
- **Running the program** (cohort economics, activation funnel, executable terms decision table, reconciliation, incrementality): [references/affiliate-operations.md](references/affiliate-operations.md). Check economics before offering a rate, and measure growth separately from attribution.

## Affiliate Power-Law Mechanics

Detail is in [../referral-program/references/viral-mechanisms.md](../referral-program/references/viral-mechanisms.md#affiliate-mechanics).

- **20/80 rule**: roughly 20% of affiliates drive ~80% of results. Identify super-promoters and invest in them (higher tiers, custom assets, co-marketing, early access) rather than recruiting passive long-tail sign-ups.
- **Buyout clauses**: for high performers on recurring commissions, reserve the right to buy out the future stream for a lump sum, commonly ~12x the monthly commission.
- **Launch-affiliate tactic**: time promotion around a launch or hard deadline with shared assets and a reason to act now, so promotion stacks instead of trickling.

## Implementation Flow

1. **Assess product fit**: Target audience size, product complexity, commission margin, tracking feasibility. SaaS subscriptions suit recurring commissions.
2. **Design commission structure**: 20%–40% typical; cookie 60–90 days; payment cycle (e.g., 15th of month); minimum payout (e.g., $50).
3. **Create marketing materials**: Banners, social posts, email templates; landing page with commission details and signup flow.
4. **Recruit partners**: Publish to affiliate program directories; outreach to creators and influencers.
5. **Monitor and optimize**: Track conversion rate, ROI, AOV; review affiliate performance; detect fraud.

## Pitfalls and Prevention

| Risk | Prevention |
|------|------------|
| **Affiliate fraud** | Fake clicks, self-referrals, fake conversions. Use platform fraud tools; vet affiliates; avoid auto-approve. |
| **Brand bidding** | Affiliates bid on your brand terms in Google Ads; you pay commission for traffic you already own. Prohibit in terms; monitor paid search; use brand monitoring tools. See **paid-ads-strategy** for paid ads context. |
| **Program terms** | Cookie length, performance bonus, sub-affiliate rules, payment threshold—set clearly in terms before launch. |

## Best Practices

- **rel=sponsored**: Tag affiliate links per Google guidelines
- **Transparent disclosure**: Disclose affiliate relationships
- **Recruit authentic affiliates**: Align with brand; avoid low-quality networks
- **Diversify partners**: Multiple affiliates reduce risk
- **SEO for affiliate content**: Affiliate content drives organic traffic

## Output Format

- **Commission model** recommendation
- **Channel** strategy
- **Recruitment** approach
- **Tool** selection
- **Checklist** for launch

## Related Skills

- **paid-ads-strategy**: Paid ads context; brand bidding monitoring; when affiliates bid on brand terms
- **discount-marketing-strategy**: Affiliate-specific promo codes; coupon sites; code strategy
- `dev/references/pages/marketing/program`: Landing page for affiliate signup; apply `dev/references/pages/marketing/landing-page` principles
- `dev/references/pages/marketing/landing-page`: Generic landing page structure, CTA, conversion; applies to affiliate signup pages
- **influencer-marketing**: Often paired; influencers can be affiliates
- **referral-program**: User-driven referral vs. affiliate-driven; virality mechanics and review programs
- **directory-submission**: Directory submission complements affiliate; both drive backlinks and traffic
- **community-forum**: Communities (Discord, Reddit, forums) as affiliate recruitment channel
