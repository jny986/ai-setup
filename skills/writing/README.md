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
- `/writing agents`: write or revise skills, AGENTS.md, CLAUDE.md or other agent instructions.

Invoke `writing` explicitly. If no sub-skill is named, it selects one from the requested task. `fragments` gathers material; `shape` and `beats` are alternative drafting approaches. Each can be used independently, and editing does not require an interview or drafting session.

The former standalone writing-fragments, writing-shape, writing-beats, humanizer and writing-for-agents skills now live in this package. Install `writing` in their place. Workflows that need the agent writing guide can read `sub-skills/agents.md` directly; shared prose guidance is at `sub-skills/humanize.md`.

## Resources

| Path | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Router and workflow selection |
| [fragments](sub-skills/fragments.md) | Interview and raw material capture |
| [shape](sub-skills/shape.md) | Paragraph-by-paragraph article drafting |
| [beats](sub-skills/beats.md) | Interactive journey through candidate beats |
| [edit](sub-skills/edit.md) | Structural and prose editing |
| [humanize](sub-skills/humanize.md) | AI writing pattern review and rewrite |
| [agents](sub-skills/agents.md) | Writing instructions that agents consume |
| [Skill mechanics](sub-skills/references/skill-mechanics.md) | Frontmatter, invocation and router guidance |
| [agents/openai.yaml](agents/openai.yaml) | Display metadata and explicit invocation policy |
