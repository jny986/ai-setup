---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/pagina
  based_on_version: main(239cb67)
  based_on_skill: create-edit
---

# Create And Edit Page

## Scope

A create and edit page lets users produce or change one domain object with clear validation, persistence, review, and completion behavior. It is not the object's read-only detail page and should not become a general settings surface.

## Contract

Define schema, defaults, required fields, validation timing, save model, draft behavior, permissions, conflicts, uploads, preview, cancellation, success destination, and destructive consequences.

## Content

- **Core:** object fields, validation, persistence controls, completion path.
- **Common:** grouped fields, status, contextual guidance, unsaved-change handling.
- **Conditional:** preview, autosave, version conflict, media, collaboration, approvals, scheduling, advanced options.

## Product Adaptation

CMS and creator products may require a full editor workspace, metadata, preview, revisions, and publishing. CRM forms emphasize structured fields and relationship creation. Ecommerce editors emphasize variants, media, pricing, inventory, and fulfillment. Simple SaaS objects may need a compact form rather than a workspace.

## Composition

Established form and editor libraries are appropriate for complex validation, rich documents, history, collaboration, or accessibility.

## Component candidates

- **Common:** [Sidebar](../../components/navigation/sidebar.md), [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md)
- **Conditional:** [Modal](../../components/conversion/popup.md), [Announcement Banner](../../components/utility/top-banner.md), [CMS Editor Workspace](../../components/layout/cms-editor-workspace.md)
- **Discouraged:** [Hero](../../components/branding/hero.md), [Carousel](../../components/layout/carousel.md)

## Acceptance coverage

New and existing values where the shared form supports both, required and invalid fields, server errors, autosave interruption, stale revisions, uploads, permissions, cancellation, destructive actions, keyboard and composition input, mobile constraints, and the post-save destination.
