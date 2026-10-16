---
name: optimize
description: "Diagnose and fix a measured UI performance bottleneck, then compare equivalent before and after scenarios."
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: pbakaus/impeccable
  based_on_version: main(2f98774)
  based_on_skill: optimize
---

# UI performance optimization

Use for a measured load, interaction, scroll, or animation problem. For a broad quality diagnosis use [audit](../audit.md); for final visual and interaction finish use [polish](polish.md). The target is a faster user task, verified under comparable conditions.

1. **Measure a baseline.** Name the slow action, affected users or devices, and a reproducible scenario. Capture the relevant evidence: load waterfall and Core Web Vitals for loading, a performance trace for interaction or animation, or render profiling for repeated updates. Record device, network, build mode, and metric before changing code. Finish when one dominant bottleneck is identified from the trace.
2. **Fix the bottleneck.** Match the remedy to the evidence: correctly sized and prioritized images, fewer blocking resources, deferred noncritical code, less main-thread work, virtualized long lists, batched layout reads and writes, bounded paint effects, or reduced unnecessary renders. Preserve the task, accessibility, and visual direction. Finish when the suspected cost is removed or reduced in the trace.
3. **Compare and check.** Reproduce the same scenario under the same conditions. Compare the before and after metric and trace; test the task, layout, and accessibility for regressions. If the metric does not improve, revise the diagnosis rather than claiming a win. Finish when the user-facing measure improves and the task still works.

| Symptom | Evidence to inspect |
|---|---|
| Slow first view | Largest Contentful Paint element, request waterfall, image dimensions, font and script blocking, server response. |
| Slow input | Interaction to Next Paint trace, long tasks, event handlers, rendering work. |
| Layout jumping | Cumulative Layout Shift entries, missing media dimensions, late font swaps, inserted content. |
| Janky scrolling or motion | Frame timeline, layout or paint work, filter and shadow area, list size, scroll handlers. |

Use field data when available to confirm lab findings; distinguish the two in the report. Report the baseline, changed cause, comparable after-measure, and any untested device or network condition.
