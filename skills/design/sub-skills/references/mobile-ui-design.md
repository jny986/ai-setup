---
name: mobile-ui-design
description: "Design mobile websites and PWAs for touch, navigation, safe areas, gestures, forms, and responsive content."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: ArnavPuri/designskills, pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable, pbakaus/impeccable
  based_on_version: main(c787301), main(2f98774), main(2f98774), main(2f98774), main(2f98774)
  based_on_skill: mobile-ui-design, adapt, adapt.native, ios, android
---

# Mobile UI Design

Touch-first UI for mobile websites and PWAs: targets, navigation, gestures, safe areas, sheets, forms, and motion. For native iOS, Android, React Native, Expo, or Flutter apps, read [native-platforms](native-platforms.md). For a change of device, window size, input, or platform, read [adapt](adapt.md). General web patterns are in [ui-design](ui-design.md); device mockups in [product-mockup](product-mockup.md).

Read `DESIGN.md` for UI tokens and the project brand kit for approved brand primitives (see [design-context](design-context.md)); when absent, inspect the project's existing CSS variables or Tailwind theme. The `indigo-*` / `gray-*` classes below are placeholders for primary and neutral tokens. The code examples below are web implementations. Preserve the project's navigation, sizing, and motion conventions; the example dimensions and patterns are fallbacks where those are missing.

## Touch Targets

| Source | Minimum | Notes |
|--------|---------|-------|
| Apple HIG | 44x44pt | Native logical points; a useful web sizing reference, not a unit conversion |
| Material Design | 48x48dp | Native logical units; the visual icon can be smaller than its hit area |
| WCAG 2.2 SC 2.5.8 (AA) | 24x24 CSS px | Web accessibility criterion; includes exceptions |
| WCAG 2.2 SC 2.5.5 (AAA) | 44x44 CSS px | |

For mobile web, aim for comfortable hit areas around 44–48 CSS px with enough separation to prevent accidental taps. Check the actual target and spacing; native point and dp values belong to their platform frameworks.

Expand small visuals with a pseudo-element:

```css
.icon-button {
  width: 24px;
  height: 24px;
  position: relative;
}
.icon-button::after {
  content: '';
  position: absolute;
  inset: -12px; /* extends tap area to 48x48 */
}
```

## Bottom Navigation

Bottom navigation suits a small set of frequently used peer destinations. Choose navigation from the task and existing information architecture; a content site may need a different structure.

```html
<nav aria-label="Main" class="fixed bottom-0 inset-x-0 bg-white border-t border-gray-200
  safe-area-bottom z-50">
  <div class="flex items-center justify-around h-16">
    <a href="#" aria-current="page" class="flex flex-col items-center justify-center gap-0.5
      text-indigo-600 min-w-[64px] min-h-[48px]">
      <svg class="w-6 h-6" fill="currentColor" aria-hidden="true"><!-- home icon --></svg>
      <span class="text-xs font-medium">Home</span>
    </a>
    <!-- gray-500, not gray-400: labels need 4.5:1 -->
    <a href="#" class="flex flex-col items-center justify-center gap-0.5
      text-gray-500 min-w-[64px] min-h-[48px]">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" aria-hidden="true"><!-- search icon --></svg>
      <span class="text-xs font-medium">Search</span>
    </a>
    <!-- 3-5 tabs total -->
  </div>
</nav>
```

- Keep the set small enough for readable labels and comfortable targets; use the existing navigation model where it works.
- Active: filled icon plus primary color. Inactive: outline icon plus gray.
- Labels required; icon-only tabs are hard to discover.
- Preserve discoverability when changing navigation; choose a drawer only when it suits the destination structure.
- Account for the bottom safe area.

## Safe Areas

```css
.top-safe { padding-top: env(safe-area-inset-top); }          /* status bar */
.bottom-safe { padding-bottom: env(safe-area-inset-bottom); } /* home indicator */
.side-safe {                                                   /* landscape notch */
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}
.safe-area {
  padding: env(safe-area-inset-top) env(safe-area-inset-right)
    env(safe-area-inset-bottom) env(safe-area-inset-left);
}

/* Elements with their own padding: add the inset, don't replace it */
.pb-safe-4 { padding-bottom: calc(1rem + env(safe-area-inset-bottom)); }
```

`.safe-area-bottom` in examples is `.bottom-safe`; `.pb-safe-4` is defined above.

- Pad the scroller (for example `pb-[calc(4rem+env(safe-area-inset-bottom))]` on `<main>`) so the last item isn't hidden behind the tab bar.
- `viewport-fit=cover` is required for `env(safe-area-inset-*)` to return non-zero values:

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
```

- Never add `maximum-scale=1` or `user-scalable=no`; it blocks pinch-zoom (WCAG 1.4.4).
- `100vh` is taller than the visible area while browser toolbars show. Use `100dvh` (tracks toolbars) for app shells and sheets, `100svh` for heroes that shouldn't resize on scroll (Tailwind `h-dvh`, `h-svh`).

## Gestures

Swipe-to-reveal (conceptual structure):

```html
<div class="relative overflow-hidden">
  <!-- Revealed on swipe; a real button, also reachable without swiping -->
  <div class="absolute inset-y-0 right-0 flex items-center bg-red-600 px-6">
    <button type="button" class="text-white font-medium">Delete</button>
  </div>
  <div class="bg-white px-4 py-3 transform transition-transform touch-pan-y">
    <div class="font-medium text-gray-900">List Item</div>
    <div class="text-sm text-gray-500">Swipe left for actions</div>
  </div>
</div>
```

Pull-to-refresh: indicator appears as the user pulls, refresh triggers around 80px, haptic feedback on native. On the web set `overscroll-behavior-y: contain` on the scroller so the browser's own refresh doesn't also fire.

| Gesture | Use | Implementation |
|---------|-----|----------------|
| Swipe left/right | Reveal actions, navigate | `touch-action: pan-y` |
| Pull down | Refresh | Overscroll detection |
| Long press | Context menu, reorder | `pointerdown` plus ~500ms timeout; cancel on `pointermove` or `pointerup` |
| Pinch | Zoom images, maps | `touch-action: none` on the element plus Pointer Events |
| Swipe up | Dismiss or expand sheet | Drag handle on bottom sheet |

`touch-action: manipulation` on buttons and links removes the double-tap-zoom delay; it does not enable custom pinch handling. Every gesture needs a visible single-tap alternative (button or menu item), for WCAG 2.5.1 and discoverability.

## Native platforms

Native navigation, controls, scalable typography, and system gestures are covered by [native-platforms](native-platforms.md). Use the shipped OS's conventions and the project's intentional cross-platform system. The web examples here do not establish native runtime behavior.

## Mobile Type Scale

This example follows an iOS-like hierarchy for web styling. Use existing project roles where present; native text styles and scaling belong to [native-platforms](native-platforms.md).

| Role | Size | Weight | Line height |
|------|------|--------|-------------|
| Large title | 34px | 700 | 1.2 |
| Title 1 | 28px | 700 | 1.2 |
| Title 2 | 22px | 700 | 1.25 |
| Title 3 | 20px | 600 | 1.25 |
| Headline | 17px | 600 | 1.3 |
| Body | 17px | 400 | 1.5 |
| Callout | 16px | 400 | 1.4 |
| Subhead | 15px | 400 | 1.4 |
| Footnote | 13px | 400 | 1.3 |
| Caption | 12px | 400 | 1.3 |

- Body at least 16px.
- Inputs, selects, and textareas at least 16px; iOS Safari zooms into smaller fields.
- Line length 35-50 characters.
- Use `rem` on a 16px root.

See [typography](typography.md) for general scale and pairing rules.

## Thumb Zone

```text
+-----------------------------+
|     Hard to reach           |  Top 25%: secondary actions, titles
|-----------------------------|
|     Comfortable stretch     |  Middle 50%: content, scrollable lists
|-----------------------------|
|     Easy / natural          |  Bottom 25%: primary actions, nav, FAB
+-----------------------------+
```

- Keep frequent actions reachable and associated with their content; a persistent bottom action is useful when the task warrants it.
- Consider bottom search bars (as iOS Safari).
- FAB: bottom-right, 56px, with shadow.
- Make destructive actions explicit and recoverable or appropriately confirmed; placement alone does not prevent accidental activation.

```html
<div class="fixed bottom-0 inset-x-0 px-4 pt-12 pb-safe-4 bg-gradient-to-t from-white via-white to-transparent">
  <button type="button" class="w-full bg-indigo-600 text-white py-4 rounded-2xl font-semibold
    text-lg active:bg-indigo-700 transition-colors">
    Continue
  </button>
</div>
```

## Sheets

A modal dialog: trap focus, close on Esc, return focus to the trigger. A native `<dialog>` opened with `showModal()` provides most of this.

```html
<div class="fixed inset-0 z-50">
  <div class="absolute inset-0 bg-black/40 backdrop-blur-sm" data-dismiss></div>
  <div role="dialog" aria-modal="true" aria-labelledby="sheet-title"
    class="absolute bottom-0 inset-x-0 bg-white rounded-t-3xl
    max-h-[85dvh] overflow-y-auto overscroll-contain pb-safe-4">
    <div class="flex justify-center pt-3 pb-2" aria-hidden="true">
      <div class="w-10 h-1 rounded-full bg-gray-300"></div>
    </div>
    <div class="px-4 pb-6">
      <div class="flex items-center justify-between mb-4">
        <h2 id="sheet-title" class="text-xl font-bold text-gray-900">Sheet Title</h2>
        <button type="button" aria-label="Close" class="w-11 h-11 -mr-2 rounded-full
          flex items-center justify-center text-gray-500">&times;</button>
      </div>
      <!-- content -->
    </div>
  </div>
</div>
```

Variants: peek sheet (30% visible, drag to expand), action sheet (iOS-style option list), full-screen sheet (with close button), map sheet (persistent over a map).

Rules:

- Drag handle: 40px wide, 4px tall, centered, rounded.
- Size the sheet to its content and available viewport; use internal scrolling when needed.
- Provide explicit close or completion and keyboard dismissal; enable backdrop or swipe dismissal when it safely preserves work.
- Snap points: collapsed, half, expanded.

## Mobile Forms

1. Inputs at least 48px tall, 16px+ font.
2. Full-width inputs.
3. Smart keyboards via `inputmode`.
4. Sticky submit button at the bottom.
5. Prefer a single column on narrow screens; group related short fields only when labels and content still fit.

```html
<input type="tel" inputmode="tel" />
<input type="email" inputmode="email" />
<input type="text" inputmode="numeric" pattern="[0-9]*" />
<input type="url" inputmode="url" />
<input type="search" inputmode="search" />
```

```html
<div class="space-y-1.5">
  <label for="phone" class="block text-sm font-medium text-gray-700">Phone number</label>
  <input type="tel" id="phone" inputmode="tel" autocomplete="tel"
    class="block w-full h-12 rounded-xl border border-gray-300 px-4
      text-base text-gray-900 placeholder:text-gray-400
      focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20"
    placeholder="+1 (555) 000-0000" />
</div>
```

## Mobile Web Motion

```css
:root {
  --ease-spring: cubic-bezier(0.175, 0.885, 0.32, 1.275); /* slight overshoot */
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);              /* entering elements */
  --ease-in: cubic-bezier(0.55, 0, 1, 0.45);              /* exiting elements */
}

.page-enter {
  transform: translateX(100%);
  animation: slide-in 350ms var(--ease-out) forwards;
}
@keyframes slide-in { to { transform: translateX(0); } }

.sheet-enter {
  transform: translateY(100%);
  animation: sheet-up 400ms var(--ease-out) forwards;
}
@keyframes sheet-up { to { transform: translateY(0); } }

.tap-feedback:active {
  transform: scale(0.97);
  opacity: 0.8;
  transition: transform 50ms ease, opacity 50ms ease;
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

- Keep routine feedback prompt; choose duration from distance, consequence, and established motion tokens.
- Prefer `transform` and `opacity` for cheap motion; measure other effects as described in [motion-design](motion-design.md).
- Use `will-change: transform` sparingly.
- Haptics for important actions (native only).

See [motion-design](motion-design.md) for general timing and easing guidance.

## Verification

Render at 320px, 390px, and landscape and view each. Fixed bars must clear safe areas. Headless browsers don't emulate notches, so confirm in code that every fixed top or bottom bar adds `env(safe-area-inset-*)`, or check on a device simulator.

## Checklist

- [ ] Comfortable web hit areas and separation; applicable accessibility target-size criterion checked
- [ ] Navigation matches the task; any bottom destinations have clear labels and usable targets
- [ ] Safe areas respected (top, bottom, sides)
- [ ] Body text 16px+; inputs 16px+ (no iOS zoom)
- [ ] Primary actions in the thumb zone
- [ ] Forms use correct `inputmode`
- [ ] Sheets have drag handles, dismiss gestures, dialog semantics and focus management
- [ ] Motion uses established timing, remains responsive, and respects interruption
- [ ] `viewport-fit=cover` set; zoom not disabled
- [ ] Full-height layouts use `dvh` or `svh`, not `100vh`
- [ ] Every gesture has a tap alternative
- [ ] `prefers-reduced-motion` respected
- [ ] Readable at 320px; no horizontal scroll
