---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/pagina
  based_on_version: main(239cb67)
  based_on_skill: community
---

# Community Pages

## Scope

Community pages support discovery, participation, identity, and moderation among members. They must make audience, visibility, authorship, community rules, and moderation consequences legible.

## Modes

- **Community home:** orient members, expose active areas and current activity, and provide clear routes to browse or contribute.
- **Topic index:** support category-aware discovery, sorting, search, following, pagination, and empty or quiet states.
- **Thread detail:** preserve the original post, replies, authorship, chronology or ranking, accepted answers where applicable, and participation actions.
- **Member profile:** show only permitted identity, contribution history, reputation, roles, and relationship actions.
- **Compose:** create a post or reply with audience, category, formatting, attachment, preview, draft, and publication controls.

## Component candidates

**Community Home, Community Topic Index, Community Thread, Member Profile:**

- **Primary candidates:** [Navigation Menu](../../components/navigation/navigation-menu.md)
- **Common:** [Sidebar](../../components/navigation/sidebar.md), [Conversation](../../components/utility/conversation.md), [List](../../components/layout/list.md)
- **Conditional:** [Task Input](../../components/utility/task-input.md), [Author Bio](../../components/content/author-bio.md), [Announcement Banner](../../components/utility/top-banner.md), [Modal](../../components/conversion/popup.md)
- **Discouraged:** [Hero](../../components/branding/hero.md)

**Community Compose:**

- **Primary candidates:** [Task Input](../../components/utility/task-input.md)
- **Common:** [How-to Section](../../components/content/howto-section.md)
- **Conditional:** [Modal](../../components/conversion/popup.md), [Announcement Banner](../../components/utility/top-banner.md), [FAQ Section](../../components/content/faq-section.md)
- **Discouraged:** [Carousel](../../components/layout/carousel.md)

## Acceptance coverage

Authentication, membership and role permissions, blocked users, moderation and appeals, drafts, edits and deletion, mentions, notifications, attachments, reporting, rate limits, private communities, accessibility, pagination, deep links, and empty states.
