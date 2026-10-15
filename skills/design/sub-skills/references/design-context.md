---
metadata:
  version: "1.0.0"
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: design-context
---

# Design Context

Canonical home of the `.agents/design-context.md` file format, default token fallbacks, CSS variable naming and style archetypes. Other references link here instead of repeating them.

## Procedure

1. Look for existing context, in priority order:
   1. `.agents/design-context.md`
   2. `tailwind.config.js` / `.ts` (theme.extend colors, fontFamily, spacing)
   3. Tailwind v4 `@theme` block, or CSS custom properties in `:root` / `globals.css`
   4. Token files: `tokens.json` (W3C DTCG `$value` / `$type`), `theme.js`, `design-system.*`
   5. Font loading: `next/font`, Google Fonts `<link>`, `@font-face`
   6. `manifest.json` / `site.webmanifest` (`theme_color`, `name`), `package.json` name
   7. Brand assets: `logo.svg`, `public/`, `assets/`, `brand/`, favicon
   8. Recurring colors, font stacks and spacing in existing components
   9. Variables from any connected design tool
2. Map what you find (see Detection mapping). Convert bare HSL components (`222 47% 11%`) and `oklch(...)` to hex when saving.
3. If anything was found, show it to the user for confirmation. Skip to step 6.
4. If nothing was found, gather the fields below conversationally, in natural groups, not as a checklist dump. Offer archetypes and defaults rather than open questions.
5. Validate the palette (see Validation) and report failures.
6. Save to `.agents/design-context.md` using the template. Add a `Last updated: YYYY-MM-DD` line and the detection source (for example "from tailwind.config.ts") at the top.
7. To update later: read the file, change only the requested fields, confirm, save. Never rewrite the whole file for one field.

Consumers: read the file first, use only its colors and fonts (never arbitrary ones), match the style archetype, respect tone and audience. With no file, use the defaults below and say so in the output.

## Detection mapping

| Found | Maps to |
|-------|---------|
| `colors.primary`, `--color-primary`, `--primary` | Primary |
| `colors.secondary`, `--color-secondary`, `--secondary` | Secondary |
| `colors.accent`, `--color-accent`, `--accent` | Accent |
| `fontFamily.heading` / `.display`, `--font-heading`, `--font-display` | Heading font |
| `fontFamily.sans`, `--font-body`, `--font-sans` | Body font |
| `--radius`, `--border-radius` | Border radius |

shadcn/ui projects use `--primary`, `--secondary`, `--accent`, `--muted`, `--destructive`, `--radius`.

## Fields to gather

### Brand core

| Field | Example |
|-------|---------|
| Brand name | Acme Studio |
| Tagline | Design without limits |
| Mission (one sentence) | Empower creators with professional tools |
| Industry | SaaS / Creative Tools |

### Color system

Collect at least the groups below as hex.

| Role | Purpose | Default |
|------|---------|---------|
| Primary | Brand color, CTAs, key UI | `#2563EB` |
| Primary Light | Hover, backgrounds | `#3B82F6` |
| Primary Dark | Active states, text on light | `#1D4ED8` |
| Secondary | Supporting color, secondary actions | `#7C3AED` |
| Accent | Highlights, badges, notifications | `#F59E0B` |
| Neutral 50 | Lightest background | `#FAFAFA` |
| Neutral 100 | Card backgrounds | `#F5F5F5` |
| Neutral 200 | Borders, dividers (decorative only) | `#E5E5E5` |
| Neutral 500 | Placeholder / muted text | `#737373` |
| Neutral 800 | Body text | `#262626` |
| Neutral 900 | Headings | `#171717` |
| Success | Positive states | `#10B981` |
| Warning | Caution states | `#F59E0B` |
| Error | Error states | `#EF4444` |

### Typography

| Field | Example |
|-------|---------|
| Heading font | Inter, sans-serif |
| Body font | Inter, sans-serif |
| Mono font | JetBrains Mono, monospace |
| Base size | 16px |
| Scale ratio | 1.25 (Major Third) |
| Heading / body weight | 700 / 400 |

Default scale (Tailwind's hand-tuned sizes, roughly but not exactly 1.25). For a true modular scale see [typography](typography.md).

| Step | px | rem |
|------|----|-----|
| xs | 12 | 0.75 |
| sm | 14 | 0.875 |
| base | 16 | 1 |
| lg | 18 | 1.125 |
| xl | 20 | 1.25 |
| 2xl | 24 | 1.5 |
| 3xl | 30 | 1.875 |
| 4xl | 36 | 2.25 |
| 5xl | 48 | 3 |
| 6xl | 60 | 3.75 |
| 7xl | 72 | 4.5 |

### Style archetype

| Style | Characteristics |
|-------|-----------------|
| Minimal | Generous whitespace, restrained palette, clean lines, subtle shadows |
| Bold | Saturated colors, large type, strong contrast, geometric shapes |
| Playful | Bright colors, rounded corners, illustrations, casual tone |
| Corporate | Structured grids, blue/gray palette, professional imagery, formal |
| Luxurious | Dark backgrounds, metallic accents, serif fonts, fine details |
| Retro | Vintage palettes, halftone textures, serif/slab type, warm tones |
| Brutalist | Raw, high contrast, monospace type, unconventional layout |
| Organic | Earth tones, natural textures, flowing shapes, warm neutrals |

### Audience and tone

Primary audience, aesthetic preferences, tone (for example "professional but approachable"), formality 1-5.

### Brand marks

Logo description and usage (placement, minimum size), icon style (for example "outlined, 2px stroke, rounded caps"), and file paths for logos and reference images (product photos, past designs). Record paths, not just descriptions: image-generation tools reproduce a logo or product far more faithfully from a reference file than from text.

### Brand rules

- Always: non-negotiables ("Logo on white or primary only", "Sentence case headlines").
- Never: things to avoid ("No gradients on the logo", "No stock handshake photos").
- Voice samples: 2-3 real headlines or taglines.

### Platform priority

High / Medium / Low for Web, Mobile, Social, Print.

## File template

```markdown
# Design Context

Last updated: YYYY-MM-DD (source: ...)

## Brand Identity
- **Name:** [name]
- **Tagline:** [tagline]
- **Mission:** [mission]
- **Industry:** [industry]

## Color System
| Role | Hex | Usage |
|------|-----|-------|
| Primary | #XXXXXX | CTAs, key elements |
| Primary Light | #XXXXXX | Hover, backgrounds |
| Primary Dark | #XXXXXX | Active, dark text |
| Secondary | #XXXXXX | Supporting elements |
| Accent | #XXXXXX | Highlights, badges |
| Neutral 50 | #XXXXXX | Light backgrounds |
| Neutral 100 | #XXXXXX | Card backgrounds |
| Neutral 200 | #XXXXXX | Borders |
| Neutral 500 | #XXXXXX | Muted text |
| Neutral 800 | #XXXXXX | Body text |
| Neutral 900 | #XXXXXX | Headings |
| Success | #XXXXXX | Positive |
| Warning | #XXXXXX | Caution |
| Error | #XXXXXX | Error |

## Typography
- **Heading Font:** [stack]
- **Body Font:** [stack]
- **Mono Font:** [stack]
- **Base Size:** [size]
- **Scale Ratio:** [ratio]
- **Heading Weight:** [weight]
- **Body Weight:** [weight]

## Design Style
- **Primary Style:** [archetype]
- **Border Radius:** [value]
- **Shadow Style:** [none/subtle/medium/dramatic]
- **Spacing System:** [4px/8px base grid]

## Audience
- **Primary:** [description]
- **Aesthetic:** [preferences]
- **Tone:** [tone]

## Brand Marks
- **Logo:** [description]
- **Logo Files:** [paths]
- **Reference Images:** [paths]
- **Icon Style:** [description]

## Brand Rules
- **Always:** [rules]
- **Never:** [rules]
- **Voice samples:** [examples]

## Platform Priority
- Web: [priority]
- Mobile: [priority]
- Social: [priority]
- Print: [priority]
```

## Validation

Check the palette before saving. Report failures and propose the nearest passing shade (same hue, adjusted lightness); never silently change brand colors. Compute contrast ratios with a WCAG calculator rather than by eye.

- Neutral 800 on Neutral 50 and on white: at least 4.5:1.
- White text on Primary buttons: at least 4.5:1. If it fails, use Primary Dark for text-bearing buttons.
- Primary as link text on white: at least 4.5:1.
- Neutral 500 on white: at least 4.5:1 when it carries meaning.
- Focus rings: at least 3:1 against their background.

## CSS variable naming

Use one convention everywhere so references and code stay interchangeable:

| Group | Pattern |
|-------|---------|
| Brand scale | `--brand-50` ... `--brand-950` |
| Neutral scale | `--gray-50` ... `--gray-950` |
| Status scales | `--success-*`, `--warning-*`, `--error-*`, `--info-*` |
| Type scale | `--text-xs` ... `--text-5xl` |
| Fonts | `--font-heading`, `--font-body`, `--font-mono` |
| Radius | `--radius` |

Scale generation lives in [color-palette](color-palette.md), the type scale in [typography](typography.md), token layering in [design-system](design-system.md).

## Default fallbacks

Use when no context exists and the user wants to proceed. State in the output that defaults were used and recommend setting up context.

| Token | Value |
|-------|-------|
| Primary | `#2563EB` (blue-600) |
| Secondary | `#7C3AED` (violet-600) |
| Accent | `#F59E0B` (amber-500) |
| Neutral | Tailwind gray scale |
| Heading / body font | Inter |
| Success | `#10B981` fills and icons, `#047857` text |
| Warning | `#F59E0B` fills and icons, `#B45309` text |
| Error | `#EF4444` fills and icons, `#B91C1C` text |
| Border radius | 8px |
| Style / tone | Minimal / Professional |

The light status shades fail 4.5:1 as text on white (about 2.5:1, 2.2:1, 3.8:1). Use them for fills, badges with dark text and icons; use the dark shades for text.

Inter plus blue-600 is the most common generic "AI" look. For anything expressive (posters, social graphics, landing pages), ask once ("any colors, fonts or sites you like the feel of?") before falling back.
