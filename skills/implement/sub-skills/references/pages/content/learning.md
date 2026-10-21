---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/pagina
  based_on_version: main(239cb67)
  based_on_skill: learning
---

# Learning Pages

## Scope

Learning pages help a learner choose, enroll in, progress through, and complete structured instruction. Curriculum, prerequisites, instructor identity, access, progress, and completion evidence must remain consistent across the learning system.

## Modes

- **Course catalog:** support discovery by subject, level, format, duration, instructor, price, and availability.
- **Course detail:** explain outcomes, audience, prerequisites, curriculum, instructor, format, schedule or access period, price, credentials, and enrollment path.
- **Learning dashboard:** show enrolled courses, current progress, deadlines, recent activity, and the most relevant resume action.
- **Lesson:** deliver one learning unit with orientation, content, resources, completion state, navigation, and accessible media or transcripts.
- **Assessment:** present instructions, attempts, questions, progress, submission, scoring or review, feedback, and recovery without leaking protected answers.
- **Certificate:** provide verifiable completion evidence with learner consent, issuer, course, issue date, credential identity, and revocation state.

## Component candidates

**Course Catalog:**

- **Common:** [Navigation Menu](../../components/navigation/navigation-menu.md), [Task Input](../../components/utility/task-input.md), [Grid](../../components/layout/grid.md), [List](../../components/layout/list.md)
- **Conditional:** [Sidebar](../../components/navigation/sidebar.md), [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md), [Card](../../components/layout/card.md)

**Course Detail, Certificate Page:**

- **Common:** [Breadcrumb](../../components/navigation/breadcrumb.md), [Card](../../components/layout/card.md)
- **Conditional:** [Carousel](../../components/layout/carousel.md), [Trust Signals](../../components/conversion/trust-badges.md), [Testimonials](../../components/conversion/testimonials.md), [Call to Action Section](../../components/conversion/cta.md)

**Learning Dashboard, Lesson Page:**

- **Primary candidates:** [Navigation Menu](../../components/navigation/navigation-menu.md)
- **Common:** [Sidebar](../../components/navigation/sidebar.md), [Breadcrumb](../../components/navigation/breadcrumb.md), [Table of Contents](../../components/navigation/toc.md)
- **Conditional:** [Article Content Layout](../../components/content/article-content-layout.md), [Tabs](../../components/content/tabs.md), [Accordion](../../components/content/accordion.md), [How-to Section](../../components/content/howto-section.md), [Task Input](../../components/utility/task-input.md), [Modal](../../components/conversion/popup.md)
- **Discouraged:** [Carousel](../../components/layout/carousel.md)

**Assessment Page:**

- **Primary candidates:** [Task Input](../../components/utility/task-input.md)
- **Common:** [How-to Section](../../components/content/howto-section.md)
- **Conditional:** [Modal](../../components/conversion/popup.md), [Announcement Banner](../../components/utility/top-banner.md), [FAQ Section](../../components/content/faq-section.md)
- **Discouraged:** [Carousel](../../components/layout/carousel.md)

## Acceptance coverage

Enrollment and entitlement, prerequisites, progress sync, autosave, attempt rules, timing, grading, accessibility, captions and transcripts, offline or reconnect behavior, completion thresholds, certificate verification, localization, and learner privacy.
