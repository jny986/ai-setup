---
name: retention-strategy
description: When the user wants to reduce churn, improve customer retention, or plan lifecycle marketing. Also use when the user mentions "retention," "churn," "customer lifecycle," "churn prevention," "at-risk customers," or "loyalty program." For lifecycle, use growth-funnel.
metadata:
  version: 1.0.0
  based_on_repo: kostja94/marketing-skills, coreyhaines31/marketingskills
  based_on_version: v1.0.0(8dd89c5), v2.13.0(e85f3cb)
  based_on_skill: retention-strategy, churn-prevention
---

# Strategies: Retention

Guides customer retention and churn prevention. Acquiring new customers costs 5–25× more than retaining; 5% retention improvement can increase profitability 25–95%. Use this skill when reducing churn, building retention programs, or identifying at-risk customers.

## Initial Assessment

**Project context:** Read the product marketing context when present and load only what is relevant to this task. Otherwise use available project material or user-provided facts and ask for missing information.

Identify:
1. **Churn type**: Voluntary (active cancel) vs involuntary (payment failure)
2. **Signals**: Login frequency, feature usage, support tickets
3. **Stage**: Onboarding, expansion, renewal

## Churn Types

| Type | Share | Causes |
|------|-------|--------|
| **Voluntary** | 60–80% | Pricing, missing features, poor onboarding, relationship |
| **Involuntary** | 20–40% | Payment failures, expired cards, billing |

**Predictability**: Most churn is predictable 30–90 days before cancellation via behavioral signals.

## Proactive vs Reactive

| Approach | Conversion |
|----------|------------|
| **Reactive** (after cancel) | 15–20% |
| **Proactive** (before decision) | 60–80% |

Move from lagging indicator to early warning systems.

## Retention Strategies

| Strategy | Use |
|----------|-----|
| **Health scoring** | Behavioral + transactional + relationship signals |
| **Loyalty programs** | 5–15 percentage point retention lift |
| **Segmentation** | Predictive modeling for at-risk |
| **Onboarding** | Prevent low value realization early |
| **Dunning** | Retry logic; pre-expiry card updates for involuntary |

## User Value & Feedback

| Dimension | Use |
|-----------|-----|
| **Product value** | Registration; feature usage; payment |
| **Marketing value** | Testimonials; customer stories; webinar guests; feedback, bug reports, feature requests |
| **Feedback analysis** | Email, community, reviews—AI-assisted analysis; prioritize by impact; route to product vs ops |

**Avoid**: Treating users only as MAU/registration denominators. See **creator-program** for creator ecosystem.

## Lifecycle Integration

Retention occurs after conversion; ongoing investment in customer success, not isolated campaigns. Map touchpoints: onboarding → adoption → expansion → renewal.

## Output Format

- **Churn analysis** (voluntary vs involuntary; signals)
- **Retention tactics** (by stage)
- **Health score** framework (if applicable)
- **Intervention** playbook (at-risk triggers)

## Churn Prevention Playbook

### Before Starting

Gather this context (ask only for what the product marketing context doesn't cover):

#### 1. Current Churn Situation
- What's your monthly churn rate? (Voluntary vs. involuntary if known)
- How many active subscribers?
- What's the average MRR per customer?
- Do you have a cancel flow today, or does cancel happen instantly?

#### 2. Billing & Platform
- What billing provider? (Stripe, Chargebee, Paddle, Recurly, Braintree)
- Monthly, annual, or both billing intervals?
- Do you support plan pausing or downgrades?
- Any existing retention tooling? (Churnkey, ProsperStack, Raaft)

#### 3. Product & Usage Data
- Do you track feature usage per user?
- Can you identify engagement drop-offs?
- Do you have cancellation reason data from past churns?
- What's your activation metric? (What do retained users do that churned users don't?)

#### 4. Constraints
- B2B or B2C? (Affects flow design)
- Self-serve cancellation required? (Some regulations mandate easy cancel)
- Brand tone for offboarding? (Empathetic, direct, playful)

### How This Skill Works

Churn has two types requiring different strategies:

| Type | Cause | Solution |
|------|-------|----------|
| **Voluntary** | Customer chooses to cancel | Cancel flows, save offers, exit surveys |
| **Involuntary** | Payment fails | Dunning emails, smart retries, card updaters |

Voluntary churn is typically 50-70% of total churn. Involuntary churn is 30-50% but is often easier to fix.

> Source conflict: the Churn Types table above puts voluntary at 60–80% and involuntary at 20–40%; kostja's figures win. The ranges here come from the former churn-prevention guide.

This skill supports three modes:

1. **Build a cancel flow** — Design from scratch with survey, save offers, and confirmation. Done when every exit-survey reason maps to a primary and fallback offer (or a deliberate skip).
2. **Optimize an existing flow** — Analyze cancel data and improve save rates. Done when each change is tied to a reason-level save-rate finding and has an A/B test or metric to judge it.
3. **Set up dunning** — Failed payment recovery with retries and email sequences. Done when pre-dunning, retry rules per decline type, the email sequence and the grace-period end state are all specified.

### Cancel Flow Design

#### The Cancel Flow Structure

Every cancel flow follows this sequence:

```
Trigger → Survey → Dynamic Offer → Confirmation → Post-Cancel
```

**Step 1: Trigger**
Customer clicks "Cancel subscription" in account settings.

**Step 2: Exit Survey**
Ask why they're cancelling. This determines which save offer to show.

**Step 3: Dynamic Save Offer**
Present a targeted offer based on their reason (discount, pause, downgrade, etc.)

**Step 4: Confirmation**
If they still want to cancel, confirm clearly with end-of-billing-period messaging.

**Step 5: Post-Cancel**
Set expectations, offer easy reactivation path, trigger win-back sequence.

#### Exit Survey Design

The exit survey is the foundation. Good reason categories:

| Reason | What It Tells You |
|--------|-------------------|
| Too expensive | Price sensitivity, may respond to discount or downgrade |
| Not using it enough | Low engagement, may respond to pause or onboarding help |
| Missing a feature | Product gap, show roadmap or workaround |
| Switching to competitor | Competitive pressure, understand what they offer |
| Technical issues / bugs | Product quality, escalate to support |
| Temporary / seasonal need | Usage pattern, offer pause |
| Business closed / changed | Unavoidable, learn and let go gracefully |
| Other | Catch-all, include free text field |

**Survey best practices:**
- 1 question, single-select with optional free text
- 5-8 reason options max (avoid decision fatigue)
- Put most common reasons first (review data quarterly)
- "Help us improve" framing works better than "Why are you leaving?"

#### Dynamic Save Offers

The key insight: **match the offer to the reason.** A discount won't save someone who isn't using the product. A feature roadmap won't save someone who can't afford it.

**Offer-to-reason mapping:**

| Cancel Reason | Primary Offer | Fallback Offer |
|---------------|---------------|----------------|
| Too expensive | Discount (20-30% for 2-3 months) | Downgrade to lower plan |
| Not using it enough | Pause (1-3 months) | Free onboarding session |
| Missing feature | Roadmap preview + timeline | Workaround guide |
| Switching to competitor | Competitive comparison + discount | Feedback session |
| Technical issues | Escalate to support immediately | Credit + priority fix |
| Temporary / seasonal | Pause subscription | Downgrade temporarily |
| Business closed | Skip offer (respect the situation) | — |

#### Save Offer Types

**Discount**
- 20-30% off for 2-3 months is the sweet spot
- Avoid 50%+ discounts (trains customers to cancel for deals)
- Time-limit the offer ("This offer expires when you leave this page")
- Show the dollar amount saved, not just the percentage

**Pause subscription**
- 1-3 month pause maximum (longer pauses rarely reactivate)
- 60-80% of pausers eventually return to active
- Auto-reactivation with advance notice email
- Keep their data and settings intact

**Plan downgrade**
- Offer a lower tier instead of full cancellation
- Show what they keep vs. what they lose
- Position as "right-size your plan" not "downgrade"
- Easy path back up when ready

**Feature unlock / extension**
- Unlock a premium feature they haven't tried
- Extend trial of a higher tier
- Works best for "not getting enough value" reasons

**Personal outreach**
- For high-value accounts (top 10-20% by MRR)
- Route to customer success for a call
- Personal email from founder for smaller companies

#### Cancel Flow UI Patterns

```
┌─────────────────────────────────────┐
│  We're sorry to see you go          │
│                                     │
│  What's the main reason you're      │
│  cancelling?                        │
│                                     │
│  ○ Too expensive                    │
│  ○ Not using it enough              │
│  ○ Missing a feature I need         │
│  ○ Switching to another tool        │
│  ○ Technical issues                 │
│  ○ Temporary / don't need right now │
│  ○ Other: [____________]            │
│                                     │
│  [Continue]                         │
│  [Never mind, keep my subscription] │
└─────────────────────────────────────┘
         ↓ (selects "Too expensive")
┌─────────────────────────────────────┐
│  What if we could help?             │
│                                     │
│  We'd love to keep you. Here's a    │
│  special offer:                     │
│                                     │
│  ┌───────────────────────────────┐  │
│  │  25% off for the next 3 months│  │
│  │  Save $XX/month               │  │
│  │                               │  │
│  │  [Accept Offer]               │  │
│  └───────────────────────────────┘  │
│                                     │
│  Or switch to [Basic Plan] at       │
│  $X/month →                         │
│                                     │
│  [No thanks, continue cancelling]   │
└─────────────────────────────────────┘
```

**UI principles:**
- Keep the "continue cancelling" option visible (no dark patterns)
- One primary offer + one fallback, not a wall of options
- Use the customer's name and account data when possible
- Mobile-friendly (many cancellations happen on mobile)

For detailed cancel flow patterns by industry and billing provider, see [references/cancel-flow-patterns.md](references/cancel-flow-patterns.md).

### Churn Prediction & Proactive Retention

The best save happens before the customer ever clicks "Cancel."

#### Risk Signals

Track these leading indicators of churn:

| Signal | Risk Level | Timeframe |
|--------|-----------|-----------|
| Login frequency drops 50%+ | High | 2-4 weeks before cancel |
| Key feature usage stops | High | 1-3 weeks before cancel |
| Support tickets spike then stop | High | 1-2 weeks before cancel |
| Email open rates decline | Medium | 2-6 weeks before cancel |
| Billing page visits increase | High | Days before cancel |
| Team seats removed | High | 1-2 weeks before cancel |
| Data export initiated | Critical | Days before cancel |
| Individual recommendation rating is 0–6 (detractor) | Medium | 1-3 months before cancel |

#### Health Score Model

Build a simple health score (0-100) from weighted signals. Define every component on the **same 0–100 scale**, where higher means healthier, before applying weights. Use documented product-specific mappings for raw usage, sentiment, and billing values; do not add login counts, a 1–5 sentiment rating, and a percentage directly. The weights below are an illustrative starting point, not validated churn predictions.

Treat missing or stale signals as unavailable, rather than automatically healthy or zero. Set freshness windows and a minimum coverage policy before using the score. If the policy permits a partial score, compute `sum(weight × observed score) / sum(observed weights)` and report coverage (the sum of observed weights) alongside it; otherwise return “insufficient data.” All unavailable means no score. For example, only login (80) and feature usage (60) produce `(0.30×80 + 0.25×60)/0.55 = 70.91`, with 55% coverage. Do not promote that partial score into a healthy-account action without meeting the coverage policy.

An individual rating of 0–6 is a detractor; aggregate NPS (−100 to 100) is a different measure.

[Gainsight's measure-weight documentation](https://support.gainsight.com/gainsight_nxt/05Scorecards/02Admin_Guides/Measure_Weights_in_Scorecards) explains redistribution for unavailable measures.

Illustrative complete-data model:

```
Health Score = (
  Login frequency score × 0.30 +
  Feature usage score   × 0.25 +
  Support sentiment     × 0.15 +
  Billing health        × 0.15 +
  Engagement score      × 0.15
)
```

Validate score mappings and intervention thresholds against later observed renewal/churn outcomes before operational use; the following tiers are illustrative.

| Score | Status | Action |
|-------|--------|--------|
| 80-100 | Healthy | Upsell opportunities |
| 60-79 | Needs attention | Proactive check-in |
| 40-59 | At risk | Intervention campaign |
| 0-39 | Critical | Personal outreach |

#### Proactive Interventions

**Before they think about cancelling:**

| Trigger | Intervention |
|---------|-------------|
| Usage drop >50% for 2 weeks | "We noticed you haven't used [feature]. Need help?" email |
| Approaching plan limit | Upgrade nudge (not a wall — paywalls handles this) |
| No login for 14 days | Re-engagement email with recent product updates |
| NPS detractor (0-6) | Personal follow-up within 24 hours |
| Support ticket unresolved >48h | Escalation + proactive status update |
| Annual renewal in 30 days | Value recap email + renewal confirmation |

### Involuntary Churn: Payment Recovery

#### The Dunning Stack

```
Pre-dunning → Smart retry → Dunning emails → Grace period → Hard cancel
```

#### Pre-Dunning (Prevent Failures)

Card expiry alerts, card updater services, backup payment methods and pre-billing notifications. Timings, templates and provider setup: [references/dunning-playbook.md](references/dunning-playbook.md#pre-dunning-prevent-failures-before-they-happen).

#### Smart Retry Logic

Not all failures are the same. Retry strategy by decline type:

| Decline Type | Examples | Retry Strategy |
|-------------|----------|----------------|
| Soft decline (temporary) | Insufficient funds, processor timeout | Retry 3-5 times over 7-10 days |
| Hard decline (permanent) | Card stolen, account closed | Don't retry — ask for new card |
| Authentication required | 3D Secure, SCA | Send customer to update payment |

**Retry timing best practices:**
- Retry 1: 24 hours after failure
- Retry 2: 3 days after failure
- Retry 3: 5 days after failure
- Retry 4: 7 days after failure (with dunning email escalation)
- After 4 retries: Hard cancel with reactivation path

#### Dunning Email Sequence

Four emails escalating from friendly alert to final warning: Day 0, 3, 7, 10. Full templates: [references/dunning-playbook.md](references/dunning-playbook.md#dunning-email-sequence).

**Dunning email best practices:**
- Direct link to payment update page (no login required if possible)
- Show what they'll lose (their data, their team's access)
- Neutral wording: "your payment failed", not "you failed to pay"
- Include support contact for help
- Plain text performs better than designed emails for dunning

#### Recovery Benchmarks

| Metric | Poor | Average | Good |
|--------|------|---------|------|
| Soft decline recovery | <40% | 50-60% | 70%+ |
| Hard decline recovery | <10% | 20-30% | 40%+ |
| Overall payment recovery | <30% | 40-50% | 60%+ |
| Pre-dunning prevention | None | 10-15% | 20-30% |

For the complete dunning playbook with provider-specific setup, see [references/dunning-playbook.md](references/dunning-playbook.md).

### Metrics & Measurement

#### Key Churn Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Monthly churn rate | Churned customers / Start-of-month customers | <5% B2C, <2% B2B |
| Revenue churn (net) | (Lost MRR - Expansion MRR) / Start MRR | Negative (net expansion) |
| Cancel flow save rate | Saved / Total cancel sessions | 25-35% |
| Offer acceptance rate | Accepted offers / Shown offers | 15-25% |
| Pause reactivation rate | Reactivated / Total paused | 60-80% |
| Dunning recovery rate | Recovered / Total failed payments | 50-60% |
| Time to cancel | Days from first churn signal to cancel | Track trend |

#### Cohort Analysis

Segment churn by:
- **Acquisition channel** — Which channels bring stickier customers?
- **Plan type** — Which plans churn most?
- **Tenure** — When do most cancellations happen? (30, 60, 90 days?)
- **Cancel reason** — Which reasons are growing?
- **Save offer type** — Which offers work best for which segments?

#### Cancel Flow A/B Tests

Test one variable at a time:

| Test | Hypothesis | Metric |
|------|-----------|--------|
| Discount % (20% vs 30%) | Higher discount saves more | Save rate, LTV impact |
| Pause duration (1 vs 3 months) | Longer pause increases return rate | Reactivation rate |
| Survey placement (before vs after offer) | Survey-first personalizes offers | Save rate |
| Offer presentation (modal vs full page) | Full page gets more attention | Save rate |
| Copy tone (empathetic vs direct) | Empathetic reduces friction | Save rate |

**How to run cancel flow experiments:** Use **ab-testing** to design statistically rigorous tests. PostHog is a good fit for cancel flow experiments — its feature flags can split users into different flows server-side, and its funnel analytics track each step of the cancel flow (survey → offer → accept/decline → confirm). See the [PostHog integration guide](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/posthog.md) for setup.

### Common Mistakes

- **No cancel flow at all** — Instant cancel leaves money on the table. Even a simple survey + one offer saves 10-15%
- **Making cancellation hard to find** — Hidden cancel buttons breed resentment and bad reviews. Many jurisdictions require easy cancellation (FTC Click-to-Cancel rule)
- **Same offer for every reason** — A blanket discount doesn't address "missing feature" or "not using it"
- **Ignoring involuntary churn** — The easiest churn to fix
- **No dunning emails** — Letting payment failures silently cancel accounts
- **Guilt-trip copy** — "Are you sure you want to abandon us?" damages brand trust
- **Not tracking save offer LTV** — A "saved" customer who churns 30 days later wasn't really saved
- **No post-cancel path** — Make reactivation easy and trigger win-back emails, because some churned users will want to come back

### Tool Integrations

For implementation, see the [tools registry](https://github.com/coreyhaines31/marketingskills/blob/main/tools/REGISTRY.md).

#### Retention Platforms

| Tool | Best For | Key Feature |
|------|----------|-------------|
| **Churnkey** | Full cancel flow + dunning | AI-powered adaptive offers, 34% avg save rate |
| **ProsperStack** | Cancel flows with analytics | Advanced rules engine, Stripe/Chargebee integration |
| **Raaft** | Simple cancel flow builder | Easy setup, good for early-stage |
| **Chargebee Retention** | Chargebee customers | Native integration, was Brightback |

#### Billing Providers (Dunning)

| Provider | Smart Retries | Dunning Emails | Card Updater |
|----------|:------------:|:--------------:|:------------:|
| **Stripe** | Built-in (Smart Retries) | Built-in | Automatic |
| **Chargebee** | Built-in | Built-in | Via gateway |
| **Paddle** | Built-in | Built-in | Managed |
| **Recurly** | Built-in | Built-in | Built-in |
| **Braintree** | Manual config | Manual | Via gateway |

#### Related CLI Tools

| Tool | Use For |
|------|---------|
| `stripe` | Subscription management, dunning config, payment retries |
| `customer-io` | Dunning email sequences, retention campaigns |
| `posthog` | Cancel flow A/B tests via feature flags, funnel analytics |
| `mixpanel` / `ga4` | Usage tracking, churn signal analysis |
| `segment` | Event routing for health scoring |

## Related Skills

- **email-marketing**: Onboarding sequences; win-back campaigns
- **pmf-strategy**: Retention as PMF signal; churn as anti-signal
- **cold-start-strategy**: First users; differs from retention
- **analytics-tracking**: Usage data; churn signals
- **traffic-analysis**: Attribution; retention cohort analysis
- **paywalls**: For in-app upgrade moments and trial expiration
- **pricing-strategy**: For plan structure and annual discount strategy
- **onboarding**: For activation to prevent early churn
- **ab-testing**: For testing cancel flow variations with statistical rigor
