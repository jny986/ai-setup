---
name: build-securely
description: Design or write a feature that accepts untrusted input, authenticates users, stores data, calls external services or an LLM, or handles personal data.
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: getsentry/skills, addyosmani/agent-skills, affaan-m/ECC
  based_on_version: main(d18b7aa), 0.6.13(aeac41d), v2.2.3-889-gb92f181b(b92f181b)
  based_on_skill: security-review, security-and-hardening, security-review
---

Build the feature with its controls in place from the start. Threat model first: controls added without one are guesses.

## Steps

1. **Map the threat.** Done when you can name each trust boundary, the assets behind it, and one abuse case per boundary.
   - Boundaries: wherever untrusted data enters: HTTP, forms, uploads, webhooks, third-party APIs, queues, **LLM output**, and local values another process wrote.
   - Assets: credentials, PII, payments, admin actions.
   - Trust follows who *wrote* a value, not which channel delivered it: another process's command line is as hostile as a form field.
   - Walk STRIDE across each boundary. The abuse case becomes your first test.

     | Threat | Ask | Typical mitigation |
     |---|---|---|
     | **S**poofing | Can someone impersonate a user or service? | Authentication, signature verification |
     | **T**ampering | Can data be altered in transit or at rest? | Integrity checks, parameterized queries, HTTPS |
     | **R**epudiation | Can an action be denied later? | Audit logging of security events |
     | **I**nformation disclosure | Can data leak? | Encryption, field allowlists, generic errors |
     | **D**enial of service | Can it be overwhelmed? | Rate limiting, input size caps, timeouts |
     | **E**levation of privilege | Can a user gain rights they shouldn't? | Authorization checks, least privilege |

2. **Pick the controls.** Every row that matches the feature applies, so apply them all. [Controls](references/controls.md) holds the rule behind each; the linked sections hold the code.

   | The feature | Controls |
   |---|---|
   | Takes input | [Schema validation](references/hardening-patterns.md#schema-validation-at-boundaries) at the boundary; [injection](references/hardening-patterns.md#injection) and [XSS](references/hardening-patterns.md#cross-site-scripting-xss) prevention |
   | Has users or sessions | [Authentication](references/hardening-patterns.md#broken-authentication); [access control](references/hardening-patterns.md#broken-access-control) on every resource, not only login |
   | Accepts uploads | [File upload safety](references/hardening-patterns.md#file-upload-safety) |
   | Fetches a user-influenced URL | [SSRF](references/hardening-patterns.md#server-side-request-forgery-ssrf) |
   | Deletes or moves derived paths | [Destructive paths](references/hardening-patterns.md#destructive-operations-on-derived-paths) |
   | Exposes an endpoint | [Rate limiting](references/hardening-patterns.md#rate-limiting); headers and CORS from [misconfiguration](references/hardening-patterns.md#security-misconfiguration); [no sensitive fields in responses](references/hardening-patterns.md#sensitive-data-exposure) |
   | Uses secrets | [Secrets management](references/hardening-patterns.md#secrets-management) |
   | Stores personal data | [Privacy](references/privacy.md): stated purpose, retention limit, working deletion path; [data classification](references/hardening-patterns.md#data-classification) |
   | Calls an LLM | [LLM features](references/llm-features.md): output is untrusted input; permissions are enforced in code; [prompt injection](references/modern-threats.md); [output handling code](references/hardening-patterns.md#llm-output-handling) |
   | Touches a Solana wallet or transaction | [Solana patterns](references/payments-solana.md) |

   For stack-specific code, read [python](references/languages/python.md) or [javascript](references/languages/javascript.md). For worked examples of each control, see [code examples](references/code-examples.md).

3. **Ask first.** Stop and get human approval before: a new auth flow or change to auth logic, a new category of sensitive data, a new external integration, a CORS change, a file-upload handler, a rate-limit change, elevated permissions.

4. **Prove it.** Done when the abuse case from step 1 has a passing test ([security tests](references/security-testing.md)) and `release-gate` passes. Check the feature against the [red flags](references/red-flags.md) before declaring it safe.

## Always

Validate at the boundary. Parameterize queries. Use the framework's output encoding. Hash passwords with bcrypt, scrypt or argon2. Use `httpOnly`, `secure`, `sameSite` cookies. Keep secrets in the environment. Return generic errors and log details server-side.

## Never

Commit secrets. Log passwords, tokens or full card numbers. Treat client-side validation as a security boundary. Disable security headers for convenience. Pass user data to `eval()` or `innerHTML`. Keep auth tokens in `localStorage`. Expose stack traces or internals to users.
