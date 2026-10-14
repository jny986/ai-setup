---
name: email-marketing
description: When the user wants to plan email marketing, EDM, newsletter strategy, email deliverability, or lifecycle email sequences. Also use when the user mentions "email marketing," "EDM," "newsletter," "SPF," "DKIM," "DMARC," "email deliverability," "email content strategy," "email campaigns," "newsletter strategy," "email automation," "cold email," "email sequence," "drip campaign," "nurture sequence," "onboarding emails," "welcome sequence," "re-engagement emails," "lifecycle emails," "trigger-based emails," "email cadence," or "what emails should I send." For signup UI, use `dev/references/components/conversion/newsletter-signup`.
metadata:
  version: 1.0.1
---

# Channels: Email Marketing

Guides email marketing strategy for AI/SaaS products. Email ROI ~$36 per dollar spent; open/click rates typically higher than social. Covers EDM vs Newsletter, five content types, deliverability (SPF/DKIM/DMARC), and SEO synergy via article delivery.

## Initial Assessment

**Project context:** Read the product marketing context when present and load only what is relevant to this task. Otherwise use available project material or user-provided facts and ask for missing information.

Identify:
1. **Goal**: Retention, conversion, brand reach, or SEO synergy
2. **Content mix**: Onboarding, campaign, announcement, features, newsletter
3. **List size**: Bulk sender rules (5,000+/day) require Gmail/Yahoo compliance

## EDM vs Newsletter

| Type | Purpose | Use |
|------|---------|-----|
| **EDM** | Direct marketing; conversion-focused | Promotions, campaigns, announcements; bulk sends |
| **Newsletter** | Ongoing value; relationship | Industry insights, curated articles; regular cadence |

**Combine both**: EDM for push; Newsletter for nurture. Cover different stages and goals.

## Five Content Types

| Type | Use |
|------|-----|
| **Onboarding** | Welcome + first-use guidance; 5-7 day sequence; behavior-triggered; drive "Aha!" moment |
| **Campaign** | Promotions, limited-time; conversion or participation |
| **Announcement** | Product launch, major update; one-time important notice |
| **Features update** | New features, improvements; help users adopt |
| **Blog/Newsletter** | Curated articles, industry insights; sustained touch |

## User Best Practices

| Practice | Guideline |
|----------|-----------|
| **Personalization** | Segment by behavior, source, stage; boosts open/click |
| **Timing** | New users: dense; existing: controlled pace; behavior-triggered > calendar-only |
| **Welcome series** | Send soon after signup; 5-7 emails over days; guide first key action |
| **Unsubscribe** | One-click required (Gmail/Yahoo); honor within 48h; clear entry |
| **Complaint rate** | Keep below 0.3%; list hygiene critical |

## Content Best Practices

| Practice | Guideline |
|----------|-----------|
| **Subject** | One clear topic per email; avoid pure promo |
| **Value first** | Useful info before promotion |
| **CTA** | Single primary CTA; clear next step |
| **Mobile** | 50%+ read on mobile; responsive layout, tappable links |

## Deliverability & Domain Config

**Subdomain**: Use subdomain (e.g. mail.example.com) for marketing; keep transactional (support@, etc.) on main domain. Isolate risk.

### SPF, DKIM, DMARC

| Protocol | Purpose |
|----------|---------|
| **SPF** | Authorizes mail servers for domain |
| **DKIM** | Cryptographic signature; verifies sender |
| **DMARC** | Policy for unauthenticated mail; start p=none, then quarantine, then reject over 60-90 days |

**Order**: SPF first, then DKIM, then DMARC. Gmail/Yahoo require all three for bulk senders (5,000+/day) since Feb 2024.

**Advanced**: TLS-RPT, MTA-STS, BIMI (brand logo). **Postmaster Tools**: Monitor deliverability, spam rate, auth status.

## Delivery Strategy: Articles + SEO Synergy

| Article Type | Use |
|--------------|-----|
| **Retention** | Deep content for existing users; improve retention |
| **ToFu** | Top of funnel; awareness (trends, concepts, problem framing) |
| **MoFu** | Middle of funnel; consideration (comparisons, reviews, best practices) |

**Dual value**: (1) Better email engagement (open, click, stickiness); (2) Drive traffic to article pages from non-search channel; signals to Google that users value content; supports SEO.

**Measurement**: GA4 email source traffic to article pages; GSC rank/click changes.

## Planning Framework

1. **Content mix**: Allocate onboarding, campaign, announcement, features, newsletter
2. **Select articles**: Pick retention, ToFu, MoFu from blog; prioritize SEO target pages
3. **Cadence**: Stable frequency (weekly/biweekly/monthly); avoid over-sending
4. **Monitor**: Open rate, click rate; GA4 email contribution to article traffic; GSC

## Frequency

| Guideline | Note |
|-----------|------|
| **Baseline** | 1 high-value email/week for most brands |
| **Peak times** | Tue-Thu, 8-11am or 2-4pm (recipient timezone) |
| **Segmentation** | New vs loyal need different cadence |
| **Quality** | Relevant, behavior-triggered > calendar volume |

**Data**: ~36% send 1-3/month; ~30% weekly; daily risks high unsubscribe.

## Lifecycle Sequences

For automated multi-email flows (welcome, nurture, onboarding, re-engagement, post-purchase, event-based). Done when you can fill the Sequence Overview in Output Format.

**Core principles**: one email, one job and one primary CTA; value before ask; relevance over volume (segment); every email points to a specific next step.

| Sequence | Typical length |
|----------|----------------|
| Welcome | 3-7 emails |
| Lead nurture | 5-10 emails |
| Onboarding | 5-10 emails |
| Re-engagement | 3-5 emails |

Length depends on sales cycle, product complexity, and relationship stage. Per-type email order and day-by-day timing: [sequence-templates.md](references/sequence-templates.md).

**Delays**: welcome email immediately; early sequence 1-2 days apart; nurture 2-4 days apart; long-term weekly or bi-weekly. B2B: avoid weekends; B2C: test weekends. Send at recipient local time.

**Coverage audit**: to find missing lifecycle emails (onboarding, retention, billing, usage, win-back, campaigns), use the checklist in [email-types.md](references/email-types.md).

## Email Copy

### Subject and Preview

- Clear > clever; specific > vague; benefit- or curiosity-driven; 40-60 characters; test emoji (polarizing)
- Patterns: question ("Still struggling with X?"), how-to ("How to [outcome] in [timeframe]"), number ("3 ways to [benefit]"), direct ("[First name], your [thing] is ready"), story tease ("The mistake I made with [topic]")
- Preview text (~90-140 characters) adds what the subject didn't say: complete the thought or add intrigue

### Structure, Format, Length

1. **Hook**: first line grabs attention
2. **Context**: why this matters to them
3. **Value**: the useful content
4. **CTA**: button for the primary action (action + outcome text), links for secondary
5. **Sign-off**: human, warm close

Short paragraphs (1-3 sentences), white space, bullets for scanning, bold sparingly. Tone: conversational, first and second person, active voice; read it aloud. Length: 50-125 words transactional, 150-300 educational, 300-500 story-driven.

### No AI Tells

Subscribers learn to recognize generated email fast and stop reading. Write from the specific thing you want them to know or do. Avoid:

- **Contrast reveals** ("It's not X, it's Y"): state Y directly, with the reason
- **Negation lists** ("No X, no Y, no Z"): say what does happen; one plain absence ("No card required") is fine
- **Trailing pile-ons**: end the sentence at the claim
- **Self-answered questions and colon reveals** ("The result? 3x faster."); FAQ questions are fine
- **Stock phrases**: "Say goodbye to," "Unlock the power of," "Take it to the next level," "Here's the thing"
- **Em dashes** in subject and preview text; at most one or two in a long email
- **Subject-line bait**: fake "Re:"/"Fwd:", "You won't believe...". The subject should hold up if it's the only line read
- **Stock openers and sign-offs**: "I hope this email finds you well," "Just checking in," "Feel free to reach out if you have any questions." Open with the reason for writing; ask for one action, or end

See **copywriting** for the full blacklist.

Personalization, merge fields, dynamic content, segmentation, testing, and metric benchmarks: [copy-guidelines.md](references/copy-guidelines.md).

## Output Format

- **Content mix** (five types)
- **EDM vs Newsletter** balance
- **Deliverability** (subdomain, SPF/DKIM/DMARC)
- **Article delivery** (Retention, ToFu, MoFu, SEO targets)
- **Cadence** and frequency
- **KPI** (open, click, GA4 email traffic, GSC); benchmarks in [copy-guidelines.md](references/copy-guidelines.md#metrics-to-track)

For a lifecycle sequence, also return:

```
Sequence Name / Trigger / Goal / Length / Timing / Exit Conditions

Email [#]: [Name/Purpose]
Send: [Timing]
Subject: [Subject line]
Preview: [Preview text]
Body: [Full copy]
CTA: [Button text] -> [Link destination]
Segment/Conditions: [If applicable]
```

## Tool Integrations

For implementation, see the [tools registry](https://github.com/coreyhaines31/marketingskills/blob/main/tools/REGISTRY.md). Key email tools:

| Tool | Best For | Guide |
|------|----------|-------|
| **Customer.io** | Behavior-based automation | [customer-io.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/customer-io.md) |
| **Mailchimp** | SMB email marketing | [mailchimp.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/mailchimp.md) |
| **Nitrosend** | AI-native email (sequences via prompts) | [nitrosend.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/nitrosend.md) |
| **Resend** | Developer-friendly transactional | [resend.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/resend.md) |
| **SendGrid** | Transactional email at scale | [sendgrid.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/sendgrid.md) |
| **Kit** | Creator/newsletter focused | [kit.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/kit.md) |

## Related Skills

- **content-marketing**: Content types, formats; email as channel in repurposing matrix
- `dev/references/components/conversion/newsletter-signup`: Signup form design
- **traffic-analysis**: Email source attribution, UTM
- **analytics-tracking**: Email click tracking
- **content-strategy**: Article selection for email delivery
- **integrated-marketing**: Email as owned media channel
- **lead-magnets**: Lead magnets that feed nurture sequences
- **retention-strategy**: Cancel flows, save offers, dunning (email supports these)
- **onboarding**: In-app onboarding (email supports it)
- **copywriting**: Landing pages emails link to
- **ab-testing**: Testing email elements
- **popups**: Email capture popups
- **revops**: Lifecycle stages that trigger sequences
- **cold-email**: Cold outreach (separate from lifecycle email)
