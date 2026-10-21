---
name: gtm-strategy
description: When the user wants to plan go-to-market strategy, GTM framework, or market entry. Also use when the user mentions "GTM," "go-to-market," "market entry," "new market," "repositioning," "PLG," "sales-led," "product-led," "marketing-led," "ICP," "buyer persona," "GTM motion," or "market expansion." For launch checklist, use product-launch.
metadata:
  version: 1.0.0
  based_on_repo: kostja94/marketing-skills, coreyhaines31/marketingskills
  based_on_version: v1.0.0(8dd89c5), v2.13.0(e85f3cb)
  based_on_skill: gtm-strategy, marketing-plan
---

# Strategies: Go-to-Market

Guides go-to-market (GTM) strategy—the blueprint for launching or repositioning a product that aligns product, marketing, sales, and customer success around reaching and winning target customers. Organizations with a defined GTM process see ~10pp higher launch success rates (63% vs 53%) and ~3× median revenue growth. However, ~72% of sales reps miss quota, often due to execution gaps. Use this skill when planning GTM for product launch, new market entry, repositioning, or feature launch.

## GTM Scenarios

| Scenario | Scope | Use |
|----------|-------|-----|
| **Product launch** | New product to market | Full GTM; see **product-launch** for launch execution |
| **New market entry** | New geography or segment | Full GTM; different buying behaviors, competitors, regulations |
| **Repositioning** | Shift who you serve, what you solve | Messaging, ICP, channel alignment; not just rebrand |
| **Feature launch** | New capability in existing product | Tiered by impact; T1 (revenue) = full planning; T2/T3 = lighter |

**GTM vs product launch**: GTM is the strategy; product launch is the execution phase. GTM applies to multiple scenarios—not just new products.

## GTM Modes

| Mode | When to Use | ACV | Buyer |
|------|-------------|-----|-------|
| **Product-led (PLG)** | Value in minutes; self-evaluate; simple adoption | &lt;$10K | Buyer = end user |
| **Sales-led (SLG)** | Multi-stakeholder; complex procurement; implementation | &gt;$25K | Enterprise; negotiation |
| **Marketing-led (MLG)** | Content, SEO, paid drive awareness; market education | Varies | Demand gen focus |
| **Hybrid** | PLG for acquisition; sales for expansion | Common | Self-serve → sales handoff |

**Decision factors**: ACV, product complexity, buyer profile, how customers want to buy. Target LTV:CAC ≥3:1; CAC payback &lt;12 months.

## 90-Day Execution Framework

| Phase | Weeks | Focus |
|-------|-------|-------|
| **Market analysis** | 1–3 | Validate demand; competitive landscape; TAM; buying signals |
| **Strategy design** | 4–6 | ICP, personas; positioning; pricing; GTM mode; channels |
| **Execution build** | 7–9 | Messaging, content, sales playbook; tech stack |
| **Launch & iterate** | 10–12 | Go live; measure; iterate |

**Key**: Connect plan to real buying activity within 90 days—not disconnected strategy documents.

## ICP vs Buyer Persona

| Type | Level | Defines |
|------|-------|---------|
| **ICP** | Company | Which organizations deliver best unit economics; firmographics (industry, size, revenue), technographics, problem intensity |
| **Buyer persona** | Individual | Decision-makers within target companies; roles, goals, pain points, objections, preferred channels |

**ICP impact**: Companies with clearly defined ICPs see higher conversion rates and lower CAC. Include negative profiles (explicit disqualifiers) to protect pipeline quality.

## Market Analysis

| Element | Purpose |
|---------|---------|
| **TAM** | Total addressable market; named account lists; primary TAM, serviceable TAM, accounts with buying signals |
| **Competitive landscape** | Customer bases, strengths, weaknesses, positioning claims |
| **Buying patterns** | Replace assumptions with data; customer pain points; decision criteria |

## Enterprise / High-ACV Challenges

| Challenge | Mitigation |
|-----------|------------|
| **Customization** | Product modularity; professional services; clear scope |
| **Data security / private deployment** | On-prem or private cloud; compliance; security certifications |
| **Procurement cycles** | Multi-stakeholder alignment; champion building; long sales cycles |
| **Buy vs SaaS** | Total cost of ownership; flexibility; ongoing value |

**Use**: When GTM targets enterprise or high-ACV—expect longer cycles, procurement, and security requirements.

## New Market Entry

~70% of international market entries fail within two years—often from overestimating demand, underestimating execution, spreading resources thin.

| Entry model | Trade-off |
|-------------|-----------|
| **Organic expansion** | High control; slower; capital-intensive |
| **Strategic partnerships** | Faster access; shared risk; reduced control |
| **M&A / Acquisition** | Immediate presence; high integration risk |
| **Asset-light** (EOR, outsourcing) | Fastest; minimal upfront; market testing |
| **Pilot testing** | Lowest commitment; validation |

**Critical**: Domestic playbook won't transfer. Buying behaviors vary (self-service US vs consultation-heavy Europe vs relationship-driven APAC); competitive landscapes shift; regulatory complexity multiplies (GDPR, data localization).

## Repositioning

**Repositioning** = Strategic shift in who you serve, what problem you solve, where you play. **Rebranding** = Visual/verbal expression (logo, voice). Repositioning ≠ rebrand.

| When to reposition | Avoid |
|--------------------|-------|
| Moving upmarket (SMB → enterprise) | Quick fix for missed quarters |
| New geography with different dynamics | Leadership boredom |
| ICP fundamentally changed | |
| Major pivot, launch, or acquisition | |

**Success factors**: Research-driven (customer discovery, market analysis); cross-functional alignment (sales, marketing, product, clinical); sharp differentiation.

## Cross-Functional Alignment

- **RACI**: Responsible, Accountable, Consulted, Informed—clarify roles across teams
- **Shared timelines, tools, accountability**
- **Consistent messaging** across all channels

## Output Format

- **Scenario** (product launch, new market, repositioning, feature)
- **GTM mode** (PLG/SLG/MLG/Hybrid) recommendation
- **90-day** phase plan
- **ICP** and **persona** (from the product marketing context when present)
- **Market analysis** checklist
- **Launch** execution → see **product-launch**

## 12-Month Marketing Plan (AARRR)

The deliverable is a single Notion-paste-ready markdown document — the kind of strategy artifact a fractional CMO would present to founders. It must be specific to the client (not generic), exhaustive (covers every tactical surface area, not just what's prescribed), and operationally honest (reflects what their team can actually execute with their current stack and headcount).

Scope: a whole-funnel plan. For a single channel's execution doc, hand off to that channel's guide (`email-marketing`, `paid-ads-strategy`, `seo-audit`, `onboarding`, …); for ideas without a plan, use `marketing-ideas`.

### Invocation

The task names a client or domain (e.g. `quietude.app`, `acme-saas`); ask for one if it doesn't.

On invocation, read `~/marketing-plans/{client-slug}/progress.md` and resume based on the state machine documented in `references/methodology.md` Step 1.1.2 (fresh → INIT → REVIEW → FINALIZE → finalized). Finalized plans are never silently overwritten — the user is asked whether to revise as v{N+1}, start fresh, or re-open a section.

**Path safety.** Build `{client-slug}` only by slugifying the client name to lowercase `[a-z0-9-]` (strip everything else); reject `..`, `/`, and absolute paths, and never read or write outside `~/marketing-plans/`. On a shared machine this keeps one client's plan — and their data — from leaking into another client's context.

### The three phases

The full workflow lives in `references/methodology.md`. Quick summary:

#### Phase 1 — INIT (research + intake)

Read all available materials about the client. Pull data from any wired tools (Ahrefs, GA4 MCP, Stripe MCP, etc.). Run the ten-topic intake in `references/methodology.md` Step 1.4 for every gap the materials leave. Save to `research.md`.

Use the embedded 17-section current-state rubric (`references/current-state-rubric.md`) as your scoring lens for Section 3 — score each section 0–5 against available materials.

#### Phase 2 — REVIEW (walk through each of 13 sections interactively)

Present each section's draft in chat. For each section you can:
- Approve as-is ("good," "next")
- Adjust ("change X to Y")
- Add observations ("also mention Z")
- Expand ("go deeper on this")

Save each confirmed section to the progress file as you go. The workflow is resumable — invoking it again for the same client picks up at the next unfinished section.

#### Phase 3 — FINALIZE (compile + verify + publish)

Compile all 13 sections into `final_plan.md`. Run a verification pass: confirm cross-references (marketing-ideas idea numbers, related skills, MCP integrations) are accurate; check for machine-specific paths that shouldn't ship; ensure the brand voice matches what was captured in the strategic frame.

Optionally offer to publish to a shared GitHub repo (e.g., `{client-org}/{client-context}/marketing/plan.md`) if the user wants to share it with the team.

### The 13-section plan structure

Full template lives in `references/plan-template.md`. The structure:

1. **Executive summary** — 3 big bets, 90-day priorities, 12-month outcome. Written so it can be lifted into an investor or board update.
2. **Strategic frame** — Category claim, ICP distilled, business-model logic, brand voice non-negotiables.
3. **Current state** — Team, budget, what's done, what's in-flight, what's stuck. Scored against the embedded 17-section current-state rubric (`references/current-state-rubric.md`).
4. **Acquisition** — How strangers become aware. Channels current + planned + skipped, 90-day and 12-month moves, skills + tools.
5. **Activation** — How a new user has an experience that converts. Onboarding, first session, App Store / signup, paywall, lifecycle setup.
6. **Retention** — How a converted user stays and deepens. Lifecycle flows, churn prevention, win-back, support-as-marketing.
7. **Referral** — How retained users bring more users. Ambassador / affiliate / Guides / WOM mechanics.
8. **Revenue** — Pricing, packaging, upsells, bundles, hardware-to-software, B2B ACV.
9. **90-day roadmap** — Weeks 1–2 (Unblock), 3–4 (Foundation), 5–8 (Velocity), 9–12 (Compound). AARRR-tagged, owner-assigned.
10. **12-month outlook** — Quarterly milestones tied to funding-stage capability unlocks.
11. **Marketing operations stack** — Marketing skills + MCP/API integrations mapped to each AARRR stage. Capability unlocks by funding stage.
12. **Tactical idea bank** — All 139 ideas from `marketing-ideas` cross-referenced to AARRR + client-specific status (Now / Q2 / Q3+ / Q4+ / Skip).
13. **Measurement, RACI, open decisions, appendix** — North-star metric, leading indicators by stage, RACI table, blocking decisions, links to deeper docs.

### The AARRR framing

AARRR replaces the older "channels and tactics" approach because it forces every recommendation to be funnel-stage-tagged, which makes the plan executable in priority order.

Full primer in `references/aarrr-framework.md`. Quick rule:

- **Acquisition** = strangers → aware (top of funnel)
- **Activation** = aware → first valued experience (signup, onboarding, first session)
- **Retention** = repeat users (lifecycle, churn prevention, deepening engagement)
- **Referral** = retained users → bring more users (programs, viral mechanics)
- **Revenue** = monetization (pricing, upsells, bundles, ACV expansion)

Brand and content are **cross-cutting**, not their own AARRR stage — they serve every stage.

When the plan defines stage metrics, every rate divides matching closed
windows: an activation rate counts only cohorts whose observation window has
ended (a trial still inside its window is pending, not failed — keep it out of
the denominator and label it pending).

### Marketing as investing — the north-star framing

AARRR gives the plan its *structure*. This gives it its *spine*. Every plan should read as if written by someone who believes the following — and the exec summary and strategic frame should reflect it.

Adapted from *Founding Marketing* by Corey Haines (Ch. 1).

- **Marketing is like investing.** Treat the plan as a **compounding portfolio**, not a campaign calendar. Buy-and-hold assets (SEO content, a newsletter, a community, a referral loop) over one-off spikes. Diversify — no single channel carries the plan. Time in market beats timing the market.
- **No silver bullets, a hundred golden pellets.** There is no one move that fixes growth. The plan wins by stacking many small compounding assets. Be suspicious of any recommendation that promises to be *the* thing.
- **One asset, many returns.** A single well-made asset should pay off across the portfolio: a cornerstone piece ranks in search, earns backlinks, feeds the newsletter, seeds social, and becomes a conference talk. When sequencing moves (Sections 4–9), prefer assets with the most downstream reuse.
- **Audition, not an auction.** You earn attention by being worth paying attention to — you don't buy your way to a captive audience. Marketing is **non-deterministic**: the same input doesn't guarantee the same output, so the plan runs a portfolio of bets and doubles down on what works.
- **Hope is not a strategy.** Every move in the plan names its mechanism and its leading indicator. "Post more and hope it works" is not a line item. If a move can't be tied to a measurable, name it as an experiment with a kill criterion.

#### The market-quality gate — problem size × frequency

Before planning *how* to market, sanity-check *what* is being marketed. Score the core problem the product solves on two axes:

- **Size** — how painful/valuable is the problem when it occurs? (small → large)
- **Frequency** — how often does the customer feel it? (rare → constant)

|  | **Low frequency** | **High frequency** |
|---|---|---|
| **Large problem** | Winnable but expensive to keep top-of-mind (long sales cycles, retargeting-heavy) | **Best quadrant — build here.** Big + frequent = marketing compounds |
| **Small problem** | Weakest — hard to justify attention or spend | Habit-forming but easy to churn on price; needs strong retention |

Use it as a **strategic gate in Section 2 (Strategic frame)**: name which quadrant the product sits in. Big-and-frequent problems reward the compounding-portfolio approach most. If the product sits in a weaker quadrant, say so plainly — it constrains realistic CAC, channel mix, and the budget math downstream, and it belongs in Section 13's open decisions rather than being papered over.

When the gate raises "is this market big enough?", size it with `references/market-sizing.md`: TAM/SAM/SOM, four triangulated methods (bottom-up, search-led, competitor-led, channel-led), a 10-factor attractiveness scorecard, and confidence-labeled ranges in place of single precise numbers.

### The current-state rubric

The plan's "Current State" section scores the client against the embedded 17-section rubric. Full rubric in `references/current-state-rubric.md` — it's the source of truth, not a derivative of any external skill.

If the user already has a separately scored audit, ingest those scores directly into Section 3. Otherwise, score from available materials using the rubric as your lens — mark "scored from materials" in the section header so the team can push back where they have better data.

### Cross-references — skills this plan integrates with

1. **`marketing-ideas`** — 139 proven marketing tactics. Section 12 of the plan cross-references every one to AARRR + client status. Detail in `references/idea-cross-reference.md`.
2. **`product-marketing`** — Creates the product marketing context (positioning, ICP, voice) that Section 2 (Strategic frame) builds on. If it's missing, offer to run it before INIT.
3. **AARRR-stage-specific skills** — `onboarding`, `signup`, `email-marketing`, `referral-program`, `pricing-strategy`, etc. The "Marketing operations stack" (Section 11) maps these to AARRR stages.

The plan is **opinionated about which skills serve which stages.** Full mapping in `references/ops-stack-mapping.md`.

### The marketing operations stack

This is the differentiator of an fCMO-style plan vs. a generic marketing plan. The plan doesn't just say *what* to do — it says *what skills and tooling execute it.*

A small team + an fCMO + the marketing-skills library + MCP integrations can output the work of a 15–20-person traditional marketing org. The plan must show this stack explicitly, AARRR-stage by AARRR-stage.

Full mapping in `references/ops-stack-mapping.md`.

### Funding-stage capability unlocks

Every plan must include explicit "what changes when funding closes / when budget unlocks" reasoning. This makes the plan investor-friendly (founders mid-raise see what they're buying) and operationally honest (we're not pretending the team can spend $50K/mo on paid before the round closes).

Standard tiers in `references/funding-stage-unlocks.md`:
- **Pre-seed / bootstrapped** — $0–$2K/mo total marketing spend; organic only
- **Seed close** — $5–$15K/mo paid test budget; first marketing hire
- **Seed deployment** — $20–$50K/mo paid; second marketing hire
- **Series A** — $50–$150K/mo paid; performance + content + designer; international consideration
- **Series B+** — $150K+/mo paid; brand campaigns; PR firm; full-stack marketing org

Use these as anchors. Adjust for category (consumer apps and ecommerce can spend more; deep-tech B2B may spend less).

### Setting the budget scientifically

The funding-stage anchors above tell you *what's in the ballpark*. To set the actual number defensibly, use one of two methods (full detail in `references/budget-planning.md`):

1. **Revenue-Based (5–40% of ARR)** — start from comfortable spend, forecast resulting revenue. Best when historical CAC data exists.
2. **Goal-Based** — reverse-engineer the budget from the revenue target via the four-step formula in `references/budget-planning.md` (retained base → ARR gap → retained new customers → CAC). Best for fundraising or when the goal is fixed.

Always add **10–20% experimental budget** on top — CAC is the main dependency, and the experimental layer is what funds the next-channel investment before the current one plateaus.

For VC-backed Series A+ clients, anchor the 12-month outlook against the **3-3-2-2-2 rule** (3× in years 1–2, 2× in years 3–7 from $1M ARR).

### Growth patterns — the real shape of SaaS growth

Pitch decks show hockey sticks. Real growth is a series of S-curves with plateaus between them. Full framework in `references/growth-patterns.md`. Key implications for the plan:

- **Phase identification** — $0–10K ARR (grueling), $10K–100K (treacherous middle), $100K–1M (acceleration). Section 3 names the current phase; Section 10 sequences the next.
- **Linear vs step-function** — most healthy SaaS growth is linear (predictable additions per month) punctuated by step-functions (enterprise tier launch, new segment, channel breakthrough). The plan should describe both honestly — not promise exponential.
- **S-curve layering** — Channel × Product × Market. Start the next S-curve while the current one is still growing. Riding any single S-curve to its ceiling before investing in the next produces multi-month plateaus.
- **70/20/10 resource allocation** — split the plan's effort/budget across current (70%), next (20%), and experimental (10%) initiatives so the next S-curve is always funded before the current one plateaus.
- **Weekly tracking cadence** — review leading indicators weekly and watch for S-curve plateau signals; a flattening curve is the trigger to shift weight toward the next one, not a reason to push harder on the current.

### Team and agency model

Strategy lives in-house. Execution can — and often should — be outsourced. Full framework in `references/team-and-agency-model.md`. Three implications for every plan:

1. **First hire is a strategist, not a tactician.** Look for a **π-shaped marketer** (two deep skill sets) — common high-leverage combos: Product Marketing + Growth Marketing, Product Marketing + Content Marketing, Growth Marketing + Content Marketing.
2. **Title conservatively.** First marketing hire is almost always Manager or Lead, not VP or CMO. Inflated titles paint the org into a corner when you scale.
3. **Use contractors and small niche agencies for execution.** Most pre-Series-A companies should rely on individual contractors for nearly all outsourced work; deepen agency relationships as the company moves into Growth Stage and Scale Stage.

### What every plan must customize

A generic plan is a failed plan. Every plan must explicitly customize for:

1. **Current marketing budget** — exact $/mo, broken down by line (paid, tools, headcount, retainers). Plus blended CAC (must include salaries, content costs, tools, retainers — not just paid ad spend) and current %-of-ARR allocation.
2. **Unit economics** — ARPC, annual retention rate, LTV. These feed the budget math in Section 8 and Section 10.
3. **Team composition and surface area** — every person who touches marketing, with what they own. Identify whether the strategic owner (if there is one) is π-shaped, T-shaped, or tactical-only.
4. **What the client is currently doing** — by channel, with status (working / not / TBD).
5. **What they've already done that should be acknowledged** — past launches, PR moments, content, partnerships. Don't write a plan that ignores work they're proud of.
6. **Phase of SaaS growth** — $0–10K ARR / $10K–100K / $100K–1M / $1M+. Each phase has its own binding constraint.
7. **Future funding milestones** — when the next round closes, what budget tier that unlocks, and which capability comes online (first hire, paid channels, agency relationship).
8. **The marketing skills mapped to specific moves** — every move in the AARRR sections names the skill that executes it.
9. **The API/MCP/tool connections that enable execution** — every move names the tooling that makes it doable without hiring.

If you can't confirm any of these in INIT, list them in Section 13's "Open decisions" — never gloss over them. **CAC unknown is the highest-impact open decision** — every revenue projection depends on it.

### Common client-type variations

Plan structure stays consistent. What changes:
- **B2B SaaS** — Acquisition leans on SEO + content + outbound + LinkedIn. Activation = signup + product trial. Retention = product engagement + CSM motion. Referral = customer advocacy. Revenue = expansion / NRR.
- **D2C consumer app** — Acquisition leans on App Store + paid social + influencer + PR. Activation = onboarding + first session + paywall. Retention = lifecycle email + push. Referral = sharing mechanics. Revenue = subscription + upsell.
- **Hardware-led** — Acquisition leans on PR + retail + Amazon + Shopify SEO. Activation = unboxing + setup + first use. Retention = software companion + community. Referral = gifting + reviews. Revenue = blended LTV hardware + accessories + subscription.
- **Marketplace** — Activation has two sides (supply + demand). Retention is repeat transaction frequency. Revenue is take-rate × GMV.
- **Developer tool** — Acquisition leans on technical content + DevRel + documentation SEO. Activation = first build / first integration. Retention = depth of integration. Referral = team adoption.

Detail in `references/client-types.md`.

### Quality bar

What separates a good plan from a generic one:

**Good plan signals:**
- Every move names the AARRR stage it serves
- Every recommendation is anchored in real client data (their actual budget, their actual team, their actual current channels)
- The 90-day roadmap has owners, not just actions
- The funding-stage section explains what changes when the next round closes
- The ops stack section names specific skills + MCPs per move
- The idea bank shows what we're *not* doing and why (skipped ideas with rationale)
- The exec summary can stand alone — could be lifted into an investor update
- Open decisions are explicit, not glossed over

**Failure modes to avoid:**
- Listing tactics without sequencing
- Recommending things the team can't execute at current size
- Pretending paid budget exists before the round closes
- Glossing over uncomfortable metrics (e.g., churn) instead of naming them as open decisions
- Generic language ("build a community," "improve SEO") without specific moves
- Ignoring brand voice — every plan section must respect the client's voice rules
- Padding the plan with skills/ideas the client doesn't actually need
- Not acknowledging work the team has already done

### Output format

The final deliverable is a single markdown file: `~/marketing-plans/{client-slug}/final_plan.md`.

Headers (`## 1. Executive summary`, etc.) are H2 for clean Notion paste. Tables for any structured comparison (RACI, idea bank, ops stack). Status legend for the idea bank. Internal references to other sections use `§N` (e.g., "see §5 for Activation detail").

Length expectation: ~8,000–12,000 words for a comprehensive plan. Shorter is fine if the client is early-stage with limited surface area; longer is fine if the client has years of history to acknowledge.

### File layout per plan

The plan folder layout, the `progress.md` schema and the resumption decision tree live in `references/methodology.md` Steps 1.1, 1.1.1 and 1.1.2.

### How exhaustive should the plan be?

Default to comprehensive. Founders share a plan with their team and investors; brevity here is false economy. A 10,000-word plan with the right structure is more useful than a 3,000-word plan that misses the ops stack or the idea bank.

Keep every section **dense, not bloated**. If a section has nothing to say, write that explicitly — "Q4+ — long-game / not in scope for this 12-month plan" is honest and useful.

### A note on tone

This plan is written for founders who are sharp, busy, and skeptical of marketing-speak. Direct claims, named tradeoffs, explicit assumptions. When unsure, name the open question rather than guessing.

The exec summary should be short enough to read in 60 seconds. The rest should reward deep reading.

## Related Skills

- **product-launch**: Launch execution; channels, timeline, checklist; implements GTM for product launch
- **pmf-strategy**: Validate PMF before scaling GTM
- **cold-start-strategy**: First users; differs from full GTM (0→1 vs commercialization)
- **rebranding-strategy**: Domain change, 301, announcement; when repositioning includes rebrand
- **localization-strategy**: New market entry; i18n, multilingual
- **paid-ads-strategy**: Ad channel for GTM
- **website-structure**: Pages needed for GTM
- **branding**: Positioning, differentiation; GTM messaging foundation
- **`product-marketing`** — Run first. Captures positioning, ICP and voice in the product marketing context so every section of the plan references the same foundation.
- **`marketing-ideas`** — Source of the 139 tactics in Section 12.
- **`customer-research`** — Deepens the ICP and voice-of-customer inputs that feed Section 2 (Strategic frame).
- **`onboarding`** — Deep work on Section 5 (Activation).
- **`email-marketing`** — Deep work on Section 6 (Retention) + onboarding emails in Section 5.
- **`referral-program`** — Deep work on Section 7 (Referral).
- **`pricing-strategy`** — Deep work on Section 8 (Revenue).
- **`seo-audit`** / **`generative-engine-optimization`** / **`programmatic-seo`** — Deep work on the SEO portion of Section 4 (Acquisition).
