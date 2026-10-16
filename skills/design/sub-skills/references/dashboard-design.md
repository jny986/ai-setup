---
name: dashboard-design
description: "Design task-focused dashboards with clear data hierarchy, navigation, tables, charts, and interaction states."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: dashboard-design
---

# Dashboard Design

Information-dense admin and analytics UI: app shell, KPI tiles, charts, tables, status badges, real-time indicators, responsive behavior. Base rules (states, forms, accessibility, breakpoints) are in [ui-design](ui-design.md); marketing feature cards in [card-design](card-design.md).

Read `DESIGN.md` for UI tokens and the project brand kit for approved brand primitives (see [design-context](design-context.md)); when absent, inspect the project's existing CSS variables or Tailwind theme. The `indigo-*` / `gray-*` classes below are placeholders for primary and neutral tokens. Map success, warning, and error tokens to status badges; derive chart colors from primary, secondary, and accent. Settle what data is shown, who uses it, and what actions they take before laying out.

## Layout

### Sidebar plus main content (most common)

```html
<div class="flex h-screen bg-gray-50">
  <!-- Hidden below lg; opens as an overlay drawer from a menu button -->
  <aside class="hidden lg:flex w-64 shrink-0 bg-white border-r border-gray-200 flex-col">
    <div class="h-16 flex items-center px-6 border-b border-gray-100">
      <img src="/logo.svg" alt="App" class="h-8" />
    </div>
    <nav aria-label="Main" class="flex-1 py-4 px-3 space-y-1 overflow-y-auto">
      <a href="#" aria-current="page" class="flex items-center gap-3 px-3 py-2 rounded-lg
        bg-indigo-50 text-indigo-700 font-medium text-sm">
        <svg class="w-5 h-5" aria-hidden="true"><!-- icon --></svg>
        Dashboard
      </a>
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg
        text-gray-600 hover:bg-gray-100 hover:text-gray-900 text-sm transition-colors">
        <svg class="w-5 h-5" aria-hidden="true"><!-- icon --></svg>
        Analytics
      </a>
      <div class="pt-4 pb-1 px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider">
        Settings
      </div>
    </nav>
    <div class="p-4 border-t border-gray-100">
      <div class="flex items-center gap-3">
        <img src="/avatar.jpg" alt="" class="w-8 h-8 rounded-full" />
        <div class="text-sm">
          <div class="font-medium text-gray-900">Jane Doe</div>
          <div class="text-gray-500 text-xs">Admin</div>
        </div>
      </div>
    </div>
  </aside>

  <main class="flex-1 min-w-0 overflow-y-auto">
    <header class="h-16 bg-white border-b border-gray-200 flex items-center
      justify-between px-6 sticky top-0 z-10">
      <h1 class="text-lg font-semibold text-gray-900">Dashboard</h1>
      <div class="flex items-center gap-4"><!-- search, notifications, profile --></div>
    </header>
    <div class="p-6"><!-- content --></div>
  </main>
</div>
```

Sidebar behavior (breakpoints per [ui-design](ui-design.md)):

- lg+: always visible, 240-280px.
- md: collapsible to 64px icon-only with tooltip labels.
- Below md: hidden; opens as an overlay drawer with backdrop from a labelled menu button (`aria-expanded`, focus moved into the drawer, Esc closes).

### Top nav plus grid

For simpler dashboards with few nav items: horizontal bar on top, content below, tabs or pills for sub-sections.

## KPI Tiles

```html
<div class="bg-white rounded-xl border border-gray-200 p-6">
  <div class="flex items-center justify-between">
    <span class="text-sm font-medium text-gray-500">Total Revenue</span>
    <span class="w-10 h-10 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center">
      <svg class="w-5 h-5" aria-hidden="true"><!-- dollar icon --></svg>
    </span>
  </div>
  <div class="mt-3"><span class="text-3xl font-bold text-gray-900">$45,231</span></div>
  <div class="mt-2 flex items-center gap-1.5 text-sm">
    <span class="text-emerald-600 font-medium flex items-center gap-0.5">
      <svg class="w-4 h-4" aria-hidden="true"><!-- arrow-up icon --></svg>
      <span class="sr-only">Up</span> +12.5%
    </span>
    <span class="text-gray-500">vs last month</span>
  </div>
</div>
```

```html
<div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4 md:gap-6">
  <!-- 4 stat cards -->
</div>
```

Variants:

- Sparkline: small inline chart under the number.
- Progress bar: completion toward a goal.
- Mini table: top 3 items under the stat.
- Negative trend: red with down-arrow and minus sign; never color alone.
- Loading: a same-size skeleton tile, not a spinner, so the grid doesn't shift.

## Chart Selection

| Data | Chart | Use for |
|------|-------|---------|
| Trend over time | Line | Revenue, users, performance |
| Comparison | Bar | Categories, A/B results |
| Composition | Pie / donut | Budget, traffic sources (max 5 slices) |
| Volume over time | Area | Bandwidth, cumulative metrics |
| Distribution | Histogram | Age or price ranges |
| Relationship | Scatter | Correlation of two variables |
| Progress | Progress bar / gauge | Goals, quotas |
| Ranking | Horizontal bar | Top pages, top products |

Rules:

1. Title each chart with what it shows, not how to read it.
2. Label axes, with units.
3. At most 5-6 colors, derived from brand tokens. Each series needs 3:1 against the chart background (WCAG 1.4.11); add direct labels or patterns so color isn't the only cue.
4. Bar charts start the Y-axis at zero; line charts may use non-zero baselines.
5. Tooltips for exact values.
6. Light dashed grid lines, used sparingly.
7. Charts resize; they don't overflow.

```css
:root {
  /* Lightness up to ~65% keeps 3:1 against white; lighten 10-15% for dark backgrounds */
  --chart-1: var(--color-primary);
  --chart-2: oklch(58% 0.12 185);  /* teal */
  --chart-3: oklch(58% 0.19 350);  /* pink */
  --chart-4: oklch(64% 0.15 60);   /* amber */
  --chart-5: oklch(55% 0.14 145);  /* green */
}
```

For infographic-style data graphics see [infographic](infographic.md).

## Data Tables

```html
<div class="bg-white rounded-xl border border-gray-200 overflow-hidden">
  <div class="px-6 py-4 border-b border-gray-100 flex items-center justify-between">
    <div class="flex items-center gap-3">
      <h2 class="font-semibold text-gray-900">Recent Orders</h2>
      <span class="bg-gray-100 text-gray-600 text-xs font-medium px-2.5 py-0.5 rounded-full">2,847</span>
    </div>
    <div class="flex items-center gap-2">
      <input type="search" placeholder="Search orders..." aria-label="Search orders"
        class="text-sm border border-gray-300 rounded-lg px-3 py-1.5 w-full sm:w-56
        focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20" />
      <button type="button" class="text-sm text-gray-600 border border-gray-300 rounded-lg
        px-3 py-1.5 hover:bg-gray-50 flex items-center gap-1.5">
        <svg class="w-4 h-4" aria-hidden="true"><!-- filter icon --></svg>
        Filters
      </button>
    </div>
  </div>

  <!-- Scroll wrapper so wide tables never break the page -->
  <div class="overflow-x-auto">
    <table class="w-full text-sm">
      <caption class="sr-only">Recent orders</caption>
      <thead>
        <tr class="border-b border-gray-100 text-left">
          <th scope="col" aria-sort="ascending" class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">
            <button type="button" class="flex items-center gap-1 hover:text-gray-700">
              Customer
              <svg class="w-3 h-3" aria-hidden="true"><!-- sort icon --></svg>
            </button>
          </th>
          <th scope="col" class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
          <th scope="col" class="px-6 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider text-right">Amount</th>
          <th scope="col" class="px-6 py-3 w-12"><span class="sr-only">Actions</span></th>
        </tr>
      </thead>
      <tbody class="divide-y divide-gray-50">
        <tr class="hover:bg-gray-50 transition-colors">
          <td class="px-6 py-4">
            <div class="flex items-center gap-3">
              <img src="/avatar.jpg" alt="" class="w-8 h-8 rounded-full" />
              <div>
                <div class="font-medium text-gray-900">Jane Cooper</div>
                <div class="text-gray-500 text-xs">jane@example.com</div>
              </div>
            </div>
          </td>
          <td class="px-6 py-4">
            <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full
              text-xs font-medium bg-emerald-50 text-emerald-700">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>Completed
            </span>
          </td>
          <td class="px-6 py-4 text-right font-medium text-gray-900 tabular-nums">$2,500.00</td>
          <td class="px-6 py-4">
            <button type="button" aria-label="Actions for Jane Cooper" aria-haspopup="menu"
              class="p-1.5 rounded-md text-gray-500 hover:text-gray-700 hover:bg-gray-100">
              <svg class="w-5 h-5" aria-hidden="true"><!-- dots icon --></svg>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <nav aria-label="Pagination" class="px-6 py-4 border-t border-gray-100 flex items-center justify-between text-sm">
    <span class="text-gray-500">Showing 1-10 of 2,847</span>
    <div class="flex gap-1">
      <button type="button" class="px-3 py-1.5 rounded-lg border border-gray-200 text-gray-600
        hover:bg-gray-50 disabled:opacity-50" disabled>Previous</button>
      <button type="button" class="px-3 py-1.5 rounded-lg bg-indigo-600 text-white" aria-current="page">1</button>
      <button type="button" class="px-3 py-1.5 rounded-lg border border-gray-200 text-gray-600 hover:bg-gray-50">2</button>
      <button type="button" class="px-3 py-1.5 rounded-lg border border-gray-200 text-gray-600 hover:bg-gray-50">Next</button>
    </div>
  </nav>
</div>
```

Rules:

- Numbers right-aligned, text left-aligned.
- Row hover highlight.
- Sticky header on scroll: `sticky top-0` on `<th>` with a solid background, or rows show through.
- Sortable columns: `<button>` inside `<th>`, `aria-sort` on the sorted column.
- Subtle dividers preferred over zebra striping.
- Row actions: three-dots icon button opening a dropdown.

## Status Indicators

Dot plus text, never color alone.

```html
<!-- Success -->
<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-50 text-emerald-700">
  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>Active
</span>
<!-- Warning -->
<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-medium bg-amber-50 text-amber-700">
  <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>Pending
</span>
<!-- Error -->
<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-50 text-red-700">
  <span class="w-1.5 h-1.5 rounded-full bg-red-500"></span>Failed
</span>
<!-- Neutral -->
<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-600">
  <span class="w-1.5 h-1.5 rounded-full bg-gray-400"></span>Draft
</span>
```

Progress bar:

```html
<div class="w-full bg-gray-100 rounded-full h-2" role="progressbar" aria-valuenow="65" aria-valuemin="0" aria-valuemax="100" aria-label="Goal progress">
  <div class="bg-indigo-600 h-2 rounded-full transition-all duration-500" style="width: 65%"></div>
</div>
```

## Dark Mode Dashboards

Monitoring and ops dashboards often run dark. Use the surface, text, and border tokens from [dark-mode](dark-mode.md) (base, surface, elevated); don't define a second set.

- Show elevation with lighter surfaces, not shadows.
- Reduce chart saturation about 15% and raise lightness so series still hit 3:1 on the dark surface.
- Borders: semi-transparent, `oklch(100% 0 0 / 0.08)`.
- Active sidebar item: lighter background, not colored.

## Real-Time Indicators

```html
<span class="relative flex h-2.5 w-2.5" aria-hidden="true">
  <span class="motion-safe:animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
  <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span>
</span>

<span class="text-xs text-gray-500 flex items-center gap-1.5" role="status">
  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500" aria-hidden="true"></span>
  Live: updated 3s ago
</span>
```

Auto-refresh:

- Show a subtle countdown or progress bar before refresh.
- Flash changed values (green up, red down); update individual data points, never the whole page.
- Keep fast-changing numbers out of `aria-live` regions; announce only meaningful events ("3 new orders").

## Dense Information Without Clutter

1. Progressive disclosure: summary first, expand for detail.
2. Tabbed sections instead of everything at once.
3. Collapsible panels.
4. Tooltips for extra context only, not essential labels; they must open on keyboard focus and tap.
5. 4px-base spacing scale from [ui-design](ui-design.md).
6. Body text 13-14px, never below 12px.
7. `tabular-nums` (`font-variant-numeric: tabular-nums`) on table and KPI numbers so digits align.

## Responsive Layouts

- Below 768px: single column, cards stack, tables become card lists, sidebar hidden.
- 768-1024px: 2-column grid, icon-only sidebar, simplified charts.
- 1024px+: full layout, expanded sidebar, multi-column grids.
- 1536px+: add a column rather than stretching; cap text-heavy content around 1440px.

Mobile table alternative: below `md`, hide the table wrapper (`hidden md:block`) and render each row as label-value pairs.

```html
<dl class="md:hidden bg-white rounded-xl border border-gray-200 p-4 space-y-2 text-sm">
  <div class="flex justify-between">
    <dt class="text-gray-500">Customer</dt>
    <dd class="font-medium text-gray-900">Jane Cooper</dd>
  </div>
  <div class="flex justify-between">
    <dt class="text-gray-500">Status</dt>
    <dd><span class="bg-emerald-50 text-emerald-700 text-xs px-2 py-0.5 rounded-full">Active</span></dd>
  </div>
  <div class="flex justify-between">
    <dt class="text-gray-500">Amount</dt>
    <dd class="font-medium text-gray-900">$2,500.00</dd>
  </div>
</dl>
```

## Verification

Render at 390px, 768px, and 1440px and view each. At 768px confirm the sidebar collapses, tables scroll or become cards, and charts resize. Tab through for visible focus. Check the dark theme if built.

## Checklist

- [ ] Sidebar nav with clear active state and section grouping
- [ ] KPI cards at top with trend indicators
- [ ] Charts have titles, labels, tooltips
- [ ] Tables have sort, search, filter, pagination
- [ ] Status badges use consistent color coding
- [ ] Works on tablet and mobile
- [ ] Loading skeletons for all async data
- [ ] Empty states for tables and charts with no data
- [ ] Dark mode considered (especially monitoring)
- [ ] Numbers use `tabular-nums`
- [ ] Icon-only buttons and search inputs have accessible names; trends don't rely on color alone
- [ ] Rendered at 390px, 768px, 1440px
