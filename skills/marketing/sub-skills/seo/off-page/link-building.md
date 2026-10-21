---
name: link-building
description: When the user wants to build backlinks, earn links or third-party mentions, or improve off-page SEO. Also use when the user mentions "link building," "backlinks," "off-page SEO," "link acquisition," "link prospecting," "link gap," "competitor backlinks," "unlinked mentions," "link reclamation," "outreach," "guest posting," "broken link building," "resource pages," "best-of list outreach," "referring domains," "anchor text," or "is this link vendor safe." Never recommend buying links that pass ranking credit; paid or exchanged placements get rel=sponsored or nofollow. For profile audit, use backlink-analysis.
metadata:
  version: 1.0.0
  based_on_repo: kostja94/marketing-skills, coreyhaines31/marketingskills
  based_on_version: v1.0.0(8dd89c5), v2.13.0(e85f3cb)
  based_on_skill: link-building, link-building
---

# SEO Off-Page: Link Building

Guides link building strategy: acquiring quality backlinks and third-party mentions to improve domain authority, rankings, and AI citations, without creating anything Google would treat as link spam.

Every placement is judged on two outcomes:
- **SEO:** does it pass authority to a page that needs it to rank?
- **AI citations:** is it a page AI engines cite for the category's prompts? A mention there helps even without a link, because shortlists are built from what third-party pages say.

## Scope (Off-Page SEO)

- **Link building**: Acquire backlinks from relevant, authoritative sites
- **Broken link building**: Find broken links on others' sites; suggest your content as replacement
- **Unlinked brand mentions**: Turn mentions into links via outreach
- **Guest posting**: Contribute to relevant publications; earn links
- **Journalist requests**: Respond to #JournoRequest; provide quotes/assets
- **Digital PR**: PR campaigns for backlinks and E-E-A-T — see **eeat-signals**

## Initial Assessment

**Project context:** Read the product marketing context when present and load only what is relevant to this task. Otherwise use available project material or user-provided facts and ask for missing information.

Identify:
1. **Current backlink profile**: Domain authority, referring domains
2. **Target keywords**: What to rank for
3. **Linkable assets**: Research, tools, guides, data, testimonials
4. **Target pages**: Which pages need to rank or be cited. Links go to pages, and a homepage link rarely moves a commercial page
5. **Target prompts**: The AI prompts where the product should appear
6. **Current position**: Rankings for those queries, and who outranks the target pages
7. **Resources and tools**: Hours per week, budget, whether someone can do outreach; Ahrefs, Semrush, DataForSEO, Moz, or none
8. **History**: Past link vendors, paid placements, link swaps, or a manual action in Search Console

## Link Building Strategies

| Strategy | Description |
|----------|-------------|
| **Content marketing** | Create link-worthy content (guides, research, tools) |
| **Guest posting** | Write for relevant sites with author bio link |
| **Broken link building** | Find broken links, suggest your content as replacement |
| **Unlinked brand mentions** | Turn mentions into links via outreach |
| **Journalist requests** | Respond to #JournoRequest; provide quotes/assets |
| **Directory and curated list submission** | Get listed on directories (Taaft, Product Hunt, G2) and curated "best-of" lists; cold-start channel—see **directory-submission** for submission workflow, **cold-start-strategy** for launch plan |
| **Digital PR** | Press releases, news, expert quotes; earn authoritative links at scale |
| **Partnerships** | Partner links, co-marketing |

## Quality Over Quantity

| Factor | Good | Avoid |
|--------|------|-------|
| **Relevance** | Links from related sites | Irrelevant niches |
| **Authority** | High-quality, trusted sites | Spammy, low-quality |
| **Anchor text** | Natural, varied | Over-optimized, exact match |
| **Context** | Editorial, contextual links | Footer, sidebar link farms |

## Outreach Best Practices

- Personalize each outreach message
- Offer value (content, data, quote) before asking for link
- Follow up politely; don't spam
- Track outreach in spreadsheet or tool

## Workflow

The steps below sit on top of the strategies above. Open a reference when the task needs that detail.

| Need | Reference |
|---|---|
| Playbooks per tactic: how to find targets, what to send, what to watch for | [Tactics](references/tactics.md) |
| Prospecting methods, qualification, outreach templates, tracker layout | [Prospecting and outreach](references/prospecting-and-outreach.md) |
| Vetting a link vendor, manual actions, disavow, Google's spam policies | [Risk policy](references/risk-policy.md) |

### Step 1: Confirm Links Are the Bottleneck

Links fix an authority gap. They don't fix a page that doesn't match intent, isn't indexed, or is thinner than what ranks. Before any outreach:

1. **Check the page itself first.** Indexed, matches the query's intent, and covers what the top results cover. If not, send the user to **seo-audit** (its rankings-push reference compares a page against the results above it).
2. **Run a page-level link gap.** Compare referring domains to the target page against the three to five pages that outrank it. Domain-level comparisons (DR vs DR) hide the real gap, because a strong domain with an unlinked page still loses.
3. **Read the gap honestly:**

| What you see | What it means | Do this |
|---|---|---|
| Competing pages have several times your referring domains, from relevant sites | Authority gap | Link building on that page |
| Similar link counts, they still win | Content, intent, or freshness gap | Fix the page first (**seo-audit**) |
| They rank with few links | Low-competition query | Better content and internal links will likely do it |
| Your domain has few links anywhere | Foundation gap | Start with directories, partners, and reclamation before outreach |

Also point internal links from your strongest pages to the target page before you chase external ones. It's free and it's often half the gap.

### Step 2: Have Something Worth Linking To

Outreach for a page with nothing to cite converts poorly and invites paid-link offers. Linkable assets, in order of how often they earn links on their own:

- **Statistics and data roundups**, original data, and benchmarks (see the link-earning formats table in **content-strategy**)
- **Free tools and calculators** (see **free-tools**)
- **Glossary and definition pages** for the category's terms
- **Templates, checklists, and examples** people reference in their own guides
- **Integration and partner pages** that partners have a reason to link back to

Put the asset near the target page and link to the target page from it. Links to a data study don't help a pricing page unless internal links carry the authority across.

### Step 3: Pick Tactics by Effort and Quality

Start at the top. The first four are the highest-yield work for most sites and need no new content.

| Tactic | Effort | Typical quality | Notes |
|---|---|---|---|
| **Unlinked mention reclamation** | Low | High | Sites already writing about you; ask for the link |
| **Partner, integration, customer, and vendor pages** | Low | High, relevant | Partner directories, integration marketplaces, "powered by" and case study pages |
| **Moved, broken, and redirected links** | Low | Varies | Links pointing to your 404s or old URLs; fix with redirects, then ask for updates |
| **"Best X" list inclusion** | Medium | High for AI citations | The listicles engines cite for your category; ask for an honest evaluation |
| **Resource and tools pages** | Medium | Medium | Curated pages listing tools or guides in your niche |
| **Broken link replacement** | Medium | Medium | A dead resource on someone's page that your asset replaces |
| **Expert contributions and guest articles** | Medium–high | Varies widely | Editorial sites only; never "write for us" networks |
| **Podcast guesting** | Medium | Medium, plus AI citations from transcripts | Hand off to **public-relations** |
| **Data-led digital PR and journalist requests** | High | Highest ceiling | Hand off to **public-relations** |
| **Directories and launch sites** | Low | Foundation only | Hand off to **directory-submission** |
| **Review platforms** | Medium | High for AI shortlists | Hand off to **referral-program** |
| **Communities and Reddit** | Ongoing | Mentions, rarely links | Hand off to **community-building**; participate as yourself |

Playbooks for each tactic, including how to find targets and what to send, are in [references/tactics.md](references/tactics.md).

#### Choosing targets for AI citations

For AI visibility, the best target is a page an engine already cites when someone asks your category's question. Run the user's prompts (or pull cited sources from a tracker; see **generative-engine-optimization**) and list the third-party pages that show up. Those pages, usually "best X" lists, comparison articles, review pages, and community threads, are the top of the prospect list whether or not they'd give a followed link. Read the citation mix first: if engines in this category mostly cite company sites, owned content does more than outreach (see the citation-mix section of **generative-engine-optimization**).

### Step 4: Prospect, Qualify, Reach Out

Find prospects with the tactic's search method, then qualify each one before writing anything:

- **Relevant:** would this site's readers plausibly need the product? Topic relevance matters more than domain rating.
- **Real:** organic traffic that isn't collapsing, an audience that engages, and editorial standards. Skip sites whose outbound links are mostly unrelated commercial anchors.
- **Reachable:** a named person who owns the page.
- **Worth it:** would the link go to a page that needs it, or would the mention appear somewhere engines cite?

Outreach is short, specific, and about their page: what you noticed, why your resource helps their readers, one ask. Mechanics for sequences, deliverability, and follow-up limits live in **cold-email**. Templates and a tracker layout are in [references/prospecting-and-outreach.md](references/prospecting-and-outreach.md).

Draft outreach for the user to approve and send. Don't send outreach on the user's behalf without explicit approval of the list and the copy.

### Step 5: Stay Inside the Rules

Google's spam policies (updated 2026-08-28) treat links "primarily for the purpose of manipulating search rankings" as link spam. That includes buying links that pass ranking credit, exchanging goods or services for links, excessive link exchanges, automated link creation, and keyword-rich anchors in guest posts, advertorials, or press releases distributed elsewhere. Paid links are fine when they carry `rel="sponsored"` or `rel="nofollow"`.

What this means for the work:

- **You can pay for a placement when the link passes no ranking credit.** Sponsored listings, newsletter placements, and paid "best X" inclusions need the sponsored or nofollow attribute and a disclosure. They can still be worth it for AI citations and referral traffic.
- **Products in exchange for a review-with-link count as payment.** The link needs a qualifying attribute.
- **Link swaps are fine in moderation and when relevant.** Partner pages built only to cross-link are not.
- **Guest posts are for reach and expertise.** Use branded or plain anchors in author bios and body links.
- **Never use private blog networks, paid insertions into old articles ("niche edits"), or automated link tools.**

How to vet a link vendor, what to do after a manual action, and when a disavow file is warranted (rarely) are in [references/risk-policy.md](references/risk-policy.md).

### Step 6: Anchors and Pace

- **Let other people choose the anchor text.** Natural profiles are mostly branded, URL, and generic anchors. Ask for the link and leave the wording to them.
- **Don't plan a link velocity.** There's no safe or unsafe number of links per month for earned links. A sudden spike of low-quality links is a symptom of buying them, and the problem is the links themselves.
- **Spread links across pages that need them.** Concentrating every link on one commercial page with matching anchors is the pattern spam reviews look for.

### Step 7: Measure Both Outcomes

| Metric | How | Cadence |
|---|---|---|
| **New referring domains to target pages** | Ahrefs, Semrush, DataForSEO, or Search Console's Links report | Monthly |
| **Rankings for target queries** | Rank tracker or Search Console average position for the page | Monthly; expect lag of weeks to months |
| **Mentions on AI-cited pages** | Count of target pages that now mention you, linked or not | Monthly |
| **AI mention and recommendation rate** | Prompt tracking for the target prompts (see **generative-engine-optimization**) | Monthly |
| **Outreach funnel** | Prospects qualified, contacted, replied, placed | Weekly |
| **Referral traffic and conversions** | Analytics, by referring domain | Monthly |

Report placements by target page. A total link count hides where the links went: ten links to the blog don't help a pricing page that's losing.

### Running It as a Loop

Link building works as a weekly habit more than a campaign. The **marketing-loops** backlink-prospecting loop runs this workflow on a schedule: find new targets, qualify them, draft outreach for approval, and track who has already been contacted. Its brand-mention loop sends unlinked mentions here for reclamation.

### Tools

| Need | Tools |
|---|---|
| Backlink data, link gap, competitor links | Ahrefs, Semrush, DataForSEO, Moz |
| Finding prospects and mentions | Search operators, Exa, Firecrawl, Google Alerts, mention monitors |
| Finding the contact | Hunter, the site's own about or contact page |
| Done-for-you placements | Managed placement services such as [LinkDR](https://linkdr.com) source sites, pitch editors, and confirm links go live. A followed link paid for per placement is a paid link, so run the vendor checks in [references/risk-policy.md](references/risk-policy.md) first |
| Free fallback | Search Console's Links report for your own links; search operators for prospects |

## Output Format

- **Diagnosis**: whether links are the bottleneck for each target page, with the page-level gap
- **Linkable asset** ideas: what exists to link to, and what to build first if nothing does
- **Tactic mix**: the three or four tactics to run first, with why
- **Outreach** strategy and templates; drafts for approval, one per tactic at minimum
- **Target sites**: types by default; once prospecting data exists, qualified targets with the page, the contact, the angle, and whether engines cite it
- **Risk notes**: anything in the current profile or a proposed vendor that breaks the rules
- **Metrics** to track (referring domains, DA, traffic, AI mentions), with targets at 30 and 90 days

## Related Skills

- **seo-strategy**: SEO workflow; link building is Off-Page phase
- **backlink-analysis**: Analyze current backlink profile
- **content-strategy**: Content strategy supports link building; link-earning formats and linkable assets
- **keyword-research**: Target keywords inform link targets
- **cold-start-strategy**: Cold start and first-user acquisition; directory submission as part of launch
- **parasite-seo**: Parasite SEO; high-authority platforms for backlinks
- **github**: GitHub repos, gists, awesome lists for backlinks
- **directory-submission**: Directory and curated list submission--preparation, platform-specific copy, Taaft/Product Hunt/G2; use when user wants to submit product to directories or get listed on best-of roundups
- **eeat-signals**: E-E-A-T implementation; Digital PR supports authority
- **seo-audit**: Diagnose whether a page's problem is authority or the page itself
- **free-tools**: Tools and calculators that earn links
- **public-relations**: Journalist requests, data-led PR, podcasts
- **referral-program**: Review programs for G2, Capterra, and other review platforms
- **community-building**: Reddit and community participation
- **generative-engine-optimization**: Citation mix, prompt tracking, and on-site work for AI answers
- **competitor-research**: Competitors' referring domains and link sources
- **cold-email**: Outreach mechanics and deliverability
- **marketing-loops**: The backlink-prospecting and brand-mention loops
