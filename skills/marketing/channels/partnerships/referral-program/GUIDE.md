---
name: referral-program
description: When the user wants to plan, implement, or optimize referral program strategy. Also use when the user mentions "referral program," "referral marketing," "user referral," "refer-a-friend," "word-of-mouth growth," "referral rewards," "referral tracking," "referral code," "referral incentives," or "viral loop." Also use when the user mentions "viral coefficient," "K-factor," "powered by badge," "product-led virality," "exposure loop," "review program," "G2 reviews," "Capterra reviews," "Trustpilot," "review requests," or "testimonials." For affiliate programs, use affiliate-marketing. For referral landing copy, use landing-page-generator.
metadata:
  version: 1.0.1
---

# Channels: Referral

Guides referral program strategy for AI/SaaS products. Leverage existing users to drive growth; 3%-5% conversion vs 1%-2% for ads; CAC 50%-70% lower; referred users LTV 30%-50% higher, retention 20%-30% higher. Referral is necessity in overseas markets, not alternative.

## Initial Assessment

**Project context:** Read the product marketing context when present and load only what is relevant to this task. Otherwise use available project material or user-provided facts and ask for missing information.

Identify:
1. **Product type**: SaaS, AI tool, subscription
2. **User base**: Size, engagement, retention
3. **Goal**: Signups, purchases, or both
4. **Economics**: Average customer LTV, current CAC from other channels, incentive budget
5. **Current state**: Existing program, current referral rate, incentives already tried
6. **Fit**: Is the product shareable, with network effects or natural word-of-mouth?

## Engineer Virality First?

Before building a reward program, check whether virality can be built into the product, which is often cheaper and more durable than paid referrals. Only build it where it fits naturally.

- **Natural** (build for it): collaboration tools, communication tools, user-facing outputs; every use exposes the product to non-users.
- **Limited** (don't force it): backend, internal-only, and infrastructure products. Invest in referral rewards, content, and partnerships instead.

On the natural end, consider Powered By badges, exposure loops, social sharing, embeds, and watermarks before or alongside a reward program. The spectrum diagnostic, the 7 mechanisms, and value-presentation and timing detail are in [references/viral-mechanisms.md](references/viral-mechanisms.md).

## Referral vs. Affiliate vs. Influencer

| Dimension | Referral | Affiliate | Influencer |
|-----------|----------|-----------|------------|
| **Who** | Existing users | Professional promoters | KOLs |
| **Incentive** | Discounts, credits | Commission | Fees, product |
| **Barrier** | Low (all users) | Medium | High |
| **Conversion** | 3%-5% | Varies | Varies |

**Referral vs affiliate**: Referral needs no landing page or application; integrated in dashboard. Affiliate requires landing page and approval.

## Reward Models

| Model | Use |
|-------|-----|
| **Two-way** | Both referrer and referee get rewards; highest participation |
| **One-way** | Only referrer rewarded; cost control |
| **Tiered** | Rewards increase with referral count (e.g. $10 for 1-5, $15 for 6-10, $20 for 11+); incentivizes volume |

**Benchmark**: Rewards typically 10%-30% of product price; ~11% off or ~$21 value; weak incentives = low participation. Triggers: signup, purchase, activation, or sustained use.

## Mechanism Types

| Type | Use |
|------|-----|
| **Link-based** | Unique referral link; easy to implement; accurate tracking; share via email, social, SMS; works for web and app |
| **Code-based** | Referral code (e.g. FRIEND20); memorable; offline events; mobile-friendly input |
| **Social referral** | Share buttons (Facebook, X, LinkedIn); viral spread; friend trust; young users |

## Referral Loop

`Trigger moment -> Share action -> Referred user converts -> Reward -> (loop)`

**Trigger moments** (high intent): right after the first "aha", after a milestone, after exceptional support, after a renewal or upgrade.

**Share mechanism, ranked by effectiveness:** in-product sharing, personalized link, email invitation, social sharing, referral code (works offline).

**Reward presentation:** lead with the bigger-*feeling* number ("$10 off", not "40% off", on a low-priced product). Reward at the aha moment or milestone, not signup. Reduce friction with one-click share and pre-written messages. See [references/viral-mechanisms.md](references/viral-mechanisms.md#referral-best-practices) for thresholds and friction detail, and [references/program-examples.md](references/program-examples.md) for examples, incentive sizing, and K-factor/referral-rate benchmarks.

## Tracking & Attribution

| Method | Use |
|-------|-----|
| **Cookie** | Web apps; 30-90 day window |
| **URL params** | All platforms; persistent in link |
| **Referral code** | Mobile, offline; manual entry |
| **Account association** | Long-term tracking; subscription products |

**Attribution window**: 30-90 days typical; 180 days for subscription. First-touch attribution to avoid double-counting.

## Fraud Prevention

| Risk | Action |
|------|--------|
| **Self-referral** | Detect same device, payment, IP |
| **Fake accounts** | Validate email, payment; monitor patterns |
| **Bulk/automation** | Rate limits; anomaly detection |
| **Per-user cap** | e.g. Max 10 referrals per user |

Use tool anti-fraud features; audit referrals regularly.

## Design Framework

1. **Reward structure**: Type (cash, discount, credits, free service); amount (10%-30% of price); trigger; cap
2. **Tracking**: Choose method; set attribution window; first-touch rule
3. **UX**: One-click share; clear rules; dashboard with referral data; notify on success
4. **Fraud prevention**: See above
5. **Monitor & optimize**: Referral rate, conversion, CAC, LTV; A/B test rewards and flow

## Optimization

**Few customers referring:** ask at better moments, simplify sharing, test incentive types, make the prompt prominent in-product.
**Referrals not converting:** improve the referred user's landing experience, strengthen the new-user incentive, make the referrer's endorsement visible.

| Problem | Fix |
|---------|-----|
| Low awareness | Prominent in-app prompts |
| Low share rate | One-click sharing |
| Low conversion | Optimize the referred-user experience |
| Fraud/abuse | Verification, limits |
| One-time referrers | Tiered or gamified rewards |

**A/B tests:** incentive (amount, type, single vs. double-sided, timing), messaging (program description, CTA, landing copy), and placement (where and when the prompt appears).

## Best Practices

- **Run multiple programs**: Target different audiences, stages, goals
- **Tiered rewards**: Motivate top performers; progressive incentives
- **Friction-free sharing**: Mobile-friendly; one-click share
- **Time-boxed incentives**: "Refer this week for $15 off" creates urgency
- **Placement**: Web, email, app, in-product touchpoints; dashboard integration primary

## Implementation

| Approach | Use |
|----------|-----|
| **Self-build** | Full control; low cost; URL params or cookie + reward logic + fraud checks; open-source (e.g. RefRef) for faster start |
| **Third-party** | Fast launch; Cello, Viral Loops, ReferralCandy (e-commerce), Impact (enterprise); monthly fee |

**Placement**: Most programs integrate in product dashboard; no landing page or application needed. Optional landing page for value prop, rewards, and case studies.

**Startup cost**: Typically hundreds for tools + dev.

## Tools

| Tool | Use |
|------|-----|
| **Cello** | SaaS; AI-driven automation |
| **Viral Loops** | Referral + waitlist + contests |
| **ReferralCandy** | Shopify, e-commerce |
| **Impact** | Enterprise; unified platform |
| **RefRef** | Open-source; self-hosted |
| **Mention Me** | Enterprise referral programs |
| **Dub.co** | Link tracking and attribution |

## KPIs

Referral rate, conversion, CAC, LTV of referred users, referred-user retention.

- **Program health**: active referrers (referred someone in the last 30 days), referral conversion rate, rewards earned/paid
- **Business impact**: % of new customers from referrals, CAC via referral vs. other channels, LTV of referred customers, program ROI

## Launch Checklist

**Before launch**
- [ ] Goals and success metrics defined; incentive structure designed
- [ ] Referral tool built or configured; tracking and attribution set up
- [ ] Fraud rules and terms and conditions defined
- [ ] Optional referral landing page created
- [ ] Full referral flow tested

**Launch:** announce to existing customers, add in-app prompts, update the website, brief support.

**First 30 days:** review the conversion funnel, identify top referrers, gather feedback, fix friction, remind non-referrers by email.

## Email Sequences

**Launch email:** subject "You can now earn [reward] for sharing [Product]"; body: what they earn, what the friend gets, the unique link, and the three steps (share, friend signs up, you both get the reward).

**Nurture:** day 7 reminder; day 30 "Know anyone who'd benefit?"; day 60 success story plus prompt; after a milestone, "You achieved [X], know others who'd want this?" See **email-marketing** for sequence design.

## Affiliate Programs

Affiliate programs have their own guide: **affiliate-marketing**. Affiliate power-law mechanics (buyout clauses, the 20/80 rule, launch-affiliate tactics) are in [references/viral-mechanisms.md](references/viral-mechanisms.md#affiliate-mechanics).

## Review Programs

Reviews are the other half of customer advocacy. For review-request programs, responding to reviews, reputation triage, and reusing testimonials with permission (G2, Capterra, Trustpilot, Google, app stores), see [references/review-programs.md](references/review-programs.md); operations are in [references/review-program-operations.md](references/review-program-operations.md). Platform rules differ, so check [references/review-platform-rules.md](references/review-platform-rules.md) before proposing incentives or automation.

## Output Format

- **Reward model** and mechanism type (link/code/social)
- **Tracking** approach and attribution window
- **Placement** (dashboard vs landing page)
- **Fraud prevention** measures
- **Tool** selection (self-build vs third-party)
- **KPI** framework

## Related Skills

- **discount-marketing-strategy**: Referral rewards (discounts, credits); 10–30% benchmark; campaign design
- **affiliate-marketing**: Different audience; can run both
- **influencer-marketing**: Brand building vs. user-driven growth
- **product-launch**: Launching the referral program
- **email-marketing**: Referral nurture campaigns
- **marketing-psychology**: Understanding referral motivation
- **directory-submission**: Directory submission for discovery; referral for user-driven growth
- **analytics-tracking**: Referral link tracking, UTM
