---
name: copywriting
description: When the user wants to write or optimize short-form marketing copy—headlines, CTAs, ad copy, landing page copy, email copy. Also use when the user mentions "copywriting," "headline," "CTA copy," "ad copy," "landing page copy," "sales copy," "conversion copy," "PAS," "AIDA," "BAB," "copy formula," or "differentiation." For long-form article bodies (blog posts, guides), use article-content. Diagnoses the input first (blank brief, real voice, or point edit) and changes only what it calls for.
metadata:
  version: 1.0.0
  based_on_repo: kostja94/marketing-skills, coreyhaines31/marketingskills
  based_on_version: v1.0.0(8dd89c5), v2.13.0(e85f3cb)
  based_on_skill: copywriting, copywriting
---

# Content: Copywriting

Guides **short-form marketing copy**—ads, landing pages, email, CTAs. Copywriting frameworks (PAS, AIDA, BAB) provide structure for conversion-focused copy. For **article body content** (blog posts, guides, long-form), see **article-content**.

## Initial Assessment

**Project context:** Read the product marketing context when present. Without it, use available project material or user-provided facts and ask for missing information.
Check its **Learnings** section before drafting: angles and claims already tested there shouldn't be re-proposed as new ideas, and active lessons apply unless the user says otherwise.

Identify:
1. **Context**: Ad, landing page, email, CTA, or general
2. **Goal**: Awareness, consideration, conversion, retention
3. **Audience**: ICP, stage, pain points

For page copy, also gather (take what the product marketing context already covers and ask only for the rest):

### 1. Page Purpose
- What type of page? (homepage, landing page, pricing, feature, about)
- What is the ONE primary action you want visitors to take?

### 2. Audience
- Who is the ideal customer?
- What problem are they trying to solve?
- What objections or hesitations do they have?
- What language do they use to describe their problem?

### 3. Product/Offer
- What are you selling or offering?
- What makes it different from alternatives?
- What's the key transformation or outcome?
- Any proof points (numbers, testimonials, case studies)?

### 4. Context
- Where is traffic coming from? (ads, organic, email)
- What do visitors already know before arriving?

## Copywriting Frameworks

| Framework | Structure | Best For |
|-----------|-----------|----------|
| **PAS** | Problem → Agitation → Solution | Direct-response; sales pages; landing pages |
| **AIDA** | Attention → Interest → Desire → Action | Story-driven; ads; emails; editorials |
| **BAB** | Before (problem) → After (outcome) → Bridge (how) | Transformation; testimonials; case studies |
| **FAB** | Features → Advantages → Benefits | Product pages; feature lists |
| **4 U's** | Useful, Urgent, Unique, Ultra-specific | Headlines; subject lines |

### PAS (Problem, Agitation, Solution)

- **Problem**: Identify the reader's pain point clearly
- **Agitation**: Intensify the emotional impact; make the problem feel urgent
- **Solution**: Present your product/service as the answer

### AIDA (Attention, Interest, Desire, Action)

- **Attention**: Grab with a powerful headline or opening
- **Interest**: Build engagement through facts, storytelling, or emotional appeals
- **Desire**: Highlight benefits and how the product solves problems
- **Action**: Include a clear call-to-action

### BAB (Before, After, Bridge)

- **Before**: Current problem state
- **After**: Desired outcome
- **Bridge**: How your solution bridges the gap

## Headline Formulas

| Formula | Example |
|---------|---------|
| **How to [outcome]** | "How to Double Your Conversions in 30 Days" |
| **[Number] Ways to [benefit]** | "7 Ways to Reduce Churn Without Hiring" |
| **[Who] + [benefit]** | "For Marketers Who Want to Ship Faster" |
| **[Problem]? Here's [solution]** | "Struggling with SEO? Here's the Fix" |
| **[Before] → [After]** | "From 0 to 10K Users in 90 Days" |
| **The [adjective] [noun] for [audience]** | "The Ultimate Guide for SaaS Founders" |

**Rules**: Front-load keywords; keep under 60 chars for SERP; avoid clickbait; match ad-to-page alignment.

**Information gain (differentiation)**: Copy that restates what competitors say adds zero value. Lead with unique angle, proprietary data, or contrarian insight. "What does this headline/promise add that others don't?" See **article-content** for full information gain strategy in long-form.

## Diagnose the Situation First

Before drafting, decide which of three situations you're in. Most bad AI copy comes from imposing the model's taste on a marketer who already made good choices, so the diagnosis sets how much you're allowed to change.

| Situation | What you were given | Your job |
|---|---|---|
| **A. Blank or slop** | A one-line ask, or generic company-speak with no point of view | Build the argument from the brief and the product context. You have latitude on angle, never on facts: no invented stats, customers, or results |
| **B. Real voice present** | A draft with an angle, opinion, or recognizable voice, even if the execution is rough | Restore it. Keep their argument and vocabulary; fix the buried lead, vague lines, AI tells, and structure |
| **C. Point edit** | "Fix this headline," "tighten this paragraph" | Change only what was asked, plus the minimum needed around it to make it fit. Return the rest untouched |

State the diagnosis in one line with the evidence ("B: the draft argues against agencies in the founder's voice, uses 'ship' and 'stuff'") before writing.

**Read taste out of the input (B and C).** What they gave you is evidence of their judgment:
- **Vocabulary is a voice choice.** If they write "stuff" and "ship," don't upgrade to "solutions" and "deploy."
- **Where they spent words is a priority choice.** Keep the emphasis.
- **What they left out is a scope choice.** Don't add sections they didn't ask for.
- **Their angle is the positioning.** Deepen it; don't replace it with one you like better.

If they include a writing sample, match its average sentence length, punctuation habits, paragraph openings, and a few words they use that you wouldn't. A sample beats the default voice when the two conflict.

## Drafting Protocol

**Decompose and lock.** Don't write the page in one pass. Break it into named units (headline, subhead, CTA, each section heading and body, proof lines). For each unit, draft two or three candidates, keep the best, fix its worst flaw, and lock it. Assemble and read the whole page once for flow. In Situation B, lines that already work are locked from the start.

**The three-question gate.** Run every line you write or keep through three questions:
1. **Can the reader picture it?** A specific image, scene, or object beats an abstraction.
2. **Can it be proven true or false?** A falsifiable claim is a claim; "best-in-class" is decoration.
3. **Could a competitor write this exact sentence?** If yes, it fails (the swap test).

Three passes, keep it. Two, sharpen the weak one. One or none, rewrite it from the facts or flag what's missing with `[NEED: ...]`.

**Ration the punch.** Most lines should be plain, specific, and declarative. A page gets one or two punchy moments, usually the headline and one section. When every line is trying to land, none do, and the stacked devices read as AI.

**The leave-it-alone test.** Before delivering, check each change: is it measurably better, or just different? Revert changes you can't give a reason for. This matters most in Situations B and C.

*Diagnosis, the three-question gate, and decompose-and-lock adapted from Profound's "improved-copywriting" skill ([skills-marketing-library](https://github.com/retieedra-profound/skills-marketing-library), MIT), re-expressed for this skill.*

## Copywriting Principles

### Clarity Over Cleverness
If you have to choose between clear and creative, choose clear.

**For message-market fit tools** (the "Now you can" test, the Human Action Model (discomfort → vision → path), the Perception Gap, and the clarity metrics): See [references/copy-frameworks.md](references/copy-frameworks.md#clarity--message-market-fit)

### Benefits Over Features
Features: What it does. Benefits: What that means for the customer.

### Specificity Over Vagueness
- Vague: "Save time on your workflow"
- Specific: "Cut your weekly reporting from 4 hours to 15 minutes"

### Customer Language Over Company Language
Use words your customers use. Mirror voice-of-customer from reviews, interviews, support tickets.

### One Idea Per Section
Each section should advance one argument. Build a logical flow down the page.

### Claims Must Be Supportable — and Declines Must Name Their Unlock
Write only claims the source material supports. When a requested claim
isn't supported, flag it in your output: name the claim, say why it falls short, offer the closest supportable alternative, and state
exactly what evidence would unlock the original — a customer-review export,
a written guarantee policy, a certification, a citable study or dataset.
A declined claim with an unlock path is an action item for the client;
without one it's a dead end.

## Writing Style Rules

### Core Principles

1. **Simple over complex**: "Use" not "utilize," "help" not "facilitate"
2. **Active over passive**: "We generate reports" not "Reports are generated"
3. **Confident over qualified**: Remove "almost," "very," "really"
4. **Show over tell**: Describe the outcome instead of using adverbs

### Quick Quality Check

- Any AI tells? (see No AI Tells below)
- Jargon that could confuse outsiders?
- Sentences trying to do too much?
- Passive voice constructions?
- Exclamation points? (remove them)
- Marketing buzzwords without substance?

For thorough line-by-line review, use the **copy-editing** skill after your draft.

**For long-form copy that needs signposting between sections**: See [references/natural-transitions.md](references/natural-transitions.md)

## No AI Tells

Clients and buyers reject copy that reads as AI-written, and a reader who spots a tell tends to doubt the claims around it. Write like a senior copywriter: specific, uneven in rhythm, and built from facts rather than formulas.

### Never write these

1. **Contrast reveals.** "It's not X, it's Y." "Not because X. Because Y." "Not just X, but Y." State Y directly, with the reason.
2. **Negation lists.** "No setup call, no templates, no waiting on IT. No contract." Say what does happen. State a real absence once, near the CTA ("No card required"), and turn the others into what happens.
3. **Trailing pile-ons.** A full claim followed by a comma and more clauses: "...the data you already have, no exports, no spreadsheets, no second copy." End the sentence at the claim.
4. **Self-answered questions and colon reveals.** "The result? 3x faster." "The best part: it learns." Just say it. FAQ questions and a reader's own question ("Need to share a screenshot?") are fine.
5. **Stock openers and phrases.** "In today's fast-paced world," "Whether you're X or Y," "Here's the thing," "Say goodbye to," "X, reimagined," "Unlock the power of," "Take it to the next level."
6. **Em dashes in short copy.** Headlines, subheads, ads, social posts, and subject lines use none.

### Keep these rare

- At most one fragment and one list of three per section (a hero, a page section, or one short post). CTA microcopy and a real three-feature list are fine.
- Words like seamless, robust, powerful, unlock, and streamline: replace them with the fact they stand in for.
- Swap test: if a line would work unchanged on a competitor's site, rewrite it. If you lack the differentiator to fix it, flag `[NEED: differentiator]`.

### Check before delivering

Before handing over any draft, run the self-check in [references/ai-tells.md](references/ai-tells.md#the-self-check) (the full blacklist with examples and rewrites). Done when every self-check step passes. Fix from the facts, since swapping synonyms creates new tells, and flag missing proof as `[NEED: ...]` rather than inventing it.

Removing tells leaves copy clean but flat. For a full rewrite, build a writer first (who's writing, what they know cold, what they'd cut, what they think) and check for second-generation tells such as wisdom-shaped sentences and tidy closers. See [references/ai-tells.md](references/ai-tells.md#build-a-writer).

## Best Practices

### Be Direct
Get to the point. Don't bury the value in qualifications.

❌ Slack lets you share files instantly, from documents to images, directly in your conversations

✅ Need to share a screenshot? Send as many documents, images, and audio files as your heart desires.

### Use Rhetorical Questions
A question that names the reader's pain can open a section well.
- "Hate returning stuff to Amazon?"
- "Tired of chasing approvals?"

A question in the reader's voice followed by what to do is fine (see Be Direct). A question that labels your own claim ("The result? 3x faster.") is an AI tell.

### Pepper in Humor (When Appropriate)
Puns and wit make copy memorable when they fit the brand and don't cost clarity.

## Page Structure Framework

### Above the Fold

**Headline**
- Your single most important message
- Communicate core value proposition

**Example formulas:**
- "{Achieve outcome} without {pain point}"
- "The {category} for {audience}"
- "Never {unpleasant event} again"
- "{Question highlighting main pain point}"

**For comprehensive headline formulas**: See [references/copy-frameworks.md](references/copy-frameworks.md)

**Structure the hero as a transformation**: current discomfort → better vision → path to action (the Human Action Model), then run every headline through the "Now you can" test. See [references/copy-frameworks.md](references/copy-frameworks.md#clarity--message-market-fit)

**Subheadline**
- Expands on headline
- Adds specificity
- 1-2 sentences max

**Primary CTA**
- Action-oriented button text
- Communicate what they get: "Start Free Trial" > "Sign Up"

### Core Sections

| Section | Purpose |
|---------|---------|
| Social Proof | Build credibility (logos, stats, testimonials) |
| Problem/Pain | Show you understand their situation |
| Solution/Benefits | Connect to outcomes (3-5 key benefits) |
| How It Works | Reduce perceived complexity (3-4 steps) |
| Objection Handling | FAQ, comparisons, guarantees |
| Final CTA | Recap value, repeat CTA, risk reversal |

**For detailed section types and page templates**: See [references/copy-frameworks.md](references/copy-frameworks.md)

## Copy by Context

| Context | Focus | Skills |
|---------|-------|--------|
| **Ad copy** | Hook, benefit, CTA; platform limits | paid-ads-strategy, google-ads, meta-ads |
| **Landing page** | Headline, value prop, CTA; above fold | `implement/sub-skills/references/pages/marketing/landing-page.md`, `implement/sub-skills/references/components/branding/hero.md` |
| **Email** | Subject line, preview, body, CTA | email-marketing |
| **CTA** | Value-focused; action verb; avoid "Submit" | `implement/sub-skills/references/components/conversion/cta.md` |
| **Article / blog** | Headline formulas, CTA copy; body → **article-content** | article-content, `implement/sub-skills/references/pages/content/article.md` |

## Ad copy vs Landing page copy

| Element | Ad | Landing Page |
|---------|-----|--------------|
| **Promise** | Must match page headline | Same promise; expand on it |
| **Length** | Concise; platform limits | Enough to explain value |
| **CTA** | Click-through; "Learn More" | Conversion; "Start Free Trial" |

**Avoid**: Ad promise not visible on page; mismatch increases bounce.

## CTA Copy Best Practices

- **Value-focused**: "Start Free Trial" not "Submit"
- **Action verb**: "Get," "Try," "Download," "Join"
- **Specific**: "Get Your Free Audit" not "Click Here"
- **A/B test**: Color, copy, placement, size

### CTA Copy Guidelines

**Weak CTAs (avoid):**
- Submit, Sign Up, Learn More, Click Here, Get Started

**Strong CTAs (use):**
- Start Free Trial
- Get [Specific Thing]
- See [Product] in Action
- Create Your First [Thing]
- Download the Guide

**Formula:** [Action Verb] + [What They Get] + [Qualifier if needed]

Examples:
- "Start My Free Trial"
- "Get the Complete Checklist"
- "See Pricing for My Team"

## Page-Specific Guidance

### Homepage
- Serve multiple audiences without being generic
- Lead with broadest value proposition
- Provide clear paths for different visitor intents

### Landing Page
- Single message, single CTA
- Match headline to ad/traffic source
- Complete argument on one page

### Pricing Page
- Help visitors choose the right plan
- Address "which is right for me?" anxiety
- Make recommended plan obvious

### Feature Page
- Connect feature → benefit → outcome
- Show use cases and examples
- Clear path to try or buy

### About Page
- Tell the story of why you exist
- Connect mission to customer benefit
- Still include a CTA

## Voice and Tone

Before writing, establish (take these from the brand voice in the product marketing context when it has them):

**Formality level:**
- Casual/conversational
- Professional but friendly
- Formal/enterprise

**Brand personality:**
- Playful or serious?
- Bold or understated?
- Technical or accessible?

Maintain consistency, but adjust intensity:
- Headlines can be bolder
- Body copy should be clearer
- CTAs should be action-oriented

## Output Format

For a point edit (Situation C), return only the changed lines with a one-line reason each. Skip the annotations and alternatives below unless asked.

- **Framework** (PAS, AIDA, BAB) recommendation
- **Headline** options (2–3 variants)
- **Body** copy structure
- **CTA** copy options
- **A/B test** suggestions (if applicable)

For page copy, also provide:

### Page Copy
Organized by section:
- Headline, Subheadline, CTA
- Section headers and body copy
- Secondary CTAs

### Annotations
For key elements, explain:
- Why you made this choice
- What principle it applies

### Alternatives
For headlines and CTAs, provide 2-3 options:
- Option A: [copy]. Rationale: [why]
- Option B: [copy]. Rationale: [why]

### Meta Content (if relevant)
- Page title (for SEO)
- Meta description

> **Source conflicts (kostja wins, ours flagged):** kostja lists "Learn More" as an acceptable ad CTA. Our copy lists it as a weak CTA. Use "Learn More" for ad click-through CTAs as kostja does; treat it as weak on landing pages and conversion CTAs.

## Related Skills

- **article-content**: Article body creation; applies PAS, AIDA, BAB to long-form; headline formulas for article titles
- `implement/sub-skills/references/pages/marketing/landing-page.md`: Landing page copy and structure
- `implement/sub-skills/references/components/branding/hero.md`: Hero headline, subheadline, CTA
- `implement/sub-skills/references/components/conversion/cta.md`: CTA design and copy
- **paid-ads-strategy**: Ad copy frameworks (PAS, BAB, Social Proof)
- **email-marketing**: Email subject lines, body copy and email copywriting
- **branding**: Brand voice, tone consistency
- **copy-editing**: Polishing existing copy (use after your draft)
- **conversion-optimization**: Page structure and strategy beyond copy
- **popups**: Popup and modal copy
- **ab-testing**: Testing copy variations
