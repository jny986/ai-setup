# Page Guide Integration

[Pagina](https://github.com/kostja94/pagina) provides page intelligence for AI agents; its guidance lives in the [page guides](../../pages/GUIDE.md). Use it when the requested outcome is a complete new page with a page-level purpose, information hierarchy, multiple visible sections, component composition, route integration, and page verification.

The component guides remain responsible for constructing a missing component or bounded interface object. Each page guide links its recommended components to their component guides. The component guides do not duplicate those mappings.

Route the task to the page guides when:

- the user names a complete page type such as homepage, pricing, article, dashboard, settings, or 404;
- success depends on ordering several sections around one page task;
- the requested output includes page content, metadata, route behavior, states, and multiple components.

Keep the task in the component guides when one component or bounded interface object is the requested deliverable, even if it will later appear on a larger page.

The page guides build new pages only. Existing-page audits, optimization, patches, and reconstruction do not become page-guide tasks merely because they affect a whole page.
