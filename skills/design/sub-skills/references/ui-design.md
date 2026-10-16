---
name: ui-design
description: "Design web UI components and screens with coherent hierarchy, states, navigation, forms, accessibility, and responsive behavior."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: ui-design
---

# UI Design Patterns

Core patterns for components and app screens: tokens, hierarchy, states, forms, navigation, feedback, accessibility, responsive rules. The other UI references build on this one.

Read `DESIGN.md` for UI tokens and the project brand kit for approved brand primitives (see [design-context](design-context.md)); when absent, inspect the project's existing CSS variables or Tailwind theme. The `indigo-*` / `gray-*` classes in examples are placeholders for the project's primary and neutral tokens. The style archetype sets radius, shadow depth, and how much of the trends section applies (Minimal and Corporate use none).

For adapting an existing interface to another context, read [adapt](adapt.md). Native apps follow [native-platforms](native-platforms.md); the HTML/CSS below applies to web UI. Choose hierarchy and expression using [surface-purpose](surface-purpose.md). Existing project conventions take precedence over the example scales, dimensions, counts, and layouts in this guide; use those as fallbacks and verify them against real content.

## Component Design Principles (Atomic Design)

Use these layers to locate responsibilities. Start at the layer the task needs and reuse existing components.

1. **Tokens**: colors, spacing, radii, shadows, type scale.
2. **Atoms**: button, input, badge, avatar, icon.
3. **Molecules**: search bar, form field (label + input + error), card header.
4. **Organisms**: nav bar, hero, comment thread, pricing table.
5. **Templates**: page layouts composed of organisms.
6. **Pages**: templates with real data.

Rules:

- Scope CSS custom properties to each component's root.
- Prefer composition over configuration: a `Card` with `children` beats a `Card` with 15 props.
- Components are stateless by default; lift state up.

```css
/* Token layer: values come from the design context (defaults shown) */
:root {
  --color-primary: #2563EB;
  --color-surface: #FFFFFF;
  --radius-md: 0.75rem;
  --shadow-sm: 0 1px 2px oklch(0% 0 0 / 0.05);
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
}
```

**Fallback spacing scale:** a 4px base offers 4, 8, 12, 16, 24, 32, 48, 64px (Tailwind `1, 2, 3, 4, 6, 8, 12, 16`). Preserve an established scale and justified optical or content-driven exceptions.

## Visual Hierarchy

Rank every element by importance, then apply these levers:

| Lever | High emphasis | Medium | Low |
|-------|--------------|--------|-----|
| Size | 2rem+ heading | 1rem body | 0.75rem caption |
| Weight | 700-800 | 500 | 400 |
| Color | Primary or high-contrast text | Muted (neutral-600) | Subtle (neutral-500, the lightest gray that passes 4.5:1 on white) |
| Spacing | More whitespace around it | Standard | Tighter |
| Position | Top-left or center | Mid-page | Bottom or sidebar |

Squint test: blur or zoom to 25%. The primary action and main heading must still be identifiable.

```html
<h1 class="text-4xl font-extrabold tracking-tight text-gray-950">Ship faster with AI</h1>
<p class="mt-4 text-lg text-gray-600 max-w-2xl">
  Build production-ready components in minutes, not hours.
</p>
<span class="text-xs text-gray-500 uppercase tracking-wide">Updated 2 hours ago</span>
```

## Interactive States

Every interactive element needs default, hover, active, focus-visible, and disabled.

```css
.btn-primary {
  background: var(--color-primary);
  color: white;
  border-radius: var(--radius-md);
  padding: var(--space-2) var(--space-4);
  font-weight: 600;
  transition: background-color 150ms ease, box-shadow 150ms ease, transform 150ms ease, filter 150ms ease;

  &:hover {
    filter: brightness(1.1);
    box-shadow: 0 4px 12px oklch(0% 0 0 / 0.15);
    transform: translateY(-1px);
  }
  &:active {
    transform: translateY(0);
    filter: brightness(0.95);
    box-shadow: var(--shadow-sm);
  }
  &:focus-visible {
    outline: 2px solid var(--color-primary);
    outline-offset: 2px;
  }
  /* No pointer-events: none; it hides the not-allowed cursor */
  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
    filter: none;
  }
}
```

Tailwind equivalent:

```html
<button class="bg-indigo-600 text-white px-4 py-2 rounded-lg font-semibold
  enabled:hover:bg-indigo-500 enabled:hover:-translate-y-0.5 enabled:hover:shadow-lg
  active:translate-y-0 active:bg-indigo-700
  focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600
  disabled:opacity-50 disabled:cursor-not-allowed
  transition-all duration-150">
  Click me
</button>
```

## Feedback Patterns

### Loading

- Skeleton screens over spinners; show the shape of incoming content.
- Pulse placeholders with `motion-safe:animate-pulse`; mark the region `aria-busy="true"` with an sr-only "Loading..." label.
- Show loading inline, near the triggering action.

```html
<div class="motion-safe:animate-pulse space-y-3" aria-busy="true">
  <span class="sr-only">Loading...</span>
  <div class="h-48 bg-gray-200 rounded-xl"></div>
  <div class="h-4 bg-gray-200 rounded w-3/4"></div>
  <div class="h-4 bg-gray-200 rounded w-1/2"></div>
</div>
```

### Success

- Green accent, checkmark, brief text; announce with `role="status"`.
- Auto-dismiss after 5s+; never auto-dismiss messages containing an action.

### Error

- Red accent, a specific message, a recovery action. Never just "Error."
- Pair red with an icon and text; use `role="alert"` for errors that appear after submit.

### Empty

Icon or illustration, explanation, primary action.

```html
<div class="text-center py-16">
  <svg class="mx-auto h-12 w-12 text-gray-400" aria-hidden="true"><!-- inbox icon --></svg>
  <h3 class="mt-4 text-lg font-semibold text-gray-900">No messages yet</h3>
  <p class="mt-2 text-sm text-gray-500">Start a conversation to see messages here.</p>
  <button type="button" class="mt-6 bg-indigo-600 text-white px-4 py-2 rounded-lg">
    New message
  </button>
</div>
```

## Navigation

- **Sidebar:** 240-280px, collapsible to 64px icon-only. Group items under subtle section headers. Active item: filled background, bold text, left accent bar, `aria-current="page"`.
- **Top nav:** fixed or sticky, 56-64px. Logo left, links center or left, actions right. Collapse to hamburger below `md`.
- **Tabs:** switch views in the same context. Active tab: 2-3px bottom border in primary plus bold text. Use `role="tablist"` and `role="tab"`, `aria-selected`, arrow-key navigation (or plain links if each tab is a URL). Max 7; overflow into a dropdown.
- **Breadcrumbs:** a slash or `>` separator; current page is text, not a link; truncate middle items on long paths.

## Forms

1. Labels above inputs, always visible (not floating, not inline).
2. Prefer one column for a linear task; use related short fields side by side when labels, content, and reading order support it.
3. Group related fields with subtle dividers.
4. Choose validation timing by field and consequence; give correction feedback when useful without interrupting incomplete input.
5. Error messages below the field, red, with specific guidance.
6. Primary action left-aligned at the bottom; secondary as a text link.

```html
<div class="space-y-1.5">
  <label for="email" class="block text-sm font-medium text-gray-700">Email address</label>
  <input
    type="email"
    id="email"
    class="block w-full rounded-lg border border-gray-300 px-3 py-2
      text-gray-900 placeholder:text-gray-400
      focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20
      transition-colors"
    placeholder="you@example.com"
    autocomplete="email"
    aria-describedby="email-error"
  />
  <!-- On error: remove `hidden` and set aria-invalid="true" on the input -->
  <p id="email-error" class="text-sm text-red-600 hidden">Please enter a valid email address.</p>
</div>
```

## Accessibility

A design constraint from the start, not a final pass.

### Contrast

- Normal text: 4.5:1 minimum (WCAG 2.2 AA).
- Large text (24px+ regular, 18.66px+ bold): 3:1.
- Non-text UI (input borders, icons, focus rings, chart marks): 3:1 against adjacent colors.
- Informative placeholder text still needs 4.5:1; a placeholder is not a label.
- Use oklch for perceptually uniform contrast adjustments.

### Focus

- Never remove `outline` without replacing it; use `focus-visible`, not `focus`.
- Ring: 2px solid, 2px offset, primary color, 3:1 against the background.
- Focused elements must not hide behind sticky headers or footers (WCAG 2.4.11): set `scroll-padding-top` to the header height.

### Target size

- WCAG 2.5.8 (AA): at least 24x24 CSS px, or spaced so a 24px circle doesn't overlap a neighbor.
- Touch: 44x44pt (Apple HIG), 48x48dp (Material). Use 44px+ for primary touch targets.

### Semantics

- One `<h1>` per page; headings in order, no skipped levels.
- Landmarks: `<nav>`, `<main>`, `<aside>`, `<footer>`.
- Buttons for actions, links for navigation; never `<div onclick>`.
- `aria-label` on icon-only buttons.

### Motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

## Responsive Breakpoints

Tailwind defaults provide examples when a project has no established breakpoints. Choose actual transitions where content or interaction needs restructuring:

| Name | Width | Target |
|------|-------|--------|
| `sm` | 640px | Large phones landscape |
| `md` | 768px | Tablets |
| `lg` | 1024px | Small laptops |
| `xl` | 1280px | Desktops |
| `2xl` | 1536px | Large screens |

Mobile-first:

- Design the mobile layout first; add complexity at larger breakpoints.
- Reflow columns when the content needs more space.
- Choose compact navigation from destination structure and discoverability.
- Scale display type where useful; keep dense UI roles stable and readable.

Container queries, for components that depend on their container, not the viewport:

```css
.card-container {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 200px 1fr;
  }
}
```

## Modern UI Trends

### Glassmorphism

```css
.glass {
  background: oklch(100% 0 0 / 0.1);
  backdrop-filter: blur(16px) saturate(180%);
  border: 1px solid oklch(100% 0 0 / 0.15);
  border-radius: 1rem;
}

@supports not (backdrop-filter: blur(1px)) {
  .glass { background: oklch(20% 0.02 265 / 0.9); }
}
```

Only works over a busy background. Check text contrast against the lightest area behind it.

### Bento grid

```css
.bento {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(200px, auto); /* fixed 200px rows clip long content */
  gap: 1rem;
}
.bento .featured {
  grid-column: span 2;
  grid-row: span 2;
}
@media (max-width: 767px) {
  .bento { grid-template-columns: 1fr; }
  .bento .featured { grid-column: auto; grid-row: auto; }
}
```

### Aurora / mesh gradient

```css
.aurora {
  background: linear-gradient(135deg, oklch(85% 0.15 280), oklch(80% 0.2 320), oklch(75% 0.18 200));
  background-size: 400% 400%;
}
@media (prefers-reduced-motion: no-preference) {
  .aurora { animation: aurora-shift 8s ease infinite; }
}
@keyframes aurora-shift {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}
```

## Advanced CSS

```css
/* :has() — parent selector */
.form-group:has(input:focus-visible) {
  background: oklch(97% 0.01 265);
  border-color: var(--color-primary);
}
.card:has(img) {
  grid-template-rows: 200px 1fr;
}

/* Subgrid — header, body, footer align across cards */
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}
.card {
  display: grid;
  grid-template-rows: subgrid;
  grid-row: span 3;
}

/* Scroll-driven animation: progressive enhancement, motion-safe only */
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .fade-in {
      animation: fade-in linear both;
      animation-timeline: view();
      animation-range: entry 0% entry 100%;
    }
  }
}
@keyframes fade-in {
  from { opacity: 0; transform: translateY(2rem); }
  to { opacity: 1; transform: translateY(0); }
}
```

## Verification

Render at 390px and 1440px wide and view both. Check: no horizontal scroll or clipped text, hierarchy reads at a glance, tokens applied, images at the right aspect ratio. Tab through once for visible focus rings in logical order. Exercise every state built (hover, focus, disabled, loading, empty, error) and contrast-check muted text.

## Checklist

- [ ] Hierarchy is clear (squint test passes)
- [ ] Interactive elements have hover, active, focus-visible, disabled states
- [ ] Contrast meets WCAG 2.2 AA (4.5:1 text; 3:1 large text and UI components)
- [ ] Targets at least 24x24px (44px+ for primary touch)
- [ ] Rendered at 390px and 1440px
- [ ] Focus order is logical
- [ ] Responsive from 320px to 1920px
- [ ] Loading, empty, and error states designed
- [ ] Spacing follows the established scale, with deliberate exceptions
- [ ] Type roles are consistent and distinguishable (see [typography](typography.md))
- [ ] Motion respects `prefers-reduced-motion`
- [ ] Semantic HTML (landmarks, headings, button vs. link)
