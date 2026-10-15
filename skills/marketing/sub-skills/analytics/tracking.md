---
name: analytics-tracking
description: When the user wants to set up, audit, or optimize analytics tracking (GA4, events, conversions). Also use when the user mentions "Google Analytics," "GA4," "event tracking," "conversions," "attribution model," "gtag," "data layer," "GA4 setup," "conversion tracking," "event setup," "User ID tracking," "CTA attribution," "tracking plan," "tag manager," "GTM," "Mixpanel," "Segment," "are my events firing," or "analytics isn't working." For traffic insights, use traffic-analysis. For choosing attribution models or reconciling conflicting numbers across tools, use attribution.
metadata:
  version: 1.3.1
  based_on_repo: kostja94/marketing-skills, coreyhaines31/marketingskills
  based_on_version: v1.0.0(8dd89c5), v2.11.29(c7d7dfb)
  based_on_skill: analytics-tracking, analytics
---

# Analytics: Tracking

Guides analytics implementation: GA4 setup, event tracking, conversions, and data quality. Applies to web and app tracking across marketing channels.

## Initial Assessment

**Project context:** Read the product marketing context when present. Without it, use available project material or user-provided facts and ask for missing information.

Before implementing tracking, establish:

1. **Business context**: What decisions will this data inform? What key actions and conversions matter?
2. **Current state**: What's already tracked? Which tools (GA4, Mixpanel, etc.)?
3. **Technical context**: What's the tech stack? Who implements, the dev team or marketing? Any privacy or consent requirements?

## Core Principles

1. **Track for decisions.** Every event maps to a decision it informs. Start from the question and the action you'd take on the answer, then work backwards to the event.
2. **Compute, don't eyeball.**
   - Derive every total, rate, and delta from row-level data with a script or spreadsheet, never by scanning rows and summing mentally. One silently dropped row corrupts every figure downstream of it.
   - Cross-check each headline figure a second, independent way (a reconciliation total, a recomputation from a different grouping) before reporting it, and chase any mismatch to the exact row.
   - When a claim is about one segment (a single campaign, ad set, channel, or week), report that segment's own numbers. Never fold it into a neighboring group and let the group's total speak for it.
3. **Match observation windows.**
   - A rate or efficiency metric divides a numerator and denominator that cover the same closed observation window. Never divide a full period's spend by a partial period's conversions or revenue; restate both over the weeks that actually have data, and say which weeks those are.
   - Cohort rates use only cohorts whose observation window has ended. A trial or signup still inside its window is pending, not failed: exclude it from the denominator and label it as pending.
4. **Recommend against the stated goal.** Analysis ends in a recommendation, and the recommendation must be argued from the goal the brief states (launch target, audience, revenue, positioning), not only from what is operationally easiest. Name which stated goal each option serves and what it trades away.

## User ID

- **Purpose**: Cross-device, cross-session user identification
- **Implementation**: Set `user_id` when user is identified (e.g., login); send to GA4
- **Benefit**: Accurate attribution across sessions; better audience building

## CTA Attribution (Article ROI)

Track CTA clicks on key articles to measure content ROI:

| Action | Purpose |
|--------|---------|
| **Event per CTA** | e.g., `cta_click` with `content_url`, `content_type` |
| **Conversion** | Mark as conversion in GA4 for attribution |
| **Use** | Compare high vs low performers; optimize CTA placement and copy |

See **seo-analytics** for article database and benchmark context.

## Infrastructure Requirements

| Component | Purpose |
|-----------|---------|
| **Data warehouse** | Centralized data; BI reporting |
| **Event tracking** | User behavior; funnel mapping |
| **Attribution** | Ad pixels; attribution model; impression-to-sale tracking |

**Optimization flow**: Clean UTM + conversion events → attribution reports → optimize channel mix.

## Scope

- **GA4**: Web data stream, gtag.js, configuration
- **User ID**: Cross-device, cross-session identification
- **CTA attribution**: Per-article conversion tracking for content ROI
- **Events**: Recommended and custom events
- **Conversions**: Key events, parameters
- **Quality**: Naming, testing, validation

## GA4 Setup

### Prerequisites

- Google Analytics property and web data stream
- Google tag (gtag.js) on all pages
- Measurement ID (e.g., `G-XXXXXXXXXX`)

### Enhanced Measurement

Enable in Admin > Data Streams > Enhanced Measurement for automatic tracking of:

- Page views, scrolls, outbound clicks
- Site search, file downloads
- Video engagement (YouTube)

For GA4 setup depth (conversions, custom dimensions, audiences, debugging), read [references/ga4-implementation.md](references/ga4-implementation.md).

## Google Tag Manager

For container structure, naming, data layer, tag configs and consent, read [references/gtm-implementation.md](references/gtm-implementation.md).

## Tracking Plan Framework

```
Event Name | Category | Properties | Trigger | Notes
---------- | -------- | ---------- | ------- | -----
```

| Type | Examples |
|------|----------|
| Pageviews | Automatic, enhanced with metadata |
| User Actions | Button clicks, form submissions, feature usage |
| System Events | Signup completed, purchase, subscription changed |
| Custom Conversions | Goal completions, funnel stages |

## Event Tracking

### Event Types

| Type | Description |
|------|-------------|
| **Automatically collected** | page_view, first_visit, session_start |
| **Enhanced measurement** | scroll, click, file_download, etc. |
| **Recommended** | purchase, sign_up, search, etc. |
| **Custom** | Business-specific actions |

### Naming Conventions

- **Length**: <=40 characters (GA4 hard limit; longer names are not logged)
- **Format**: `snake_case`, lowercase
- **Verb first**: `download_pdf`, `submit_form`, `video_play`
- **Context**: `pricing_page_scroll` vs generic `scroll`
- Be specific (`cta_hero_clicked` vs `button_clicked`), put context in properties rather than the event name, and avoid spaces and special characters.
- Keep provider-defined names when using automatic or recommended events (e.g. GA4 `click`, `view_search_results`, `purchase`). Map internal business names explicitly; naming a custom event does not make the provider collect it automatically.

> **Source conflicts (kostja wins, ours flagged):** our copy recommends object-action names (`signup_completed`, `form_submitted`). kostja says verb first (`submit_form`). Use verb first for new custom events; keep recommended-event names as the provider defines them.

### gtag.js Syntax

```javascript
gtag('event', '<event_name>', {
  <parameter_name>: <value>,
  // e.g. value: 99.99, currency: 'USD'
});
```

Place below the Google tag snippet. Events fire on page load or user action (e.g., button click).

### Recommended Events

| Event | Use | Key Parameters |
|-------|-----|----------------|
| `purchase` | E-commerce | value, currency, items |
| `sign_up` | Registration | method |
| `login` | Login | method |
| `search` | Site search | search_term |
| `view_item` | Product view | items |
| `add_to_cart` | Add to cart | items |

### Custom Events

- Focus on 15-25 meaningful events aligned with KPIs
- Add parameters for context (e.g., `content_type`, `item_id`)
- Avoid tracking everything; prioritize quality over quantity

### Events and Properties

Pick events and standard properties (user, session, campaign, product context) from [references/event-library.md](references/event-library.md), which lists them by business type with funnel sequences.

- Rely on automatic properties rather than re-sending them
- Keep PII out of properties

## Conversions (Key Events)

- Mark important events as conversions in GA4 Admin
- Use for attribution, audiences, and reporting
- Typical: purchase, sign_up, lead, contact

## Attribution & Conversion Optimization

Attribution models determine how conversion credit is assigned across touchpoints. Use attribution data to optimize ads and growth channels. For choosing a model, MMM, incrementality and reconciling conflicting numbers, use **attribution**.

| Model | Use |
|-------|-----|
| **Data-driven** (GA4 default) | ML assigns credit by actual contribution; best for multi-touch journeys |
| **Last-click** | 100% to final touchpoint; simple but undervalues awareness/consideration |

**Optimization flow**: Clean UTM (source, medium, campaign) + conversion events → GA4 attribution reports → compare channels by attributed conversions → reallocate budget to ads/channels that drive results. Inconsistent UTM fragments data; multi-touch attribution requires reliable touchpoint data. UTM conventions live in **traffic-analysis**.

**Reference**: [UTM.io – UTMs for Marketing Attribution](https://web.utm.io/blog/utms-for-marketing-attribution/), [GA4 – Get started with attribution](https://support.google.com/analytics/answer/10596866)

## Testing & Validation

| Tool | Use |
|------|-----|
| **Realtime** | See events as they fire |
| **DebugView** | Detailed event/parameter inspection; requires debug mode |
| **GA4 Debug mode** | `gtag('config', 'G-XXX', { 'debug_mode': true });` or GTM preview |
| **Browser extensions** | Tag Assistant, dataLayer Inspector |

- Test before launch; verify parameters and naming
- Check for duplicate events, missing values

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

## Privacy and Compliance

- Cookie consent required in EU/UK/CA
- Data retention settings and user deletion capabilities
- Use consent mode (wait for consent); integrate with a consent management platform
- IP anonymization; only collect what you need

## Output Format

- **Event list** (name, trigger, parameters)
- **Implementation** notes (gtag or GTM)
- **Conversion** mapping
- **Testing** checklist

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

## Tool Integrations

For implementation, see the [tools registry](https://github.com/coreyhaines31/marketingskills/blob/main/tools/REGISTRY.md). Key analytics tools:

| Tool | Best For | MCP | Guide |
|------|----------|:---:|-------|
| **GA4** | Web analytics, Google ecosystem | ✓ | [ga4.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/ga4.md) |
| **Mixpanel** | Product analytics, event tracking | - | [mixpanel.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/mixpanel.md) |
| **Amplitude** | Product analytics, cohort analysis | - | [amplitude.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/amplitude.md) |
| **PostHog** | Open-source analytics, session replay | - | [posthog.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/posthog.md) |
| **Segment** | Customer data platform, routing | - | [segment.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/segment.md) |

## Related Skills

- **traffic-analysis**: UTM, source attribution, AI traffic in GA4; attribution for channel optimization
- **seo-analytics**: GSC analysis (correlate with GA4); article database, benchmark, SEO monitoring
- **attribution**: Attribution models, multi-touch/MMM/incrementality, reconciling conflicting numbers (once tracking is live)
- **ab-testing**: Experiment tracking
- **conversion-optimization**: Conversion optimization (uses this data)
- **revops**: Pipeline metrics, CRM tracking, and revenue attribution
- **seo-audit**: Organic traffic analysis
