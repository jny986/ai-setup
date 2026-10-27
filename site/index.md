---
title: A reference for your agent setup.
description: Skills, agents and templates from my personal AI coding setup. Browse their instructions, choose what fits your project, and customize the rest.
eyebrow: jny986 / ai-setup
---

## Browse the package

- [Skills](./skills.md) — what each skill does, how to invoke it, and its complete primary instructions.
- [Agents](./agents.md) — Explore and Review definitions for Claude Code and Codex, with setup guidance.
- [Templates](./templates.md) — project instructions and settings to review and customize.
- [Sources](./sources.md) — the upstream repositories and recorded website sources behind the shipped skills.

## Install the skills

### Install all skills

Install every skill in this package.

```sh
npx skills add jny986/ai-setup --skill '*'
```

### Install specific skills

Replace `tdd` and `git` with the names you want from the [Skills reference](./skills.md).

```sh
npx skills add jny986/ai-setup --skill tdd --skill git
```

### Update skills

```sh
npx skills update
```

## Set up a project

If the setup skill isn't already installed globally, install it in the target project:

```sh
npx skills add jny986/ai-setup --skill setup
```

Then run the skill in your agent from the target project:

```text
/setup
```

Setup configures project instructions and engineering workflows, asks for unresolved project details, and shows proposed file changes for approval. You can also request a read-only readiness check. See the [Skills reference](./skills.md#skill-setup) for its full instructions.

Name a skill and describe your task in plain language. Clients with slash commands also accept `/skill-name <task>`. For a router workflow, use `/git code-review <branch or commit>` or `/design audit <page or interface>`.

Agent definitions and templates use their own placement conventions; see their indexes before copying files. Browse or clone the [repository](https://github.com/jny986/ai-setup) for the original files. You do not need its upstream submodules to use the shipped skills.
