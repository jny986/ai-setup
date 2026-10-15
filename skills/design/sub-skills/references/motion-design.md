---
metadata:
  version: "1.0.0"
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: motion-design
---

# Motion Design

Purposeful UI animation and micro-interactions in CSS and JS: duration and easing, feedback, transitions, scroll reveals, loaders, staggering, reduced motion and performance. Not for video or animated image generation.

Tokens come from `.agents/design-context.md` (see [design-context](design-context.md)); with none, extend the project's existing CSS variables or Tailwind theme. The style archetype sets motion character: Minimal and Corporate are short with no overshoot; Playful allows springs; Luxurious is slower with smooth ease-out. Use the project's transition tokens if it has them; the `--duration-*` and `--ease-*` names below match [design-system](design-system.md). Always respect `prefers-reduced-motion`.

## Principles

1. Every animation has a purpose: guide attention, give feedback, show relationships or convey state change.
2. Faster is almost always better: 100-500ms.
3. Animate only what changes.

| Action | Duration |
|--------|----------|
| Button hover / press | 100-150ms |
| Toggle / switch | 200ms |
| Dropdown / menu open | 200-250ms |
| Modal / dialog appear | 250-300ms |
| Page transition | 300-400ms |
| Expand / collapse | 250-350ms |
| Loading spinner cycle | 700-1200ms |

Exits run 20-30% shorter than the matching entrance (modal in 250ms, out 200ms). Long-distance movement takes longer than short; mobile is typically shorter than desktop.

```css
:root {
  --duration-fast: 100ms; --duration-normal: 200ms; --duration-slow: 300ms; --duration-slower: 500ms;

  --ease-out: cubic-bezier(0, 0, 0.2, 1);               /* decelerate: ENTER */
  --ease-in: cubic-bezier(0.4, 0, 1, 1);                 /* accelerate: EXIT */
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);           /* MOVE */
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);      /* bouncy overshoot */
  --ease-bounce: cubic-bezier(0.68, -0.55, 0.27, 1.55);  /* strong bounce */
}
```

Ease-out for entrances, ease-in for exits, ease-in-out for moves, spring for playful feedback.

## Micro-interactions

### Button press

```css
.btn {
  transition: transform 0.1s var(--ease-out), background-color 0.15s var(--ease-out), box-shadow 0.15s var(--ease-out);
}
.btn:hover { box-shadow: 0 4px 12px oklch(from var(--interactive-primary) l c h / 0.3); }
.btn:active { transform: scale(0.97); }
```

### Toggle switch

```css
.toggle-track { width: 44px; height: 24px; background: var(--gray-300); border-radius: 12px; padding: 2px; cursor: pointer; transition: background-color 0.2s var(--ease-out); }
.toggle-thumb { width: 20px; height: 20px; background: white; border-radius: 50%; transition: transform 0.2s var(--ease-spring); }
.toggle-input:checked + .toggle-track { background: var(--brand-500); }
.toggle-input:checked + .toggle-track .toggle-thumb { transform: translateX(20px); }
.toggle-input:focus-visible + .toggle-track { outline: 2px solid var(--interactive-primary); outline-offset: 2px; }
```

`.toggle-input` must be a real `<input type="checkbox" role="switch">` inside a `<label>`, visually hidden (not `display: none`) so it stays keyboard and screen-reader operable.

### Like / heart

```css
.like-btn.is-liked .heart-icon { animation: like-pop 0.4s var(--ease-spring); color: var(--error-500); fill: currentColor; }
@keyframes like-pop { 0% { transform: scale(1); } 30% { transform: scale(1.3); } 60% { transform: scale(0.9); } 100% { transform: scale(1); } }
```

## Page transitions

```css
.page-enter { animation: slideUpFade 0.4s var(--ease-out) both; }
@keyframes slideUpFade {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

View Transitions API:

```css
/* Cross-document (MPA, same origin): opt in on BOTH pages */
@view-transition { navigation: auto; }
::view-transition-old(root) { animation: vt-fade-out 0.2s var(--ease-in) both; }
::view-transition-new(root) { animation: vt-fade-in 0.3s var(--ease-out) both; }
@keyframes vt-fade-out { to { opacity: 0; } }
@keyframes vt-fade-in { from { opacity: 0; } }
.hero-image { view-transition-name: hero; } /* must be unique on the page */
@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*), ::view-transition-old(*), ::view-transition-new(*) { animation: none !important; }
}
```

For SPAs wrap the DOM update: `document.startViewTransition ? document.startViewTransition(update) : update();`. Unsupported browsers skip the animation.

## Scroll-triggered animation

CSS-only with `animation-timeline`:

```css
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .scroll-reveal { animation: reveal linear both; animation-timeline: view(); animation-range: entry 0% entry 100%; }
  }
}
@keyframes reveal { from { opacity: 0; transform: translateY(40px); } to { opacity: 1; transform: translateY(0); } }
```

`animation-timeline` must come after the `animation` shorthand, which resets it. Content stays visible where unsupported.

Intersection Observer. Hide only when JS runs, so content is never lost without it:

```css
.js .reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.6s var(--ease-out), transform 0.6s var(--ease-out); }
.js .reveal.is-visible { opacity: 1; transform: translateY(0); }
```

```js
document.documentElement.classList.add('js');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) { entry.target.classList.add('is-visible'); observer.unobserve(entry.target); }
  });
}, { threshold: 0.1 });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```

## Loaders

Skeletons for content loading, spinners for actions.

```css
.skeleton { background: var(--gray-200); border-radius: var(--radius-md); position: relative; overflow: hidden; }
.skeleton::after {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(90deg, transparent, oklch(1 0 0 / 0.4), transparent);
  animation: shimmer 1.5s infinite;
}
@keyframes shimmer { from { transform: translateX(-100%); } to { transform: translateX(100%); } }
.skeleton-text { height: 1em; margin-bottom: 0.75em; }
.skeleton-text:last-child { width: 60%; }
.skeleton-avatar { width: 48px; height: 48px; border-radius: 50%; }

.spinner { width: 24px; height: 24px; border: 3px solid var(--gray-200); border-top-color: var(--brand-500); border-radius: 50%; animation: spin 0.7s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }

.dots-loader { display: flex; gap: 4px; }
.dots-loader span { width: 8px; height: 8px; background: var(--brand-500); border-radius: 50%; animation: dot-bounce 1.2s ease-in-out infinite; }
.dots-loader span:nth-child(2) { animation-delay: 0.15s; }
.dots-loader span:nth-child(3) { animation-delay: 0.3s; }
@keyframes dot-bounce { 0%, 80%, 100% { transform: scale(0.6); opacity: 0.4; } 40% { transform: scale(1); opacity: 1; } }
```

## Transition vs animation

- `transition`: state changes (hover, focus, class toggle), A to B.
- `animation`: multi-step sequences, continuous effects, entrances.

| Fill mode | Behavior |
|-----------|----------|
| none | Reverts after the animation |
| forwards | Stays at the last keyframe |
| backwards | Applies the first keyframe during the delay |
| both | forwards + backwards; usually what you want |

## Springs

```css
:root {
  --spring-gentle: cubic-bezier(0.34, 1.2, 0.64, 1);    /* slight overshoot */
  --spring-medium: cubic-bezier(0.34, 1.56, 0.64, 1);   /* noticeable bounce */
  --spring-strong: cubic-bezier(0.22, 1.8, 0.36, 1);    /* dramatic bounce */
  --spring-snappy: cubic-bezier(0.075, 0.82, 0.165, 1); /* not a spring: fast ease-out, no overshoot */
}
```

Multi-bounce needs keyframes:

```css
@keyframes spring-bounce {
  0% { transform: scale(0.8); } 40% { transform: scale(1.08); }
  60% { transform: scale(0.97); } 80% { transform: scale(1.02); } 100% { transform: scale(1); }
}
```

## Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important; animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important; scroll-behavior: auto !important;
  }
}
```

Preferred: replace motion with non-motion changes (opacity instead of transforms). The global rule is a safety net. It also stops spinners after one turn, so give loaders a non-rotating fallback (pulsing opacity or "Loading..." text).

For JS-driven animation (Web Animations API, GSAP, Framer Motion) check the preference and listen for changes:

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const duration = () => (reduce.matches ? 0 : 300);
reduce.addEventListener('change', () => { /* re-read duration(), stop autoplaying loops */ });
```

Also: no flashing more than 3 times per second (WCAG 2.3.1); auto-playing motion over 5 seconds needs a pause control (WCAG 2.2.2).

## Performance

Animate only `transform` and `opacity`: GPU-composited, no layout or paint.

| Property | Layout | Paint | Composite | Cost |
|----------|--------|-------|-----------|------|
| transform | no | no | yes | Excellent |
| opacity | no | no | yes | Excellent |
| filter | no | often | varies | Good (blur is costly on large areas) |
| box-shadow | no | yes | no | Moderate |
| width / height | yes | yes | no | Poor |
| top / left | yes | yes | no | Poor |

Use `will-change` only on elements about to animate and remove it afterward; never set it permanently on many elements. Test on low-end devices: jittery animation is worse than none.

## Staggered lists

```css
.stagger-list > * {
  animation: stagger-in 0.4s var(--ease-out) both;
  animation-delay: calc(min(var(--index, 0), 8) * 60ms);
}
@keyframes stagger-in { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
```

```html
<ul class="stagger-list">
  <li style="--index: 0">Item 1</li>
  <li style="--index: 1">Item 2</li>
  <li style="--index: 2">Item 3</li>
</ul>
```

- 40-80ms between items; total stagger under 600ms.
- Cap the index (8-10) so long lists appear together; the `min()` above does this.

## Review

Judge motion by running it, not reading code.

1. Capture the element mid-animation and at rest (after duration + 50ms). Confirm start and end states are correct and nothing jumps or overflows.
2. Emulate `prefers-reduced-motion: reduce` and confirm content is visible and static immediately.
3. Profile the animation. Long frames or layout work mean switching to `transform` and `opacity`.
