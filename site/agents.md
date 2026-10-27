---
title: Delegate exploration and reviews.
description: The agent definitions shipped with this setup, grouped by logical agent with their supported client formats.
section: agents
---

From a repository checkout, run `./install.sh` to choose installed
clients and install or update their agent definitions. Existing changed files
are replaced only with your permission and backed up. You can also copy the
definitions manually as described below.

## Set up Explore

Explore is a read-only search agent. Choose the format for your client and review its model and tools before use.

- **Claude Code:** copy the contents of `agents/explore/agent.md` to `.claude/agents/explore.md` in a project, or `~/.claude/agents/explore.md` for personal use. Preserve its YAML frontmatter; adjust the model and permitted tools for your environment.
- **Codex:** copy `agents/explore/explore.toml` to `.codex/agents/explore.toml` in a project, or `~/.codex/agents/explore.toml` for personal use. Use a model available to your account and review the reasoning setting. The file includes its own name, description and developer instructions.

Ask your agent to delegate a repository search to Explore and specify the breadth: “medium” or “very thorough.” Its instructions require read-only exploration and a short answer with file references. The definitions below are the shipped content; client support and account model availability may vary.

## Set up Review

Review follows the caller's instructions for the target, scope, criteria, workflow and output format. Supply the review brief and any required sources or skills when delegating.

- **Claude Code:** copy `agents/review/agent.md` to `.claude/agents/review.md` in a project, or `~/.claude/agents/review.md` for personal use. It selects `claude-opus-5-5` with `effort: high`.
- **Codex:** copy `agents/review/review.toml` to `.codex/agents/review.toml` in a project, or `~/.codex/agents/review.toml` for personal use. It selects `gpt-6.1-sol` with `model_reasoning_effort = "high"`.

For example: “Use the review agent to review the current changes against the acceptance criteria in this issue. Report findings by severity with file and line references.” A caller can also supply a focused brief such as checking documentation for broken setup instructions, or request a specific installed review skill. The agent asks the caller when missing instructions prevent a reliable review.

Review reports findings and suggested remedies without editing files, changing the checkout or publishing reviews. It reports missing dependencies and validation gaps. Tool permissions and sandbox settings still come from the client; these instructions do not create a separate read-only sandbox. See the [Claude Code subagent configuration](https://code.claude.com/docs/en/sub-agents), [Claude model configuration](https://code.claude.com/docs/en/model-config) and [Codex subagent configuration](https://learn.chatgpt.com/docs/agent-configuration/subagents) for client support and model settings.
