---
name: infographic
description: "Turn information into an understandable visual narrative with accurate data, hierarchy, and readable labels."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: ArnavPuri/designskills
  based_on_version: main(c787301)
  based_on_skill: infographic
---

# Infographic Design

Standalone graphics that explain data, processes, comparisons, and timelines. Interactive app dashboards: [dashboard-design](dashboard-design.md). Single stat posts for feeds: [social-media-graphic](social-media-graphic.md).

Read `DESIGN.md` for UI tokens and the project brand kit for approved brand primitives (see [design-context](design-context.md)); when absent, inspect the project's existing CSS variables or Tailwind theme. A consistent color system for data categories matters most here.

## Choosing the path

Chart geometry and numbers from image-generation tools are illustrative, not accurate: bar heights will not match data and digits get garbled. Use HTML/CSS/SVG whenever the graphic plots real data or has more than about 8 short text labels. Use image generation for illustrated, low-text pieces (icons, scenes, a few big stats), or generate illustrations and lay out the data in code around them.

### Image-generation path

Prompt craft, cropping, and text-overlay fallback: [image-generation](image-generation.md).

1. Ratios: 2:3 or 9:16 vertical (Pinterest-style), 1:4 long-form scroll, 4:5 or 1:1 feeds, 16:9 slides. Use the highest resolution available; tall ratios make text tiny.
2. Quote every number and label exactly; keep to about 8 short labels. Split long infographics into sections generated separately and stacked in code.
3. View the output and check every number, label, and unit against the source data. Any mismatch is a defect: fix it in a follow-up or move that text to a code overlay.

Example prompts:

- **Statistics:** "Create an infographic showing [topic] statistics. [number] key metrics displayed as large numbers with icons. [color palette] color scheme. Clean grid layout with section headers. Professional, data-driven design."
- **Process flow:** "Create a process flow infographic for [process name]. [number] steps connected by arrows. Each step has an icon, title, and one-line description. [color] gradient progression from start to finish. Vertical layout, modern style."
- **Timeline:** "Create a timeline infographic for [subject]. [number] milestones from [start year] to [end year]. Alternating left-right layout along a vertical line. [color palette]. Key dates and brief descriptions at each point."

## Types

| Type | Best for | Layout |
|------|----------|--------|
| Process flow | Step-by-step procedures | Horizontal or vertical chain |
| Comparison | Two or more options | Columns or split |
| Statistics | Key numbers | Grid of stat cards |
| Timeline | Chronological events | Vertical or horizontal line |
| List / ranking | Top N items | Numbered vertical list |
| Data chart | Quantitative data | Bar, pie, line via SVG |
| Icon grid | Category overview | Grid of icon + label pairs |

## Color coding

Assign colors systematically; never use random colors for categories. Palette generation: [color-palette](color-palette.md).

```css
/* Sequential (ordered data) */
:root { --data-1: #EFF6FF; --data-2: #BFDBFE; --data-3: #60A5FA; --data-4: #2563EB; --data-5: #1E40AF; }

/* Categorical (distinct categories) */
:root { --cat-a: #6366F1; --cat-b: #EC4899; --cat-c: #F59E0B; --cat-d: #10B981; --cat-e: #8B5CF6; --cat-f: #EF4444; }

/* Diverging (positive/negative) */
:root { --neg-strong: #EF4444; --neg-light: #FCA5A5; --neutral: #E5E7EB; --pos-light: #86EFAC; --pos-strong: #22C55E; }
```

Rules:

- Brand primary for the most important data point; neutral grays for context and baseline.
- Chart marks (bars, lines, slices) need 3:1 contrast against the background and adjacent marks (WCAG 1.4.11). Light steps (`--data-1`, amber `--cat-c`) fail on white: add a darker outline or use them only on dark backgrounds.
- Text needs 4.5:1 (3:1 if 24px+, or 18.66px+ bold).
- Never rely on color alone: label series directly or add patterns/icons (WCAG 1.4.1).
- Maximum 6 distinct colors per chart.

## Process flow

```css
.process-flow { display: flex; align-items: flex-start; gap: 0; padding: 40px; }
.step { flex: 1; text-align: center; position: relative; padding: 0 20px; }
.step-icon {
  width: 48px; height: 48px; border-radius: 50%; background: var(--primary);
  color: #fff; display: flex; align-items: center; justify-content: center;
  font-size: 18px; font-weight: 700; margin: 0 auto 16px; position: relative; z-index: 2;
}
.step-connector {
  position: absolute; top: 24px; left: calc(50% + 24px); right: calc(-50% + 24px);
  height: 2px; background: var(--primary); opacity: 0.3; z-index: 1;
}
.step:last-child .step-connector { display: none; }
```

Vertical: `flex-direction: column` with a `::before` pseudo-element as the connecting line, absolutely positioned left of the items.

## Comparison

```css
.comparison-table { width: 100%; border-collapse: separate; border-spacing: 0; }
.comparison-table thead th { padding: 20px; font-size: 18px; font-weight: 700; text-align: center; border-bottom: 2px solid #E5E7EB; }
.comparison-table thead th.highlighted { background: var(--primary); color: #fff; border-radius: 12px 12px 0 0; }
.comparison-table td { padding: 14px 20px; text-align: center; border-bottom: 1px solid #F3F4F6; font-size: 14px; }
.check { color: #15803D; } .cross { color: #6B7280; } /* 3:1+ on white; pair with check/cross glyphs, not color alone */
```

Versus layout: `grid-template-columns: 1fr auto 1fr` with a large "VS" element between two option cards.

## Statistics

### Big number card

```css
.stat-card { text-align: center; padding: 32px; border-radius: 16px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); }
.stat-number {
  font-size: 56px; font-weight: 800; line-height: 1; margin-bottom: 8px;
  color: var(--primary); /* solid fallback */
  background: linear-gradient(135deg, var(--primary), var(--accent));
  -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
}
.stat-label { font-size: 14px; font-weight: 500; color: #9CA3AF; text-transform: uppercase; letter-spacing: 0.05em; }
```

Gradient text must still meet 3:1 (large text) at both gradient ends; the label color above assumes a dark card.

### Progress indicators

```css
/* Percentage bar */
.percent-bar { height: 8px; background: #E5E7EB; border-radius: 4px; overflow: hidden; }
.percent-bar .fill { height: 100%; background: linear-gradient(90deg, var(--primary), var(--accent)); border-radius: 4px; animation: fillBar 1.5s ease-out; }
@keyframes fillBar { from { width: 0; } }

/* Circular progress: set a unitless --progress, e.g. style="--progress: 72" */
.circle-progress {
  width: 120px; height: 120px; border-radius: 50%;
  background: conic-gradient(var(--primary) 0deg, var(--primary) calc(var(--progress) * 3.6deg), #E5E7EB calc(var(--progress) * 3.6deg));
  display: flex; align-items: center; justify-content: center;
}
```

## Timelines

```css
.timeline { position: relative; padding: 20px 0; max-width: 600px; margin: 0 auto; }
.timeline::before {
  content: ''; position: absolute; left: 50%; top: 0; bottom: 0; width: 2px;
  background: linear-gradient(180deg, transparent, var(--primary), var(--primary), transparent);
  transform: translateX(-50%);
}
.timeline-item { display: flex; align-items: flex-start; margin-bottom: 40px; position: relative; }
.timeline-item:nth-child(odd) { padding-right: calc(50% + 30px); text-align: right; }
.timeline-item:nth-child(even) { flex-direction: row-reverse; padding-left: calc(50% + 30px); text-align: left; }
.timeline-dot {
  position: absolute; left: 50%; transform: translateX(-50%);
  width: 16px; height: 16px; border-radius: 50%; background: var(--primary);
  border: 3px solid var(--bg-color); z-index: 2;
}
.timeline-content { padding: 16px 20px; background: rgba(255,255,255,0.05); border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); }
```

Horizontal: `display: flex` with a `::before` horizontal line; each item has a dot with content below.

## SVG charts

- **Bar:** `<rect>` elements on a y-axis baseline; `<animate>` for entrance on height/y; `<text>` axis labels; `<line>` gridlines.
- **Donut:** `<circle>` with `stroke-dasharray`/`stroke-dashoffset` per segment; `rotate(-90)` to start at the top; center `<text>` for the key metric.
- **Line:** `<polyline>` for the data, filled `<path>` for the area, `<circle>` per point, `<linearGradient>` for the area fill.

Compute geometry from the data; never eyeball it.

```html
<svg viewBox="0 0 400 250" width="400" height="250" xmlns="http://www.w3.org/2000/svg">
  <!-- Grid lines, axes, labels -->
  <!-- Data elements with optional <animate> -->
  <!-- Gradient definitions in <defs> -->
</svg>
```

For responsive charts set CSS `width: 100%; height: auto`.

## Icon-driven data points

```css
.icon-stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 32px; padding: 40px; }
.icon-stat { display: flex; align-items: flex-start; gap: 16px; }
.icon-stat .icon-circle {
  width: 48px; height: 48px; border-radius: 12px; flex-shrink: 0;
  background: color-mix(in srgb, var(--primary) 10%, transparent);
  display: flex; align-items: center; justify-content: center;
}
.icon-stat .value { font-size: 28px; font-weight: 800; line-height: 1; margin-bottom: 4px; }
.icon-stat .label { font-size: 13px; color: #6B7280; }
```

Icon sourcing and style: [icon-design](icon-design.md).

## Layout templates

- **Long-form vertical:** 800px wide (web) or 1000px (print). Header, then sections separated by dividers, then takeaway and footer; 60px between sections.
- **Dashboard-style grid:**

```css
.info-dashboard { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; padding: 40px; }
.info-dashboard .header { grid-column: 1 / -1; }
.info-dashboard .chart-main { grid-column: 1 / 3; }
.info-dashboard .chart-side { grid-column: 3; }
.info-dashboard .footer { grid-column: 1 / -1; }
```

## Checklist

- [ ] Numbers match visuals; bar/slice sizes computed from data
- [ ] Rendered output viewed; every number, label, and unit checked against the source
- [ ] Color coding consistent and meaningful (max 6 colors)
- [ ] All data points labeled
- [ ] Hierarchy guides the reader through the content
- [ ] Source attribution where appropriate
- [ ] Brand colors applied
- [ ] SVG charts have a viewBox and scale correctly
- [ ] Text and marks meet contrast; color is not the only encoding
- [ ] Animation subtle and explanatory
- [ ] Enough whitespace between sections
