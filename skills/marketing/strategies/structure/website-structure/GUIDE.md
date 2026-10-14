---
name: website-structure
description: When the user wants to plan website structure, decide which pages to build, or prioritize pages for a new or existing site. Also use when the user mentions "website structure," "site structure," "which pages do I need," "page planning," "sitemap planning," "Must Have pages," "website architecture," or "site hierarchy." For a specific page template (e.g. homepage), use homepage-generator or landing-page-generator as appropriate. Not for organic SEO roadmap alone; use seo-strategy.
metadata:
  version: 1.5.0
---

# Strategy: Website Structure

Guides website structure planning: which pages to build, page priority, and how structure supports UX, SEO, and growth. Structure is the organization and connection of pages; it affects user navigation, Google's understanding of content importance, crawlability, and sitelinks in SERPs. See **serp-features** for sitelinks and SERP optimization.

## Initial Assessment

**Project context:** Read the product marketing context when present and load only what is relevant to this task. Otherwise use available project material or user-provided facts and ask for missing information.

Identify:
1. **Website type**: Product/SaaS, B2B, E-commerce, Portfolio, Forum, Directory
2. **Stage**: New site (plan from scratch) vs. existing (extend or audit)
3. **Growth strategy**: Affiliate, education, multi-language, community, B2B, developer
4. **Constraints**: Team size, budget, tech stack

## Page Priority Framework

Plan pages by priority for development scheduling. See the page guides in `dev/references/pages` for full page types and website-type mapping.

| Priority | Pages | Notes |
|----------|-------|-------|
| **Must Have** | Home, Product/Features, Pricing, Blog, About, Privacy, Terms, Contact | Essential for trust and conversion; Pricing: public page in nav for self-serve; enterprise-only may use "Contact sales" instead; see **pricing-page-generator** (Visibility & Placement) |
| **Great to Have** | Testimonials, FAQ, Sitemap (HTML), 404, Refund/Returns | Support UX and SEO |
| **Optional** | Search Results, News, Careers, Disclosure | Situational |
| **Traffic-driven** | Category/Collection pages | For content-heavy or e-commerce; needs Category + Tags |

## Generic Template Structure

Applicable to SaaS, tools, and content sites. Adapt by removing unused nodes (e.g. no API → drop API) and adding specific modules (e.g. industry, region).

| Section | Typical Paths | Page Skills |
|---------|---------------|-------------|
| **Root** | /, /features, /pricing, /demo, /contact | homepage-generator, features-page-generator, pricing-page-generator |
| **Tools** | /tools, /free-tools; hub + per-tool pages | tools-page-generator; free tools for lead gen; often SPA; programmatic; see **programmatic-seo** |
| **Resources** | /blog, /changelog, /glossary, /faq, /tutorials | blog-page-generator, changelog-page-generator, glossary-page-generator, faq-page-generator |
| **Partnership** | /affiliate, /startups, /ambassadors | affiliate-page-generator, landing-page-generator |
| **Legal** | /terms, /privacy, /careers | terms-page-generator, privacy-page-generator, careers-page-generator |
| **Competitor** | /alternatives, /compare, /migrate | alternatives-page-generator, migration-page-generator |
| **Standalone** | /dashboard, /login, /signup, /docs, /api, /status, /support | signup-login-page-generator, docs-page-generator, api-page-generator, status-page-generator |

## Growth Strategy → Structure Mapping

Structure reflects growth strategy. Subdirectories signal channels:

| Goal | Path Example | Page/Channel |
|------|--------------|--------------|
| Affiliate conversion | /affiliate | affiliate-page-generator |
| Education/student plan | /education, /startups, /student-discount | education-program, startups-page-generator |
| Multi-language | /zh-CN, /ja | localization-strategy |
| Community | /ambassadors, /showcase | creator-program, landing-page-generator |
| B2B / Enterprise | Solutions (industry-first), Use cases (scenario-first; can be sub-pages), Customer stories | solutions-page-generator, use-cases-page-generator, customer-stories-page-generator |
| Developer product | /api, /docs, /status | api-page-generator, docs-page-generator, status-page-generator |
| User feedback | Feedback, Roadmap | feedback-page-generator; External (Canny, FeatureBase) |
| Plugins/Integrations | /integrations, /plugins | integrations-page-generator, category-page-generator |
| Giveaway/Contest | /giveaway | contest-page-generator |

## Domain Structure (Multiple Products)

When planning for multiple products or brands, see **domain-architecture** for subfolder vs subdomain vs independent domain. This skill covers page structure within a single domain. For initial domain choice (Brand vs PMD vs EMD, TLD), see **domain-selection**.

## Planning Workflow

1. **Choose template**: Start from generic structure; map to the page guides in `dev/references/pages` website types
2. **Trim modules**: Remove irrelevant nodes (e.g. no API → drop /api, /docs)
3. **Add specifics**: Industry pages, region, product variants
4. **Assign URLs**: Per node; follow **url-structure** (lowercase, hyphens, short, keyword-rich)
5. **Export list**: "Page type + URL + Priority" for dev scheduling
6. **Tech stack**: Match page types to services (DNS, auth, CMS, status page, etc.)
7. **Iterate**: Expand with new features, markets; keep structure clear

## Structure Principles

| Principle | Guideline |
|-----------|-----------|
| **Flat structure** | Max 4 clicks from homepage to any page; improves crawlability and weight distribution |
| **Early planning** | Plan structure before growth; can start right after domain purchase |
| **Sitelinks** | Good structure + TOC + authoritative internal links → natural sitelinks in SERP (cannot be forced via schema); see **serp-features** |
| **Orphan prevention** | Every page needs internal links; see **site-crawlability** and **internal-links** |
| **Features vs Use cases** | /features = capability-first; /use-cases = scenario-first; differentiate content angle, link between, avoid overlap; see **features-page-generator**, **use-cases-page-generator** |
| **Clear navigation** | Clear hierarchy and nav improve task completion; users find what they need faster; see **navigation-menu-generator** |
| **Pricing placement** | Marketing site: /pricing in main nav for prospects; in-app: Settings → Billing in sidebar for logged-in users (subscription management). Enterprise-only: "Contact sales" may replace public pricing page; see **pricing-page-generator** |

## Homepage Module Reference

See **homepage-generator** for common modules (Headline, Subheadline, CTA, Benefits, Social Proof, etc.), navigation options, and **hero-generator** for hero design.

## Output Format

- **Page list** with priority (Must Have / Great to Have / Optional)
- **URL structure** (paths per section)
- **Website-type fit** (which pages apply, per the page guides in `dev/references/pages`)
- **Growth mapping** (which paths support which channels)
- **Next steps**: url-structure for URL rules; xml-sitemap for submission; site-crawlability for audit

## References

- [Website structure SEO guide](https://alignify.co/zh/seo/website-structure) — Alignify: structure importance, page priority, generic template, planning workflow, growth mapping, homepage modules

## Site Architecture Planning

### Before Planning

Gather this context (ask if not provided):

#### 1. Business Context
- What does the company do?
- Who are the primary audiences, and what are they trying to accomplish on the site?
- What are the top 3 goals for the site? (conversions, SEO traffic, education, support)

#### 2. Current State
- New site or restructuring an existing one?
- If restructuring: what's broken? (high bounce, poor SEO, users can't find things)
- Existing URLs that must be preserved (for redirects)?
- What platform is it on, and is a platform change on the table? (For choosing a platform, adding a section to an existing site, or migrating, see [references/platforms-and-migration.md](references/platforms-and-migration.md).)

#### 3. Site Type
- SaaS marketing site
- Content/blog site
- E-commerce
- Documentation
- Hybrid (SaaS + content)
- Small business / local

#### 4. Content Inventory
- How many pages exist or are planned?
- What are the 5 most important pages? (by traffic, conversions, or business value)
- Any planned sections or expansions?

### Site Types and Starting Points

| Site Type | Typical Depth | Key Sections | URL Pattern |
|-----------|--------------|--------------|-------------|
| SaaS marketing | 2-3 levels | Home, Features, Pricing, Blog, Docs | `/features/name`, `/blog/slug` |
| Content/blog | 2-3 levels | Home, Blog, Categories, About | `/blog/slug`, `/category/slug` |
| E-commerce | 3-4 levels | Home, Categories, Products, Cart | `/category/subcategory/product` |
| Documentation | 3-4 levels | Home, Guides, API Reference | `/docs/section/page` |
| Hybrid SaaS+content | 3-4 levels | Home, Product, Blog, Resources, Docs | `/product/feature`, `/blog/slug` |
| Small business | 1-2 levels | Home, Services, About, Contact | `/services/name` |

**For full page hierarchy templates**: See [references/site-type-templates.md](references/site-type-templates.md)

### Page Hierarchy Design

#### The 3-Click Rule

> Source conflict: the Structure Principles table above allows a max of 4 clicks from the homepage, and kostja's wording wins. The 3-click figure below comes from the former site-architecture guide.

Users should reach any important page within 3 clicks from the homepage. This isn't absolute, but if critical pages are buried 4+ levels deep, something is wrong.

#### Flat vs Deep

| Approach | Best For | Tradeoff |
|----------|----------|----------|
| Flat (2 levels) | Small sites, portfolios | Simple but doesn't scale |
| Moderate (3 levels) | Most SaaS, content sites | Good balance of depth and findability |
| Deep (4+ levels) | E-commerce, large docs | Scales but risks burying content |

**Rule of thumb**: Go as flat as possible while keeping navigation clean. If a nav dropdown has 20+ items, add a level of hierarchy.

#### Hierarchy Levels

| Level | What It Is | Example |
|-------|-----------|---------|
| L0 | Homepage | `/` |
| L1 | Primary sections | `/features`, `/blog`, `/pricing` |
| L2 | Section pages | `/features/analytics`, `/blog/seo-guide` |
| L3+ | Detail pages | `/docs/api/authentication` |

#### ASCII Tree Format

Use this format for page hierarchies:

```
Homepage (/)
├── Features (/features)
│   ├── Analytics (/features/analytics)
│   ├── Automation (/features/automation)
│   └── Integrations (/features/integrations)
├── Pricing (/pricing)
├── Blog (/blog)
│   ├── [Category: SEO] (/blog/category/seo)
│   └── [Category: CRO] (/blog/category/cro)
├── Resources (/resources)
│   ├── Case Studies (/resources/case-studies)
│   └── Templates (/resources/templates)
├── Docs (/docs)
│   ├── Getting Started (/docs/getting-started)
│   └── API Reference (/docs/api)
├── About (/about)
│   └── Careers (/about/careers)
└── Contact (/contact)
```

**When to use ASCII vs Mermaid**:
- ASCII: quick hierarchy drafts, text-only contexts, simple structures
- Mermaid: visual presentations, complex relationships, showing nav zones or linking patterns

### Navigation Design

#### Navigation Types

| Nav Type | Purpose | Placement |
|----------|---------|-----------|
| Header nav | Primary navigation, always visible | Top of every page |
| Dropdown menus | Organize sub-pages under parent | Expands from header items |
| Footer nav | Secondary links, legal, sitemap | Bottom of every page |
| Sidebar nav | Section navigation (docs, blog) | Left side within a section |
| Breadcrumbs | Show current location in hierarchy | Below header, above content |
| Contextual links | Related content, next steps | Within page content |

#### Header Navigation Rules

- **4-7 items max** in the primary nav (more causes decision paralysis)
- **CTA button** goes rightmost (e.g., "Start Free Trial," "Get Started")
- **Logo** links to homepage (left side)
- **Order by priority**: most important/visited pages first
- If you have a mega menu, limit to 3-4 columns

#### Footer Organization

Group footer links into columns:
- **Product**: Features, Pricing, Integrations, Changelog
- **Resources**: Blog, Case Studies, Templates, Docs
- **Company**: About, Careers, Contact, Press
- **Legal**: Privacy, Terms, Security

#### Breadcrumb Format

```
Home > Features > Analytics
Home > Blog > SEO Category > Post Title
```

Breadcrumbs should mirror the URL hierarchy. Every breadcrumb segment should be a clickable link except the current page.

**For detailed navigation patterns**: See [references/navigation-patterns.md](references/navigation-patterns.md)

### Plan Deliverables

When creating a site architecture plan, provide these deliverables:

#### 1. Page Hierarchy (ASCII Tree)
Full site structure with URLs at each node. Use the ASCII tree format from the Page Hierarchy Design section.

#### 2. Visual Sitemap (Mermaid)

Templates and method: see **xml-sitemap** (Visual Sitemap Planning).

Mermaid diagram showing page relationships and navigation zones. Use `graph TD` with subgraphs for nav zones where helpful.

#### 3. URL Map Table

URL patterns and common URL mistakes: see **url-structure**.

| Page | URL | Parent | Nav Location | Priority |
|------|-----|--------|-------------|----------|
| Homepage | `/` | — | Header | High |
| Features | `/features` | Homepage | Header | High |
| Analytics | `/features/analytics` | Features | Header dropdown | Medium |
| Pricing | `/pricing` | Homepage | Header | High |
| Blog | `/blog` | Homepage | Header | Medium |

#### 4. Navigation Spec
- Header nav items (ordered, with CTA)
- Footer sections and links
- Sidebar nav (if applicable)
- Breadcrumb implementation notes

#### 5. Internal Linking Plan

Link types, rules, the hub-and-spoke model and the link audit checklist: see **internal-links**.

- Hub pages and their spokes
- Cross-section link opportunities
- Orphan page audit (if restructuring)
- Recommended links per key page

## Related Skills

- **seo-strategy**: SEO workflow order; structure planning fits before Technical phase
- **domain-selection**: Initial domain choice; do before structure when choosing domain
- **domain-architecture**: Subfolder vs subdomain vs independent; do before structure if domain decision pending
- **url-structure**: URL optimization, hierarchy, slugs; apply after structure is defined
- **site-crawlability**: Crawlability, orphan pages, redirects; audit existing structure
- **internal-links**: Link strategy, hub-spoke; implement after pages exist
- **xml-sitemap**: Sitemap creation; include planned URLs
- **breadcrumb-generator**: Breadcrumb for hierarchy; large sites, e-commerce
- **navigation-menu-generator**: Nav design; primary, footer, mobile
- **content-strategy**: Content clusters, pillar pages; complements structure planning
- **programmatic-seo**: For building SEO pages at scale with templates and data
- **seo-audit**: For technical SEO, on-page optimization, and indexation issues
- **conversion-optimization**: For optimizing individual pages for conversion
- **schema-markup**: For implementing breadcrumb and site navigation structured data
- **comparison-pages**: For comparison page frameworks and URL patterns
- **product-launch**: For site go-live QA after a build or migration
