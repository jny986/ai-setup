# AGENTS.md

## Agent skills

### Issue tracker

Issues are tracked in GitHub Issues on `jny986/ai-setup` (via `gh`). See `docs/agents/issue-tracker.md`.

### Triage labels

Default canonical labels: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one root `GLOSSARY.md` plus `docs/adr/`; ignore the upstream submodules in `source-skills/`. See `docs/agents/domain.md`.

### Agent Docs

Adding or modifying a skill, its frontmatter or `based_on_*` provenance: `docs/agents/skills.md`. Building a router and its sub-skills: `docs/agents/router-skills.md`. Regenerating `skills.html` and `SKILLS.md`: `docs/agents/skills-html.md`.

## Shell commands

- Run one command per call. Chains (`&&`, `;`, `|`) can be rejected as a whole.
- If a chained command is rejected, rerun its parts separately before telling the user.

## Plan Mode

- Make the plan extremely concise. Sacrifice grammar for the sake of concision.
- At the end of each plan, give me a list of unresolved questions to answer, if any.
