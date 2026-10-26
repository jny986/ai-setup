---
name: technical
description: Write or revise technical documentation using ASD-STE100 Simplified Technical English writing rules and controlled vocabulary.
argument-hint: "Document path or topic, audience and requested output"
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_url: "https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf (2026-10-26), https://asd-ste100.org/STE_faq.html (2026-10-26), https://asd-ste100.org/STEsoftware.html (2026-10-26)"
---

# Technical documentation

Use this workflow when the user requests ASD-STE100 Simplified Technical English (STE), explicitly selects `/writing technical`, or the project requires STE. Generic technical-writing requests retain the router's ISO plain-language default. Apply STE to the requested document, not automatically to every file or conversation. For agent-facing documentation, also follow [agents](agents.md); a structural review uses [review](review.md).

STE combines writing rules with a controlled dictionary. Clear prose alone does not establish compliance. The linked reference summarizes the writing rules; the official standard remains authoritative.

## Process

1. **Establish the document contract.** Read the request, existing documentation and relevant technical sources. Identify the audience, task, output path and required technical facts. Classify each passage as a procedure or description; a document can contain both. Reuse established terminology and ask only about gaps that affect correctness.

   Done when the reader's task and the sources for the technical content are clear.

2. **Select the standard and terminology.** Use the edition required by the project. Otherwise use Issue 9, dated 2025-01-15, the baseline for this guide. Read the [agent rules reference](references/asd-ste100-rules.md) for all 53 writing rules, terminology categories, exceptions and counting conventions. Consult the official standard for the dictionary and detailed rule explanations. Use the [official downloads page](https://asd-ste100.org/STE_downloads.html) to locate a copy if necessary.

   Use dictionary-approved words with their approved meanings and parts of speech. Use project terminology for technical nouns and technical verbs only when it meets the standard's categories. A familiar word is not necessarily approved. Keep terminology consistent; consult the glossary rather than introducing synonyms.

   Done when the edition, technical terminology and available validation sources are identified. If the standard or dictionary is unavailable, continue with the available guidance and record what remains unverified.

3. **Draft or revise.** Apply the linked rules reference, then consult the applicable sections of the standard for details and exceptions. Preserve the technical meaning, prerequisites, limits and consequences. Rewrite the sentence when a word substitution changes its meaning.

   Preserve commands, code, identifiers, API fields, paths, units, values and literal interface labels. Explain them in the surrounding prose. Do not rename a software interface or alter a command to simplify its English. Preserve normative distinctions such as required, permitted and optional behavior.

   Done when the requested document is complete and each technical statement remains supported by its sources.

4. **Verify meaning and language separately.** Compare the result with the technical sources before checking STE rules. Verify vocabulary in context, including meaning and part of speech. Use section 8 for word counts; a whitespace count is only a preliminary check. Check the applicable noun-cluster, verb, punctuation and safety rules in the selected edition.

   Use an existing STE checker when available, but review its findings against the standard. A checker cannot establish technical accuracy or guarantee compliance. Do not install or require a paid tool for this workflow.

   Report the output path, material changes, edition used and checks completed. Claim compliance only when both the applicable rules and vocabulary have been verified; otherwise identify the remaining checks. Keep this verification note outside the document unless requested.

## Documentation structure

These are workflow choices for technical documentation, not additional ASD-STE100 rules:

- For a procedure, state the goal and prerequisites. Number actions in execution order and give an observable completion result.
- For a description, introduce the concept before its details. Group related facts and explain specialized terms at first use.
- Place necessary risk information before the affected action. Preserve mandated safety wording and report conflicts for resolution.
- Keep articles and other words needed for complete, unambiguous sentences. Resolve vague references to objects, states or actors.
- Use lists and tables when they make conditions or alternatives easier to compare. Retain causal relationships when splitting sentences.

For example, revise “Following the modification of the configuration, the service should be restarted” to “After you change the configuration, restart the service.” This illustrates a direct instruction; verify its vocabulary before calling it STE-compliant.
