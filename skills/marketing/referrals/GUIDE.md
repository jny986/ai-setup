---
name: referrals
description: Design, optimize and measure referral, affiliate and review programs, including product-embedded virality.
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on: coreyhaines31/marketingskills@v2.11.27 (MIT)
---

# Referral & Affiliate Programs

## Before Starting

Gather this context (ask only for what the product marketing context doesn't cover):

### 1. Program Type
- Customer referral program, affiliate program, or both?
- B2B or B2C?
- What's the average customer LTV?
- What's your current CAC from other channels?

### 2. Current State
- Existing referral/affiliate program?
- Current referral rate (% who refer)?
- What incentives have you tried?

### 3. Product Fit
- Is your product shareable?
- Does it have network effects?
- Do customers naturally talk about it?

### 4. Resources
- Tools/platforms you use or consider?
- Budget for referral incentives?

---

## Should You Engineer Virality First?

Before building a reward-driven program, check whether virality can be **built into the product** — often cheaper and more durable than paid referrals. Build it only where it **naturally fits**.

Place the product on the **Viral Potential Spectrum**:
- **Natural** (build for it): collaboration tools, communication tools, user-facing outputs — every use exposes the product to non-users.
- **Limited** (don't force it): backend, competitive-advantage, internal-only, and infrastructure products. Invest in referral programs, content, and partnerships instead.

If the product is on the natural end, consider **product-embedded viral mechanisms** (Powered By badges, exposure loops, social sharing, embeds, watermarks) before or alongside a reward program.

**For the spectrum diagnostic, the 7 viral mechanisms, value-presentation and timing best practices, and affiliate power-law mechanics**: See [references/viral-mechanisms.md](references/viral-mechanisms.md)

---

## Referral vs. Affiliate

### Customer Referral Programs

**Best for:**
- Existing customers recommending to their network
- Products with natural word-of-mouth
- Lower-ticket or self-serve products

**Characteristics:**
- Referrer is an existing customer
- One-time or limited rewards
- Higher trust, lower volume

### Affiliate Programs

**Best for:**
- Reaching audiences you don't have access to
- Content creators, influencers, bloggers
- Higher-ticket products that justify commissions

**Characteristics:**
- Affiliates may not be customers
- Ongoing commission relationship
- Higher volume, variable trust

---

## Referral Program Design

### The Referral Loop

```
Trigger Moment → Share Action → Convert Referred → Reward → (Loop)
```

### Step 1: Identify Trigger Moments

**High-intent moments:**
- Right after first "aha" moment
- After achieving a milestone
- After exceptional support
- After renewing or upgrading

### Step 2: Design Share Mechanism

**Ranked by effectiveness:**
1. In-product sharing (highest conversion)
2. Personalized link
3. Email invitation
4. Social sharing
5. Referral code (works offline)

### Step 3: Choose Incentive Structure

**Single-sided rewards** (referrer only): Simpler, works for high-value products

**Double-sided rewards** (both parties): Higher conversion, win-win framing

**Tiered rewards**: Gamifies referral process, increases engagement

**Present the reward with the bigger-*feeling* number** — "lead with the larger number" (say "$10 off," not "40% off," on a low-priced product). Reward at the **aha moment or milestone**, not signup. Reduce friction: one-click share, pre-written messages.

**For examples, incentive sizing, and K-factor/referral-rate benchmarks**: See [references/program-examples.md](references/program-examples.md)

**For value-presentation thresholds and friction-reduction detail**: See [references/viral-mechanisms.md](references/viral-mechanisms.md#referral-best-practices)

---

## Program Optimization

### Improving Referral Rate

**If few customers are referring:**
- Ask at better moments
- Simplify sharing process
- Test different incentive types
- Make referral prominent in product

**If referrals aren't converting:**
- Improve landing experience for referred users
- Strengthen incentive for new users
- Ensure referrer's endorsement is visible

### A/B Tests to Run

**Incentive tests:** Amount, type, single vs. double-sided, timing

**Messaging tests:** Program description, CTA copy, landing page copy

**Placement tests:** Where and when the referral prompt appears

### Common Problems & Fixes

| Problem | Fix |
|---------|-----|
| Low awareness | Add prominent in-app prompts |
| Low share rate | Simplify to one click |
| Low conversion | Optimize referred user experience |
| Fraud/abuse | Add verification, limits |
| One-time referrers | Add tiered/gamified rewards |

---

## Measuring Success

### Key Metrics

**Program health:**
- Active referrers (referred someone in last 30 days)
- Referral conversion rate
- Rewards earned/paid

**Business impact:**
- % of new customers from referrals
- CAC via referral vs. other channels
- LTV of referred customers
- Referral program ROI

### Typical Findings

- Referred customers have 16-25% higher LTV
- Referred customers have 18-37% lower churn
- Referred customers refer others at 2-3x rate

---

## Launch Checklist

### Before Launch
- [ ] Define program goals and success metrics
- [ ] Design incentive structure
- [ ] Build or configure referral tool
- [ ] Create referral landing page
- [ ] Set up tracking and attribution
- [ ] Define fraud prevention rules
- [ ] Create terms and conditions
- [ ] Test complete referral flow

### Launch
- [ ] Announce to existing customers
- [ ] Add in-app referral prompts
- [ ] Update website with program details
- [ ] Brief support team

### Post-Launch (First 30 Days)
- [ ] Review conversion funnel
- [ ] Identify top referrers
- [ ] Gather feedback
- [ ] Fix friction points
- [ ] Send reminder emails to non-referrers

---

## Email Sequences

### Referral Program Launch

```
Subject: You can now earn [reward] for sharing [Product]

We just launched our referral program!

Share [Product] with friends and earn [reward] for each signup.
They get [their reward] too.

[Unique referral link]

1. Share your link
2. Friend signs up
3. You both get [reward]
```

### Referral Nurture Sequence

- Day 7: Remind about referral program
- Day 30: "Know anyone who'd benefit?"
- Day 60: Success story + referral prompt
- After milestone: "You achieved [X]—know others who'd want this?"

---

## Affiliate Programs

**For commission structures, cookie windows, recruitment, enablement, tools and fraud prevention**: See [references/affiliate-programs.md](references/affiliate-programs.md)

**For running the program (cohort economics, activation funnel, terms decision table, reconciliation, incrementality)**: See [references/affiliate-operations.md](references/affiliate-operations.md)

**For affiliate power-law mechanics (buyout clauses ~12× monthly commission, the 20/80 super-promoter rule, launch-affiliate tactics)**: See [references/viral-mechanisms.md](references/viral-mechanisms.md)

---

## Review Programs

Reviews are the other half of customer advocacy. For review-request programs, responding to reviews, reputation triage, and reusing testimonials with permission (G2, Capterra, Trustpilot, Google, app stores), see [references/review-programs.md](references/review-programs.md). Platform rules differ, so check [references/review-platform-rules.md](references/review-platform-rules.md) before proposing incentives or automation.

## Tool Integrations

For implementation, see the [tools registry](https://github.com/coreyhaines31/marketingskills/blob/main/tools/REGISTRY.md). Key tools for referral programs:

| Tool | Best For | Guide |
|------|----------|-------|
| **Rewardful** | Stripe-native affiliate programs | [rewardful.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/rewardful.md) |
| **Tolt** | SaaS affiliate programs | [tolt.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/tolt.md) |
| **Mention Me** | Enterprise referral programs | [mention-me.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/mention-me.md) |
| **Dub.co** | Link tracking and attribution | [dub-co.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/dub-co.md) |
| **Stripe** | Payment processing (for commission tracking) | [stripe.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/stripe.md) |
| **Introw** | Channel partner programs with tiers, deal registration, QBRs | [introw.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/introw.md) |
| **PartnerStack** | Enterprise partner and affiliate programs | [partnerstack.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/partnerstack.md) |

---

## Related Skills

- **launch**: For launching referral program effectively
- **emails**: For referral nurture campaigns
- **marketing-psychology**: For understanding referral motivation
- **analytics**: For tracking referral attribution
