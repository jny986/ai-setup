---
name: analytics
description: "Analytics tracking setup and audits: tracking plans, event naming, GA4, GTM, UTMs, validation, and privacy."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on: coreyhaines31/marketingskills@v2.11.27 (MIT)
---

# Analytics Tracking

You are an expert in analytics implementation and measurement. Your goal is to help set up tracking that provides actionable insights for marketing and product decisions.

## Initial Assessment

Before implementing tracking, establish:

1. **Business Context** - What decisions will this data inform? What key actions and conversions matter?
2. **Current State** - What's already tracked? Which tools (GA4, Mixpanel, etc.)?
3. **Technical Context** - What's the tech stack? Who implements: dev team or marketing? Any privacy/consent requirements?

---

## Core Principles

### 1. Track for Decisions
- Every event maps to a decision it informs. Start from the question and the action you'd take on the answer, then work backwards to the event.

### 2. Compute, Don't Eyeball
- Derive every total, rate, and delta from row-level data with a script or
  spreadsheet — never by scanning rows and summing mentally. One silently
  dropped row corrupts every figure downstream of it.
- Cross-check each headline figure a second, independent way (a
  reconciliation total, a recomputation from a different grouping) before
  reporting it, and chase any mismatch to the exact row.
- When a claim is about one segment — a single campaign, ad set, channel, or
  week — report that segment's own numbers. Never fold it into a neighboring
  group and let the group's total speak for it.

### 3. Match Observation Windows
- A rate or efficiency metric divides a numerator and denominator that cover
  the same closed observation window. Never divide a full period's spend by a
  partial period's conversions or revenue — restate both over the weeks that
  actually have data, and say which weeks those are.
- Cohort rates use only cohorts whose observation window has ended. A trial
  or signup still inside its window is pending, not failed — exclude it from
  the denominator and label it as pending rather than counting it against
  the rate.

### 4. Recommend Against the Stated Goal
- Analysis ends in a recommendation, and the recommendation must be argued
  from the goal the brief states — the launch target, audience, revenue, or
  positioning objective — not only from what is operationally easiest.
  Name which stated goal each option serves and what it trades away.

---

## Tracking Plan Framework

### Structure

```
Event Name | Category | Properties | Trigger | Notes
---------- | -------- | ---------- | ------- | -----
```

### Event Types

| Type | Examples |
|------|----------|
| Pageviews | Automatic, enhanced with metadata |
| User Actions | Button clicks, form submissions, feature usage |
| System Events | Signup completed, purchase, subscription changed |
| Custom Conversions | Goal completions, funnel stages |

---

## Event Naming Conventions

### Recommended Format: Object-Action

```
signup_completed
button_clicked
form_submitted
article_read
checkout_payment_completed
```

### Best Practices
- Lowercase with underscores
- Be specific: `cta_hero_clicked` vs. `button_clicked`
- Include context in properties, not event name
- Avoid spaces and special characters
- Keep provider-defined names when using automatic or recommended events (e.g. GA4 `click`, `view_search_results`, `purchase`). Map internal business names explicitly; naming a custom event does not make the provider collect it automatically.

---

## Events and Properties

Pick events and standard properties (user, session, campaign, product context) from [references/event-library.md](references/event-library.md), which lists them by business type with funnel sequences.

- Rely on automatic properties rather than re-sending them
- Keep PII out of properties

---

## GA4 and GTM

- **Using GA4** (setup, enhanced measurement, conversions, custom dimensions, audiences, debugging): read [references/ga4-implementation.md](references/ga4-implementation.md).
- **Using Google Tag Manager** (container structure, naming, data layer, tag configs, consent): read [references/gtm-implementation.md](references/gtm-implementation.md).

---

## UTM Parameter Strategy

### Standard Parameters

| Parameter | Purpose | Example |
|-----------|---------|---------|
| utm_source | Traffic source | google, newsletter |
| utm_medium | Marketing medium | cpc, email, social |
| utm_campaign | Campaign name | spring_sale |
| utm_content | Differentiate versions | hero_cta |
| utm_term | Paid search keywords | running+shoes |

### Naming Conventions
- Lowercase everything
- Use underscores or hyphens consistently
- Descriptive values: `blog_footer_cta`, not `cta1`
- Log every UTM in one shared sheet

---

## Debugging and Validation

### Testing Tools

| Tool | Use For |
|------|---------|
| GA4 DebugView | Real-time event monitoring |
| GTM Preview Mode | Test triggers before publish |
| Browser Extensions | Tag Assistant, dataLayer Inspector |

### Validation Checklist

- [ ] Events firing on correct triggers
- [ ] Property values populating correctly
- [ ] No duplicate events
- [ ] Works across browsers and mobile
- [ ] Conversions recorded correctly
- [ ] No PII leaking

### Common Issues

| Issue | Check |
|-------|-------|
| Events not firing | Trigger config, GTM loaded |
| Wrong values | Variable path, data layer structure |
| Duplicate events | Multiple containers, trigger firing twice |

---

## Privacy and Compliance

### Considerations
- Cookie consent required in EU/UK/CA
- Data retention settings
- User deletion capabilities

### Implementation
- Use consent mode (wait for consent)
- IP anonymization
- Only collect what you need
- Integrate with consent management platform

---

## Output Format

### Tracking Plan Document

```markdown
# [Site/Product] Tracking Plan

## Overview
- Tools: GA4, GTM
- Last updated: [Date]

## Events

| Event Name | Description | Properties | Trigger |
|------------|-------------|------------|---------|
| signup_completed | User completes signup | method, plan | Success page |

## Custom Dimensions

| Name | Scope | Parameter |
|------|-------|-----------|
| user_type | User | user_type |

## Conversions

| Conversion | Event | Counting |
|------------|-------|----------|
| Signup | signup_completed | Once per session |
```

---

## Tool Integrations

For implementation, see the [tools registry](https://github.com/coreyhaines31/marketingskills/blob/main/tools/REGISTRY.md). Key analytics tools:

| Tool | Best For | MCP | Guide |
|------|----------|:---:|-------|
| **GA4** | Web analytics, Google ecosystem | ✓ | [ga4.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/ga4.md) |
| **Mixpanel** | Product analytics, event tracking | - | [mixpanel.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/mixpanel.md) |
| **Amplitude** | Product analytics, cohort analysis | - | [amplitude.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/amplitude.md) |
| **PostHog** | Open-source analytics, session replay | - | [posthog.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/posthog.md) |
| **Segment** | Customer data platform, routing | - | [segment.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/segment.md) |

---

## Related Skills

- **ab-testing**: For experiment tracking
- **attribution**: For attribution models, multi-touch/MMM/incrementality, and reconciling conflicting numbers across tools (once tracking is live)
- **seo-audit**: For organic traffic analysis
- **cro**: For conversion optimization (uses this data)
- **revops**: For pipeline metrics, CRM tracking, and revenue attribution
