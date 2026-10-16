---
name: hero-section
description: "Design a page opening that communicates the offer, presents relevant evidence, and makes the next action clear."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: hero-section
---

# Hero Section Design

Above-the-fold hero patterns (centered, split, video, minimal type), backgrounds, and LCP performance. Full multi-section pages are in [landing-page-design](landing-page-design.md); static hero images or banner graphics in [banner-design](banner-design.md).

Read `DESIGN.md` for UI tokens and the project brand kit for approved brand primitives (see [design-context](design-context.md)); when absent, inspect the project's existing CSS variables or Tailwind theme. The `indigo-*` / `gray-*` classes below are placeholders for primary and neutral tokens. Settle the product and primary CTA first. Let the style archetype pick the pattern: Minimal or Corporate: centered or split; Bold or Playful: gradient backgrounds; Luxurious: minimal typography on a dark surface.

## Headline Hierarchy

```text
[Optional: badge / announcement]
[Headline: value proposition]
[Subheadline: supporting detail]
[CTA button(s)]
[Trust signals]
[Visual: image, mockup, or illustration]
```

Headline:

- One sentence, 10 words max.
- State the benefit, not the feature: "Ship faster" over "CI/CD pipeline tool".
- Scale `text-4xl sm:text-5xl lg:text-6xl`, `font-extrabold tracking-tight leading-[1.1]`.

Subheadline:

- 1-2 sentences; answer "what is this, and why should I care?"
- `text-lg sm:text-xl text-gray-600 max-w-2xl`.

## Centered with Gradient Background

The most versatile pattern: SaaS, tools, platforms.

```html
<section class="relative isolate overflow-hidden bg-white">
  <div class="absolute inset-0 -z-10">
    <div class="absolute inset-0 bg-gradient-to-b from-indigo-50/80 via-white to-white"></div>
    <div class="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/4
      w-[800px] h-[600px] rounded-full
      bg-gradient-to-br from-indigo-200/40 via-purple-200/30 to-pink-100/20
      blur-3xl"></div>
  </div>

  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 pt-24 pb-16 sm:pt-32 sm:pb-24 text-center">
    <a href="#" class="inline-flex items-center gap-2 rounded-full bg-indigo-50 px-4 py-1.5
      text-sm font-medium text-indigo-700 ring-1 ring-inset ring-indigo-600/10
      hover:bg-indigo-100 transition-colors mb-8">
      <span class="h-1.5 w-1.5 rounded-full bg-indigo-600 motion-safe:animate-pulse" aria-hidden="true"></span>
      Announcing our Series A
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
      </svg>
    </a>

    <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight
      text-gray-950 max-w-4xl mx-auto leading-[1.1]">
      Build products that
      <span class="bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">users love</span>
    </h1>

    <p class="mt-6 text-lg sm:text-xl text-gray-600 max-w-2xl mx-auto leading-relaxed">
      The design-to-code platform that turns your ideas into production-ready
      interfaces in minutes, not weeks.
    </p>

    <div class="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4">
      <a href="#" class="w-full sm:w-auto inline-flex items-center justify-center
        bg-indigo-600 text-white px-8 py-3.5 rounded-xl font-semibold text-lg
        hover:bg-indigo-500 shadow-lg shadow-indigo-600/25
        hover:shadow-xl hover:shadow-indigo-600/30
        hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200">
        Start building free
      </a>
      <a href="#" class="w-full sm:w-auto inline-flex items-center justify-center gap-2
        text-gray-700 px-8 py-3.5 rounded-xl font-semibold text-lg
        hover:bg-gray-100 transition-colors">
        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
          <path d="M6.3 2.84A1.5 1.5 0 004 4.11v11.78a1.5 1.5 0 002.3 1.27l9.344-5.891a1.5 1.5 0 000-2.538L6.3 2.841z"/>
        </svg>
        Watch demo
      </a>
    </div>

    <!-- Trust signals: repeat the check icon per item -->
    <div class="mt-10 flex flex-wrap items-center justify-center gap-x-6 gap-y-2 text-sm text-gray-500">
      <span class="flex items-center gap-1.5">
        <svg class="w-4 h-4 text-emerald-500" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
          <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd"/>
        </svg>
        No credit card required
      </span>
      <!-- Free for individuals; Setup in 2 minutes -->
    </div>

    <div class="mt-16 relative">
      <div class="rounded-2xl border border-gray-200/60 shadow-2xl shadow-gray-900/10 overflow-hidden bg-white">
        <img src="/dashboard-preview.webp" alt="Product dashboard showing weekly revenue"
          width="1280" height="800" class="w-full h-auto" fetchpriority="high" />
      </div>
      <div class="absolute -inset-4 -z-10 bg-gradient-to-b from-indigo-100/50
        to-transparent rounded-3xl blur-2xl"></div>
    </div>
  </div>
</section>
```

## Split (Text Left, Image Right)

For products with a strong visual (app screenshots, mockups).

```html
<section class="relative overflow-hidden bg-white">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-20 lg:py-32">
    <div class="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center">
      <div class="max-w-xl">
        <div class="inline-flex items-center gap-2 rounded-full bg-emerald-50 px-3 py-1
          text-sm font-medium text-emerald-700 ring-1 ring-emerald-600/10 mb-6">
          New: AI assistant is here
        </div>
        <h1 class="text-4xl lg:text-5xl xl:text-6xl font-extrabold tracking-tight text-gray-950 leading-[1.1]">
          Your finances, finally simple
        </h1>
        <p class="mt-6 text-lg text-gray-600 leading-relaxed">
          Track spending, set budgets, and reach your goals with an app that
          actually makes sense.
        </p>
        <div class="mt-8 flex flex-wrap gap-4">
          <a href="#" class="bg-gray-950 text-white px-6 py-3 rounded-xl font-semibold
            hover:bg-gray-800 transition-colors">Download the app</a>
          <a href="#" class="text-gray-700 px-6 py-3 rounded-xl font-semibold
            hover:bg-gray-100 transition-colors flex items-center gap-2">
            See how it works
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
            </svg>
          </a>
        </div>
        <div class="mt-8 flex items-center gap-4">
          <div class="flex -space-x-2">
            <img src="/avatar-1.jpg" class="w-8 h-8 rounded-full ring-2 ring-white" alt="" />
            <img src="/avatar-2.jpg" class="w-8 h-8 rounded-full ring-2 ring-white" alt="" />
            <img src="/avatar-3.jpg" class="w-8 h-8 rounded-full ring-2 ring-white" alt="" />
          </div>
          <div class="text-sm text-gray-600"><span class="font-semibold text-gray-900">4,000+</span> happy users</div>
        </div>
      </div>

      <div class="relative lg:ml-auto">
        <div class="relative z-10">
          <img src="/app-mockup.webp" alt="App home screen with monthly budget overview"
            width="448" height="896" class="w-full h-auto max-w-md mx-auto rounded-3xl shadow-2xl"
            fetchpriority="high" />
        </div>
        <div class="absolute -inset-8 bg-gradient-to-tr from-indigo-100 via-purple-50
          to-pink-50 rounded-[2rem] -z-10 blur-sm"></div>
      </div>
    </div>
  </div>
</section>
```

## Video / Animated Background

```html
<!-- svh, not h-screen/100vh: 100vh is taller than the visible area on mobile browsers -->
<section class="relative h-svh min-h-[600px] max-h-[900px] flex items-center overflow-hidden">
  <video autoplay muted loop playsinline aria-hidden="true" poster="/hero-poster.jpg"
    class="absolute inset-0 w-full h-full object-cover">
    <source src="/hero-bg.webm" type="video/webm" />
    <source src="/hero-bg.mp4" type="video/mp4" />
  </video>
  <div class="absolute inset-0 bg-gray-950/60"></div>

  <div class="relative z-10 mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 text-center">
    <h1 class="text-4xl sm:text-5xl lg:text-7xl font-extrabold tracking-tight text-white leading-[1.1]">
      Experience the future
    </h1>
    <p class="mt-6 text-lg sm:text-xl text-white/80 max-w-2xl mx-auto">
      Immersive technology that transforms how you create.
    </p>
    <div class="mt-10">
      <a href="#" class="inline-flex items-center bg-white text-gray-950 px-8 py-4
        rounded-xl font-semibold text-lg hover:bg-gray-100 transition-colors">Get early access</a>
    </div>
  </div>

  <!-- Pause control: required for motion lasting over 5s (WCAG 2.2.2).
       JS: toggle video.pause()/play() and swap the label to "Play background video" -->
  <button type="button" class="absolute bottom-6 right-6 z-10 rounded-full bg-black/50
    px-4 py-2 text-sm text-white focus-visible:outline focus-visible:outline-2
    focus-visible:outline-white">Pause background video</button>

  <div class="absolute bottom-8 left-1/2 -translate-x-1/2 motion-safe:animate-bounce" aria-hidden="true">
    <svg class="w-6 h-6 text-white/60" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"/>
    </svg>
  </div>
</section>
```

Rules:

- 5-15 second loop, under 5MB; ship WebM plus MP4.
- Always set a `poster`; it is the LCP candidate, so preload it with `fetchpriority="high"`.
- `playsinline` for iOS.
- Provide a pause button. Under `prefers-reduced-motion: reduce`, don't autoplay: call `video.pause()` when `matchMedia('(prefers-reduced-motion: reduce)').matches` and show the poster.
- Text needs sufficient contrast against the overlay.

## Minimal Typography

For premium brands, agencies, portfolios.

```html
<section class="min-h-svh flex items-center bg-gray-950">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-32">
    <h1 class="text-5xl sm:text-7xl lg:text-9xl font-extrabold text-white tracking-tighter leading-[0.9]">
      We design<br />
      <span class="text-gray-500">digital</span><br />
      experiences
    </h1>
    <div class="mt-12 flex items-center gap-6">
      <a href="#" class="text-white border border-white/20 px-6 py-3 rounded-full
        hover:bg-white hover:text-gray-950 transition-all font-medium">View our work</a>
      <a href="#" class="text-gray-400 hover:text-white transition-colors font-medium">Contact us</a>
    </div>
  </div>
</section>
```

## Backgrounds

```css
/* Mesh gradient */
.mesh-gradient {
  background-color: oklch(97% 0.01 265);
  background-image:
    radial-gradient(at 20% 20%, oklch(90% 0.12 280 / 0.4) 0px, transparent 50%),
    radial-gradient(at 80% 10%, oklch(90% 0.10 320 / 0.3) 0px, transparent 50%),
    radial-gradient(at 50% 80%, oklch(90% 0.12 200 / 0.3) 0px, transparent 50%);
}

/* Animated gradient: build stops from brand tokens, not arbitrary colors */
.animated-gradient {
  background: linear-gradient(-45deg, var(--color-primary), var(--color-secondary), var(--color-accent), var(--color-primary-light));
  background-size: 400% 400%;
}
@media (prefers-reduced-motion: no-preference) {
  .animated-gradient { animation: gradient-shift 15s ease infinite; }
}
@keyframes gradient-shift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Dot grid */
.dot-grid {
  background-image: radial-gradient(circle, #d1d5db 1px, transparent 1px);
  background-size: 24px 24px;
}

/* Noise texture */
.noise { position: relative; }
.noise::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none;
}
```

For photographic or generated backgrounds see [image-treatment](image-treatment.md).

## Responsive Strategy

```text
Mobile (< 640px):
  - h1 text-3xl to text-4xl
  - Stack CTAs (flex-col), full-width buttons
  - Hide decorative elements
  - Product image below text

Tablet (640-1024px):
  - h1 text-4xl to text-5xl
  - CTAs side by side
  - Product image scales down

Desktop (1024px+):
  - h1 text-5xl to text-6xl
  - Split layout side by side
  - Full decorative elements
```

Art-directed images:

```html
<picture>
  <source media="(min-width: 1024px)" srcset="/hero-desktop.webp" />
  <source media="(min-width: 640px)" srcset="/hero-tablet.webp" />
  <img src="/hero-mobile.webp" alt="Product preview" width="640" height="480"
    class="w-full h-auto rounded-2xl" fetchpriority="high" />
</picture>
```

## LCP Performance

The hero is almost always the Largest Contentful Paint element.

1. `fetchpriority="high"` on the hero `<img>`, with `width` and `height` to prevent CLS.
2. Never `loading="lazy"` on it.
3. Preload only late-discovered images: CSS backgrounds, JS-rendered heroes, video posters, `<picture>` art direction. An `<img>` already in the HTML doesn't need it.
4. Inline critical CSS for the hero. Don't animate the headline in from `opacity: 0`; it delays LCP.
5. WebP or AVIF with fallback.
6. Size appropriately with `srcset` and `sizes`; no 4000px image in a 1200px container.

```html
<head>
  <link rel="preload" href="/hero.webp" as="image" fetchpriority="high"
    imagesrcset="/hero-400.webp 400w, /hero-800.webp 800w, /hero-1200.webp 1200w"
    imagesizes="100vw" />
</head>
```

## Verification

Render at 390px and 1440px and view both. At 390px the headline and primary CTA must sit above the fold. Confirm the LCP image isn't lazy-loaded. Tab through for visible focus.

## Checklist

- [ ] Headline under 10 words, states the benefit
- [ ] Subheadline expands the value in 1-2 sentences
- [ ] Primary CTA large, high-contrast, action-oriented
- [ ] Secondary CTA visually subordinate
- [ ] Trust signals near the CTA
- [ ] Hero image has `fetchpriority="high"`, `width` and `height`, no `loading="lazy"`
- [ ] Decorative SVGs `aria-hidden`; text over images or video meets 4.5:1
- [ ] Responsive: text scales, layout adapts, images swap
- [ ] Background adds interest without competing with content
- [ ] Animation respects `prefers-reduced-motion`; background video has a pause control
- [ ] LCP under 2.5s
