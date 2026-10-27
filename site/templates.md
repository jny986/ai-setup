---
title: Start with your own conventions.
description: Complete starter files for project instructions and Claude settings, with placement and customization guidance.
section: templates
---

From a repository checkout, `./install.sh` can copy the instruction
templates to existing Claude and Codex home directories. It asks before
replacing changed files and saves backups. Claude settings are a separate,
optional whole-file copy, not a merge; review the template before applying it.

## Place and customize

Copy `templates/AGENTS.md` to the root of your project, then adapt the shell and planning conventions. `templates/CLAUDE.md` contains `@AGENTS.md`: put both files beside each other at the project root so Claude reads the shared instructions. Keep project-specific guidance in the shared file when it applies to both clients.

The settings template records a personal Claude configuration. Merge only the settings you want into `.claude/settings.json` for a project or `~/.claude/settings.json` for your account. Replace or remove all `/Users/jny986/.claude-personal/` hook commands. Check plugin installation, permissions, model selection and the `pnpx ccstatusline` dependency. The full file is shown for reference; review each choice before applying it.
