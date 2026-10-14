---
name: internal-links
description: When the user wants to optimize internal linking, fix orphan pages, or improve link structure. Also use when the user mentions "internal links," "internal linking," "anchor text," "link equity," "internal linking strategy," or "orphan pages." For IA, use website-structure.
metadata:
  version: 1.0.1
---

# SEO On-Page: Internal Links

Guides internal linking strategy for SEO: crawlability, link equity distribution, and user navigation.

## Scope (On-Page SEO)

- **Internal links**: Contextual links; descriptive anchor text; related posts; hub pages
- **Breadcrumbs**: Implement for large sites (e.g. ecommerce); see **breadcrumb-generator**

## Initial Assessment

**Project context:** Read the product marketing context when present and load only what is relevant to this task. Otherwise use available project material or user-provided facts and ask for missing information.

Identify:
1. **Site structure**: Hub pages, pillar content, supporting pages
2. **Orphan pages**: Pages with no or few internal links
3. **Priority pages**: Pages that need more link equity

## Best Practices

### Link Structure

| Principle | Guideline |
|-----------|-----------|
| **Depth** | Important pages within 3 clicks from homepage |
| **Orphan pages** | Avoid; ensure every page has at least one internal link; see **site-crawlability** for technical detection and crawl issues |
| **Hub-to-spoke** | Link from hub/pillar pages to cluster articles; topic cluster structure |
| **Contextual** | Place links in relevant body content, not just footers |

### Anchor Text

| Principle | Guideline |
|-----------|-----------|
| **Descriptive** | Use anchor text that describes the target page |
| **Variation** | Avoid over-optimization; use natural variation |
| **Keyword** | Include target keyword when natural |

### Placement

| Location | Use |
|----------|-----|
| **First paragraph** | Primary link to related content |
| **Body** | Contextual links throughout |
| **Related/Recommended** | End-of-article links |
| **Navigation** | Key site sections |

## Link Types and Rules

| Type | Purpose | Example |
|------|---------|---------|
| **Navigational** | Move between sections | Header, footer, sidebar links |
| **Contextual** | Related content within text | "Learn more about [analytics](/features/analytics)" |
| **Hub-and-spoke** | Connect cluster content to hub | Blog posts linking to pillar page |
| **Cross-section** | Connect related pages across sections | Feature page linking to a related case study |

- **Volume**: roughly 5-10 internal links per 1,000 words (approximate guideline)
- **Priority pages**: link to the homepage, key feature pages and pricing more often
- **Breadcrumbs**: free internal links on every page; they should mirror the URL hierarchy
- **Related content**: add a "Related posts" or "You might also like" block at the bottom of articles

### Hub-and-Spoke Model

```
Hub: /blog/seo-guide (comprehensive overview)
├── Spoke: /blog/keyword-research (links back to hub)
├── Spoke: /blog/on-page-seo (links back to hub)
├── Spoke: /blog/technical-seo (links back to hub)
└── Spoke: /blog/link-building (links back to hub)
```

Each spoke links back to the hub. The hub links to all spokes. Spokes link to each other where relevant.

### Link Audit Checklist

- [ ] Every page has at least one inbound internal link
- [ ] No broken internal links (404s)
- [ ] Anchor text is descriptive (not "click here" or "read more")
- [ ] Important pages have the most inbound internal links
- [ ] Breadcrumbs are implemented on all pages
- [ ] Related content links exist on blog posts
- [ ] Cross-section links connect features to case studies, and blog to product pages

## Common Issues

| Issue | Fix |
|-------|-----|
| Orphan pages | Add internal links from hub pages or navigation; **site-crawlability** for technical audit |
| Too many links | Focus on most important; avoid link stuffing |
| Generic anchors | Use descriptive "learn more about X" instead of "click here" |
| Broken links | Audit and fix 404s; see **site-crawlability** for technical audit |

## Output Format

- **Internal link audit** (if auditing)
- **Link opportunities** for key pages
- **Anchor text** recommendations
- **Structure** improvements

## Related Skills

- **article-page-generator**: Related posts, contextual links, end-of-article recommendations
- **website-structure**: Plan page structure and hierarchy; informs internal linking
- **site-crawlability**: Internal links enable crawling
- **url-structure**: URL structure affects link patterns
- **content-strategy**: Topic clusters inform link structure; pillar <-> cluster; cluster <-> cluster
- **breadcrumb-generator**: Breadcrumbs are internal links; category hierarchy
