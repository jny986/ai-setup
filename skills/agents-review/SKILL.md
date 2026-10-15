---
name: agents-review
description: Refactor an AGENTS.md or CLAUDE.md into a minimal root file plus linked docs, following progressive disclosure.
argument-hint: "Path to the file, defaults to AGENTS.md or CLAUDE.md in the repo root"
disable-model-invocation: true
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

Refactor the user's AGENTS.md or CLAUDE.md to follow progressive disclosure. Use the file named in the arguments, else the one in the repo root. If both exist and one is only an `@AGENTS.md` import, treat AGENTS.md as the source.

Subagents cannot ask the user questions, so they report back and you ask.

## Steps

1. **Find contradictions.** Have a subagent list instructions that conflict, including with imported files and linked docs. Ask the user which version to keep for each, then apply their answers to every later step.

2. **Identify the essentials.** Keep only what belongs in the root file:
   - One-sentence project description
   - Package manager (if not npm)
   - Non-standard build, test or typecheck commands
   - Anything relevant to every single task

3. **Group the rest.** Sort remaining instructions into logical categories (TypeScript conventions, testing patterns, API design, Git workflow). Each group becomes its own markdown file.

4. **Create the file structure.** Output:
   - A minimal root file linking to each separate file, with a one-line "read when" cue per link
   - Each separate file with its instructions
   - A suggested `docs/` layout

5. **Flag for deletion.** List instructions that are:
   - Redundant (the agent already knows this)
   - Too vague to act on
   - Obvious (like "write clean code")

Show the proposed structure and deletions before writing files. Keep the root file's imports (such as `@AGENTS.md`) working.
