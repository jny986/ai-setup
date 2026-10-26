---
name: writing
description: "Writing workflows: explore fragments, shape an article, choose beats, edit a draft, humanize prose, write technical documentation using ASD-STE100, write documents for agents, or review and improve agent-facing documentation. Sub-skills: fragments, shape, beats, edit, humanize, technical, agents, review."
argument-hint: "[sub-skill] [task]"
disable-model-invocation: true
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

A router for writing workflows. Read the sub-skills required by the steps below.

For all writing, read and follow the [ISO 24495-1 plain-language reference](sub-skills/references/iso-24495-plain-language.md) unless the user or project provides another writing standard. Follow the provided standard when one is specified. Respect the reference's preview coverage limits when reporting conformity.

## Steps

1. **Pick the sub-skill.** Use the sub-skill named in the argument. Otherwise match the task to the table below; ask once if the intended workflow is unclear. For an agent-consumed document, read `agents` first, then another sub-skill only if the task needs it.
2. **Follow it.** Read the linked document and follow it as if it were the skill. Keep the user's requested scope and pace; an interactive drafting session starts only when requested.
3. **Humanize before finalizing.** After creating writing for human readers, run [humanize](sub-skills/humanize.md) in embedded mode before delivering or saving the final content. Preserve facts, the author's voice and the applicable writing standard. Skip this pass for agent-facing writing. If `humanize` was already the selected workflow, its completed pass satisfies this step.

## Sub-skills

| Sub-skill | Use when |
|---|---|
| [`fragments`](sub-skills/fragments.md) | Explore an idea through conversation and capture raw material before choosing a structure |
| [`shape`](sub-skills/shape.md) | Shape existing raw material into an article together, paragraph by paragraph |
| [`beats`](sub-skills/beats.md) | Build a piece together by choosing the next narrative or argumentative move from candidate beats |
| [`edit`](sub-skills/edit.md) | Improve an existing draft's argument, structure, clarity and flow while preserving meaning and voice |
| [`humanize`](sub-skills/humanize.md) | Remove AI writing patterns from prose while preserving its facts and the author's voice |
| [`technical`](sub-skills/technical.md) | Write or revise technical documentation when the user requests or the project requires ASD-STE100 Simplified Technical English |
| [`agents`](sub-skills/agents.md) | Write or revise skills, AGENTS.md, CLAUDE.md and other documents consumed by agents |
| [`review`](sub-skills/review.md) | Review or improve agent-facing documents, including skills, routers, references, AGENTS.md and CLAUDE.md |

## How they fit

`fragments` gathers material. `shape` and `beats` are alternative interactive ways to draft from it. `edit` revises an existing draft; `humanize` targets AI writing patterns and supplies the required final pass for newly created writing for human readers.

`agents` supplies shared guidance for writing agent-facing documents. `review` applies that guidance to existing documents and their consumers, reporting findings or making requested improvements.

`technical` applies ASD-STE100 when the user explicitly selects that workflow or the user or project specifies STE. Other technical-writing requests keep the ISO plain-language default. Combine `technical` with `agents` for agent-facing technical documents when requested; keep technical accuracy and verify the standard's vocabulary as well as its writing rules.

Marketing copy, SEO content, campaigns and sales email use the specialist workflows in `marketing` when that skill is available. A prose-only editing request can stay here.
