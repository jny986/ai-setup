---
name: url-structure
description: When the user wants to optimize URL structure, fix URL issues, or plan URL hierarchy. Also use when the user mentions "URL structure," "URL optimization," "slug," "clean URLs," "URL hierarchy," "URL path," "permalink structure," "URL best practices," "dynamic URLs," or "URL parameters." For per-page slug wording, use url-slug. For canonical consolidation, use canonical-tag.
metadata:
  version: 1.1.0
  based_on_repo: kostja94/marketing-skills, coreyhaines31/marketingskills
  based_on_version: v1.0.0(8dd89c5), v2.11.29(c7d7dfb)
  based_on_skill: url-structure, site-architecture
---

# SEO On-Page: URL Structure

Guides URL structure optimization for SEO: readability, hierarchy, and best practices.

## Scope (On-Page SEO)

- **URL hierarchy**: Path structure, categories, depth
- **URL format**: Static vs dynamic; omit file extensions
- **URL slug**: See **url-slug** for slug creation (3–5 words, under 60 chars)
- **Duplicate variants**: See **canonical-tag** for HTTPS, www, trailing slash

## Initial Assessment

**Project context:** Read the product marketing context when present and load only what is relevant to this task. Otherwise use available project material or user-provided facts and ask for missing information.

Identify:
1. **Site structure**: Categories, subcategories, content types
2. **Current URLs**: Existing patterns and issues
3. **Multi-language**: URL structure for zh/en (e.g., /zh/, /en/ or subdomains)

## Best Practices

### URL Guidelines

| Principle | Guideline |
|-----------|-----------|
| **Readable** | Use words, not IDs; `/blog/seo-guide` not `/p/12345` |
| **Short** | Shorter is generally better; avoid unnecessary depth |
| **Keyword** | Include target keyword when natural |
| **Lowercase** | Use lowercase; avoid mixed case |
| **Hyphens** | Use hyphens to separate words: `seo-guide` |
| **Avoid** | Special chars, query params for core content, session IDs |

### Hierarchy

| Pattern | Example | Use |
|---------|---------|-----|
| **Flat** | `/page-name` | Simple sites |
| **Category** | `/blog/post-name`, `/tools/tool-name` | Content sites |
| **Nested** | `/category/subcategory/page` | Deep hierarchies (keep shallow) |

### Multi-language

| Pattern | Example |
|---------|---------|
| **Path prefix** | `/zh/page`, `/en/page` |
| **Subdomain** | `zh.example.com`, `en.example.com` |
| **ccTLD** | `example.cn`, `example.com` |

### Static vs Dynamic vs Pseudo-Static URLs

| Type | Example | Use |
|------|---------|-----|
| **Static** | `/blog/seo-guide` | Direct file; best SEO; content stable |
| **Dynamic** | `/product?id=123` | Program-generated; avoid for indexable content |
| **Pseudo-static** | `/blog/seo-guide` (rewritten from `.php`) | Combines both; common in CMS |
| **Rule** | Prefer static or pseudo-static; if dynamic, keep params ≤2; use **canonical-tag** and **robots-txt** (Clean-param) | |

### File Extensions

- **Omit** `.html`, `.php`, `.aspx` — keeps URLs technology-agnostic, shorter, easier to refactor
- **Example**: `/seo-guide` not `/seo-guide.html`

### URL Parameter Handling

| Scenario | Approach |
|----------|----------|
| **UTM / tracking** | Canonical to base URL; params in query string only |
| **Search results** | Canonical to search page; avoid indexing result URLs |
| **Filters / sort** | Canonical to base; or **robots-txt** Clean-param |
| **Session IDs** | Use cookies; never in indexable URLs |

### Use Cases

| Scenario | Focus |
|----------|-------|
| **New site** | Plan hierarchy upfront; avoid later restructuring |
| **Migration** | 301 mapping; canonical; see **canonical-tag** |
| **Large site** | Dynamic URLs, params, multi-language — canonical + robots |
| **SEO audit** | Check structure, params, canonical consistency |

## URL Patterns by Page Type

| Page Type | Pattern | Example |
|-----------|---------|---------|
| Homepage | `/` | `example.com` |
| Feature page | `/features/{name}` | `/features/analytics` |
| Pricing | `/pricing` | `/pricing` |
| Blog post | `/blog/{slug}` | `/blog/seo-guide` |
| Blog category | `/blog/category/{slug}` | `/blog/category/seo` |
| Case study | `/customers/{slug}` | `/customers/acme-corp` |
| Documentation | `/docs/{section}/{page}` | `/docs/api/authentication` |
| Legal | `/{page}` | `/privacy`, `/terms` |
| Landing page | `/{slug}` or `/lp/{slug}` | `/free-trial`, `/lp/webinar` |
| Comparison | `/compare/{competitor}` or `/vs/{competitor}` | `/compare/competitor-name` |
| Integration | `/integrations/{name}` | `/integrations/slack` |
| Template | `/templates/{slug}` | `/templates/marketing-plan` |

Pick one trailing-slash policy (with or without) and enforce it with redirects. Keep one parent per section: don't mix `/features/analytics` and `/product/automation`.

### Common Mistakes

- **Dates in blog URLs**: `/blog/2024/01/15/post-title` adds length and no value; use `/blog/post-title`
- **Over-nesting**: `/products/category/subcategory/item/detail`; flatten where possible
- **Changing URLs without redirects**: every old URL needs a 301 to its new URL, or backlink equity is lost and bookmarked links break
- **IDs in URLs**: `/product/12345`; use slugs
- **Query parameters for content**: `/blog?id=123` should be `/blog/post-title`

## Common Issues

| Issue | Fix |
|-------|-----|
| Long URLs | Shorten; remove redundant words |
| Dynamic params | Use canonical; clean params in robots (Yandex Clean-param) |
| Mixed case | Redirect to lowercase |
| Changed URLs | 301 redirect old to new |

## Output Format

- **URL structure** recommendation
- **Slug** conventions
- **Hierarchy** for key content types
- **Redirect** plan if changing URLs
- **References**: [Alignify URL optimization](https://alignify.co/zh/seo/url-optimization); [Google URL guidelines](https://developers.google.com/search/docs/crawling-indexing/url-structure)

## Related Skills

- **website-structure**: Plan structure and URL paths; apply url-structure rules after structure is defined

- **canonical-tag**: HTTPS, www, trailing slash — handles duplicate URL variants
- **url-slug**: Slug creation for content pages; length, keywords, format
- `implement/sub-skills/references/pages/marketing/commerce.md`: E-commerce category URL hierarchy, faceted URLs
- `implement/sub-skills/references/pages/marketing/commerce.md`: Product URL hierarchy
- `implement/sub-skills/references/pages/marketing/service-solution.md`: Service URL hierarchy
- **robots-txt**: Clean-param for query params
- **internal-links**: URL structure affects link patterns
