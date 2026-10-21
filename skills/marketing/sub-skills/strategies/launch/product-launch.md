---
name: product-launch
description: When the user wants to plan a product launch, execute launch channels, or create a launch checklist. Also use when the user mentions "product launch," "launch strategy," "product announcement," "launch channels," or "market launch." For GTM motion and positioning, use gtm-strategy. For cold start and first users, use cold-start-strategy. For Product Hunt day-of, use product-hunt-launch.
metadata:
  version: 1.0.0
  based_on_repo: kostja94/marketing-skills, coreyhaines31/marketingskills
  based_on_version: v1.0.0(8dd89c5), v2.13.0(e85f3cb)
  based_on_skill: product-launch, launch
---

# Strategies: Product Launch

Guides product launch execution—channels, timeline, checklist, and cross-functional coordination. Use this skill when planning the launch of a new product or major feature. For GTM strategy (PLG/SLG/MLG, 90-day framework, ICP, new market entry, repositioning), see **gtm-strategy**. For cold start (first users, no product yet), see **cold-start-strategy**.

## Initial Assessment

**Project context:** Read the product marketing context when present and load only what is relevant to this task. Otherwise use available project material or user-provided facts and ask for missing information.

Identify:
1. **Launch type**: New product, major feature, market expansion
2. **GTM mode**: Sales-led, product-led, marketing-led, hybrid (from **gtm-strategy**)
3. **Channels**: PR, paid, organic, email, events

## Launch Checklist

- [ ] GTM strategy defined (see **gtm-strategy**)
- [ ] PMF validated (see **pmf-strategy**)
- [ ] Target market and ICP clear
- [ ] Messaging consistent across teams
- [ ] Channel mix chosen (PR, paid, organic, email)
- [ ] Timeline and milestones set
- [ ] Cross-functional owners assigned (RACI)

## Channel Mix

| Channel | Use | Skills |
|---------|-----|--------|
| **PR** | Press release, media relations | public-relations |
| **Paid ads** | Scale acquisition post-PMF | paid-ads-strategy |
| **Organic** | SEO, content, community | seo-strategy, content-marketing |
| **Email** | Announcement to existing users | email-marketing |
| **Product Hunt / Directories** | Launch-day buzz; early adopters | cold-start-strategy, directory-submission |

## Critical Success Factors

| Factor | Guideline |
|--------|-----------|
| **PMF first** | Validate product-market fit before scaling; see **pmf-strategy** |
| **GTM alignment** | One clear story; all teams use same messaging; see **gtm-strategy** |
| **Avoid rush** | Most failures = scale before PMF |

## Output Format

- **Launch plan** (timeline, channels, owners)
- **Channel** actions (PR, paid, organic, email)
- **Checklist** (pre-launch, launch, post-launch)
- **Cross-ref** to gtm-strategy for framework

## Launch Playbook

For Product Hunt pros and cons, the before/during/after playbook and case studies, see **product-hunt-launch**.

### Core Philosophy

The best companies don't just launch once—they launch again and again. Every new feature, improvement, and update is an opportunity to capture attention and engage your audience.

A strong launch isn't about a single moment. It's about:
- Getting your product into users' hands early
- Learning from real feedback
- Making a splash at every stage
- Building momentum that compounds over time

### The ORB Framework

Structure your launch marketing across three channel types. Everything should ultimately lead back to owned channels.

#### Owned Channels
You own the channel (though not the audience). Direct access without algorithms or platform rules.

**Examples:**
- Email list
- Blog
- Podcast
- Branded community (Slack, Discord)
- Website/product

**Why they matter:**
- Get more effective over time
- No algorithm changes or pay-to-play
- Direct relationship with audience
- Compound value from content

**Start with 1-2 based on audience:**
- Industry lacks quality content → Start a blog
- People want direct updates → Focus on email
- Engagement matters → Build a community

**Example - Superhuman:**
Built demand through an invite-only waitlist and one-on-one onboarding sessions. Every new user got a 30-minute live demo. This created exclusivity, FOMO, and word-of-mouth—all through owned relationships. Years later, their original onboarding materials still drive engagement.

#### Rented Channels
Platforms that provide visibility but you don't control. Algorithms shift, rules change, pay-to-play increases.

**Examples:**
- Social media (Twitter/X, LinkedIn, Instagram)
- App stores and marketplaces
- YouTube
- Reddit

**How to use correctly:**
- Pick 1-2 platforms where your audience is active
- Use them to drive traffic to owned channels

**Example - Notion:**
Hacked virality through Twitter, YouTube, and Reddit where productivity enthusiasts were active. Encouraged community to share templates and workflows. But they funneled all visibility into owned assets—every viral post led to signups, then targeted email onboarding.

**Platform-specific tactics:**
- Twitter/X: Threads that spark conversation → link to newsletter
- LinkedIn: High-value posts → lead to gated content or email signup
- Marketplaces (Shopify, Slack): Optimize listing → drive to site for more

Rented channels give speed, not stability. Capture momentum by bringing users into your owned ecosystem.

#### Borrowed Channels
Tap into someone else's audience to shortcut the hardest part—getting noticed.

**Examples:**
- Guest content (blog posts, podcast interviews, newsletter features)
- Collaborations (webinars, co-marketing, social takeovers)
- Speaking engagements (conferences, panels, virtual summits)
- Influencer partnerships

**Be proactive, not passive:**
1. List industry leaders your audience follows
2. Pitch win-win collaborations
3. Use tools like SparkToro or Listen Notes to find audience overlap
4. Set up affiliate/referral incentives (for channel partner launches, use [Introw](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/introw.md) to manage deal registration and commissions)

**Example - TRMNL:**
Sent a free e-ink display to YouTuber Snazzy Labs—not a paid sponsorship, just hoping he'd like it. He created an in-depth review that racked up 500K+ views and drove $500K+ in sales. They also set up an affiliate program for ongoing promotion.

Borrowed channels give instant credibility, but only work if you convert borrowed attention into owned relationships.

### Readiness Gate: Are You Ready to Launch?

Run this **before** the phased mechanics. Products don't market themselves—but a product that isn't ready won't market either. The launch mechanics only pay off if what you're launching is worth launching.

Two failure modes kill launches from opposite ends:

- **Stealth Mode** — launching too late. "Procrastination in a fancy suit." You keep polishing in private, waiting for the product to be perfect. It never ships, and nobody learns you exist.
- **"Just One More Feature"** — never launching. Every proposed launch date gets pushed for one more thing. The scope creeps forever; the launch never comes.

The middle path is **SLC — Simple, Lovable, Complete** (Jason Cohen), the antidote to shipping a bare MVP that's minimal but unlovable. Don't launch a stub nobody wants; don't wait for a bloated everything-app. A launchable v1 is:

- **Simple** — it does *one* thing. Not many things poorly. One clear job, done well.
- **Lovable** — people *want* to use it, not just tolerate it. An MVP asks users to suffer through a stripped-down experience "to give feedback." SLC gives them something they'd choose. If nobody would be sad to lose it, it isn't lovable yet.
- **Complete** — it's a *whole* experience for that one thing, not a stub with obvious holes. Complete at its chosen scope, not a teaser of a bigger promise.

**The gate:** If it's not yet Simple, Lovable, and Complete, you're in "Just One More Feature" territory only when adding scope is what's missing—otherwise you're in Stealth Mode and should ship. Cut scope until one thing is lovable and complete, then launch that. SLC gives you a real launch now instead of a perfect launch never.

**Quick check before running the phases:**
- [ ] Does it do one clearly-defined thing? (Simple)
- [ ] Would a target user *choose* to use it, not just endure it? (Lovable)
- [ ] Is that one thing a whole experience, with no glaring stubs? (Complete)
- [ ] Are you polishing past this bar? → Stop. You're in Stealth Mode. Ship.
- [ ] Are you still adding new things to the scope? → Stop. You're in "Just One More Feature." Cut back to SLC.

Pass the gate, then run the phases below.

### Five-Phase Launch Approach

Launching isn't a one-day event. It's a phased process that builds momentum.

#### Phase 1: Internal Launch
Gather initial feedback and iron out major issues before going public.

**Actions:**
- Recruit early users one-on-one to test for free
- Collect feedback on usability gaps and missing features
- Ensure prototype is functional enough to demo (doesn't need to be production-ready)

**Goal:** Validate core functionality with friendly users.

#### Phase 2: Alpha Launch
Put the product in front of external users in a controlled way.

**Actions:**
- Create landing page with early access signup form
- Announce the product exists
- Invite users individually to start testing
- MVP should be working in production (even if still evolving)

**Goal:** First external validation and initial waitlist building.

#### Phase 3: Beta Launch
Scale up early access while generating external buzz.

**Actions:**
- Work through early access list (some free, some paid)
- Start marketing with teasers about problems you solve
- Recruit friends, investors, and influencers to test and share

**Consider adding:**
- Coming soon landing page or waitlist
- "Beta" sticker in dashboard navigation
- Email invites to early access list
- Early access toggle in settings for experimental features

**Goal:** Build buzz and refine product with broader feedback.

#### Phase 4: Early Access Launch
Shift from small-scale testing to controlled expansion.

**Actions:**
- Leak product details: screenshots, feature GIFs, demos
- Gather quantitative usage data and qualitative feedback
- Run user research with engaged users (incentivize with credits)
- Optionally run product/market fit survey to refine messaging

**Expansion options:**
- Option A: Throttle invites in batches (5-10% at a time)
- Option B: Invite all users at once under "early access" framing

**Goal:** Validate at scale and prepare for full launch.

#### Phase 5: Full Launch
Open the floodgates.

**Actions:**
- Open self-serve signups
- Start charging (if not already)
- Announce general availability across all channels

**Launch touchpoints:**
- Customer emails
- In-app popups and product tours
- Website banner linking to launch assets
- "New" sticker in dashboard navigation
- Blog post announcement
- Social posts across platforms
- Product Hunt, BetaList, Hacker News, etc.

**Goal:** Maximum visibility and conversion to paying users.

### Post-Launch Product Marketing

Your launch isn't over when the announcement goes live. Now comes adoption and retention work.

#### Immediate Post-Launch Actions

**Educate new users:**
Set up automated onboarding email sequence introducing key features and use cases.

**Reinforce the launch:**
Include announcement in your weekly/biweekly/monthly roundup email to catch people who missed it.

**Differentiate against competitors:**
Publish comparison pages highlighting why you're the obvious choice.

**Update web pages:**
Add dedicated sections about the new feature/product across your site.

**Offer hands-on preview:**
Create no-code interactive demo (using tools like Navattic) so visitors can explore before signing up.

### Ongoing Launch Strategy

Sustain engagement with regular updates and feature rollouts, each treated as its own launch moment.

#### How to Prioritize What to Announce

Use this matrix to decide how much marketing each update deserves:

| Tier | Typical changes | Output |
|------|-----------------|--------|
| **Major** | New capability, new plan, product overhaul, big workflow change | Full campaign: changelog + blog post + email + social + in-app |
| **Medium** | New integration, notable UX improvement, performance gain customers can feel | Targeted: changelog + email to relevant segments or in-app banner + one social post |
| **Minor** | Fixes, polish, small tweaks | Changelog and release notes only, batched |

Several medium changes that share a theme ("five improvements to reporting") can be bundled into one major-tier story.

#### Announcement Tactics

**Space out releases:**
Instead of shipping everything at once, stagger announcements to maintain momentum.

**Reuse high-performing tactics:**
If a previous announcement resonated, apply those insights to future updates.

**Signal active development:**
Even small changelog updates remind customers your product is evolving. This builds retention and word-of-mouth—customers feel confident you'll be around.

**Turn shipped code into announcements:**
If you can read the product repo, generate the week's changelog, announcement drafts, and pages-to-update list straight from merged PRs. See [references/shipped-changes.md](references/shipped-changes.md).

### Launch Checklist

#### Pre-Launch
- [ ] Landing page with clear value proposition
- [ ] Email capture / waitlist signup
- [ ] Early access list built
- [ ] Owned channels established (email, blog, community)
- [ ] Rented channel presence (social profiles optimized)
- [ ] Borrowed channel opportunities identified (podcasts, influencers)
- [ ] Product Hunt listing prepared (if using)
- [ ] Launch assets created (screenshots, demo video, GIFs)
- [ ] Onboarding flow ready
- [ ] Analytics/tracking in place
- [ ] Site QA done if the launch includes a new site, redesign, or migration (see [references/site-launch-qa.md](references/site-launch-qa.md))

#### Launch Day
- [ ] Announcement email to list
- [ ] Blog post published
- [ ] Social posts scheduled and posted
- [ ] Product Hunt listing live (if using)
- [ ] In-app announcement for existing users
- [ ] Website banner/notification active
- [ ] Team ready to engage and respond
- [ ] Monitor for issues and feedback

#### Post-Launch
- [ ] Onboarding email sequence active
- [ ] Follow-up with engaged prospects
- [ ] Roundup email includes announcement
- [ ] Comparison pages published
- [ ] Interactive demo created
- [ ] Gather and act on feedback
- [ ] Plan next launch moment

### Task-Specific Questions

1. What are you launching? (New product, major feature, minor update)
2. What's your current audience size and engagement?
3. What owned channels do you have? (Email list size, blog traffic, community)
4. What's your timeline for launch?
5. Have you launched before? What worked/didn't work?
6. Are you considering Product Hunt? What's your preparation status?

## Related Skills

- **gtm-strategy**: GTM framework; modes, 90-day, ICP, new market, repositioning; product launch implements GTM for new product
- **pmf-strategy**: Validate PMF before scaling
- **cold-start-strategy**: First users; Product Hunt; differs from full GTM launch
- **indie-hacker-strategy**: Indie hacker launch; Build in Public; first 100 users
- **public-relations**: Press release; media relations for launch
- **paid-ads-strategy**: Paid channel for launch
- **website-structure**: Pages needed for launch
- **marketing-ideas**: For additional launch tactics (#77-86, e.g. #78 Product Hunt, #81 Early Access Pricing)
- **offers**: For the offer being launched (bonuses, guarantees, scarcity, naming)
- **directory-submission**: For the directory layer of a launch
- **email-marketing**: For launch and onboarding email sequences
- **conversion-optimization**: For optimizing launch landing pages
- **marketing-psychology**: For psychology behind waitlists and exclusivity
- **comparison-pages**: For the comparison pages in post-launch
- **sales-enablement**: For launch sales collateral and enablement materials
