---
name: conversion-optimization
description: When the user wants to improve conversion rates, run A/B tests, optimize funnels, or reduce friction. Also use when the user mentions "CRO," "conversion rate optimization," "A/B test," "split test," "funnel optimization," "checkout optimization," "form optimization," or "conversion funnel." For pricing psychology, use pricing-strategy.
metadata:
  version: 1.1.1
---

# Strategies: Conversion Optimization

Guides conversion rate optimization (CRO): increasing the percentage of visitors who complete desired actions. Higher conversion rates mean increased revenue, reduced CAC, and better ROI. Use this skill when optimizing funnels, running experiments, or reducing friction on high-traffic pages.

## Initial Assessment

**Project context:** Read the product marketing context when present and load only what is relevant to this task. Otherwise use available project material or user-provided facts and ask for missing information.

Identify:
1. **Funnel stage**: Awareness, consideration, decision, post-purchase
2. **Conversion goal**: Signup, purchase, download, demo request
3. **Traffic**: Volume; mobile vs desktop split
4. **Current conversion rate**: Baseline for improvement

## CRO Process

| Step | Action |
|------|--------|
| **1. Research** | Map funnel; identify high-traffic, low-conversion pages |
| **2. Hypothesize** | Form testable hypothesis (if X, then Y because Z) |
| **3. Prioritize** | Score by Potential, Importance, Ease (PIE) |
| **4. Test** | A/B or multivariate; adequate sample size |
| **5. Analyze** | Statistical significance; implement winner |

## PIE Prioritization Framework

Score each test idea 1–10:

| Factor | Question |
|--------|----------|
| **Potential** | How much improvement is possible? |
| **Importance** | How much traffic does this page get? |
| **Ease** | How easy to implement? |

Rank backlog by total score; run highest-impact tests first.

## A/B Testing Best Practices

| Practice | Guideline |
|----------|-----------|
| **Sample size** | Calculate minimum before launch; 95% significance without adequate sample = false positives |
| **Duration** | Run full week cycles; account for day-of-week effects |
| **One variable** | Test one element per experiment (or use MVT for multiple) |
| **Mobile separate** | Mobile converts ~50% of desktop; test mobile independently—thumb reach, form complexity differ |
| **Low traffic** | Use Bayesian testing for faster, actionable results |

## Key Testing Areas

| Page Type | Test Ideas |
|-----------|------------|
| **Homepage** | Search bar prominence; personalized content; hero CTA; social proof placement |
| **Landing page** | Headline; form length; CTA copy; above-fold layout |
| **Product/Category** | Quick view; descriptions; add-to-cart placement |
| **Checkout** | Form fields; progress indicator; trust badges; guest checkout |
| **Pricing** | Plan order; anchoring; CTA per tier |

**Personalization**: Personalized experiences generate ~41% more impact than generic ones.

## Commercialization Infrastructure

| Module | Purpose |
|--------|---------|
| **Data & BI** | Data warehouse; user behavior events; agile surveys |
| **A/B testing** | Experiment platform; statistical significance; backend-controlled variants |
| **User education** | Help docs (multi-language); update notifications; EDM |
| **Attribution** | Ad pixels; attribution model; impression-to-click-to-sale tracking |

**Avoid**: Intrusive interstitials; popups that block content. Prefer non-intrusive ad formats.

## Foundational Requirements

- **Analytics**: Map funnels; identify drop-off points (analytics-tracking, traffic-analysis)
- **Qualitative**: Heatmaps, session recordings, user tests—understand *why* drop-off occurs
- **Technical**: Dedicated resources for 2–4 tests/month; maintain momentum

## Output Format

- **Funnel map** (stages, conversion rates, drop-off)
- **Hypothesis** (if X, then Y because Z)
- **Test plan** (variant, metric, sample size, duration)
- **Implementation** checklist

## Page-Level CRO Analysis

### Reference Routing

Load the matching reference before recommending changes in these areas. Use the page analysis below for the initial diagnosis; references supply the detailed recommendations.

| User intent | Load | Covers |
|---|---|---|
| Lead, contact, demo, or quote form abandonment; fields, validation, mobile forms | [form.md](references/form.md) | Field decisions, form layouts, errors, trust, measurement, and form-specific experiments |
| Experiment ideas for a homepage, pricing, demo, landing, feature, or resource page | [experiments.md](references/experiments.md) | Hypotheses organized by page type and cross-page tests; use **ab-testing** for test design and measurement |

### Initial Assessment

Before providing recommendations, identify:

1. **Page Type**: Homepage, landing page, pricing, feature, blog, about, other
2. **Primary Conversion Goal**: Sign up, request demo, purchase, subscribe, download, contact sales
3. **Traffic Context**: Where are visitors coming from? (organic, paid, email, social)

### CRO Analysis Framework

Analyze the page across these dimensions, in order of impact:

#### 1. Value Proposition Clarity (Highest Impact)

**Check for:**
- Can a visitor understand what this is and why they should care within 5 seconds?
- Is the primary benefit clear, specific, and differentiated?
- Is it written in the customer's language rather than company jargon?

**Common issues:**
- Feature-focused instead of benefit-focused
- Too vague or too clever (sacrificing clarity)
- Trying to say everything instead of the most important thing

#### 2. Headline Effectiveness

**Evaluate:**
- Does it communicate the core value proposition?
- Is it specific enough to be meaningful?
- Does it match the traffic source's messaging?

**Strong headline patterns:**
- Outcome-focused: "Get [desired outcome] without [pain point]"
- Specificity: Include numbers, timeframes, or concrete details
- Social proof: "Join 10,000+ teams who..."

#### 3. CTA Placement, Copy, and Hierarchy

**Primary CTA assessment:**
- Is there one clear primary action?
- Is it visible without scrolling?
- Does the button copy communicate value, not just action?
  - Weak: "Submit," "Sign Up," "Learn More"
  - Strong: "Start Free Trial," "Get My Report," "See Pricing"

**CTA hierarchy:**
- Is there a logical primary vs. secondary CTA structure?
- Are CTAs repeated at key decision points?

#### 4. Visual Hierarchy and Scannability

**Check:**
- Can someone scanning get the main message?
- Are the most important elements visually prominent?
- Do images support or distract from the message?

#### 5. Trust Signals and Social Proof

**Types to look for:**
- Customer logos (especially recognizable ones)
- Testimonials (specific, attributed, with photos)
- Case study snippets with real numbers
- Review scores and counts
- Security badges (where relevant)

**Placement:** Near CTAs and after benefit claims

#### 6. Objection Handling

**Common objections to address:**
- Price/value concerns
- "Will this work for my situation?"
- Implementation difficulty
- "What if it doesn't work?"

**Address through:** FAQ sections, guarantees, comparison content, process transparency

#### 7. Friction Points

**Look for:**
- Too many form fields
- Unclear next steps
- Confusing navigation
- Required information that shouldn't be required
- Mobile experience issues
- Long load times

### Output Format

Structure your recommendations as:

#### Quick Wins (Implement Now)
Easy changes with likely immediate impact.

#### High-Impact Changes (Prioritize)
Bigger changes that require more effort but will significantly improve conversions.

#### Test Ideas
Hypotheses worth A/B testing rather than assuming.

#### Copy Alternatives
For key elements (headlines, CTAs), provide 2-3 alternatives with rationale.

### Page-Specific Frameworks

#### Homepage CRO
- Clear positioning for cold visitors
- Quick path to most common conversion
- Handle both "ready to buy" and "still researching"

#### Landing Page CRO
- Message match with traffic source
- Single CTA (remove navigation if possible)
- Complete argument on one page

#### Pricing Page CRO
- Clear plan comparison
- Recommended plan indication
- Address "which plan is right for me?" anxiety

#### Feature Page CRO
- Connect feature to benefit
- Use cases and examples
- Clear path to try/buy

#### Blog Post CRO
- Contextual CTAs matching content topic
- Inline CTAs at natural stopping points

### Task-Specific Questions

1. What's your current conversion rate and goal?
2. What does your signup/purchase flow look like after this page?
3. Do you have user research, heatmaps, or session recordings?
4. What have you already tried?

### Form Enrichment

When enrichment controls the next step after a lead form, use the [revops inbound-routing playbook](../../../revops/references/inbound-routing.md): preserve valid submissions, bound the lookup wait, and provide a useful fallback when qualification is unknown.

## Related Skills

- **landing-page-generator**: Landing page structure and copy
- **cta-generator**: CTA design and placement
- **analytics-tracking**: GA4, events, conversion tracking
- **traffic-analysis**: Attribution, funnel analysis
- **copywriting**: Headline, CTA copy for tests
- **signup**: If the issue is in the signup process itself
- **popups**: If considering popups as part of the strategy
- **ab-testing**: To properly test recommended changes
