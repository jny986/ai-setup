---
metadata:
  version: "1.0.0"
  based_on_repo: kostja94/bricks
  based_on_version: main(fa7e1e0)
  based_on_skill: chat-panel
---

# Chat Panel

## Scope

A chat panel is a bounded conversational region embedded beside another primary work surface. It provides discussion or assistance without becoming the complete product workspace.

## Context Decisions

- A document editor may use it for questions and suggested revisions.
- An analytics view may use it to explain the visible data.
- A support console may use it to draft or summarize while the record remains primary.
- A builder may place it beside files or preview, but the complete arrangement is an Agent Workspace when tools and artifacts share task state.

## Composition

The [Conversation reference](conversation.md) owns messages, composition, streaming, failure, and persistence. Add only the context bridge required by the host surface, such as current selection, visible record, or document section.

## Constraints

- Make panel scope visible so users know which artifact or record the conversation concerns.
- Preserve enough space for the primary work surface; use a drawer or separate view on narrow screens when side-by-side use becomes incoherent.
- Closing and reopening must follow an explicit persistence policy.
- Do not label a panel as an Agent Workspace when it cannot show or control tools, actions, and artifacts.

## Acceptance criteria

Selection or record changes update the panel context or expose stale context. Resize/drawer behavior, focus transfer, closing/reopening, and long conversations preserve the declared persistence policy and keep the primary surface usable.
