# Profile Templates

Ready-to-use templates for competitor profile sections and the summary document.

## Contents
- Deep Profile Template
- Quick Scan Template
- Summary Comparison Table
- Positioning Map
- Competitive SWOT
- Profile Update Changelog

---

## Deep Profile Template

Full profile, used for deep profiles.

```markdown
# [Competitor Name] — Competitor Profile

**URL**: [website]
**Generated**: [date]
**Depth**: [quick scan / deep profile]

---

## At a Glance

| Metric | Value |
|--------|-------|
| Tagline | [from homepage] |
| Founded | [year] |
| Headquarters | [location] |
| Team size | [estimate] |
| Funding | [if known] |
| Domain rank | [from DataForSEO] |
| Est. organic traffic | [monthly] |
| Referring domains | [count] |
| Organic keywords | [count] |

---

## Positioning & Messaging

**Primary value proposition**: [headline + subheadline from homepage]

**Target audience**: [who they're speaking to, based on copy analysis]

**Positioning angle**: [how they position — e.g., "simplicity-first," "enterprise-grade," "all-in-one"]

**Key messaging themes**:
- [theme 1 — with source page]
- [theme 2]
- [theme 3]

---

## Product & Features

### Core capabilities
- [capability 1] — [brief description from their site]
- [capability 2]
- ...

### Notable differentiators
- [what they emphasize as unique]

### Integrations
- [count] integrations
- Key: [list top 5-10]

### Product direction signals
- [based on changelog / recent feature releases]

---

## Pricing

| Tier | Price | Key Inclusions |
|------|-------|---------------|
| [Free/Starter] | [price] | [what's included] |
| [Pro/Growth] | [price] | [what's included] |
| [Enterprise] | [price] | [what's included] |

**Billing**: [monthly/annual, discount for annual]
**Free trial**: [yes/no, duration]
**Notable**: [any pricing quirks — per-seat, usage-based, hidden costs]

---

## Customers & Social Proof

**Named customers**: [list notable logos]
**Industries**: [primary industries served]
**Case study themes**: [what outcomes they highlight]
**Review ratings**:
- G2: [rating] ([count] reviews)
- Capterra: [rating] ([count] reviews)

---

## SEO & Content Strategy

**Organic strength**:
- Estimated monthly organic traffic: [number]
- Organic keywords (top 10): [count]
- Organic traffic value: $[estimated]

**Top organic pages** (by estimated traffic):
1. [page URL] — [keyword] — [est. traffic]
2. [page URL] — [keyword] — [est. traffic]
3. [page URL] — [keyword] — [est. traffic]

**Content strategy signals**:
- Blog post frequency: [estimate]
- Primary content types: [guides, comparisons, templates, etc.]
- Content focus areas: [topics they invest in]

**Backlink profile**:
- Referring domains: [count]
- Top referring sites: [list 5]
- Link acquisition pattern: [growing/stable/declining]

---

## Strengths & Weaknesses

### Strengths
- [strength 1 — with evidence source]
- [strength 2]
- [strength 3]

### Weaknesses
- [weakness 1 — with evidence source]
- [weakness 2]
- [weakness 3]

---

## Competitive Implications for [Your Product]

**Where they're strong vs. us**: [areas where this competitor has an advantage]

**Where we're strong vs. them**: [areas where you have an advantage — cite customer, win/loss, or review evidence; without it, label these as hypotheses]

**Opportunities**: [gaps in their offering or positioning we can exploit]

**Threats**: [areas where they're improving or gaining ground]

---

## Raw Data Sources

- Raw folder: `competitor-profiles/raw/<competitor-slug>/<YYYY-MM-DD>/`
- Homepage scraped: [date]
- Pricing page scraped: [date]
- SEO data pulled: [date]
- Review data pulled: [date, sources]
```

---

## Quick Scan Template

Abbreviated profile for when speed matters more than depth.

```markdown
# [Competitor Name] — Quick Profile

**URL**: [website]
**Generated**: [date]

## At a Glance

| Metric | Value |
|--------|-------|
| Tagline | [from homepage] |
| Target audience | [inferred from copy] |
| Pricing starts at | [lowest paid tier] |
| Free tier/trial | [yes/no + details] |
| Domain rank | [from DataForSEO] |
| Est. organic traffic | [monthly] |
| Organic keywords (top 10) | [count] |
| Referring domains | [count] |

## Positioning

**Headline**: "[exact homepage headline]"
**Subheadline**: "[exact subheadline]"
**Positioning angle**: [1-2 sentence summary of how they position]

## Pricing Summary

| Tier | Price | Notable Inclusions |
|------|-------|-------------------|
| [tier] | [price] | [key items] |
| [tier] | [price] | [key items] |

## Key Takeaway

[2-3 sentences: what makes this competitor notable, where they're strong, where they're weak]
```

---

## Summary Comparison Table

Use after profiling all competitors to create a side-by-side view.

```markdown
# Competitive Landscape Summary

**Generated**: [date]
**Your product**: [name]
**Competitors profiled**: [count]

## Side-by-Side Comparison

| Dimension | [Your Product] | [Competitor 1] | [Competitor 2] | [Competitor 3] |
|-----------|---------------|----------------|----------------|----------------|
| **Tagline** | [yours] | [theirs] | [theirs] | [theirs] |
| **Target audience** | [yours] | [theirs] | [theirs] | [theirs] |
| **Positioning** | [angle] | [angle] | [angle] | [angle] |
| **Starting price** | $[X]/mo | $[X]/mo | $[X]/mo | $[X]/mo |
| **Free tier** | [yes/no] | [yes/no] | [yes/no] | [yes/no] |
| **Domain rank** | [score] | [score] | [score] | [score] |
| **Est. organic traffic** | [number] | [number] | [number] | [number] |
| **Referring domains** | [count] | [count] | [count] | [count] |
| **G2 rating** | [score] | [score] | [score] | [score] |
| **Key strength** | [one-liner] | [one-liner] | [one-liner] | [one-liner] |
| **Key weakness** | [one-liner] | [one-liner] | [one-liner] | [one-liner] |
```

---

## Positioning Map

Visual representation of where competitors sit along two key dimensions. Choose the two axes most relevant to your market.

### Common Axis Pairs

| Market Type | X-Axis | Y-Axis |
|-------------|--------|--------|
| SaaS tools | Simple → Complex | Cheap → Expensive |
| Developer tools | Low-code → Code-first | Individual → Team |
| B2B platforms | SMB-focused → Enterprise-focused | Point solution → Platform |
| Content tools | Template-driven → Custom | Self-serve → Managed |

### Format

```markdown
## Positioning Map

**Axes**: [X-axis label] vs. [Y-axis label]

                    [Y-axis high label]
                           │
                           │
          [Competitor A]   │    [Competitor B]
                           │
    ───────────────────────┼───────────────────────
    [X-axis low]           │           [X-axis high]
                           │
          [Your Product]   │    [Competitor C]
                           │
                    [Y-axis low label]

### Interpretation
- [1-2 sentences about what the map reveals]
- [where the whitespace / opportunity is]
```

---

## Competitive SWOT

Per-competitor SWOT relative to your product.

```markdown
## SWOT: [Competitor] vs. [Your Product]

### Strengths (theirs vs. ours)
- [Where they genuinely outperform us — be honest]

### Weaknesses (theirs vs. ours)
- [Where they fall short compared to us — with evidence]

### Opportunities (for us)
- [Gaps in their offering we can exploit]
- [Segments they're ignoring]
- [Messaging angles they're missing]

### Threats (from them)
- [Areas where they're improving fast]
- [Features they're building that overlap with us]
- [Market moves that could shift perception]
```

---

## Profile Update Changelog

Append to the bottom of any profile when updating it.

```markdown
---

## Change Log

| Date | What Changed | Source |
|------|-------------|--------|
| [date] | Pricing increased from $X to $Y | Pricing page re-scrape |
| [date] | Launched [feature] | Changelog scrape |
| [date] | Domain rank changed from X to Y | DataForSEO re-pull |
| [date] | Added [integration] | Integrations page re-scrape |
```
