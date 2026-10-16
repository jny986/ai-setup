# Conversation

## Scope

A conversation presents an ordered exchange whose later messages depend on earlier context. It owns message continuity, composition, streaming behavior, and any supported conversation persistence. It does not automatically include tool execution, files, previews, or a broader agent workspace.

## Core Model

Use stable conversation and message identifiers when persistence, retries, branching, or tool results require them. Represent message content according to the product’s message model, preserving rich parts. Agent/model runtime roles apply only when the conversation actually uses that runtime.

The conversation contract includes:

- supported roles and content parts;
- streaming and interruption behavior;
- retry, edit, regenerate, and branch semantics;
- persistence and authentication boundary;
- attachment limits and retention;
- rendering policy for Markdown, code, links, and unsafe content.

## Interaction

- Enter and multiline behavior must match the product and input method.
- During streaming, provide an explicit stop action when the runtime supports cancellation.
- Follow new output only while the user remains near the latest message; do not steal scroll position after deliberate upward navigation.
- Communicate streaming updates without flooding assistive technology.
- Empty states should help begin the real task rather than display decorative prompts unrelated to product capability.

## Security And Failure

Rendered message content is untrusted, whether written by a person or a model. Transport failure, rate limits, canceled output, and retries retain truthful delivery state. For AI-assisted conversations, model credentials and privileged tools stay behind the server boundary.

## Acceptance criteria

Multiple turns, interrupted streams, failed-response retries, long messages, and code preserve message continuity. Keyboard and screen-reader access, scroll ownership, and refresh behavior follow the contract; credentials stay out of the client bundle.
