# Documentation And Glossary Pages

## Shared Responsibility

Documentation pages help users learn, complete tasks, understand concepts, and recover from problems. The page guides own individual page contracts; a future Website Layer owns documentation-wide architecture, navigation, version policy, and publishing topology.

## Modes

- **Docs home:** orient by audience and task, expose search and clear starting paths, and show version or product scope.
- **Docs article:** complete one task or explain one concept with prerequisites, steps, examples, expected results, failure recovery, and next references.
- **API reference:** document callable resources or endpoints from an authoritative schema, including authentication, parameters, examples, responses, errors, limits, and version.
- **Glossary index:** support browsing and search across maintained terminology.
- **Glossary term:** define one term in its domain context with examples, distinctions, related terms, and relevant product or learning links.

## Boundaries

The human-facing API introduction page remains `api`; endpoint-level material uses `api-reference`. A docs article is not a marketing article with code added. Glossary terms must resolve real language ambiguity rather than exist only to create URLs.

## Components And Verification

Sidebar, Navigation, Breadcrumb, Table of Contents, Task Input or Search, Tabs, How-to, code surfaces supplied by the host project, feedback, and related links may apply. Verify source version, runnable examples, permissions, errors, deep links, search, navigation state, code overflow, copy actions, accessibility, indexing policy, stale notices, and version switching.

## Components

Catalog recommendations; links go to the component guides in this tree.

- Documentation Home (`docs-home`): **Core:** [Navigation Menu](../../../components/navigation/navigation-menu/GUIDE.md), [Sidebar](../../../components/navigation/sidebar/GUIDE.md), [Task Input](../../../components/utility/task-input/GUIDE.md); **Common:** [Grid](../../../components/layout/grid/GUIDE.md), [Card](../../../components/layout/card/GUIDE.md); **Conditional:** [Announcement Banner](../../../components/utility/top-banner/GUIDE.md); **Discouraged:** [Hero](../../../components/branding/hero/GUIDE.md)
- Documentation Article (`docs-article`): **Core:** [Sidebar](../../../components/navigation/sidebar/GUIDE.md), [Table of Contents](../../../components/navigation/toc/GUIDE.md), [Breadcrumb](../../../components/navigation/breadcrumb/GUIDE.md); **Common:** [How-to Section](../../../components/content/howto-section/GUIDE.md); **Conditional:** [Tabs](../../../components/content/tabs/GUIDE.md), [Accordion](../../../components/content/accordion/GUIDE.md), [Task Input](../../../components/utility/task-input/GUIDE.md); **Discouraged:** [Hero](../../../components/branding/hero/GUIDE.md)
- API Reference (`api-reference`): **Core:** [Sidebar](../../../components/navigation/sidebar/GUIDE.md), [Table of Contents](../../../components/navigation/toc/GUIDE.md), [Breadcrumb](../../../components/navigation/breadcrumb/GUIDE.md); **Common:** [How-to Section](../../../components/content/howto-section/GUIDE.md); **Conditional:** [Tabs](../../../components/content/tabs/GUIDE.md), [Accordion](../../../components/content/accordion/GUIDE.md), [Task Input](../../../components/utility/task-input/GUIDE.md); **Discouraged:** [Hero](../../../components/branding/hero/GUIDE.md)
- Glossary Index (`glossary-index`): **Common:** [Navigation Menu](../../../components/navigation/navigation-menu/GUIDE.md), [Grid](../../../components/layout/grid/GUIDE.md), [List](../../../components/layout/list/GUIDE.md); **Conditional:** [Task Input](../../../components/utility/task-input/GUIDE.md), [Tabs](../../../components/content/tabs/GUIDE.md), [Accordion](../../../components/content/accordion/GUIDE.md)
- Glossary Term (`glossary-term`): **Common:** [Breadcrumb](../../../components/navigation/breadcrumb/GUIDE.md), [Table of Contents](../../../components/navigation/toc/GUIDE.md); **Conditional:** [How-to Section](../../../components/content/howto-section/GUIDE.md), [Social Share](../../../components/utility/social-share/GUIDE.md), [Call to Action Section](../../../components/conversion/cta/GUIDE.md)
