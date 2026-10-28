# AGENTS.md

## Shell commands

- Run one command per call. Chains (`&&`, `;`, `|`) can be rejected as a whole.
- If a chained command is rejected, rerun its parts separately before telling the user.

## Plan Mode

- Make the plan extremely concise. Sacrifice grammar for the sake of concision.
- At the end of each plan, give me a list of unresolved questions to answer, if any.
