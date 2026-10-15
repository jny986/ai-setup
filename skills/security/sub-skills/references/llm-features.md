---
metadata:
  version: "1.0.0"
  based_on_repo: addyosmani/agent-skills
  based_on_version: 0.6.13(aeac41d)
  based_on_skill: security-and-hardening
---

# AI / LLM Features

Calling an LLM — chatbots, summarizers, agents, RAG — adds a new attack surface; map it to the [OWASP Top 10 for LLM Applications (2025)](https://genai.owasp.org/llm-top-10/):

- **Model output is untrusted input** (LLM05). Never into `eval`, SQL, a shell, `innerHTML`, or a file path; parse defensively, validate against a schema, then encode.
- **Prompts can be hijacked** (LLM01). Untrusted text in the context — a user message, a fetched page, a PDF — can carry instructions. The system prompt is not a security boundary; enforce permissions in code.
- **Keep secrets, other tenants' data, and the full system prompt out of the context window** (LLM02, LLM07); scope tool permissions, validate every tool argument, and confirm destructive actions (LLM06); cap tokens, request rate, and recursion depth (LLM10); partition RAG embeddings per tenant and validate documents before indexing (LLM08).

Pattern: [LLM output handling](hardening-patterns.md#llm-output-handling).
