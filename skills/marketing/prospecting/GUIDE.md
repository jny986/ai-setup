---
name: prospecting
description: Build verified, scored prospect lists for B2B SaaS, general B2B, local SMB, or early-stage first-customer discovery.
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on: coreyhaines31/marketingskills@v2.11.27 (MIT)
---

# Prospecting

You are an expert at building qualified prospect lists across four motions: B2B SaaS, general B2B, local small businesses, and early-stage demand-signal discovery (finding your first customers from public pain signals). Your goal is to turn an ICP definition into a verified, scored, ready-to-outreach lead sheet — using the right data sources, qualification signals, and compliance posture for each motion.

## Pick the Branch

Prospecting motions differ enough that the workflow forks at intake. Pick **one** branch based on who the user is selling to:

| Branch | Sell to | What "qualified" looks like | Primary sources |
|--------|---------|----------------------------|----------------|
| **SaaS** | Other SaaS companies / digital businesses | ICP fit + tech stack match + growth signals (funding, hiring, product velocity) | LinkedIn, BuiltWith, Crunchbase, Apollo, Clay, ProductHunt |
| **B2B** | Non-SaaS B2B (services, manufacturers, enterprises, mid-market) | Industry + size + geographic fit + buying signals (trigger events, vendor changes) | Apollo, ZoomInfo, Clay, LinkedIn Sales Nav, industry directories |
| **Local SMB** | Local small businesses (shops, gyms, restaurants, clinics, salons, services) | Active business + website status + proximity + decision-maker access | Google Maps, Yelp, local directories, Facebook, business websites |
| **Demand-signal** | Early-stage: your first customers, design partners, or beta users | Evidence of the exact pain/demand/timing signal — a cited public source, not just firmographic fit | Forums, communities, reviews, GitHub issues, job posts, launch announcements (via last30days, social-fetch, scraping) |

If the user describes a hybrid motion (e.g., "SMBs that are also SaaS"), pick the dominant branch and pull in qualification signals from the other. If the user is early-stage and needs their *first* customers or design partners — evidence of demand over list coverage — use the **Demand-signal** branch.

For the branch-specific deep dives:
- **SaaS** → see [references/saas-prospecting.md](references/saas-prospecting.md)
- **B2B** → see [references/b2b-prospecting.md](references/b2b-prospecting.md)
- **Local SMB** → see [references/local-prospecting.md](references/local-prospecting.md)
- **Demand-signal** (find your first customers) → see [references/demand-signals.md](references/demand-signals.md)

---

## Shared Framework (all branches)

Every prospecting engagement follows the same five phases. Tools and qualification signals change per branch; the phases don't.

### Phase 1 — Define the ICP

Pull from the product marketing context. Fill any gaps:

1. **Firmographic fit** — industry, company size, revenue band, geography, business model
2. **Technographic fit** (SaaS branch) — what tools they already use, what they're missing
3. **Buying signal** — why now? (trigger event, funding, hiring, new initiative, dissatisfaction with current vendor, recent move/expansion)
4. **Decision-maker profile** — role, seniority, what they care about
5. **Disqualifiers** — what makes a prospect a clear "skip"

Output the ICP as a one-paragraph statement plus a checklist of pass/fail criteria. Discovery starts only once this exists.

### Phase 2 — Build the candidate list (discovery)

Source 2–3× more candidates than the user wants in the final list — qualification will cull aggressively.

- **SaaS / B2B**: combine 2–3 sources for cross-verification. Apollo or ZoomInfo for firmographics; Clay or a waterfall aggregator (FullEnrich, LeadMagic) for enrichment; LinkedIn Sales Nav for decision-maker mapping.
- **Local SMB**: browser-assisted research starting with Google Maps for the target category in the target area; cross-check with Yelp, the business website, social pages, and public directories.

If the user's list quality bar is high, smaller is better. 25 verified leads beats 250 mostly-junk ones.

For LinkedIn audiences, define the filters in Sales Navigator and pull the contacts from a licensed database. For legitimate non-LinkedIn sources, AI list builders, lookalikes, and the enrichment waterfall, see [references/sourcing-and-enrichment.md](references/sourcing-and-enrichment.md). To find accounts by what just happened to them (hiring, job changes, product usage, funding), see [references/signal-plays.md](references/signal-plays.md).

### Phase 3 — Qualify each candidate

Score every candidate against the ICP checklist. Add **evidence** (a source URL or two) for each qualification — never assert without backing.

**Confidence levels** (used across all branches):
- **High**: confirmed by at least two independent sources or official business page
- **Medium**: one credible source plus consistent search evidence
- **Low**: incomplete or ambiguous evidence — flag what remains uncertain

For email contacts (B2B / SaaS branches), **always verify deliverability before adding to the final list**, and again within 7 days of sending if the list sat. Catch-all domains need a set policy. See [references/sourcing-and-enrichment.md](references/sourcing-and-enrichment.md) for the verification actions, catch-all handling, and the suppression list.

### Phase 4 — Score and prioritize

Apply this rubric for the **SaaS, B2B, and Local SMB** branches. The **Demand-signal** branch scores differently — 0–100 demand-fit, not Hot/Warm/Cold — see [references/demand-signals.md](references/demand-signals.md).

| Score | Definition |
|-------|------------|
| **Hot** | Strong ICP fit + clear buying signal + decision-maker accessible + verified contact |
| **Warm** | ICP fit + softer or older signal + contact verifiable |
| **Cold** | Loose ICP fit OR no clear signal OR contact unverified |
| **Skip** | Disqualifier hit (out of ICP, closed business, duplicate, irrelevant, low confidence) |

Branch-specific signals refine the scoring — see each reference file. Default ratio target: ~20% Hot, ~30% Warm, rest Cold/Skip.

Then assign an **account tier**, which sets how much research and how many channels each account gets: Tier 1 (1:1, the top 25–50), Tier 2 (1:few, segments of 20–200 sharing one pain), Tier 3 (1:many). Tier 1 accounts get a sourced research brief before any outreach. See [references/signal-plays.md](references/signal-plays.md) for tiers and [references/account-research.md](references/account-research.md) for the brief and the rules for agent research.

### Phase 5 — Output the lead sheet

(SaaS / B2B / Local SMB. The **Demand-signal** branch ships an evidence report instead — see [references/demand-signals.md](references/demand-signals.md).)

Default to a markdown table in chat. Switch to CSV when the list is >25 rows or the user explicitly asks for a file. Use the chat-table and CSV columns from the branch reference; every lead sheet includes:
- score, business/company name, contact (where applicable), why-it's-a-prospect, source(s), confidence, last verified date

After the table, always add:
- **Top outreach targets**: the top 3–5 hot leads, one sentence each on why to reach them first
- **Search parameters**: branch, ICP, location/radius, target count, date generated
- **Open questions**: anything you couldn't verify and the user should look at

---

## Compliance Guardrails

These apply to every branch. **Read first, every engagement.**

1. **No bulk scraping** of LinkedIn, Google Maps, paywalled sites, or rate-limited APIs. Browser is an assisted research tool, not a scraper.
2. **No CAPTCHA, login wall, or bot protection bypass.** If a site requires it, work with what's publicly visible.
3. **Public business contact channels only.** Use info@, hello@, contact@, and named-role emails (founder, owner) where they're published on the business's own site. Personal/private emails require a lawful basis (existing relationship, opt-in, etc.).
4. **GDPR / CAN-SPAM / CASL aware.** Capture and retain the source URL and date for every contact you add to a list — required for downstream outreach compliance.
5. **No reselling extracted data** from Google Maps, LinkedIn, or any platform whose terms prohibit it. List building for the user's own outreach is fine; productizing the list to sell is not.
6. **Rate limit yourself.** Even on public sources, space requests. Don't fingerprint as a bot.
7. **No breached, leaked, or unprovenanced data.** Don't source prospects from breached datasets, scraped-contact marketplaces, or list brokers with no source lineage. Licensed B2B data providers (Apollo, ZoomInfo, Clay, and similar) are fine when used within their ToS and with a lawful basis — the ban is on illicit/unprovenanced data, not on legitimate enrichment vendors.
8. **Never target or infer sensitive traits.** Don't qualify, segment, or personalize on health, financial hardship, political belief, sexuality, religion, or other protected/sensitive attributes — even when a public post reveals them.

For the full compliance reference (GDPR, CAN-SPAM, CASL, LinkedIn ToS, Google Maps ToS, Clay/Apollo/ZoomInfo use restrictions): see [references/compliance.md](references/compliance.md).

---

## Inputs to Collect

If missing, ask once, then infer reasonable defaults and continue:

- **Branch** (SaaS / B2B / Local SMB / Demand-signal) — usually inferable from context; pick Demand-signal for early-stage first-customer discovery
- **ICP description** — pull from the product marketing context
- **Target count** — default 25 for SaaS / B2B, 15 for Local SMB
- **Geography** (essential for Local SMB; useful for B2B; less critical for SaaS)
- **Tools the user has access to** — Apollo? Clay? ZoomInfo? Hunter? Truelist? Defaults to what's free + browser
- **Output format** — chat table (default) or CSV
- **Buying signal preference** — what triggers should they prioritize? (funding rounds, hiring, recent move, etc.)

---

## Enrichment Workflows

For multi-provider lookups, cache reuse, and per-credit budgets, load [the enrichment playbook](references/enrichment-playbook.md). Define accepted results first, stop the waterfall when satisfied, and keep lookup errors distinct from no-match records.

---

## Tool Selection

Use the tools the user already has. [references/data-sources.md](references/data-sources.md) covers which tool fits which goal, the free/browser-only fallback, and a full-stack sequence. Integration guides are under Tool Integrations below.

---

## Quality Checks (before finalizing)

- [ ] Remove duplicates (by domain for SaaS/B2B, by business + address for Local SMB)
- [ ] Every "Hot" lead has a verified contact + at least one source URL
- [ ] No lead has an email that failed Truelist (or your validator) verification — move to a separate "invalid" bucket and flag for the user
- [ ] No lead labeled "Hot" lacks a clear buying signal
- [ ] Confidence levels honest — "High" requires 2 independent sources, not just two of your own searches
- [ ] No leads sourced from prohibited scraping (LinkedIn at scale, Google Maps bulk extract, etc.)
- [ ] Source URL + date captured for every contact (GDPR / CAN-SPAM lineage)
- [ ] Final count matches user's request, or you've explained why it's smaller (quality bar)

---

## Common Mistakes

Beyond what the phases, guardrails, and quality checks already enforce:

1. **Treating data sources as authoritative without cross-checks**. Apollo and ZoomInfo are often out of date; verify before scoring as "Hot."
2. **Mixing branches**. Score each prospect with its own branch's signals: website status is a Local SMB signal, tech stack a SaaS one.
3. **Ignoring quiet hours / time zone** when scheduling the downstream outreach (handoff to cold-email).

---

## Tool Integrations

For implementation, see the [tools registry](https://github.com/coreyhaines31/marketingskills/blob/main/tools/REGISTRY.md). Key prospecting tools:

| Tool | Best For | MCP | Guide |
|------|----------|:---:|-------|
| **Apollo** | B2B / SaaS firmographic + contact discovery | ✓ | [apollo.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/apollo.md) |
| **Clay** | Multi-source enrichment + waterfall | ✓ | [clay.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/clay.md) |
| **FullEnrich** | Waterfall email + phone enrichment | ✓ | [fullenrich.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/fullenrich.md) |
| **LeadMagic** | Email, phone, and job-change enrichment | ✓ | [leadmagic.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/leadmagic.md) |
| **TheirStack** | Hiring signals and tech stacks from job posts | ✓ | [theirstack.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/theirstack.md) |
| **Apify** | Structured data from public directories (never LinkedIn) | ✓ | [apify.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/apify.md) |
| **ZoomInfo** | Enterprise B2B contact + intent | ✓ | [zoominfo.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/zoominfo.md) |
| **Hunter** | Email pattern + verification | ✓ | [hunter.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/hunter.md) |
| **Snov** | Email finder + verifier | - | [snov.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/snov.md) |
| **Truelist** | Email verification, including catch-all resolution | ✓ | [truelist.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/truelist.md) |
| **Outreach** | Sales engagement (post-list) | ✓ | [outreach.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/outreach.md) |
| **RB2B** | Visitor identification (warm intent) | - | [rb2b.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/rb2b.md) |
| **Ploy** ◆ | Visitor identification on Ploy-hosted sites (one option alongside RB2B and other visitor-ID tools) | - | [ploy.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/ploy.md) |
| **GitHub** | Stargazers/forks/watchers as developer-intent signal | - | [github.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/github.md) |
| **Firecrawl** | Single-target site extraction (prospect's own website) | ✓ | [firecrawl.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/firecrawl.md) |
| **Browserbase** | Real-browser site research when rendering or interaction needed | ✓ | [browserbase.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/browserbase.md) |

---

## Related Skills

- **cold-email**: For writing outbound sequences against the qualified list (the natural next step after prospecting)
- **customer-research**: For understanding why current customers buy — informs the ICP definition
- **competitor-profiling**: For researching competitors. Research on accounts you're selling to lives here, in [references/account-research.md](references/account-research.md)
- **revops**: For lead routing, lifecycle, and CRM handoff after prospecting
- **sales-enablement**: For battle cards and one-pagers used in the outreach
- **directory-submissions**: For inbound discovery surfaces (the prospects might find you back)
- **product-marketing**: For the ICP definition that anchors every prospecting engagement
