---
name: product-marketing
description: "When the user wants to create or update the product marketing context: positioning, ICP, audience, objections, brand voice. Also use when the user mentions \"product marketing context,\" \"positioning,\" \"ICP,\" \"target audience,\" \"customer language,\" \"set up marketing context,\" \"define our positioning,\" \"brand voice,\" \"tone of voice,\" \"brand guidelines,\" \"what have we learned,\" or \"log this learning.\" Every other marketing guide reads this document."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: coreyhaines31/marketingskills
  based_on_version: v2.13.0(e85f3cb)
  based_on_skill: product-marketing
---

# Strategies: Product Marketing Context

Guides creating and maintaining the product marketing context document that other marketing guides read, so users don't repeat themselves.

The document is stored at `docs/marketing/product-marketing.md`.

## Initial Assessment

**Project context:** Read the product marketing context when present. Without it, use available project material or user-provided facts and ask for missing information.

Identify:
1. **Existing context**: check whether `docs/marketing/product-marketing.md` exists
2. **Mode**: create from scratch, or update specific sections
3. **Sources**: codebase, site, existing docs, or user answers

## Workflow

### Step 1: Check for Existing Context

First, check if `docs/marketing/product-marketing.md` already exists. Also check `.agents/product-marketing.md`, `.claude/product-marketing.md` and the legacy filename `product-marketing-context.md` (in either `.agents/` or `.claude/`) for older setups — if found anywhere other than `docs/marketing/product-marketing.md`, offer to move it to the canonical location.

**If it exists:**
- Read it and summarize what's captured — note its current **Document version** and the last few **Changelog** entries so the user sees where the doc stands and what's changed recently
- Ask which sections they want to update
- Only gather info for those sections
- On save, version it per Step 4

**If it doesn't exist, offer two options:**

1. **Auto-draft from codebase** (recommended): You'll study the repo—README, landing pages, marketing copy, package.json, etc.—and draft a V1 of the context document. The user then reviews, corrects, and fills gaps. This is faster than starting from scratch.

2. **Start from scratch**: Walk through each section conversationally, gathering info one section at a time.

Most users prefer option 1.

### Step 2: Gather Information

**If auto-drafting:**
1. Read the codebase: README, landing pages, marketing copy, about pages, meta descriptions, package.json, any existing docs
2. Draft all sections based on what you find
3. Present the draft and ask what needs correcting or is missing
4. Iterate until the user is satisfied

**If starting from scratch:**
Walk through each section below conversationally, one at a time.

For each section:
1. Briefly explain what you're capturing
2. Ask pointed questions ("What's the #1 frustration that brings them to you?", not "What problem do they solve?") and ask for examples
3. Summarize the section back and confirm it before moving to the next

Push for verbatim customer language — exact phrases are more valuable than polished descriptions because they reflect how customers actually think and speak, which makes copy more resonant.

---

## Sections to Capture

Skip sections that don't apply (e.g., Personas for B2C, Paid Ads if they don't run ads).

### 1. Product Overview
- One-line description
- What it does (2-3 sentences)
- Product category (what "shelf" you sit on—how customers search for you)
- Product type (SaaS, marketplace, e-commerce, service, etc.)
- Business model and pricing

### 2. Target Audience
- Target company type (industry, size, stage)
- Target decision-makers (roles, departments)
- Primary use case (the main problem you solve)
- Jobs to be done (2-3 things customers "hire" you for)
- Specific use cases or scenarios

### 3. Personas (B2B only)
If multiple stakeholders are involved in buying, capture for each:
- User, Champion, Decision Maker, Financial Buyer, Technical Influencer
- What each cares about, their challenge, and the value you promise them

### 4. Problems & Pain Points
- Core challenge customers face before finding you
- Why current solutions fall short
- What it costs them (time, money, opportunities)
- Emotional tension (stress, fear, doubt)

### 5. Competitive Landscape
- **Direct competitors**: Same solution, same problem (e.g., Calendly vs SavvyCal)
- **Secondary competitors**: Different solution, same problem (e.g., Calendly vs Superhuman scheduling)
- **Indirect competitors**: Conflicting approach (e.g., Calendly vs personal assistant)
- How each falls short for customers

### 6. Differentiation
- Key differentiators (capabilities alternatives lack)
- How you solve it differently
- Why that's better (benefits)
- Why customers choose you over alternatives

### 7. Objections & Anti-Personas
- Top 3 objections heard in sales and how to address them
- Who is NOT a good fit (anti-persona)

### 8. Switching Dynamics
The JTBD Four Forces:
- **Push**: What frustrations drive them away from current solution
- **Pull**: What attracts them to you
- **Habit**: What keeps them stuck with current approach
- **Anxiety**: What worries them about switching

### 9. Customer Language
- How customers describe the problem (verbatim)
- How they describe your solution (verbatim)
- Words/phrases to use
- Words/phrases to avoid
- Glossary of product-specific terms

### 10. Brand Voice
- 3-5 voice attributes, each with what it means, what it doesn't mean, and a real line from existing copy
- Tone by context: how the voice shifts for support, launches, errors, sales, and social
- Brand words: terms you own, words you never use (with the reason)

Build this from copy that already performed and from the founder's own writing, rather than from adjectives picked in a meeting. See [references/brand-voice.md](references/brand-voice.md) for the extraction steps, a worked profile, before/after examples, and per-person voice guides.

### 11. Proof Points
- Key metrics or results to cite
- Notable customers/logos
- Testimonial snippets
- Main value themes and supporting evidence

### 12. Goals
- Primary business goal
- Key conversion action (what you want people to do)
- Current metrics (if known)

### 13. Paid Ads (optional, only if they run ads)
The **paid-ads-strategy** guide reads this so the user doesn't re-explain the account every session.
- Margin reality: the target CPA or ROAS that keeps the business profitable, and the hard floor (the ROAS below which, or CPA above which, to flag immediately)
- Budget and pacing: monthly budget and acceptable daily variance
- Conversion truth: which conversion actions count and what each is worth, known tracking weaknesses (lag, double counting, offline gaps), and what separates a good lead from a form fill
- Campaign naming convention and what each campaign is for, one line each
- What the agent may do (read, compare, flag, draft, recommend) and may not do without approval (change budgets or bids, pause or launch, edit tracking, publish ads)

### 14. Learnings
Start this empty. It fills up as work ships (see "Maintaining Learnings" below).

---

## Step 3: Create the Document

After gathering information, create `docs/marketing/product-marketing.md` with this structure:

```markdown
# Product Marketing Context

**Document version:** v1
**Last updated:** [date]

## Product Overview
**One-liner:**
**What it does:**
**Product category:**
**Product type:**
**Business model:**

## Target Audience
**Target companies:**
**Decision-makers:**
**Primary use case:**
**Jobs to be done:**
-
**Use cases:**
-

## Personas
| Persona | Cares about | Challenge | Value we promise |
|---------|-------------|-----------|------------------|
| | | | |

## Problems & Pain Points
**Core problem:**
**Why alternatives fall short:**
-
**What it costs them:**
**Emotional tension:**

## Competitive Landscape
**Direct:** [Competitor] — falls short because...
**Secondary:** [Approach] — falls short because...
**Indirect:** [Alternative] — falls short because...

## Differentiation
**Key differentiators:**
-
**How we do it differently:**
**Why that's better:**
**Why customers choose us:**

## Objections
| Objection | Response |
|-----------|----------|
| | |

**Anti-persona:**

## Switching Dynamics
**Push:**
**Pull:**
**Habit:**
**Anxiety:**

## Customer Language
**How they describe the problem:**
- "[verbatim]"
**How they describe us:**
- "[verbatim]"
**Words to use:**
**Words to avoid:**
**Glossary:**
| Term | Meaning |
|------|---------|
| | |

## Brand Voice
| Attribute | Means | Doesn't mean | Example line |
|-----------|-------|--------------|--------------|
| | | | |

**Tone by context:**
- Support:
- Launch:
- Errors:
- Sales:
- Social:
**Terms we own:**
**Never use (and why):**

## Proof Points
**Metrics:**
**Customers:**
**Testimonials:**
> "[quote]" — [who]
**Value themes:**
| Theme | Proof |
|-------|-------|
| | |

## Goals
**Business goal:**
**Conversion action:**
**Current metrics:**

## Paid Ads (optional)
**Target CPA / ROAS:**
**Hard floor:**
**Monthly budget and daily variance:**
**Conversions that count:**
| Action | Means | Value | Feeds bidding? |
|--------|-------|-------|----------------|
| | | | |
**Known tracking weaknesses:**
**Good lead vs. form fill:**
**Campaigns:** [name] — [what it's for]
**Agent may:** read, compare, flag, draft, recommend
**Agent may not (without approval):** change budgets or bids, pause or launch, edit tracking, publish ads

## Learnings
*Decisions and tested lessons. Newest first. Keep it to about 20 active entries.*
| Date | Learning | Evidence | Applies to | Status |
|------|----------|----------|------------|--------|
| | | | | |

## Changelog
*Newest first. One line per revision: what changed and why.*
- v1 ([date]) — Initial context.
```

---

## Step 4: Confirm, Version, and Save

- Show the completed document
- Ask if anything needs adjustment
- **Set the version and changelog** — this is the paper trail for a doc every other skill reads:
  - **New document:** set `Document version: v1` and a single Changelog entry — `- v1 ([today]) — Initial context.`
  - **Updating an existing document:** increment the version (v2 → v3 …), update `Last updated` to today, and **prepend a new Changelog entry** at the top of the list (newest first) summarizing *what changed and why* in one line. Past entries stay exactly as written.
  - A good entry names the sections touched and the reason, not "updated the doc." Examples:
    - `- v3 (2026-07-16) — Repositioned from "email tool" to "deliverability platform"; added RevOps to the ICP.`
    - `- v2 (2026-06-02) — Rewrote value prop and objections after 5 customer interviews; added competitor Acme.`
  - Use today's date in ISO form (YYYY-MM-DD) for the entry and `Last updated`.
  - **Pure typo-only fix:** save the correction with no version bump or entry. Every other change bumps the version and gets an entry. When the change is a real repositioning, say so plainly — downstream skills will now generate against the new context.
- Save to `docs/marketing/product-marketing.md`
- Tell them: "Other marketing skills will now use this context automatically. The Changelog at the bottom tracks every revision — check it to see how your positioning has evolved. Run `/marketing product-marketing` anytime to update it."

## Maintaining Learnings

The Changelog records how the document changed. **Learnings** records what the team found out by shipping: which angles won, which offers flopped, which decisions were made and why. Drafting guides (copywriting, email-marketing, paid-ads-strategy, ad-creative, social) read it before writing so the next brief starts from what's already known.

**Entry format:** one row per learning.
- **Learning:** one sentence, specific enough to change a draft. "Price-anchored headlines beat outcome headlines on the pricing page" works. "Be clearer" doesn't.
- **Evidence:** the test, campaign, or source, with the number and sample size. "Variant B +18% trial starts, 2,400 visitors per arm, 3 weeks."
- **Applies to:** the channels, segments, or guides it affects.
- **Status:** `active`, `watch` (one data point, worth retesting), or `retired`.

**What earns a place:**
- A test result that reached its planned sample, or the same pattern seen in two or more campaigns
- A decision the user made with a reason (positioning, pricing, a channel cut) that future drafts must respect
- A correction the user gave more than once ("never call it a platform")

**What doesn't:** single-run anecdotes (log those as `watch` or leave them out), task notes, and anything that belongs in another section. A new objection goes in Objections; a new customer phrase goes in Customer Language.

**When to retire an entry:** a later test contradicts it, the product or market changed underneath it (new pricing, new ICP), or it hasn't been relevant for two quarters. Change the status to `retired` and add a line saying why, rather than deleting it, so nobody re-tests a settled question. Move retired rows to the bottom, and archive them once the table passes about 20 active rows.

**Who writes it:** any guide that finishes a test, campaign, or postmortem may propose a row. Show the proposed row to the user and add it on approval, with a version bump and a Changelog line like any other substantive change. Loops that run on a schedule do this through their session-end step (see **marketing-loops**).

## Related Skills

- **customer-research**: Interviews, surveys, and reviews that feed the context
- **competitor-research**: Competitor profiles for the Competitive Landscape section
- **branding**: Brand voice and positioning beyond this document
- **copywriting**: Copy that uses the captured customer language
