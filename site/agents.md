---
title: Delegate a focused exploration.
description: The agent definitions shipped with this setup, grouped by logical agent with their supported client formats.
section: agents
---

## Set up Explore

Explore is a read-only search agent. Choose the format for your client and review its model and tools before use.

- **Claude Code:** copy the contents of `agents/explore/agent.md` to `.claude/agents/explore.md` in a project, or `~/.claude/agents/explore.md` for personal use. Preserve its YAML frontmatter; adjust the model and permitted tools for your environment.
- **Codex:** copy `agents/explore/explore.toml` to `.codex/agents/explore.toml` in a project, or `~/.codex/agents/explore.toml` for personal use. Use a model available to your account and review the reasoning setting. The file includes its own name, description and developer instructions.

Ask your agent to delegate a repository search to Explore and specify the breadth: “medium” or “very thorough.” Its instructions require read-only exploration and a short answer with file references. The definitions below are the shipped content; client support and account model availability may vary.
