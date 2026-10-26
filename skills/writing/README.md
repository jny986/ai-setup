# Writing

One entry point for exploring ideas, drafting together, editing prose and writing agent instructions.

## Install

```sh
npx skills add jny986/ai-setup --skill writing
```

## Usage

```text
/writing [sub-skill] [task]
```

- `/writing fragments`: explore an idea and collect raw material.
- `/writing shape notes.md`: shape notes into an article paragraph by paragraph.
- `/writing beats notes.md`: choose the next narrative or argumentative move as the piece develops.
- `/writing edit draft.md`: improve the draft's argument, structure and prose.
- `/writing humanize draft.md`: remove AI writing patterns while preserving facts and voice.
- `/writing technical docs/setup.md`: write or revise technical documentation using ASD-STE100 Simplified Technical English.
- `/writing agents`: write or revise skills, AGENTS.md, CLAUDE.md or other agent instructions.
- `/writing review skills/example`: review a skill's instructions, routing and supporting documents.
- `/writing review AGENTS.md`: review project instructions and their linked documents; ask to improve them to apply corrections.

Invoke `writing` explicitly. If no sub-skill is named, it selects one from the requested task. `fragments` gathers material; `shape` and `beats` are alternative drafting approaches. Each can be used independently, and editing does not require an interview or drafting session.

Writing follows the ISO 24495-1 plain-language reference unless the user or project provides another standard. Selecting `/writing technical` requests ASD-STE100. Newly created writing for human readers gets a final `humanize` pass; agent-facing writing skips that pass.

The former standalone writing-fragments, writing-shape, writing-beats, humanizer, writing-for-agents and agents-review skills now live in this package. Install `writing` in their place. The former agents-review workflow is `/writing review` and covers all agent-facing documents. Workflows that need the agent writing guide can read `sub-skills/agents.md` directly; shared prose guidance is at `sub-skills/humanize.md`.

## Resources

| Path | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Router and workflow selection |
| [fragments](sub-skills/fragments.md) | Interview and raw material capture |
| [shape](sub-skills/shape.md) | Paragraph-by-paragraph article drafting |
| [beats](sub-skills/beats.md) | Interactive journey through candidate beats |
| [edit](sub-skills/edit.md) | Structural and prose editing |
| [humanize](sub-skills/humanize.md) | AI writing pattern review and rewrite |
| [technical](sub-skills/technical.md) | Technical documentation using ASD-STE100 rules and vocabulary |
| [ASD-STE100 rules](sub-skills/references/asd-ste100-rules.md) | Agent reference for all 53 Issue 9 writing rules, exceptions and word counts |
| [ISO 24495-1 plain language](sub-skills/references/iso-24495-plain-language.md) | Reader-centered principles and available guidelines from the 2023 preview, with coverage limits |
| [agents](sub-skills/agents.md) | Writing instructions that agents consume |
| [review](sub-skills/review.md) | Review and improve agent-facing documents and skills |
| [Skill mechanics](sub-skills/references/skill-mechanics.md) | Frontmatter, invocation and router guidance |
| [agents/openai.yaml](agents/openai.yaml) | Display metadata and explicit invocation policy |
