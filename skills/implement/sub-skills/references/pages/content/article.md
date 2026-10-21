---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/pagina
  based_on_version: main(239cb67)
  based_on_skill: article
---

# Article Page

## Scope

An article page presents one publication entry for focused reading, establishes its identity and credibility, supports rich content, and offers relevant continuation without overwhelming the article.

## Contract

Use the article's canonical title, description, author, publication and update dates, body, media, taxonomy, references, and URL. Keep editorial content as the source of truth and preserve publication history.

## Content

- **Core:** article identity and body.
- **Common:** metadata, cover media, breadcrumbs, author context, continuation.
- **Conditional:** summary, table of contents, sharing, tags, references, embeds, newsletter, related articles, FAQ.

## Product Adaptation

News emphasizes attribution, time, corrections, and recency. SaaS education may connect carefully to product use without turning the article into a landing page. Creator publications may foreground first-person authority and subscription. Technical content needs robust code, tables, media, and anchors.

## Composition

Optional reading aids depend on the article and publication policy; the body remains primary.

## Component candidates

- **Primary candidates:** [Article Content Layout](../../components/content/article-content-layout.md)
- **Common:** [Breadcrumb](../../components/navigation/breadcrumb.md), [Table of Contents](../../components/navigation/toc.md), [Author Bio](../../components/content/author-bio.md)
- **Conditional:** [Social Share](../../components/utility/social-share.md), [Newsletter Signup](../../components/conversion/newsletter-signup.md), [FAQ Section](../../components/content/faq-section.md)
- **Discouraged:** [Carousel](../../components/layout/carousel.md)

## Acceptance coverage

Short and long articles, heading anchors, code and tables, media and embeds, missing optional metadata, dates, canonical and social metadata, structured data, keyboard navigation, mobile reading, references, and related-content relevance.
