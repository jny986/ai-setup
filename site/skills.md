---
title: Find the right skill for the task.
description: Browse every skill shipped in this package, its primary instructions and its router workflows.
section: skills
---

## Install and ask

Install with `npx skills add jny986/ai-setup`, then name a skill and describe your task. In clients that support slash commands, use `/skill-name <task>`. For a specific workflow, use `/git code-review <branch or commit>`, or ask the router to choose. [Shared setup instructions](./index.md#install-the-skills) cover selection and updates.

`git code-review` reviews development changes and repositories. It prefers the [Review agent](./agents.md#set-up-review) for each applicable axis and falls back to other reviewers or direct review. It reports findings without fixing code. `git pr-review` reviews a single PR, including prior feedback and selected publication.

**Automatic or explicit** means the agent may select the skill when your request fits. **Explicit request** means you must ask for it. Expand any skill for its complete primary instructions and nested sub-skill summaries. Reference documents remain linked on GitHub.
