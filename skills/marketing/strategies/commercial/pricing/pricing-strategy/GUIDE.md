---
name: pricing-strategy
description: When the user wants to plan, design, or optimize pricing strategy and structure. Also use when the user mentions "pricing strategy," "pricing model," "pricing tiers," "freemium," "value-based pricing," "anchoring," "price structure," or "monetization strategy." For pricing page, use `dev/references/pages/marketing/pricing`.
metadata:
  version: 1.0.1
  based_on_repo: kostja94/marketing-skills, coreyhaines31/marketingskills
  based_on_version: v1.0.0(8dd89c5), v2.11.27(28e4a81)
  based_on_skill: pricing-strategy, pricing
---

# Strategies: Pricing

Guides pricing strategy and structure for SaaS, tools, and products. Covers pricing models, tier design, anchoring, and when to apply discounts. For pricing **page** content and layout, see `dev/references/pages/marketing/pricing`. For **discount** and promotional pricing, see **discount-marketing-strategy**.

## Initial Assessment

**Project context:** Read the product marketing context when present. Without it, use available project material or user-provided facts and ask for missing information.

Identify:
1. **Product type**: SaaS, tool, e-commerce
2. **Value metric**: What drives value (seats, usage, features)
3. **Market**: Competitor pricing; willingness to pay
4. **Goals**: Revenue, adoption, retention

## Pricing Models

| Model | Use |
|-------|-----|
| **Subscription** | Recurring; monthly/annual; most SaaS |
| **Freemium** | Free tier + paid; adoption then conversion |
| **Usage-based** | Pay per use; API, credits |
| **One-time** | Perpetual license; some tools |
| **Hybrid** | Base + usage; tiered + overage |

**Variable-cost products** (compute, API, AI): When per-user cost varies widely (heavy users cost 10×+ light users), uniform subscription often fails. Use usage-based, credits, or tiered-by-usage; align price to cost structure.

## Tier Design

- **2–4 tiers** typical; avoid too many options
- **Differentiation**: Clear "best for" per tier; feature gates
- **Anchoring**: Lead with mid-tier or annual; make target option obvious
- **Value metric**: Align price to value (seats, projects, API calls)

## Anchoring & Presentation

- **Annual discount**: 15–25% for annual prepay; improves cash flow
- **Decoy**: Higher tier makes mid-tier look better
- **Most popular**: Highlight recommended plan
- **Price display**: Monthly vs annual; show savings

## When to Use Discounts

Discounts apply on top of base pricing. See **discount-marketing-strategy** for:

- Annual commitment discounts
- First-time / new customer promotions
- Lifetime deals (LTD)
- Seasonal (BFCM)
- Referral, contest, affiliate codes

**Principle**: Set base price for long-term value; use discounts tactically for acquisition, retention, or cash flow.

> **Source conflicts (kostja wins, ours flagged):** kostja says 2-4 tiers, annual discounts of 15-25%, and to lead with the mid-tier or annual as the anchor. Our sections below say Good-Better-Best, an annual discount callout of 17-20%, and to show the higher-priced option first.

## Pricing Context to Gather

Ask only for what the product marketing context and the conversation leave open:

### 1. Business Context
- What type of product? (SaaS, marketplace, e-commerce, service)
- What's your current pricing (if any)?
- What's your target market? (SMB, mid-market, enterprise)
- What's your go-to-market motion? (self-serve, sales-led, hybrid)

### 2. Value & Competition
- What's the primary value you deliver?
- What alternatives do customers consider?
- How do competitors price?

### 3. Current Performance
- What's your current conversion rate?
- What's your ARPU and churn rate?
- Any feedback on pricing from customers/prospects?

### 4. Goals
- Optimizing for growth, revenue, or profitability?
- Moving upmarket or expanding downmarket?

### 5. Pricing Work So Far
- What pricing research have you done?
- What's your primary value metric?
- Who are your main pricing personas?
- What pricing changes are you considering?

## Pricing Fundamentals

### The Three Pricing Axes

**1. Packaging** — What's included at each tier?
- Features, limits, support level
- How tiers differ from each other

**2. Pricing Metric** — What do you charge for?
- Per user, per usage, flat fee
- How price scales with value

**3. Price Point** — How much do you charge?
- The actual dollar amounts
- Perceived value vs. cost

### Value-Based Pricing

Price should be based on value delivered, not cost to serve:

- **Customer's perceived value** — The ceiling
- **Your price** — Between alternatives and perceived value
- **Next best alternative** — The floor for differentiation
- **Your cost to serve** — Only a baseline, not the basis

**Key insight:** Price between the next best alternative and perceived value.

**Anchor on value and differentiation; treat these as inputs only:**
- **Competitor prices** — a data point, not a target. Matching a competitor's price copies their strategy, not their economics.
- **Cost** — a floor, never the basis.

## Initial Pricing — "Pick a Price You Can Learn From"

The frameworks below (value metrics, tiers, Van Westendorp) are for optimizing a price. **On day one you don't have a price to optimize — you have a bet to place.** The goal of your first price is *learning*, not precision. Pick a number, ship it, and let real buyers tell you if it's wrong.

### The $10 / $100 / $1,000 rule of thumb

When you have nothing to go on, start with the order of magnitude that matches who you serve:

- **~$10/mo** — prosumer / individual, high volume, low touch
- **~$100/mo** — SMB / team tool, the SaaS default
- **~$1,000/mo** — mid-market / business-critical / sales-assisted

Pick the bucket by **who the customer is and how much value you deliver**, then start near the round number. You can move within the bucket fast once you have signal.

### Avoid the $9 trap

Resist the urge to price ultra-low (e.g. **$9/mo**) to reduce friction. Ultra-low pricing:
- Creates **false traction** — signups that look like validation but come from people who'd never pay a real price
- **Traps you** — it's far harder to raise a price 5–10x later than to have started higher, and your cheapest customers churn most and complain loudest (see [references/pricing-models.md](references/pricing-models.md) on low-price retention)

Round-and-slightly-higher beats clever-and-cheap.

### "Just charge $50 and see what happens"

When early Intercom agonized over pricing, Jason Fried's advice was essentially: **just charge $50 and see what happens.** Stop modeling; get a real signal. If people pay without flinching, raise it. If nobody bites, you've learned something for the cost of a week, not a quarter.

**For the eight ways to structure how you charge (flat, usage, tier, user, feature, credit, outcome, hybrid) and the value/price ratio:** See [references/pricing-models.md](references/pricing-models.md).

## Value Metrics

### What is a Value Metric?

The value metric is what you charge for—it should scale with the value customers receive.

**Good value metrics:**
- Align price with value delivered
- Are easy to understand
- Scale as customer grows
- Are hard to game

### Common Value Metrics

| Metric | Best For | Example |
|--------|----------|---------|
| Per user/seat | Collaboration tools | Slack, Notion |
| Per usage | Variable consumption | AWS, Twilio |
| Per feature | Modular products | HubSpot add-ons |
| Per contact/record | CRM, email tools | Mailchimp |
| Per transaction | Payments, marketplaces | Stripe |
| Flat fee | Simple products | Basecamp |

### Choosing Your Value Metric

Ask: "As a customer uses more of [metric], do they get more value?"
- If yes → good value metric
- If no → price doesn't align with value

**The value metric picks the pricing model.** Once you know what scales with value, choose how to charge on it — flat, usage, tier, user, feature, credit, outcome, or a hybrid. See [references/pricing-models.md](references/pricing-models.md).

## Tier Structure (Good-Better-Best)

Default to Good-Better-Best: an entry tier, a recommended middle tier where most customers land, and a premium tier at 2-3x the middle.

**When designing tiers, choosing freemium vs. free trial, or adding an enterprise tier:** see [references/tier-structure.md](references/tier-structure.md) for tier count, differentiation levers, an example table, persona-based packaging, trial length and enterprise elements.

## Pricing Research

- **Van Westendorp** finds the acceptable price range and candidate prices to test. It measures perception, not demand: its "Optimal Price Point" is a survey intersection, not a revenue maximum.
- **MaxDiff** ranks which features customers value most, to inform packaging.
- **Gabor-Granger / conjoint** build a demand curve or per-feature price sensitivity.
- **Usage-value correlation** finds the metric and thresholds that predict retention and expansion.

**When running or analysing any of these:** see [references/research-methods.md](references/research-methods.md) for the exact questions, analysis steps, sample sizes and example output.

## When to Raise Prices

### Signs It's Time

**Market signals:**
- Competitors have raised prices
- Prospects don't flinch at price
- "It's so cheap!" feedback

**Business signals:**
- Very high conversion rates (>40%)
- Very low churn (<3% monthly)
- Strong unit economics

**Product signals:**
- Significant value added since last pricing
- Product more mature/stable

### Price Increase Strategies

1. **Grandfather existing** — New price for new customers only
2. **Delayed increase** — Announce 3-6 months out
3. **Tied to value** — Raise price but add features
4. **Plan restructure** — Change plans entirely

### Rollout Methodology

A price change is a rollout, not a switch you flip. Sequence it to de-risk:

1. **Test on new customers first.** Raise the price only for *new* signups and watch conversion. New customers have no anchor and no relationship at stake, so they give you a clean read on whether the market accepts the number — before you touch a single existing account.
2. **Grandfather as a transition, not forever.** Grandfathering feels kind, but it can leave enormous money on the table. Run the math: a customer paying **$50/mo** who *should* be at **$250/mo** is a **$2,400/yr** gap — and $200/mo you're subsidizing indefinitely across your whole base. Grandfather as a *transition* (a grace period), not a permanent exemption.
3. **Roll out small, then gradually.** Move **5–10%** of existing customers to the new price first. Watch churn and support volume for a cycle, then expand in staggered waves. A staggered rollout contains the blast radius and gives you an off-ramp if churn spikes.
4. **Communicate the *why*, months ahead, with a generous offer.** Tell customers why the price is changing (usually: more value shipped) well in advance. Soften it: lock-in-the-old-price-if-you-upgrade-to-annual-now, an extended grace window, or a one-time credit. Advance notice + a generous option converts a resentment moment into a loyalty one.

Expect — and accept — some churn. The customers most likely to leave over a justified increase are usually your least-profitable, highest-support, most price-sensitive accounts.

## Pricing Page Best Practices

For page construction, see `dev/references/pages/marketing/pricing`.

### Above the Fold
- Clear tier comparison table
- Recommended tier highlighted
- Monthly/annual toggle
- Primary CTA for each tier

### Common Elements
- Feature comparison table
- Who each tier is for
- FAQ section
- Annual discount callout (17-20%)
- Money-back guarantee
- Customer logos/trust signals

### Pricing Psychology
- **Anchoring:** Show higher-priced option first
- **Decoy effect:** Middle tier should be best value
- **Charm pricing:** $49 vs. $50 (for value-focused)
- **Round pricing:** $50 vs. $49 (for premium)

## Pricing Page Teardown

When someone wants to audit an existing pricing *page* for **clarity, transparency, and AI-readability** (not the pricing strategy itself, and not conversion-rate optimization — that's **conversion-optimization**), run a **teardown** that scores it across two axes and returns prioritized fixes:

- **Human buyer experience** — value-prop clarity, plan differentiation, cognitive load, trust signals, pricing psychology, and price transparency.
- **AI-agent readiness** — whether the LLMs and agents that shortlist and compare tools can read and quote your pricing: prices in text, extractable FAQ, per-tier depth in words, structured data.

**For every teardown:** follow [references/pricing-page-teardown.md](references/pricing-page-teardown.md) for the paste test, the 10-dimension rubric, the run steps, the report template and the **schema-markup** / **generative-engine-optimization** handoffs. *(AI-agent-readiness lens adapted from Kyle Poyar / Growth Unhinged.)*

## Pricing Checklist

### Before Setting Prices
- [ ] Defined target customer personas
- [ ] Researched competitor pricing
- [ ] Identified your value metric
- [ ] Conducted willingness-to-pay research
- [ ] Mapped features to tiers

### Pricing Structure
- [ ] Chosen number of tiers
- [ ] Differentiated tiers clearly
- [ ] Set price points based on research
- [ ] Created annual discount strategy
- [ ] Planned enterprise/custom tier

## Output Format

- **Pricing model** recommendation
- **Tier structure** (plans, features, price points)
- **Anchoring** approach
- **Discount** fit (when to use; reference discount-marketing-strategy)
- `dev/references/pages/marketing/pricing` (page execution)

## Related Skills

- **discount-marketing-strategy**: Promotional pricing; when and how to discount
- `dev/references/pages/marketing/pricing`: Pricing page content, structure, conversion
- `dev/references/pages/marketing/landing-page`: Click-through to pricing
- **localization-strategy**: Pricing by market (true localization vs cosmetic); see Pricing Strategies section
- **retention-strategy**: Cancel flows, save offers, and reducing revenue churn
- **conversion-optimization**: Optimizing pricing page conversion
- **generative-engine-optimization**: Making the pricing page extractable and citable by AI (the teardown's AI-agent-readiness axis)
- **schema-markup**: Product/Offer structured data so machines can read your tiers and prices
- **copywriting**: Pricing page copy
- **marketing-psychology**: Pricing psychology principles
- **ab-testing**: Testing pricing changes
- **revops**: Deal desk processes and pipeline pricing
- **sales-enablement**: Proposal templates and pricing presentations
