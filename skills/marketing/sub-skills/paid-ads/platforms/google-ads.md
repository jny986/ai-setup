---
name: google-ads
description: When the user wants to set up, optimize, or manage Google Ads campaigns. Also use when the user mentions "Google Ads," "Google Search Ads," "PPC," "SEM," "PMF testing with ads," "test product-market fit," "Responsive Search Ads," "RSA," "Performance Max," "Quality Score," "keyword bidding," or "Google Display/YouTube ads." For paid mix, use paid-ads-strategy.
metadata:
  version: 1.0.0
  based_on_repo: kostja94/marketing-skills, coreyhaines31/marketingskills
  based_on_version: v1.0.0(8dd89c5), v2.13.0(e85f3cb)
  based_on_skill: google-ads, ads
---

# Paid Ads: Google Ads

Guides Google Ads setup, campaign structure, keyword targeting, and optimization. Google Ads excels at high-intent search traffic; use when people actively search for your solution.

## Two Modes: PMF Testing vs Conversion-Driven

| Mode | When | Budget | Landing page | Metrics |
|------|------|--------|--------------|---------|
| **PMF testing** | Pre-PMF; validate idea before building | $47–500; start small | Simple LP: headline, benefits, problem solved, CTA ("Join Waitlist," "Get Early Access") | CTR, sign-up rate, bounce rate; low CTR/high bounce = messaging/positioning issue |
| **Conversion-driven** | PMF validated; commercialization | Scale; ROAS target | Full funnel; ad-to-page alignment | ROAS, CAC, conversion rate |

**PMF testing**: No full product needed. Build landing page with Unbounce, Carrd, or Webflow. Run ads to relevant search terms; measure clicks, engagement, signups. Test messaging (e.g., "Fastest App for Freelancers" vs "Simplest Time Tracker for Teams"), pricing (different price points in ads/LP), and audiences (keyword targeting, in-market). Allow 4–6 weeks for PMax learning phase. Use as learning tool, not just marketing channel.

**Reference**: [Marketing Cactus – Using Google Ads to Test Product-Market Fit](https://mktcactus.com/en/using-google-ads-to-test-product-market-fit-before-launching/)

## Campaign Structure

```
Account
├── Campaign: Brand (Search)
├── Campaign: Non-Brand (Search)
├── Campaign: Competitor (Search) — optional; bid on competitor brand + "alternative"/"vs"
├── Campaign: Retargeting (Display)
└── Campaign: Performance Max
```

### Competitor Brand Keywords

**When**: Bid on "[Competitor] alternative," "[Competitor] vs [You]" to intercept high-intent traffic. Google allows competitor terms as keywords; you cannot use competitor names in ad copy without permission.

**Landing page**: Use a **dedicated landing page** (comparison/alternatives page), not a blog article. Users searching competitor brands expect direct alternatives—a blog increases bounce; a comparison page matches intent and converts better. See **comparison-pages** for structure.

**Best practices**:
- Separate campaign; exact/phrase match; add your brand as negative
- H1 mirrors search intent (e.g., "[Competitor] vs [You]")
- Feature comparison table; one-line differentiator; strong CTA
- Expect lower Quality Score, higher CPC than non-brand; optimize LP relevance

**Naming**: `GOOG_[Objective]_[Audience]_[Offer]_[Date]` (e.g., `GOOG_Search_Brand_Demo_Ongoing`)

## Campaign Types

| Type | Best for |
|------|----------|
| **Search** | High-intent queries; keyword-targeted; landing page critical |
| **Display** | Awareness; retargeting; broader reach |
| **YouTube** | Video; awareness; consideration |
| **Performance Max** | Automated; cross-channel; feed + search + display |

## Performance Max (PMax) Optimization

**Learning period**: Run at least **6 weeks** for algorithm ramp-up. Works best as complement to Search, not replacement.

**Asset groups**: Organize by *audience intent* (e.g., high-intent searchers, cart abandoners, category researchers), not product category alone. Audience signals improve CPA and ROAS vs. no signals.

**Asset requirements** (per asset group):
- ≥5 images (include 1200×1200)
- ≥5 text assets (4 headlines, 5 descriptions)
- Video when possible
- Refresh creative regularly to maintain performance

**Signals**: Add remarketing lists and Customer Match to accelerate learning.

**Weekly health check**: Flag if brand terms &gt;30% of conversions; unexpected geo conversions; any placement &gt;15% of total spend; asset group performance below "Good."

## Keyword Strategy

- **Brand**: Protect brand terms; exclude from non-brand campaigns
- **Negative keywords**: Build weekly; avoid irrelevant queries. Add **support terms** (login, forum, pricing, help) from **keyword-research**—these are existing customers, not prospects.
- **Match types**: Broad (discovery) → Phrase → Exact (control)

**Keyword sources**: Use **keyword-research** for keyword list, clusters, and intent. Map each cluster to a dedicated landing page; relevance improves Quality Score and lowers CPC.

## Quality Score Levers

| Factor | Action |
|--------|--------|
| Expected CTR | Improve ad relevance; test headlines |
| Ad relevance | Align ad copy to keyword intent |
| Landing page | Ad-to-page alignment; fast load; mobile-friendly |

**Target**: Quality Score ≥6; higher = lower CPC, better ad rank. **Benchmark**: Improving Quality Score from 5 to 7 can reduce CPC by 30–50%.

## Bidding Strategy

| Conversions/month | Strategy |
|-------------------|----------|
| &lt;30 | Manual CPC (smart bidding needs volume to optimize) |
| 30–50 | Target CPA; minimum for effective smart bidding |
| 50–100 | Target CPA |
| 100+ | Target ROAS |

**Smart bidding**: AI-powered bidding (Target CPA, Target ROAS) typically delivers better ROI than manual when conversion volume is sufficient; requires ≥30 conversions in 30 days to work effectively.

## Tracking

- **Enhanced Conversions**: Server-side signals for better attribution
- **Offline conversion imports**: B2B; CRM → Google Ads
- **UTM**: Consistent parameters for GA4 cross-check

## Paid–Organic Cannibalization

When you rank organically (position 4+) for a keyword and also run PPC, paid ads can absorb clicks that would go to organic. **Audit**: Cross-reference GSC organic rankings with Search Terms report. If organic ranks well, test pausing PPC on those terms to free budget for higher-impact keywords.

**Reference**: [Backlinko – SEO and PPC: 8 Smart Ways to Align](https://backlinko.com/seo-and-ppc)

## Pre-Launch Checklist

- [ ] Conversion tracking tested with real conversion
- [ ] Landing page loads &lt;3s; mobile-friendly
- [ ] UTM parameters working
- [ ] Negative keyword list built (include support terms from keyword-research)
- [ ] Budget set; targeting matches audience

## Operating Playbooks

Deeper operating rules for live accounts; load the one that fits the task.

| Task | Load |
|------|------|
| Where to spend first, account structure, match-type gates, negatives, bidding by volume, PMax guardrails | [google-search-playbook.md](references/google-search-playbook.md) |
| Generating RSAs (mandatory output spec: limits, sidecars, template, self-check) | [rsa-output-spec.md](references/rsa-output-spec.md) |
| Auditing or grading a live account, quoting benchmarks, recommending changes | [audit-guardrails.md](references/audit-guardrails.md) |
| Itemised Search + Shopping + PMax + GMC + Demand Gen audit (32 checks, plus deep dives for conversion signals and wasted-spend negatives) | [google-ads-audit-checklist.md](references/google-ads-audit-checklist.md) |
| Reading Google Ads data: withheld search terms, conversions vs all_conversions, attribution dates, zero-in-N table | [reading-google-ads-data.md](references/reading-google-ads-data.md) |

### Audience knowledge: creative vs targeting

Where to apply audience knowledge differs by campaign type. Directional ratios, test in your own account:

| Campaign type | Creative | Targeting filters |
|---------------|----------|-------------------|
| Search | 40% | **60%**: keywords are the dominant signal; match types, intent layering and negatives still drive results |
| Performance Max / Demand Gen | **70%** | 30%: audience signals are advisory; creative and feed quality dominate |

### Brand vs non-brand

Split brand from non-brand before evaluating or optimising anything. Branded queries harvest demand that already exists, so a cheap brand CPA reflects awareness, not media efficiency. Report blended ROAS/CAC as the top-line health number; set targets, bids and budgets against non-brand ROAS. Treat a low brand CPA as a win only with an incrementality test (e.g. a brand-campaign holdout).

### Conflicts with ours (kostja wording above wins)

- **Bidding thresholds:** the table above says manual CPC under 30 conversions/month and Target CPA from 30. Ours says manual CPC or Maximize Conversions at 0-15, and merge any campaign that can't reach ~15-30 conversions/month because it can't feed smart bidding (see the playbook's bidding table).

## Related Skills

- **pmf-strategy**: PMF validation framework; when to use PMF testing vs conversion-driven
- **paid-ads-strategy**: Channel selection; budget allocation; ad-to-page alignment; competitor brand bidding
- **comparison-pages**: Competitor brand keyword ads → dedicated LP (not blog); comparison page structure
- **keyword-research**: Keyword list, clusters, intent; support terms for negative keywords; PPC data feeds back SEO priority
- **traffic-analysis**: UTM for attribution; paid–organic cannibalization audit
- **implement/sub-skills/references/pages/marketing/landing-page.md**: LP structure for paid traffic; PAA → FAQ
- **conversion-tracking**: Pixel and conversion tag setup, CAPI, tracking audits
- **analytics-tracking**: ROAS measurement
