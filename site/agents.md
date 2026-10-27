---
title: Delegate exploration and code review.
description: The agent definitions shipped with this setup, grouped by logical agent with their supported client formats.
section: agents
---

## Set up Explore

Explore is a read-only search agent. Choose the format for your client and review its model and tools before use.

- **Claude Code:** copy the contents of `agents/explore/agent.md` to `.claude/agents/explore.md` in a project, or `~/.claude/agents/explore.md` for personal use. Preserve its YAML frontmatter; adjust the model and permitted tools for your environment.
- **Codex:** copy `agents/explore/explore.toml` to `.codex/agents/explore.toml` in a project, or `~/.codex/agents/explore.toml` for personal use. Use a model available to your account and review the reasoning setting. The file includes its own name, description and developer instructions.

Ask your agent to delegate a repository search to Explore and specify the breadth: “medium” or “very thorough.” Its instructions require read-only exploration and a short answer with file references. The definitions below are the shipped content; client support and account model availability may vary.

## Set up Code Review

Code Review uses the installed `git` skill's `code-review` sub-skill to review standards, spec compliance, UI/UX, security and prior comments. Install the `git` skill and its required dependencies, including `security`, in the client where you use the agent. Missing dependencies are reported as incomplete coverage.

- **Claude Code:** copy `agents/code-review/agent.md` to `.claude/agents/code-review.md` in a project, or `~/.claude/agents/code-review.md` for personal use. It preloads `git` and selects `claude-opus-5-5` with `effort: high`.
- **Codex:** copy `agents/code-review/code-review.toml` to `.codex/agents/code-review.toml` in a project, or `~/.codex/agents/code-review.toml` for personal use. It selects `gpt-6.1-sol` with `model_reasoning_effort = "high"` and loads the inherited `git` skill when reviewing.

Ask: “Use the code-review agent to review this PR,” or specify a branch, repository scope or current changes. Explicit scope wins; otherwise it resolves known targets in this order: PR, branch, repository, current changes. It asks when the target or comparison is unclear. Current-change reviews include staged, unstaged and relevant untracked files; repository audits include existing issues within the established scope.

The agent reports findings with severity, file/line evidence, impact and suggested remedies. It overrides the sub-skill's fix and publication steps: it never edits files, changes the checkout or posts GitHub reviews. Tool permissions and sandbox settings still come from the client; these instructions do not create a separate read-only sandbox. See the [Claude Code subagent configuration](https://code.claude.com/docs/en/sub-agents), [Claude model configuration](https://code.claude.com/docs/en/model-config) and [Codex subagent configuration](https://learn.chatgpt.com/docs/agent-configuration/subagents) for client support and model settings.
