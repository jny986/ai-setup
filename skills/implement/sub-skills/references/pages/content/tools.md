---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/pagina
  based_on_version: main(239cb67)
  based_on_skill: tool
---

# Tool Pages

## Scope

Tool pages let a visitor complete a bounded task on the page. The working input-to-output experience is primary; explanatory and commercial content must support that task rather than bury it.

## Modes

- **Hub:** organize calculators, checkers, converters, generators, analyzers, or other utilities around user tasks.
- **Detail:** provide one functioning tool with inputs, constraints, processing state, results, recovery, explanation, and a relevant next step.

## Boundaries

A Tool page performs work. A Feature page explains a product capability, and a Resource page provides an asset or information. A tool may lead into a paid product, but it must deliver the promised result before asking for an unjustified signup.

## Component candidates

**Tool Hub:**

- **Common:** [Grid](../../components/layout/grid.md), [Card](../../components/layout/card.md), [Task Input](../../components/utility/task-input.md)
- **Conditional:** [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md), [Navigation Menu](../../components/navigation/navigation-menu.md)

**Tool Detail:**

- **Primary candidates:** [Task Input](../../components/utility/task-input.md)
- **Common:** [How-to Section](../../components/content/howto-section.md)
- **Conditional:** [Agent Workspace](../../components/layout/agent-workspace.md), [FAQ Section](../../components/content/faq-section.md), [Modal](../../components/conversion/popup.md), [Call to Action Section](../../components/conversion/cta.md)

## Acceptance coverage

Validation, loading, failure, limits, privacy, data retention, accessibility, mobile input, deterministic or AI uncertainty, result export, abuse controls, authentication gates, analytics, metadata, and truthful conversion claims.
