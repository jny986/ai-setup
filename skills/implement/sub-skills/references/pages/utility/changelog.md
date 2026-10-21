---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/pagina
  based_on_version: main(239cb67)
  based_on_skill: changelog
---

# Changelog Pages

## Scope

Changelog pages communicate shipped product changes. They do not promise future work, replace technical release notes for maintainers, or turn every update into a marketing article.

## Index Mode

Help users scan updates by date, product, category, or importance. Core capabilities are ordered entries, concise summaries, stable detail links where provided, and continuation for a growing archive.

## Entry Mode

Explain one shipped change with release date, affected users, availability, limitations, migration or action required, media, and related documentation. Preserve amendments and correction dates.

## Source

Release entries come from the product’s maintained release content source.

## Component candidates

**Changelog Index:**

- **Primary candidates:** [List](../../components/layout/list.md)
- **Common:** [Card](../../components/layout/card.md)
- **Conditional:** [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md), [Announcement Banner](../../components/utility/top-banner.md)

**Changelog Entry:**

- **Common:** [Breadcrumb](../../components/navigation/breadcrumb.md)
- **Conditional:** [Social Share](../../components/utility/social-share.md), [Call to Action Section](../../components/conversion/cta.md), [Announcement Banner](../../components/utility/top-banner.md)

## Acceptance coverage

Ordering, draft exclusion, dates and time zones, categories, pagination, canonical URLs, feeds when present, media, product availability, and links from Index to Entry.
