---
name: dark-mode
description: "Design dark appearance through semantic colors, surface hierarchy, readable contrast, and theme behavior."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: dark-mode
---

# Dark Mode Design

Dark themes for web UI: surface elevation, desaturated brand colors, text and border tokens, `color-scheme`, system-preference detection, a no-flash toggle, Tailwind dark variants. Palette construction is in [color-palette](color-palette.md); dark mode in HTML email is in [email-design](email-design.md).

Read `DESIGN.md` for UI tokens and the project brand kit for approved brand primitives (see [design-context](design-context.md)); when absent, inspect the project's existing CSS variables or Tailwind theme. Use the documented light theme values when present. Derive dark values from them (raise lightness, lower chroma) rather than inventing a new palette. Settle whether this is dark-first or dark added to an existing light UI.

## Core Rule: Don't Just Invert

| Element | Light | Dark |
|---------|-------|------|
| Background | White | Dark gray, not pure black |
| Text | Near-black | Near-white, not pure white |
| Borders | Gray-200 | White at 8-12% opacity |
| Shadows | Black at 5-15% | Nearly invisible or none |
| Primary color | Full saturation | Reduced saturation |
| Images | Full brightness | Slightly dimmed |
| Elevation | Shadows | Lighter surface color |

Avoid:

- Pure `#fff` text on pure `#000` (21:1 causes halation and glare for many readers, especially with astigmatism).
- Pure black as the default background: no headroom to show elevation, and OLED panels can smear while scrolling. Reserve true black for an explicit OLED option.
- Light-mode shadow values; they barely show on dark surfaces.

## Elevation Through Luminance

Elevated surfaces get lighter.

```css
:root {
  --bg-base: oklch(100% 0 0);
  --bg-surface: oklch(100% 0 0);
  --bg-elevated: oklch(100% 0 0);   /* white + shadow */
  --bg-overlay: oklch(100% 0 0);    /* white + deeper shadow */
}

[data-theme="dark"] {
  --bg-base: oklch(13% 0.01 265);     /* page background */
  --bg-surface: oklch(18% 0.01 265);  /* cards, sidebar */
  --bg-elevated: oklch(23% 0.01 265); /* dropdowns, popovers */
  --bg-overlay: oklch(28% 0.01 265);  /* modals, tooltips */
}

.card { background: var(--bg-surface); border: 1px solid var(--border); }
.dropdown { background: var(--bg-elevated); border: 1px solid var(--border); }
.modal { background: var(--bg-overlay); }
```

Material 2 overlay model: each elevation adds a white overlay on `#121212`.

- 0dp base: 0%; 1dp card: 5%; 4dp app bar: 9%
- 8dp menu: 12%; 16dp nav drawer: 15%; 24dp dialog: 16%

Material 3 replaces overlays with tonal `surface-container` roles; the tokens above follow the same idea.

## Color Saturation

Bright, saturated colors on dark backgrounds vibrate and strain the eye.

```css
:root {
  --color-primary: oklch(60% 0.25 265);
  --color-success: oklch(55% 0.20 155);
  --color-error: oklch(55% 0.22 25);
}

[data-theme="dark"] {
  --color-primary: oklch(72% 0.18 265);   /* lighter, less saturated */
  --color-success: oklch(70% 0.15 155);
  --color-error: oklch(70% 0.16 25);
}
```

- Raise lightness 10-15%; lower chroma 15-25%.
- Tinted backgrounds (badges) use lower opacity.
- Re-check contrast: a primary that passes with white text on white often fails in dark. Use a lighter primary with dark text on filled buttons.

```css
.badge-success { background: oklch(95% 0.05 155); color: oklch(35% 0.15 155); }
[data-theme="dark"] .badge-success { background: oklch(35% 0.08 155); color: oklch(80% 0.12 155); }
```

## Text Contrast

White at varying opacity builds hierarchy on dark surfaces.

| Role | Opacity | Use |
|------|---------|-----|
| High emphasis | 87-90% (`oklch(100% 0 0 / 0.87)`) | Headings, primary text |
| Medium emphasis | 60-70% (`oklch(100% 0 0 / 0.70)`) | Body, secondary, muted |
| Disabled | 38% (`oklch(100% 0 0 / 0.38)`) | Disabled controls only (exempt from contrast rules) |

Anything the user must read, including informative muted captions and placeholders, needs 4.5:1 against its surface. Below about 55% white fails on typical dark surfaces. Use the `--text-*` tokens in the token system below (`--text-muted` at 62% lightness is the lowest that keeps 4.5:1 on base and surface).

```html
<h1 class="text-white/90">Main Heading</h1>
<p class="text-white/70">Body text content here.</p>
<!-- Not below /60; /40 fails 4.5:1 -->
<span class="text-white/60">Last updated 2 hours ago</span>
```

## Borders and Dividers

Use semi-transparent white so borders adapt to any surface.

```css
[data-theme="dark"] {
  --border: oklch(100% 0 0 / 0.08);        /* subtle */
  --border-strong: oklch(100% 0 0 / 0.15); /* emphasized */
  --divider: oklch(100% 0 0 / 0.06);       /* section dividers */
}
```

Decorative dividers can be this faint. Input and control borders need 3:1 against the surface (WCAG 1.4.11): use `oklch(100% 0 0 / 0.3)` or stronger.

## Images

```css
[data-theme="dark"] img:not([data-no-dim]) { filter: brightness(0.85); }
/* Restore on hover for galleries */
[data-theme="dark"] img:not([data-no-dim]):hover { filter: brightness(1); }
```

Hero image overlay:

```html
<div class="relative">
  <img src="/hero.jpg" alt="" class="w-full" />
  <div class="absolute inset-0 bg-gray-950/30 dark:bg-gray-950/50"></div>
</div>
```

Icons use `currentColor` so they inherit text color:

```html
<svg class="w-5 h-5 text-gray-600 dark:text-gray-400" fill="currentColor"><!-- paths --></svg>
```

Provide separate logos per theme:

```html
<img src="/logo-dark.svg" alt="Logo" class="dark:hidden" />
<img src="/logo-light.svg" alt="Logo" class="hidden dark:block" />
```

## CSS Implementation

### color-scheme

Renders native controls, scrollbars, form fields, and the default canvas in the right theme. Without it `<select>`s and scrollbars stay light.

```css
:root { color-scheme: light dark; }
:root[data-theme="light"] { color-scheme: light; }
:root[data-theme="dark"]  { color-scheme: dark; }
```

Also add `<meta name="color-scheme" content="light dark">` in `<head>` so the page background is right before CSS loads.

### Method 1: system preference

```css
:root {
  --bg: oklch(100% 0 0);
  --text: oklch(15% 0 0);
  --surface: oklch(100% 0 0);
  --border: oklch(90% 0 0);
}

@media (prefers-color-scheme: dark) {
  /* :not() lets a manual "light" choice (Method 2) override the system */
  :root:not([data-theme="light"]) {
    --bg: oklch(13% 0.01 265);
    --text: oklch(95% 0 0);
    --surface: oklch(18% 0.01 265);
    --border: oklch(100% 0 0 / 0.08);
  }
}
```

### Method 2: attribute toggle (user preference)

```css
:root { --bg: oklch(100% 0 0); --text: oklch(15% 0 0); }
[data-theme="dark"] { --bg: oklch(13% 0.01 265); --text: oklch(95% 0 0); }
body { background: var(--bg); color: var(--text); }
```

```javascript
// Keeps data-theme, the Tailwind `dark` class, and the button state in sync
function applyTheme(theme) {
  const root = document.documentElement;
  root.setAttribute('data-theme', theme);
  root.classList.toggle('dark', theme === 'dark');
  document.querySelectorAll('[data-theme-toggle]')
    .forEach((btn) => btn.setAttribute('aria-pressed', String(theme === 'dark')));
}
function toggleTheme() {
  const next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
  applyTheme(next);
  try { localStorage.setItem('theme', next); } catch (e) { /* storage blocked: session-only */ }
}
// Follow system changes until the user makes an explicit choice
matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
  let saved = null;
  try { saved = localStorage.getItem('theme'); } catch (e) {}
  if (!saved) applyTheme(e.matches ? 'dark' : 'light');
});
```

The initial theme is set by the inline head script below, not a function that runs after load. Consider a three-way control (Light / Dark / System); "System" clears the saved value.

### Method 3: Tailwind `dark:` variant

```html
<div class="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100
  border-gray-200 dark:border-white/10">
  <h2 class="text-gray-950 dark:text-white">Title</h2>
  <p class="text-gray-600 dark:text-gray-400">Description</p>
</div>
```

```javascript
// tailwind.config.js (v3.4.1+)
module.exports = {
  darkMode: 'selector',                            // `.dark` on <html>
  // darkMode: ['selector', '[data-theme="dark"]'], // or drive it from data-theme
}
```

```css
/* Tailwind v4, in the main CSS file */
@custom-variant dark (&:where([data-theme="dark"], [data-theme="dark"] *));
```

### Prevent flash of wrong theme

Add an inline, blocking script in `<head>` before any stylesheet. Not `defer`, not `async`, not a bundled module; those run after first paint.

```html
<script>
  (function () {
    var theme = null;
    try { theme = localStorage.getItem('theme'); } catch (e) {}
    if (!theme) theme = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    var root = document.documentElement;
    root.setAttribute('data-theme', theme);
    root.classList.toggle('dark', theme === 'dark');
  })();
</script>
```

With SSR frameworks (Next.js and similar), add `suppressHydrationWarning` to `<html>`; the attribute differs from the server render.

## Component Patterns

```html
<!-- Input -->
<input class="bg-white border-gray-300 text-gray-900 placeholder:text-gray-400
  focus:border-indigo-500 focus:ring-indigo-500/20
  dark:bg-white/5 dark:border-white/30 dark:text-gray-100 dark:placeholder:text-gray-400
  dark:focus:border-indigo-400 dark:focus:ring-indigo-400/20" />

<!-- Card -->
<div class="bg-white border border-gray-200 shadow-sm
  dark:bg-white/5 dark:border-white/10 dark:shadow-none">

<!-- Primary button: lighter fill with dark text keeps 4.5:1 (white on indigo-500 is about 4.4:1) -->
<button class="bg-indigo-600 text-white hover:bg-indigo-500
  dark:bg-indigo-400 dark:text-indigo-950 dark:hover:bg-indigo-300">Primary</button>

<!-- Secondary button -->
<button class="bg-gray-100 text-gray-700 hover:bg-gray-200
  dark:bg-white/10 dark:text-gray-200 dark:hover:bg-white/15">Secondary</button>

<!-- Dropdown / popover -->
<div class="bg-white border border-gray-200 shadow-lg rounded-xl
  dark:bg-gray-800 dark:border-white/10 dark:shadow-2xl dark:shadow-black/20">

<!-- Table row -->
<tr class="border-b border-gray-100 hover:bg-gray-50 dark:border-white/5 dark:hover:bg-white/5">
```

## Theme Transition

Don't keep a permanent `* { transition: ... }` rule: it overrides every component's own transitions and animates colors on first paint. Add a temporary class only while switching.

```css
@media (prefers-reduced-motion: no-preference) {
  .theme-transition,
  .theme-transition *,
  .theme-transition *::before,
  .theme-transition *::after {
    transition: background-color 200ms ease, border-color 200ms ease,
      color 200ms ease, fill 200ms ease, stroke 200ms ease !important;
  }
}
```

```javascript
// In toggleTheme(), wrap the switch:
const root = document.documentElement;
root.classList.add('theme-transition');
applyTheme(next);
setTimeout(() => root.classList.remove('theme-transition'), 250);
```

Alternative where supported: `document.startViewTransition(() => applyTheme(next))` for a cross-fade.

Toggle button. `applyTheme()` keeps `aria-pressed` in sync; the accessible name stays constant.

```html
<button type="button" data-theme-toggle aria-pressed="false" aria-label="Dark mode"
  onclick="toggleTheme()" class="relative w-14 h-7 rounded-full
  bg-gray-500 dark:bg-indigo-500 transition-colors
  focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500">
  <span class="absolute top-0.5 left-0.5 w-6 h-6 rounded-full bg-white shadow
    motion-safe:transition-transform dark:translate-x-7 flex items-center justify-center">
    <svg class="w-4 h-4 text-amber-500 dark:hidden" aria-hidden="true"><!-- sun icon --></svg>
    <svg class="w-4 h-4 text-indigo-500 hidden dark:block" aria-hidden="true"><!-- moon icon --></svg>
  </span>
</button>
```

## Token System

Shared by the UI references ([dashboard-design](dashboard-design.md) reuses these). Derive `--color-primary` and status colors from the `DESIGN.md` values per the saturation rules; the oklch values below are the defaults for primary `#2563EB`.

```css
[data-theme="dark"] {
  color-scheme: dark;

  /* Surfaces */
  --bg-base: oklch(13% 0.01 265);
  --bg-surface: oklch(18% 0.01 265);
  --bg-elevated: oklch(23% 0.01 265);
  --bg-overlay: oklch(28% 0.01 265);

  /* Text */
  --text-primary: oklch(95% 0 0);
  --text-secondary: oklch(75% 0 0);
  --text-muted: oklch(62% 0 0);          /* 4.5:1+ on base and surface */

  /* Borders */
  --border: oklch(100% 0 0 / 0.08);       /* decorative dividers */
  --border-strong: oklch(100% 0 0 / 0.15);
  --border-input: oklch(100% 0 0 / 0.30); /* form controls: 3:1+ */

  /* Interactive */
  --color-primary: oklch(72% 0.18 265);
  --color-primary-hover: oklch(78% 0.16 265);

  /* Status */
  --color-success: oklch(70% 0.15 155);
  --color-warning: oklch(75% 0.15 80);
  --color-error: oklch(70% 0.16 25);
  --color-info: oklch(72% 0.15 230);
}
```

## Verification

Render both themes (emulate the light and dark system preference) at mobile and desktop widths. Reload in dark to confirm no flash of the light theme. Contrast-check muted text and borders in dark. Tab through for visible focus rings.

## Checklist

- [ ] Dark gray background, off-white text (no pure `#fff` on pure `#000`)
- [ ] `color-scheme` set (CSS property and meta tag)
- [ ] Elevation uses lighter surfaces, not shadows
- [ ] Primary colors desaturated and lightened
- [ ] Borders are semi-transparent white
- [ ] Images slightly dimmed
- [ ] Logos have light variants
- [ ] No flash of wrong theme (inline blocking head script)
- [ ] System preference detected and respected
- [ ] User preference persisted in `localStorage`
- [ ] Theme transition is temporary (not a global `*` rule) and skipped under reduced motion
- [ ] Dark contrast meets AA: 4.5:1 text (including muted), 3:1 input borders, icons, focus rings
- [ ] Toggle is a real `<button>` with an accessible name and `aria-pressed`
- [ ] Both themes rendered and checked
