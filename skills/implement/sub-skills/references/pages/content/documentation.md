---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/pagina
  based_on_version: main(239cb67)
  based_on_skill: documentation
---

# Documentation And Glossary Pages

## Scope

Documentation pages help users learn, complete tasks, understand concepts, and recover from problems. Each reference covers an individual page. Documentation-wide architecture, navigation, version policy, and publishing topology belong to the project’s maintained documentation system.

## Modes

- **Docs home:** orient by audience and task, expose search and clear starting paths, and show version or product scope.
- **Docs article:** complete one task or explain one concept with prerequisites, steps, examples, expected results, failure recovery, and next references.
- **API reference:** document callable resources or endpoints from an authoritative schema, including authentication, parameters, examples, responses, errors, limits, and version.
- **Glossary index:** support browsing and search across maintained terminology.
- **Glossary term:** define one term in its domain context with examples, distinctions, related terms, and relevant product or learning links.

## Boundaries

The human-facing API introduction belongs to [Product Interface](product-interface.md); endpoint-level material belongs to the API reference mode here. A docs article is not a marketing article with code added. Glossary terms must resolve real language ambiguity rather than exist only to create URLs.

## Component candidates

**Documentation Home:**

- **Primary candidates:** [Navigation Menu](../../components/navigation/navigation-menu.md), [Sidebar](../../components/navigation/sidebar.md), [Task Input](../../components/utility/task-input.md)
- **Common:** [Grid](../../components/layout/grid.md), [Card](../../components/layout/card.md)
- **Conditional:** [Announcement Banner](../../components/utility/top-banner.md)
- **Discouraged:** [Hero](../../components/branding/hero.md)

**Documentation Article, API Reference:**

- **Primary candidates:** [Sidebar](../../components/navigation/sidebar.md), [Table of Contents](../../components/navigation/toc.md), [Breadcrumb](../../components/navigation/breadcrumb.md)
- **Common:** [How-to Section](../../components/content/howto-section.md)
- **Conditional:** [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md), [Task Input](../../components/utility/task-input.md)
- **Discouraged:** [Hero](../../components/branding/hero.md)

**Glossary Index:**

- **Common:** [Navigation Menu](../../components/navigation/navigation-menu.md), [Grid](../../components/layout/grid.md), [List](../../components/layout/list.md)
- **Conditional:** [Task Input](../../components/utility/task-input.md), [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md)

**Glossary Term:**

- **Common:** [Breadcrumb](../../components/navigation/breadcrumb.md), [Table of Contents](../../components/navigation/toc.md)
- **Conditional:** [How-to Section](../../components/content/howto-section.md), [Social Share](../../components/utility/social-share.md), [Call to Action Section](../../components/conversion/cta.md)

## Acceptance coverage

Source version, runnable examples, permissions, errors, deep links, search, navigation state, code overflow, copy actions, accessibility, indexing policy, stale notices, and version switching.
