---
name: landing-page-design
description: "Design landing pages around the audience, offer, evidence, conversion action, and responsive composition."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: landing-page-design
---

# Landing Page Design

Full multi-section marketing and conversion pages: section order, CTA strategy, page-level performance. The hero block is in [hero-section](hero-section.md); individual cards in [card-design](card-design.md); general components in [ui-design](ui-design.md).

Read `DESIGN.md` for UI tokens and the project brand kit for approved brand primitives (see [design-context](design-context.md)); when absent, inspect the project's existing CSS variables or Tailwind theme. The `indigo-*` / `gray-*` classes below are placeholders for primary and neutral tokens. Settle the product, the audience, and the single desired action first. Use `PRODUCT.md` and the brand kit for voice, and `DESIGN.md` for the visual direction of the hero and section backgrounds.

## Section Framework

Reorder or omit as needed; this is the proven sequence:

```text
1. Hero          Value prop + primary CTA (above the fold)
2. Social proof  Logos, stats, or trust badges
3. Features      Benefits, not features
4. How it works  3-step simplicity
5. Testimonials  Real people, real outcomes
6. Pricing       Clear tiers, obvious recommendation
7. FAQ           Overcome objections
8. Final CTA     Repeat the primary action
9. Footer        Links, legal, secondary nav
```

- Major sections: `py-20 md:py-28 lg:py-32`; alternate white and `bg-gray-50`.
- Content container: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`.
- Use a minimal header; no competing navigation.

## Hero

Use the patterns, backgrounds, and LCP rules in [hero-section](hero-section.md). Default is the centered hero (best for SaaS): optional badge, 10-word benefit headline, 1-2 sentence subhead, primary CTA plus subordinate ghost CTA, one line of trust text ("No credit card required. Free for up to 3 projects.").

## Social Proof

Logo bar:

```html
<section class="bg-gray-50 py-12 border-y border-gray-100">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <p class="text-center text-sm font-medium text-gray-500 mb-8">Trusted by 2,000+ teams worldwide</p>
    <div class="flex flex-wrap items-center justify-center gap-x-12 gap-y-6
      grayscale opacity-60 hover:grayscale-0 hover:opacity-100 transition-all">
      <!-- SVG logos preferred, h-7, auto width -->
      <img src="/logos/stripe.svg" alt="Stripe" width="112" height="28" class="h-7 w-auto" loading="lazy" />
      <img src="/logos/vercel.svg" alt="Vercel" width="112" height="28" class="h-7 w-auto" loading="lazy" />
    </div>
  </div>
</section>
```

Stats:

```html
<div class="grid grid-cols-2 lg:grid-cols-4 gap-8 text-center">
  <div>
    <div class="text-4xl font-extrabold text-gray-950">10K+</div>
    <div class="mt-1 text-sm text-gray-500">Active users</div>
  </div>
  <div>
    <div class="text-4xl font-extrabold text-gray-950">99.9%</div>
    <div class="mt-1 text-sm text-gray-500">Uptime SLA</div>
  </div>
</div>
```

Use only logos, counts, and claims that are true and sourced.

## Features

Bento grid (modern, visual):

```html
<section class="py-20 bg-white">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16">
      <h2 class="text-3xl sm:text-4xl font-bold text-gray-950">Everything you need</h2>
      <p class="mt-4 text-lg text-gray-600 max-w-2xl mx-auto">A complete toolkit for modern teams.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div class="md:col-span-2 bg-gradient-to-br from-indigo-600 to-purple-700
        rounded-2xl p-8 text-white min-h-[300px] flex flex-col justify-end">
        <h3 class="text-2xl font-bold">AI-powered insights</h3>
        <p class="mt-2 text-white/90">Automatically surface what matters most.</p>
      </div>
      <div class="bg-gray-50 rounded-2xl p-8 min-h-[300px] flex flex-col justify-end">
        <div class="w-10 h-10 rounded-lg bg-indigo-100 text-indigo-600 flex items-center
          justify-center mb-4" aria-hidden="true"><!-- icon --></div>
        <h3 class="text-lg font-bold text-gray-950">Real-time sync</h3>
        <p class="mt-2 text-gray-600">Changes appear instantly across all devices.</p>
      </div>
    </div>
  </div>
</section>
```

- Alternating rows (classic, detailed): odd rows text left and image right, even rows reversed; one feature per row with heading, description, visual.
- Icon grid (simple, scannable): 3 or 4 columns of icon, heading, short description. One icon style throughout (outline or filled, not mixed).

Card patterns are in [card-design](card-design.md).

## CTA Design

- Size: at least 48px tall, 200px+ wide; larger than any other button on the page.
- Color: the highest-contrast element on the page, in the primary brand color.
- Copy: action verb. "Start free trial" over "Submit"; "Get started" over "Sign up".
- Urgency (optional): "Start free, no credit card required."
- Repetition: primary CTA at least 3 times (hero, mid-page, bottom).
- Secondary: ghost button beside the primary, or a text link with arrow. Never two equally weighted CTAs side by side.
- `<a>` for CTAs that navigate; `<button>` for ones that open a modal or submit.

Sticky mobile CTA. Add `pb-24` to `<body>` on mobile so the bar never covers the footer.

```html
<div class="fixed bottom-0 inset-x-0 bg-white/90 backdrop-blur-lg border-t
  border-gray-200 px-4 pt-4 pb-[calc(1rem+env(safe-area-inset-bottom))] sm:hidden z-50">
  <a href="#" class="block w-full bg-indigo-600 text-white text-center py-3.5 rounded-xl font-semibold text-lg">
    Start free trial
  </a>
</div>
```

## How It Works

Three steps; if the process has more, simplify or group.

```html
<section class="py-20 bg-gray-50">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-bold text-center text-gray-950 mb-16">Get started in minutes</h2>
    <div class="grid md:grid-cols-3 gap-12">
      <div class="text-center">
        <div class="w-12 h-12 rounded-full bg-indigo-100 text-indigo-600 font-bold
          text-lg flex items-center justify-center mx-auto">1</div>
        <h3 class="mt-4 text-lg font-semibold text-gray-950">Connect your data</h3>
        <p class="mt-2 text-gray-600">Import from 50+ sources with one click.</p>
      </div>
      <!-- steps 2 and 3 repeat the pattern -->
    </div>
  </div>
</section>
```

## Testimonials

```html
<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
  <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100">
    <div class="flex gap-1 text-amber-400 mb-4" role="img" aria-label="Rated 5 out of 5">
      <!-- 5 star icons, each aria-hidden="true" -->
    </div>
    <blockquote class="text-gray-700 leading-relaxed">
      "This completely changed how our team works. We shipped 3x faster in the first month."
    </blockquote>
    <div class="mt-4 flex items-center gap-3">
      <img src="/avatars/sarah.jpg" alt="" width="40" height="40" loading="lazy" class="w-10 h-10 rounded-full" />
      <div>
        <div class="font-semibold text-gray-950 text-sm">Sarah Chen</div>
        <div class="text-gray-500 text-sm">CTO, Acme Corp</div>
      </div>
    </div>
  </div>
</div>
```

- Real photos, names, and companies, with role or title.
- Highlight specific outcomes ("3x faster", "saved 20 hours/week").
- Star ratings add credibility.

## Pricing

Three tiers:

- Free/Basic: anchor price, limited features.
- Pro (recommended): highlighted with border, badge, or shadow; most features.
- Enterprise: "Contact sales", unlimited.

Rules:

- Highlight the recommended plan with `ring-2 ring-indigo-600` and `lg:scale-105` (no scaling on mobile; stacked cards overflow).
- "Most Popular" badge.
- Annual/monthly toggle with a savings callout: a real `<button role="switch" aria-checked>` or radio group, not a styled `<div>`.
- Checkmarks for included features, dashes or X for excluded.
- Price: large number, small period (**$29**/mo).

## Trust Signals

Spread through the page, not one section:

- Security badges: SSL, SOC 2, GDPR (only those actually held).
- Guarantee: "30-day full refund, no questions asked."
- Support: "24/7 support" or "Avg. response time: 2 hours."
- Social proof near CTAs: "Join 10,000+ teams."
- Press logos.

## Performance

Above the fold: follow the LCP rules in [hero-section](hero-section.md). Targets (Core Web Vitals, 75th percentile): LCP 2.5s or under, INP 200ms or under, CLS 0.1 or under.

Below the fold:

- `loading="lazy"` on all images.
- `srcset` for responsive images.
- Defer non-critical JS.
- `content-visibility: auto` with `contain-intrinsic-size: auto 800px` on far-down sections (without the size hint the scrollbar jumps).
- `width` and `height` (or `aspect-ratio`) on every image to prevent layout shift.

```html
<img src="/feature.webp"
  srcset="/feature-400.webp 400w, /feature-800.webp 800w, /feature-1200.webp 1200w"
  sizes="(max-width: 768px) 100vw, 50vw"
  width="1200" height="800" loading="lazy" alt="Feature description" class="rounded-2xl" />
```

## Flow and Spacing

1. F-pattern for text-heavy pages (scan top-left to right, then down-left).
2. Z-pattern for minimal pages.
3. Each section answers one question, then leads to the next.
4. White space reads as trustworthy; cramped pages don't.

Spacing:

- Between major sections: `py-20 md:py-28 lg:py-32`
- Between subsections: `py-12 lg:py-16`
- Heading to content: `mb-12 lg:mb-16`
- Between content items: `gap-6 lg:gap-8`

## Verification

Render at 390px and 1440px and view both. At 390px the headline and primary CTA must show without scrolling, and the sticky CTA must not cover content. Run a performance and accessibility audit if a server is available. Tab through for visible focus.

## Checklist

- [ ] One clear CTA, repeated 3+ times
- [ ] Hero LCP image: `fetchpriority="high"`, width/height, not lazy-loaded
- [ ] Social proof within the first scroll
- [ ] Copy leads with benefits over features
- [ ] Mobile-optimized (sticky CTA, stacked layout)
- [ ] LCP 2.5s or under, INP 200ms or under, CLS 0.1 or under
- [ ] Animations respect `prefers-reduced-motion`; text meets 4.5:1 contrast
- [ ] No competing navigation (minimal header)
