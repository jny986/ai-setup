---
name: traffic-analysis
description: When the user wants to analyze website traffic sources, attribution, or dark traffic. Also use when the user mentions "traffic sources," "dark traffic," "direct traffic," "UTM parameters," "traffic attribution," "channel attribution," "attribution optimization," "channel analysis," "traffic analysis," "traffic diversification," "natural traffic benchmark," or "organic vs paid traffic," "AI traffic," "ChatGPT referral," "Perplexity traffic," "AI Overviews," "GA4 AI sources," "track AI referrals," or "Claude traffic." For GA4 setup, use analytics-tracking.
metadata:
  version: 1.0.0
  based_on_repo: kostja94/marketing-skills, coreyhaines31/marketingskills
  based_on_version: v1.0.0(8dd89c5), v2.13.0(e85f3cb)
  based_on_skill: traffic-analysis, analytics, ai-traffic-tracking, ai-seo
---

# Analytics: Traffic

Guides website traffic analysis across all channels (organic, paid, social, referral, direct). Covers traffic source attribution, dark traffic identification, and multi-channel reporting.

## Initial Assessment

**Project context:** Read the product marketing context when present. Without it, use available project material or user-provided facts and ask for missing information.

Identify the channels in use, current UTM conventions, and which analytics tool reports traffic.

## Scope

- **Traffic sources**: Organic, paid, social, referral, direct, email
- **Dark traffic**: Unattributed visits labeled as "Direct / None"
- **Attribution**: UTM tagging, segmenting, reporting accuracy

## Branded vs. Non-Branded Traffic (Organic)

| Type | Characteristics |
|------|-----------------|
| **Branded** | Higher CTR, conversion, purchase intent; users closer to funnel bottom |
| **Non-branded** | Touchpoint with future users; most sites get more non-brand traffic; competition fiercer |

Brand traffic grows over time as brand awareness increases.

## Bot Traffic

A large share of traffic can be **bot traffic**—RPA, search crawlers, spiders, scrapers. Exclude or segment when evaluating real user behavior; use GA4 filters or segments to isolate human traffic.

## Traffic Channels

| Channel | Typical Sources | Attribution |
|---------|-----------------|-------------|
| **Organic** | Google, Bing, other search | Referrer preserved |
| **Paid (web)** | Google Ads, Meta Ads, etc. | UTM required |
| **Paid (app)** | App install ads; Google App Campaigns, Apple Search Ads | UTM; in-app events |
| **Paid (TV/CTV)** | Streaming ads; Hulu, Roku, YouTube TV | UTM for QR/URL; brand lift |
| **Social** | Public posts (Facebook, LinkedIn, etc.) | Often preserved |
| **Referral** | External sites, backlinks | Referrer preserved |
| **Direct** | Typed URL, bookmarks | No referrer |
| **Email** | Newsletters, campaigns | Often dark without UTM |

## Dark Traffic

### What It Is

Traffic without clear origin--analytics tools default to "Direct" when referrer is missing. Common causes:

- **Private/dark social**: WhatsApp, Messenger, Slack, Discord, TikTok shares
- **Email clients**: Many strip referrer headers
- **HTTPS->HTTP**: Referrer not passed
- **Mobile apps**: In-app browsers often omit referrer
- **Ad blockers, privacy tools**: Block tracking

### Misattribution (Research)

When traffic was sent from known sources, analytics often misattributed:

- **100% as direct**: TikTok, Slack, Discord, WhatsApp, Mastodon
- **75%**: Facebook Messenger
- **30%**: Instagram DMs
- **14%**: LinkedIn public posts
- **12%**: Pinterest

### Mitigation

| Action | Purpose |
|--------|---------|
| **UTM parameters** | Tag links in emails, social, campaigns: `?utm_source=X&utm_medium=Y&utm_campaign=Z` |
| **Block internal IPs** | Exclude company visits from reports |
| **Segment direct traffic** | Split by page type to estimate dark vs. genuine direct |

### Segmenting Direct Traffic

1. **Expected direct**: Homepage, short URLs, brand pages--likely real direct
2. **Unexpected direct**: Long URLs, deep pages, product pages--likely dark traffic
3. **Report separately**: Use segments in GA4/analytics to avoid overcounting direct

## Attribution for Channel Optimization

Ads, growth channels, and medium can be optimized by viewing **attribution data**. Clean UTM + conversion tracking feeds attribution models; reliable attribution drives budget allocation and channel decisions.

| Use | Action |
|-----|--------|
| **Optimize ads** | Compare paid channels (Google, Meta, LinkedIn) by attributed conversions; reallocate budget to winners |
| **Optimize growth channels** | Identify which medium (cpc, email, social, referral) drives conversions; scale what works |
| **Multi-touch attribution** | Requires clean UTM data; inconsistent tagging (e.g., `facebook` vs `Facebook`) fragments reports and misattributes |

**GA4 Default Channel Grouping**: Align `utm_medium` and `utm_source` with [GA4's rules](https://support.google.com/analytics/answer/9756891) to avoid "Unassigned" traffic. ~30% of campaigns lack proper UTM markup, leading to wasted ad spend; teams standardizing UTM see 29% improvement in attribution accuracy.

**Reference**: [UTM.io – utm_medium, utm_campaign & utm_source Optimization](https://web.utm.io/blog/utm_medium-utm_campaign-utm_source/), [UTMs for Marketing Attribution](https://web.utm.io/blog/utms-for-marketing-attribution/)

## UTM Best Practices

| Parameter | Use | Example |
|-----------|-----|---------|
| `utm_source` | Origin | `newsletter`, `facebook`, `google` |
| `utm_medium` | Channel type | `email`, `cpc`, `social` |
| `utm_campaign` | Campaign name | `summer-sale`, `product-launch` |
| `utm_content` | Variant (optional) | `banner-a`, `cta-button` |
| `utm_term` | Paid keyword (optional) | `running-shoes` |

**GA4 alignment** (avoid Unassigned):

| Channel | utm_medium | utm_source |
|---------|------------|------------|
| Paid Search | `cpc` | `google`, `bing` |
| Paid Social | `paid-social`, `cpc` | `facebook`, `instagram` |
| Email | `email` | `newsletter`, `mailchimp` |
| Organic Social | `social` | `twitter`, `linkedin` |
| App install | `cpc`, `app` | `google`, `facebook`, `apple` |
| CTV / Streaming | `video`, `ctv` | `hulu`, `roku`, `youtube` |
| Display / Banner | `display`, `cpc` | Publisher or network name |
| Directory ads | `paid`, `cpc` | `taaft`, `shopify`, `g2`, `capterra` |

- **Never tag internal links** (overwrites session attribution)
- **Apply everywhere**: Every link in emails, social posts, ads
- **Avoid**: Typos, inconsistent values; causes fragmentation
- **Use `utm_content`** to tell versions of the same placement apart (`hero-cta`)

### Naming Conventions

- **Lowercase everything.** GA4 treats `LinkedIn` and `linkedin` as two sources, and the split never merges back.
- **Hyphens between words.** No spaces, underscores, or `+`. Pick one separator for the whole company; this skill uses hyphens.
- **One spelling per source.** `linkedin`, never also `li` or `linkedin.com`. Keep the allowed values in a shared sheet and build links from it.
- **No personal data.** Never put emails, names, phone numbers, or user IDs in a UTM. They land in analytics reports and in referrer logs, and Google's terms prohibit sending PII to GA4.
- **Specific but short:** `blog-footer-cta`, not `cta1`.
- **Test the final URL.** Shorteners and redirects can drop or double parameters. Click the live link and check the landing URL before the campaign ships.

### UTM Patterns by Partner Type

Partner links break most often because each deal gets named on the spot. Fix the pattern per partner type once: `utm_medium` names the kind of deal, `utm_source` names who sent the traffic.

| Partner type | utm_source | utm_medium | utm_campaign | utm_content |
|---|---|---|---|---|
| Newsletter | `{partner}` (one per partner, across all their publications) | `newsletter` | `{partner}-{publication}-{yyyy}-{mm}` | `{placement}-{yyyy-mm-dd}` |
| Creator (YouTube, LinkedIn, TikTok) | `{platform}` | `creator` | `{creator}` | `{post-date}` or the video ID |
| Podcast | `{podcast}` | `podcast` | `{podcast}-{yyyy}-{mm}` | `{spot}-{yyyy-mm-dd}` (pre-roll, mid-roll) |
| Affiliate | `{partner}` | `affiliate` | `{partner}-affiliate` | placement, if they have several |
| Community | `{community}` | `community` | `{community}-{program}` | the channel or post, if known |

- **Use `creator` as the medium for paid creator deals**, not `social` (which mixes them with your organic posts) or `video` (which mixes them with paid video ads). The platform goes in `utm_source`.
- **One link per placement.** A newsletter that runs you on two dates gets two links, so each date's clicks stay separate. The monthly `utm_campaign` rolls them up.
- **Add a custom channel group in GA4.** GA4's default grouping sends mediums like `newsletter`, `creator`, `podcast`, and `community` to Unassigned (only `affiliate` and `email` map to a default channel). Create a channel group with a rule per medium so partner traffic shows up as its own channels.
- Podcast and video links often aren't clickable, so pair the UTM link with a promo code or vanity URL. See **influencer-marketing** for the rest of partner measurement.

*The partner-type pattern is adapted from Wispr Flow's link-creator skill (MIT), published in the skills.marketing library.*

## AI Traffic

For AI search referrals (ChatGPT, Perplexity, Claude), AI Overviews and AI visibility monitoring, see [references/ai-traffic.md](references/ai-traffic.md).

### Traffic From AI Assistants

You can't tag links that ChatGPT, Claude, Perplexity, Gemini, or Copilot put in their answers. Some of those visits arrive with a referrer (`chatgpt.com`, `perplexity.ai`) or an assistant-added `utm_source`; many arrive as direct, or come later through a branded search.

- Add a GA4 channel group rule that matches known assistant referrers and sources into an "AI assistants" channel, and update the list as new assistants appear.
- Treat that channel as the floor. Assistant-driven visits that show up as direct or branded search can be most of the effect, and they won't carry the referrer.
- For measuring the full effect (exposure, delayed visits, and longer attribution windows), see **generative-engine-optimization**. For reconciling it with other sources, see **attribution**.

## Traffic Diversification

| Principle | Guideline |
|-----------|-----------|
| **Search share** | Keep organic search below ~75% of total traffic |
| **Health** | Higher direct + referral share = healthier profile |
| **Brand sites** | Diversified traffic is common for strong brands |
| **Engagement** | Content, email, social, free tools drive return visits |

See **seo-analytics** for full SEO data analysis framework.

## Natural Traffic Benchmark

**Location**: GA4 > Reports > Acquisition > Traffic acquisition

1. Review organic traffic trend
2. Record baseline (e.g., monthly total)
3. Compare periodically to detect growth or decline

## Output Format

- **Traffic source** breakdown
- **Dark traffic** estimate and actions
- **UTM** tagging recommendations
- **Segmentation** approach for reporting

## Related Skills

- **analytics-tracking**: Implement events and conversions; attribution models
- **attribution**: Choosing models and reconciling conflicting numbers across tools
- **google-ads**, **paid-ads-strategy**: Paid channels; attribution informs budget allocation
- **seo-analytics**: GSC performance and indexing analysis; SEO monitoring system, benchmark, article database
- **email-marketing**: Email strategy; UTM for email links
