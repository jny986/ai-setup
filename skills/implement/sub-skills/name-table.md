# Implement name table

Use these names as `/implement <name>`, or resolve them when a feature needs page/component guidance. The router preserves the request’s scope; [root Implementation steps](../SKILL.md#implementation) select the surface workflow and matching reference.

## Reference names

Reference catalogs and page/component types reached through the implement router. `page` and `component` select their sub-skills; their rows here index the corresponding catalogs. Names resolve directly, without aliases. Paths are relative to `skills/`. Pages come from kostja94/pagina `page-builder/references/pages/`, components from kostja94/bricks `component-builder/references/components/`; the Source column names the reference and the kostja stubs it replaces.

| Name | Path | Source |
|---|---|---|
| `page` | `implement/sub-skills/references/pages.md` | pagina `page-builder` (+workflow, quality-gates, delivery-localization; contextus dropped) |
| `about` | `implement/sub-skills/references/pages/brand/about.md` | pagina `about` (stub `pages/brand/about`) |
| `contact` | `implement/sub-skills/references/pages/brand/contact.md` | pagina `contact` (stub `pages/brand/contact`) |
| `homepage` | `implement/sub-skills/references/pages/brand/home.md` | pagina `homepage` (stub `pages/brand/home`) |
| `community` | `implement/sub-skills/references/pages/brand/community.md` | pagina `community` (no stub) |
| `portfolio` | `implement/sub-skills/references/pages/brand/portfolio.md` | pagina `portfolio` (no stub) |
| `product-interface` | `implement/sub-skills/references/pages/content/product-interface.md` | pagina `product-interface` (stubs `pages/content/api`, `pages/marketing/download`) |
| `article` | `implement/sub-skills/references/pages/content/article.md` | pagina `article` (stub `pages/content/article`) |
| `blog-index` | `implement/sub-skills/references/pages/content/blog.md` | pagina `blog-index` (stub `pages/content/blog`) |
| `documentation` | `implement/sub-skills/references/pages/content/documentation.md` | pagina `documentation` (stubs `pages/content/docs`, `pages/content/glossary`) |
| `faq` | `implement/sub-skills/references/pages/content/faq.md` | pagina `faq` (stub `pages/content/faq`) |
| `product-capability` | `implement/sub-skills/references/pages/content/features.md` | pagina `product-capability` (stub `pages/content/features`) |
| `resource` | `implement/sub-skills/references/pages/content/resources.md` | pagina `resource` (stub `pages/content/resources`) |
| `template` | `implement/sub-skills/references/pages/content/template-page.md` | pagina `template` (stub `pages/content/template-page`) |
| `tool` | `implement/sub-skills/references/pages/content/tools.md` | pagina `tool` (stub `pages/content/tools`) |
| `collection` | `implement/sub-skills/references/pages/content/collection.md` | pagina `collection` (no stub) |
| `detail` | `implement/sub-skills/references/pages/content/detail.md` | pagina `detail` (no stub) |
| `learning` | `implement/sub-skills/references/pages/content/learning.md` | pagina `learning` (no stub) |
| `publication` | `implement/sub-skills/references/pages/content/publication.md` | pagina `publication` (no stub) |
| `legal-policy` | `implement/sub-skills/references/pages/legal/legal-policy.md` | pagina `legal-policy` (stubs `pages/legal/{cookie-policy,legal,privacy,refund,shipping,terms}`) |
| `trust-security-compliance` | `implement/sub-skills/references/pages/legal/trust-security-compliance.md` | pagina `trust-security-compliance` (no stub) |
| `program` | `implement/sub-skills/references/pages/marketing/program.md` | pagina `program` (stubs `pages/marketing/{affiliate-program,startups}`) |
| `comparison` | `implement/sub-skills/references/pages/marketing/alternatives.md` | pagina `comparison` (stub `pages/marketing/alternatives`) |
| `commerce` | `implement/sub-skills/references/pages/marketing/commerce.md` | pagina `commerce` (stubs `pages/marketing/{category-pages,products}`) |
| `campaign` | `implement/sub-skills/references/pages/marketing/contest.md` | pagina `campaign` (stub `pages/marketing/contest`) |
| `case-study` | `implement/sub-skills/references/pages/marketing/customer-stories.md` | pagina `case-study` (stub `pages/marketing/customer-stories`) |
| `integration` | `implement/sub-skills/references/pages/marketing/integrations.md` | pagina `integration` (stub `pages/marketing/integrations`) |
| `landing` | `implement/sub-skills/references/pages/marketing/landing-page.md` | pagina `landing` (stub `pages/marketing/landing-page`) |
| `press` | `implement/sub-skills/references/pages/marketing/press.md` | pagina `press` (stubs `pages/marketing/{media-kit,press-coverage}`) |
| `migration` | `implement/sub-skills/references/pages/marketing/migration.md` | pagina `migration` (stub `pages/marketing/migration`) |
| `pricing` | `implement/sub-skills/references/pages/marketing/pricing.md` | pagina `pricing` (stub `pages/marketing/pricing`) |
| `service-solution` | `implement/sub-skills/references/pages/marketing/service-solution.md` | pagina `service-solution` (stubs `pages/marketing/{services,solutions}`) |
| `showcase` | `implement/sub-skills/references/pages/marketing/showcase.md` | pagina `showcase` (stub `pages/marketing/showcase`) |
| `use-case` | `implement/sub-skills/references/pages/marketing/use-cases.md` | pagina `use-case` (stub `pages/marketing/use-cases`) |
| `marketplace-directory` | `implement/sub-skills/references/pages/marketing/marketplace-directory.md` | pagina `marketplace-directory` (no stub) |
| `404` | `implement/sub-skills/references/pages/utility/404.md` | pagina `404` (stub `pages/utility/404`) |
| `careers` | `implement/sub-skills/references/pages/utility/careers.md` | pagina `careers` (stub `pages/utility/careers`) |
| `changelog` | `implement/sub-skills/references/pages/utility/changelog.md` | pagina `changelog` (stub `pages/utility/changelog`) |
| `feedback-disclosure` | `implement/sub-skills/references/pages/utility/feedback-disclosure.md` | pagina `feedback-disclosure` (stubs `pages/utility/{disclosure,feedback}`) |
| `auth` | `implement/sub-skills/references/pages/utility/signup-login.md` | pagina `auth` (stub `pages/utility/signup-login`) |
| `status` | `implement/sub-skills/references/pages/utility/status.md` | pagina `status` (stub `pages/utility/status`) |
| `create-edit` | `implement/sub-skills/references/pages/utility/create-edit.md` | pagina `create-edit` (no stub) |
| `dashboard` | `implement/sub-skills/references/pages/utility/dashboard.md` | pagina `dashboard` (no stub) |
| `roadmap` | `implement/sub-skills/references/pages/utility/roadmap.md` | pagina `roadmap` (no stub) |
| `settings` | `implement/sub-skills/references/pages/utility/settings.md` | pagina `settings` (no stub) |
| `component` | `implement/sub-skills/references/components.md` | bricks `component-builder` (+workflow, quality-gates, foundational-controls, pagina) |
| `favicon` | `implement/sub-skills/references/components/branding/favicon.md` | kostja `components/branding/favicon` (`favicon-generator`) |
| `hero` | `implement/sub-skills/references/components/branding/hero.md` | bricks `hero` (stub `components/branding/hero`) |
| `logo` | `implement/sub-skills/references/components/branding/logo.md` | bricks `logo` (stub `components/branding/logo`) |
| `comparison-table` | `implement/sub-skills/references/components/content/comparison-table.md` | bricks `comparison-table` (stub `components/content/comparison-table`) |
| `howto-section` | `implement/sub-skills/references/components/content/howto-section.md` | bricks `howto-section` (stub `components/content/howto-section`) |
| `tabs` | `implement/sub-skills/references/components/content/tabs.md` | bricks `tabs` (stub `components/content/tab-accordion`, split) |
| `accordion` | `implement/sub-skills/references/components/content/accordion.md` | bricks `accordion` (stub `components/content/tab-accordion`, split) |
| `article-content-layout` | `implement/sub-skills/references/components/content/article-content-layout.md` | bricks `article-content-layout` (no stub) |
| `author-bio` | `implement/sub-skills/references/components/content/author-bio.md` | bricks `author-bio` (no stub) |
| `faq-section` | `implement/sub-skills/references/components/content/faq-section.md` | bricks `faq-section` (no stub) |
| `post-collection` | `implement/sub-skills/references/components/content/post-collection.md` | bricks `post-collection` (no stub) |
| `cta-section` | `implement/sub-skills/references/components/conversion/cta.md` | bricks `cta-section` (stub `components/conversion/cta`) |
| `newsletter-signup` | `implement/sub-skills/references/components/conversion/newsletter-signup.md` | bricks `newsletter-signup` (stub `components/conversion/newsletter-signup`) |
| `modal` | `implement/sub-skills/references/components/conversion/popup.md` | bricks `modal` (stub `components/conversion/popup`) |
| `testimonials` | `implement/sub-skills/references/components/conversion/testimonials.md` | bricks `testimonials` (stub `components/conversion/testimonials`) |
| `trust-signals` | `implement/sub-skills/references/components/conversion/trust-badges.md` | bricks `trust-signals` (stub `components/conversion/trust-badges`) |
| `card` | `implement/sub-skills/references/components/layout/card.md` | bricks `card` (stub `components/layout/card`) |
| `carousel` | `implement/sub-skills/references/components/layout/carousel.md` | bricks `carousel` (stub `components/layout/carousel`) |
| `grid` | `implement/sub-skills/references/components/layout/grid.md` | bricks `grid` (stub `components/layout/grid`) |
| `list` | `implement/sub-skills/references/components/layout/list.md` | bricks `list` (stub `components/layout/list`) |
| `masonry` | `implement/sub-skills/references/components/layout/masonry.md` | bricks `masonry` (stub `components/layout/masonry`) |
| `agent-workspace` | `implement/sub-skills/references/components/layout/agent-workspace.md` | bricks `agent-workspace` (no stub) |
| `cms-editor-workspace` | `implement/sub-skills/references/components/layout/cms-editor-workspace.md` | bricks `cms-editor-workspace` (no stub) |
| `breadcrumb` | `implement/sub-skills/references/components/navigation/breadcrumb.md` | bricks `breadcrumb` (stub `components/navigation/breadcrumb`) |
| `footer` | `implement/sub-skills/references/components/navigation/footer.md` | bricks `footer` (stub `components/navigation/footer`) |
| `navigation-menu` | `implement/sub-skills/references/components/navigation/navigation-menu.md` | bricks `navigation-menu` (stub `components/navigation/navigation-menu`) |
| `sidebar` | `implement/sub-skills/references/components/navigation/sidebar.md` | bricks `sidebar` (stub `components/navigation/sidebar`) |
| `table-of-contents` | `implement/sub-skills/references/components/navigation/toc.md` | bricks `table-of-contents` (stub `components/navigation/toc`) |
| `social-share` | `implement/sub-skills/references/components/utility/social-share.md` | bricks `social-share` (stub `components/utility/social-share`) |
| `announcement-banner` | `implement/sub-skills/references/components/utility/top-banner.md` | bricks `announcement-banner` (stub `components/utility/top-banner`) |
| `chat-panel` | `implement/sub-skills/references/components/utility/chat-panel.md` | bricks `chat-panel` (no stub) |
| `conversation` | `implement/sub-skills/references/components/utility/conversation.md` | bricks `conversation` (no stub) |
| `task-input` | `implement/sub-skills/references/components/utility/task-input.md` | bricks `task-input` (no stub) |
