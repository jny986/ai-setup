---
name: offers
description: "When the user wants to design or improve the offer itself rather than the copy. Also use when the user mentions \"offer,\" \"value equation,\" \"bonus stack,\" \"guarantee,\" \"risk reversal,\" \"scarcity,\" \"urgency,\" \"offer naming,\" \"payment plan,\" \"irresistible offer,\" or \"my offer isn't converting.\" For copy that sells the offer, use copywriting. For promotional discounts, use discount-marketing-strategy."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: coreyhaines31/marketingskills
  based_on_version: v2.11.29(c7d7dfb)
  based_on_skill: offers
---

# Strategies: Offers

Guides offer construction: value equation, bonuses, guarantees, honest scarcity, naming, and payment structure. Improve the offer before writing better copy on a worse one.

## Initial Assessment

**Project context:** Read the product marketing context when present. Without it, use available project material or user-provided facts and ask for missing information.

Identify:
1. **What is sold** and to whom
2. **Current offer**: price, inclusions, guarantee, any urgency
3. **Symptom**: low conversion, discount pressure, weak launch

## Core Philosophy

**The offer is the thing, not the page.** Better copy on a weak offer compounds slowly. A stronger offer with average copy converts immediately. Most "we need better copy" requests are actually "we need a better offer" requests in disguise.

This skill exists because the rest of the repo handles the *expression* of an offer — `copywriting` writes the sales page, `conversion-optimization` optimizes the conversion path, `pricing-strategy` sets the tier structure, `product-launch` orchestrates the moment, `paywalls` shapes the upgrade prompt. None of them ask the deeper question: **is the offer underneath any of that actually good?**

### When this skill matters

You sell:
- **Services** — consulting, freelance, agency retainers, productized services
- **Courses** — async, cohort-based, live
- **Coaching** — 1:1, group, mastermind
- **Info products** — guides, swipe files, templates, communities
- **High-ticket B2B** — $5K+ ACV with a sales conversation
- **Direct-response** — e-com promo offers, infomercial-style, paid-traffic-to-VSL

### When `pricing-strategy` does more of the work

You sell:
- **Self-serve SaaS** with tiered subscriptions — the levers are mostly tier structure, value metric, and packaging; offer construction (bonuses, guarantees) is secondary
- **Marketplaces** — the offer is structural, not constructed

Skim this skill in those cases for the value equation framing, then go to `pricing-strategy`.

---

## The Value Equation

The single most useful frame for offer design. Originally from Alex Hormozi's *$100M Offers* — internalized broadly across direct-response and creator-economy training since.

```
              Dream Outcome  ×  Perceived Likelihood of Achievement
  Value  =  ─────────────────────────────────────────────────────────
              Time Delay     ×   Effort & Sacrifice
```

You move the four levers like this:

| Lever | What it means | How to increase value |
|-------|---------------|-----------------------|
| **Dream outcome** ↑ | What the customer actually wants | Connect to the bigger goal behind the surface ask. Specify and name it. |
| **Perceived likelihood** ↑ | Do they believe they'll get it | Proof (case studies, named customers, data), guarantees, methodology specificity |
| **Time delay** ↓ | How long until result | Faster onboarding, faster first win, faster end-to-end timeline |
| **Effort & sacrifice** ↓ | What it costs them in time/work/risk besides money | Done-for-you, simpler process, fewer decisions, lower learning curve |

**Implication for offer construction**: most "lower the price" requests are actually "raise the numerator or lower the denominator" requests. Price is the comparison, not the value.

---

## The Anatomy of a Complete Offer

A complete offer has six components. Skip any one and conversion suffers.

| # | Component | Question it answers |
|---|-----------|---------------------|
| 1 | **Core deliverable** | What do they get? |
| 2 | **Bonus stack** | What else do they get that makes the core feel undervalued? |
| 3 | **Guarantee** | What happens if it doesn't work? |
| 4 | **Scarcity / urgency** | Why now, not later? |
| 5 | **Name** | What is this thing called? |
| 6 | **Price + payment structure** | What do they pay and how? |

Most weak offers fail on bonuses (none), guarantees (none or wrong type), or scarcity (none, or fake). Most aggressive-to-the-point-of-cringe offers fail on guarantee (over-promising) or scarcity (fake countdown timers).

---

## Reference Library

| Reference | When to read |
|-----------|--------------|
| [value-equation.md](references/value-equation.md) | Diagnosing which lever is broken on a stuck offer |
| [offer-anatomy.md](references/offer-anatomy.md) | Building a complete offer from scratch |
| [guarantee-design.md](references/guarantee-design.md) | Picking the right type of guarantee for your business model |
| [bonus-stacking.md](references/bonus-stacking.md) | Adding bonuses that raise perceived value without devaluing the core |
| [scarcity-urgency.md](references/scarcity-urgency.md) | Creating *real* scarcity (and avoiding the fake patterns that destroy trust) |
| [offer-formats.md](references/offer-formats.md) | Format playbooks by business type — service, course, coaching, info product, high-ticket B2B, agency retainer, self-serve SaaS, direct response |
| [saas-offers.md](references/saas-offers.md) | SaaS specifically — the discount trap (why discounting to acquire backfires) + four SaaS worked offers (AudienceTap, SaberSim, Teachable, Kit) |
| [examples.md](references/examples.md) | Anonymized worked examples — before/after for each business type |

---

## The Diagnostic Loop

When the user says "my offer isn't converting" or "I want to improve my offer":

1. **Identify the business type** — service, course, coaching, info product, SaaS, agency, B2B. Open its default format in [offer-formats.md](references/offer-formats.md) (SaaS: also [saas-offers.md](references/saas-offers.md)).
2. **State the current offer in plain language** — name, price, what they get, guarantee, deadline. Write it down even if it lives in scattered places now.
3. **Run the value equation** — score each of the four levers 1–10 with the scoring prompts in [value-equation.md](references/value-equation.md). The lowest is the binding constraint.
4. **Audit the anatomy** — mark each of the six components present, weak or missing.
5. **Pick one lever to fix this iteration** — usually the one scoring lowest. Change one component; leave the rest for the next iteration.
6. **Draft the changed component** — new bonus, new guarantee, new scarcity, new name, new payment plan — using that component's reference from the library above. Done when the drafted component is written out in buyer-facing words.
7. **Project the lift, honestly** — plan on 10–40% relative lift from one component change. Multiply the lifts, don't add them: +20% then +30% = `1.20 × 1.30 = 1.56` (2% → 3.12%, +1.12 percentage points). Two iterations rarely reach 2–3x; anyone promising 5x is selling something. Confirm the combined offer with a test (see ab-testing).

---

## Tactics That Cost More Than They Return

- **Manipulative scarcity** — fake countdown timers, "only 3 spots left" lies. Short-term lift, long-term trust collapse. Don't.
- **Over-promising guarantees** — "double your revenue or refund + $1,000." Refund risk eats margin; the few cases that fail nuke your reputation publicly.
- **Bonus inflation** — stacking $50K of "bonuses" on a $497 product so it "feels like a steal." Sophisticated buyers see this. Treat bonuses as additive, not exaggerated.
- **Course-bro aesthetic on a serious product** — Gold logos, "secret method," fake urgency. Pattern-matches to scam. Wrong room.
- **Discounting to acquire** — raise value with an offer instead; discount only for upgrades/cross-sells or real seasonal windows. See [saas-offers.md](references/saas-offers.md).

---

## Banned Vocabulary

When drafting offer language (sales pages, emails, headlines), use specific numbers, named customers, concrete outcomes and real timelines. Avoid:

- **"Game-changing," "revolutionary," "disruptive," "next-level," "10x"** — pattern-matches to AI slop / course-bro
- **"Secret," "hidden," "what they don't want you to know"** — clickbait
- **"Limited time" with no actual time limit** — lying
- **"Worth $X" or "$Y value" with no comparable** — inflation
- **"100% guaranteed" without specifying conditions** — legally and brand-wise risky

---

## Related Skills

- **pricing-strategy** — for price levels, tier structure, value metric, packaging, freemium
- **copywriting** — for the page that presents the offer
- **conversion-optimization** — for optimizing the conversion path the offer travels through
- **product-launch** — for the moment you ship the offer
- **paywalls** — for in-app upgrade-prompt versions of an offer
- **sales-enablement** — for the deck and one-pager that carry the offer into a sales conversation
- **email-marketing** — for the email sequence that warms up the offer
- **marketing-psychology** — for the cognitive biases that make offers land or bounce
