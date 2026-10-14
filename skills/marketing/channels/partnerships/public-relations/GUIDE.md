---
name: public-relations
description: When the user wants to plan PR, write a press release, or manage media relations. Also use when the user mentions "public relations," "PR," "press release," "media relations," "news release," "journalist," "media coverage," "product announcement," or "earned media." Also use when the user mentions "newsjacking," "pitch a journalist," "HARO," "Qwoted," "press requests," "press page," "newsroom," "podcast guest prep," "crisis communications," "data breach statement," "outage statement," or "story angle." For on-site "As Seen In" or logos page, use `dev/references/pages/marketing/press`.
metadata:
  version: 1.1.0
---

# Channels: Public Relations

Guides PR and press release strategy. Journalists use ~3% of releases they receive; proper structure is critical. Use this skill when writing press releases, planning product announcements, or building media relations.

Earned media for software products. PR multiplies distribution; it does not replace it.

## Initial Assessment

**Project context:** Read the product marketing context when present and load only what is relevant to this task. Otherwise use available project material or user-provided facts and ask for missing information.

Identify:
1. **News angle**: Product launch, funding, partnership, milestone
2. **Audience**: Trade press, mainstream, bloggers
3. **Timing**: Embargo or immediate
4. **Capacity**: A real story, founder/exec time, and a destination (press page, post, launch) to convert attention

## Core Philosophy

- **Earned media rarely drives direct conversions.** It gives backlinks, legitimacy, AI-citation surface, and ammo for sales conversations.
- **Pitch journalists like customers:** specific, useful, fast, never about you.
- **The story is the trend, the data, the conflict, or the human.** The product is the evidence.
- **Chase compound effects, not the traffic bump.** Build media relationships before you need them and run one core asset through the repurposing flywheel.
- **Speed beats polish on reactive PR.** A B+ pitch in the first hour beats an A+ on day three.

**Worth it when** you have a real story (proprietary data, strong opinion, milestone, sharp customer before/after), exec time for quotes, and a destination page. **Skip for now** when pre-launch with no story beyond "we exist", nobody can sustain 4–6 weeks of pitching, or the ICP is unclear.

## The PR Mix

Run at least three modes; most teams over-index on one.

| Mode | What it is | Effort | Speed to coverage |
|------|------------|--------|-------------------|
| **Reactive (newsjacking)** | Inject your POV into trending news | Low–medium | Hours to days |
| **Proactive (pitching)** | Build a media list, pitch original stories | High | 2–8 weeks |
| **Inbound (press requests)** | Answer journalist queries on HARO/Qwoted/Featured | Low | Days to weeks |
| **Owned (press page + media kit)** | Make it easy for journalists to find you | One-time setup | N/A |

- Story angles (Founding Story / David vs Goliath / Have an Enemy), data stories, relationship-building, repurposing flywheel: [references/story-angles.md](references/story-angles.md)
- Reactive newsjacking workflow: [references/newsjacking.md](references/newsjacking.md)
- Proactive journalist pitching: [references/journalist-pitching.md](references/journalist-pitching.md)
- Inbound press-request platforms: [references/press-platforms.md](references/press-platforms.md)
- Where to pitch (outlets, podcasts, newsletters): [references/media-outlets.md](references/media-outlets.md); for startup/SaaS/AI directories see **directory-submission**
- Prepping a podcast appearance: [references/podcast-guest-prep.md](references/podcast-guest-prep.md)

## Press Release Structure

| Section | Guideline |
|---------|-----------|
| **Header** | Logo; contact (name, title, email, phone); "FOR IMMEDIATE RELEASE" or embargo |
| **Headline** | Under 100 chars; strong action verbs; "Why should I care?" |
| **Subheadline** | Optional; additional context |
| **Dateline** | City, state, date |
| **Lead** | 50–75 words; all 5 W's (Who, What, When, Where, Why) |
| **Body** | 1–2 paragraphs; inverted pyramid; most newsworthy first |
| **Quote** | Executive/stakeholder; perspective, not fact repetition |
| **Boilerplate** | 2–3 sentence company description |
| **Media contact** | Name, email, phone |

## Lead Paragraph

Journalist should understand the full story from the lead alone. Specific details, not vague language ("important update" → what changed and impact).

## Quote Quality

- Add perspective or emotion
- Avoid generic corporate-speak
- Don't repeat facts already stated

## Writing Style

- AP style
- Short paragraphs (one idea each)
- Clear language for easy journalist adaptation
- Data and context to support claims

## Pitch Quality Bar

Send only if every answer is yes:

- [ ] Does the journalist cover this beat? (Check their last 5 articles.)
- [ ] Is there a clear news hook, something that just happened or is about to?
- [ ] Could they write a full story from the email alone (data, quotes, customer name, contact)?
- [ ] Is the subject line specific enough to predict the headline?
- [ ] Is it under 150 words?
- [ ] Is it free of the [banned vocabulary](references/journalist-pitching.md#banned-vocabulary)?
- [ ] Is the ask clear (interview, embargo, exclusive, quote)?

## Owned: Press Page + Media Kit

Set up once; the highest-ROI owned PR asset. At `/press` or `/newsroom`:
- Copy-paste company description, founder bios with high-res headshots
- Logo pack (SVG + PNG, light + dark, usage guidelines) and product screenshots
- Recent coverage list, recent releases, founding date, headcount, funding if disclosed
- Press contact **email, not a form**, with a stated 24-hour response time; then actually respond within 24 hours

## When Something Goes Wrong

Breaches, outages, viral complaints, and exec controversies shift the goal from earning coverage to responding fast and accurately. Assign a severity tier, then run the first 60 minutes: confirm facts, designate one spokesperson, publish a holding statement, set the next update time. Loop in legal counsel before admitting fault or publishing for a breach, injury, lawsuit, or regulator.

- Severity tiers, channel order, playbooks by crisis type: [references/crisis-communications.md](references/crisis-communications.md)
- Holding, breach, outage, apology, billing-error, and postmortem templates: [references/statement-templates.md](references/statement-templates.md)

## Measurement

| Metric | Why |
|--------|-----|
| **Coverage count** (placements/month) | Activity baseline |
| **Domain rating of placements** | Backlink value |
| **Referral traffic from coverage** | Did anyone click? |
| **Brand search lift** | Did people search you afterward? |
| **AI citation rate** (ChatGPT, Perplexity) | Increasingly the measure that matters |
| **Sales conversations citing the article** | The revenue signal |

Ignore AVE (advertising value equivalency); it is a vanity metric.

## Common Workflows

- **Newsjack a trending story**: [newsjacking.md](references/newsjacking.md); run the scoring rubric, draft 2–3 angles, pick one, draft the pitch.
- **Find journalists for a beat**: [journalist-pitching.md](references/journalist-pitching.md); discovery checklist plus a browser tool to read recent articles, then a scored list.
- **What's worth pitching this week**: combine recent milestones, active news cycles, and collected data; score each against the quality bar.
- **No news / story angle**: [story-angles.md](references/story-angles.md); a milestone alone isn't a story, a milestone with narrative is.
- **Respond to a HARO query**: [press-platforms.md](references/press-platforms.md); use the template, under 200 words.
- **Podcast prep**: [podcast-guest-prep.md](references/podcast-guest-prep.md); research the show, extract recurring threads and host profiles, map your stories onto them.

## Output Format

- **Headline** and subheadline
- **Lead** paragraph
- **Body** copy
- **Quote** suggestion
- **Boilerplate**

## Related Skills

- `dev/references/pages/marketing/press`: Media kit for press (assets)
- `dev/references/pages/marketing/press`: Aggregation of coverage; outcome of PR; "As Seen In"
- **branding**: Brand voice for PR copy
- **cold-start-strategy**: Product Hunt, launch channels
- **product-launch**: GTM; PR as launch channel
- **directory-submission**: Startup/SaaS/AI directories for discovery and backlinks
- **cold-email**: Writing the outreach itself
- **generative-engine-optimization**: Coverage as AI-citation surface
