---
name: writing
description: "Writing workflows: explore fragments, shape an article, choose beats, edit a draft, humanize prose, or write documents for agents. Sub-skills: fragments, shape, beats, edit, humanize, agents."
argument-hint: "[sub-skill] [task]"
disable-model-invocation: true
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

A router for writing workflows. Read only the sub-skill needed for the current task.

## Steps

1. **Pick the sub-skill.** Use the sub-skill named in the argument. Otherwise match the task to the table below; ask once if the intended workflow is unclear. For an agent-consumed document, read `agents` first, then another sub-skill only if the task needs it.
2. **Follow it.** Read the linked document and follow it as if it were the skill. Keep the user's requested scope and pace; an interactive drafting session starts only when requested.

## Sub-skills

| Sub-skill | Use when |
|---|---|
| [`fragments`](sub-skills/fragments.md) | Explore an idea through conversation and capture raw material before choosing a structure |
| [`shape`](sub-skills/shape.md) | Shape existing raw material into an article together, paragraph by paragraph |
| [`beats`](sub-skills/beats.md) | Build a piece together by choosing the next narrative or argumentative move from candidate beats |
| [`edit`](sub-skills/edit.md) | Improve an existing draft's argument, structure, clarity and flow while preserving meaning and voice |
| [`humanize`](sub-skills/humanize.md) | Remove AI writing patterns from prose while preserving its facts and the author's voice |
| [`agents`](sub-skills/agents.md) | Write or revise skills, AGENTS.md, CLAUDE.md and other documents consumed by agents |

## How they fit

`fragments` gathers material. `shape` and `beats` are alternative interactive ways to draft from it. `edit` revises an existing draft; `humanize` targets AI writing patterns. Run only the stages the user requests.

Marketing copy, SEO content, campaigns and sales email use the specialist workflows in `marketing` when that skill is available. A prose-only editing request can stay here.
