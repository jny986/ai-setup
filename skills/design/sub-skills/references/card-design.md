---
metadata:
  version: "1.0.0"
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: card-design
---

# Card Design

Individual cards and card grids: anatomy, layouts, hover effects, ready patterns, skeletons. General component rules live in [ui-design](ui-design.md); KPI tiles in [dashboard-design](dashboard-design.md).

Tokens come from `.agents/design-context.md` (see [design-context](design-context.md)); with none, extend the project's existing CSS variables or Tailwind theme. Use the context's radius and shadow style on every card. Settle what content the card holds and the single action it leads to before designing.

## Anatomy

Up to five zones; not all required.

```text
+---------------------------+
|        [Media]            |  Image, video, illustration
+---------------------------+
|  [Header]                 |  Title, subtitle, avatar, badge
|  [Body]                   |  Description, content, data
|  [Actions]                |  Buttons, links, icons
|  [Metadata]               |  Date, author, tags, stats
+---------------------------+
```

```css
.card {
  background: var(--color-surface, #fff);
  border-radius: var(--radius, 1rem);
  border: 1px solid var(--color-neutral-200, oklch(92% 0 0));
  overflow: hidden;
  transition: box-shadow 200ms ease, transform 200ms ease, border-color 200ms ease;
}
```

```html
<div class="bg-white rounded-2xl border border-gray-200 overflow-hidden
  shadow-sm hover:shadow-md transition-shadow">
  <!-- content -->
</div>
```

## Grid Layouts

Uniform:

```html
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
  <!-- equal-sized cards -->
</div>
```

Featured plus grid:

```html
<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
  <div class="lg:col-span-2 lg:row-span-2"><!-- large featured card --></div>
  <div><!-- card --></div>
  <div><!-- card --></div>
</div>
```

Masonry:

```css
.masonry {
  columns: 3;
  column-gap: 1.5rem;
}
.masonry > * {
  break-inside: avoid;
  margin-bottom: 1.5rem;
}
@media (max-width: 1024px) { .masonry { columns: 2; } }
@media (max-width: 640px) { .masonry { columns: 1; } }
```

Horizontal scroll on mobile. Make it a focusable, labelled region so keyboard users can scroll. `scrollbar-hide` is not core Tailwind (needs a plugin); keep the scrollbar if unsure.

```html
<div class="flex gap-4 overflow-x-auto snap-x snap-mandatory scroll-px-4 pb-4 -mx-4 px-4"
  tabindex="0" role="region" aria-label="Featured products">
  <div class="snap-start shrink-0 w-72"><!-- card --></div>
  <div class="snap-start shrink-0 w-72"><!-- card --></div>
  <div class="snap-start shrink-0 w-72"><!-- card --></div>
</div>
```

## Hover Effects

Lift (subtle, professional):

```html
<div class="bg-white rounded-2xl border border-gray-200 p-6
  hover:-translate-y-1 hover:shadow-lg transition-all duration-200">
```

Glow:

```html
<div class="bg-white rounded-2xl border border-gray-200 p-6
  hover:border-indigo-300 hover:shadow-[0_0_24px_-4px_rgba(99,102,241,0.25)]
  transition-all duration-300">
```

Gradient border reveal: surface clipped to the padding box, gradient to the border box behind a transparent border.

```css
.card-gradient-border {
  border: 1px solid transparent;
  border-radius: var(--radius, 1rem);
  background:
    linear-gradient(var(--color-surface, #fff), var(--color-surface, #fff)) padding-box,
    linear-gradient(var(--color-neutral-200, #e5e7eb), var(--color-neutral-200, #e5e7eb)) border-box;
}
.card-gradient-border:hover,
.card-gradient-border:focus-within {
  background:
    linear-gradient(var(--color-surface, #fff), var(--color-surface, #fff)) padding-box,
    linear-gradient(135deg, var(--color-primary), var(--color-accent)) border-box;
}
```

Content slide-up. Actions appear on hover and keyboard focus, and are always visible on touch.

```html
<div class="group relative bg-white rounded-2xl overflow-hidden border border-gray-200">
  <img src="/image.jpg" alt="" class="w-full h-48 object-cover" />
  <div class="p-6">
    <h3 class="font-bold text-gray-900">Card Title</h3>
    <p class="mt-2 text-gray-600 text-sm">Description text here.</p>
  </div>
  <div class="absolute bottom-0 inset-x-0 p-4 bg-gradient-to-t from-white via-white
    translate-y-full group-hover:translate-y-0 group-focus-within:translate-y-0
    [@media(hover:none)]:translate-y-0 motion-safe:transition-transform duration-300">
    <button type="button" class="w-full bg-indigo-600 text-white py-2 rounded-lg font-medium">
      View details
    </button>
  </div>
</div>
```

Image zoom:

```html
<div class="group rounded-2xl overflow-hidden border border-gray-200">
  <div class="overflow-hidden">
    <img src="/image.jpg" alt="" width="600" height="400" loading="lazy"
      class="w-full h-48 object-cover motion-safe:transition-transform duration-500
        motion-safe:group-hover:scale-110" />
  </div>
</div>
```

## Product Card

Star icons: repeat the star path for each star, `aria-hidden="true"`; the wrapper carries the rating label.

```html
<div class="group bg-white rounded-2xl border border-gray-200 overflow-hidden
  hover:shadow-lg transition-all duration-200">
  <div class="relative overflow-hidden">
    <img src="/product.jpg" alt="Product name" width="600" height="448" loading="lazy"
      class="w-full h-56 object-cover motion-safe:group-hover:scale-105 transition-transform duration-500" />
    <!-- red-600, not red-500: white text needs 4.5:1 -->
    <span class="absolute top-3 left-3 bg-red-600 text-white text-xs font-bold
      px-2.5 py-1 rounded-full">-20%</span>
    <!-- Wishlist: visible on hover, keyboard focus, and touch -->
    <button type="button" aria-label="Add to wishlist" aria-pressed="false"
      class="absolute top-3 right-3 w-11 h-11 bg-white/90 backdrop-blur rounded-full
      flex items-center justify-center text-gray-600 hover:text-red-600
      opacity-0 group-hover:opacity-100 focus-visible:opacity-100
      [@media(hover:none)]:opacity-100 transition-opacity">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
      </svg>
    </button>
  </div>

  <div class="p-4">
    <span class="text-xs font-medium text-indigo-600 uppercase tracking-wide">Electronics</span>
    <h3 class="mt-1 font-semibold text-gray-900 line-clamp-2">
      Wireless Noise-Cancelling Headphones Pro Max
    </h3>
    <div class="mt-2 flex items-center gap-1.5">
      <div class="flex text-amber-400" role="img" aria-label="Rated 4.5 out of 5">
        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
        <!-- repeat for remaining stars -->
      </div>
      <span class="text-sm text-gray-500">(128<span class="sr-only"> reviews</span>)</span>
    </div>
    <div class="mt-3 flex items-baseline gap-2">
      <span class="text-xl font-bold text-gray-900"><span class="sr-only">Sale price </span>$249</span>
      <del class="text-sm text-gray-500"><span class="sr-only">Original price </span>$319</del>
    </div>
  </div>

  <div class="px-4 pb-4">
    <button type="button" class="w-full bg-gray-950 text-white py-2.5 rounded-xl font-medium
      hover:bg-gray-800 active:bg-gray-900 transition-colors">
      Add to cart
    </button>
  </div>
</div>
```

## Feature / Benefit Card

```html
<div class="bg-white rounded-2xl border border-gray-200 p-6
  hover:border-indigo-200 hover:shadow-md transition-all duration-200">
  <div class="w-12 h-12 rounded-xl bg-indigo-50 text-indigo-600 flex items-center justify-center">
    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
    </svg>
  </div>
  <h3 class="mt-4 text-lg font-semibold text-gray-900">Lightning Fast</h3>
  <p class="mt-2 text-gray-600 text-sm leading-relaxed">
    Built on edge infrastructure for sub-100ms response times worldwide.
  </p>
  <a href="#" class="mt-4 inline-flex items-center gap-1 text-sm font-medium
    text-indigo-600 hover:text-indigo-500 transition-colors">
    Learn more
    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
    </svg>
  </a>
</div>
```

## Testimonial Card

```html
<div class="bg-white rounded-2xl border border-gray-200 p-6">
  <div class="flex gap-0.5 text-amber-400 mb-4" role="img" aria-label="Rated 5 out of 5">
    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true"><!-- star path, repeat 5x --></svg>
  </div>
  <blockquote class="text-gray-700 leading-relaxed">
    "This tool saved our team 20 hours per week. The onboarding was seamless
    and we saw results from day one."
  </blockquote>
  <div class="mt-6 flex items-center gap-3">
    <img src="/avatar.jpg" alt="" class="w-10 h-10 rounded-full" />
    <div>
      <div class="font-semibold text-gray-900 text-sm">Alex Rivera</div>
      <div class="text-gray-500 text-sm">VP Engineering, Acme Inc</div>
    </div>
  </div>
</div>
```

## Blog Post Card

```html
<a href="/blog/post-slug" class="group block bg-white rounded-2xl border border-gray-200
  overflow-hidden hover:shadow-lg transition-shadow duration-200
  focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
  <div class="overflow-hidden">
    <img src="/blog-cover.jpg" alt="" width="600" height="384" loading="lazy"
      class="w-full h-48 object-cover motion-safe:group-hover:scale-105 transition-transform duration-500" />
  </div>
  <div class="p-5">
    <div class="flex items-center gap-2 text-sm text-gray-500 mb-3">
      <span class="bg-indigo-50 text-indigo-700 px-2 py-0.5 rounded-full text-xs font-medium">Engineering</span>
      <span>5 min read</span>
    </div>
    <h3 class="font-bold text-gray-900 text-lg group-hover:text-indigo-600
      transition-colors line-clamp-2">
      How We Reduced Our Build Times by 80%
    </h3>
    <p class="mt-2 text-gray-600 text-sm line-clamp-3 leading-relaxed">
      A deep dive into our migration to incremental builds and how it
      transformed our developer experience across 12 teams.
    </p>
    <div class="mt-4 flex items-center gap-2">
      <img src="/avatar.jpg" alt="" class="w-6 h-6 rounded-full" />
      <span class="text-sm text-gray-600">Sarah Kim</span>
      <time datetime="2026-03-15" class="text-sm text-gray-500">Mar 15, 2026</time>
    </div>
  </div>
</a>
```

## Interactive Cards

### Expandable

```html
<details class="group bg-white rounded-2xl border border-gray-200 overflow-hidden">
  <summary class="flex items-center justify-between p-6 cursor-pointer
    list-none hover:bg-gray-50 transition-colors">
    <div>
      <h3 class="font-semibold text-gray-900">Card Title</h3>
      <p class="text-sm text-gray-500 mt-1">Click to expand</p>
    </div>
    <svg class="w-5 h-5 text-gray-400 group-open:rotate-180 transition-transform"
      fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
    </svg>
  </summary>
  <div class="px-6 pb-6 text-gray-600 text-sm leading-relaxed">Expanded content.</div>
</details>
```

### Flippable

Use sparingly; hidden content is easy to miss. Prefer expandable when the back holds important content. The flip must also trigger on keyboard focus, and be a simple swap (no 3D) under reduced motion.

```html
<div class="group [perspective:1000px] h-64 w-full">
  <div class="relative h-full w-full motion-safe:transition-transform duration-500
    [transform-style:preserve-3d] group-hover:[transform:rotateY(180deg)]
    group-focus-within:[transform:rotateY(180deg)]">
    <div class="absolute inset-0 bg-white rounded-2xl border border-gray-200
      p-6 flex flex-col items-center justify-center [backface-visibility:hidden]">
      <h3 class="font-bold text-gray-900">Feature Name</h3>
      <p class="mt-2 text-sm text-gray-500 text-center">Hover or focus to learn more</p>
    </div>
    <div class="absolute inset-0 bg-indigo-600 rounded-2xl p-6
      flex flex-col items-center justify-center text-white text-center
      [backface-visibility:hidden] [transform:rotateY(180deg)]">
      <p class="text-sm leading-relaxed">Detailed description with specific benefits.</p>
      <!-- Focusing this link flips the card (group-focus-within) -->
      <a href="#" class="mt-4 bg-white text-indigo-700 px-4 py-2 rounded-lg
        font-medium text-sm">Learn more about Feature Name</a>
    </div>
  </div>
</div>
```

## Skeleton Loading

Put `aria-busy="true"` and an sr-only "Loading..." on the grid container, not on each card.

```html
<div class="bg-white rounded-2xl border border-gray-200 overflow-hidden motion-safe:animate-pulse"
  aria-hidden="true">
  <div class="h-48 bg-gray-200"></div>
  <div class="p-5 space-y-3">
    <div class="h-3 bg-gray-200 rounded-full w-1/4"></div>
    <div class="h-5 bg-gray-200 rounded-full w-3/4"></div>
    <div class="space-y-2">
      <div class="h-3 bg-gray-200 rounded-full w-full"></div>
      <div class="h-3 bg-gray-200 rounded-full w-5/6"></div>
    </div>
    <div class="flex items-center gap-2 pt-2">
      <div class="w-6 h-6 bg-gray-200 rounded-full"></div>
      <div class="h-3 bg-gray-200 rounded-full w-20"></div>
    </div>
  </div>
</div>
```

Rules:

1. Match the real card's layout exactly (heights, widths, spacing).
2. Animate the container, not individual elements.
3. `rounded-full` for text placeholders, `rounded-lg` for images.
4. Show 3-6 skeletons matching the expected grid.
5. Swap to real content with no layout shift.

## Verification

Render at 390px and 1440px and view both. Test the grid with long and short content (equal heights, `line-clamp` works). Confirm hover-only content is reachable by keyboard and on touch.

## Checklist

- [ ] Clear visual boundaries (border, shadow, or background contrast)
- [ ] Content hierarchy: media > title > description > actions
- [ ] Hover effect gives feedback (lift, glow, or border change)
- [ ] Interactive cards use a real `<a>` or `<button>` (not `tabindex` on a `<div>`) with a `focus-visible` ring
- [ ] Hover-only content also appears on focus and on touch
- [ ] Hover motion respects `prefers-reduced-motion`; images have width/height and `loading="lazy"`
- [ ] Text truncated with `line-clamp` where needed
- [ ] Responsive grid (3 columns desktop, 2 tablet, 1 mobile)
- [ ] Skeleton matches card layout
- [ ] Images have proper `alt` and `object-cover`
- [ ] Card links wrap the whole card, or use the stretched-link pattern (`::after { inset: 0 }` on the title link) when the card has other buttons; never nest interactive elements inside an `<a>`
- [ ] Consistent radius, padding, and spacing across cards
