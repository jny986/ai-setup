---
name: edit
description: Improve an existing draft's argument, structure, clarity and flow while preserving its meaning and the author's voice.
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

Edit the supplied draft to serve its reader. Scale the intervention to the request: a copyedit keeps the structure; a substantive edit may reorder, combine or cut passages.

For an ISO 24495-1 plain-language review, consult the [plain-language reference](references/iso-24495-plain-language.md) for the governing principles, available guidelines and preview coverage limits.

## Steps

1. **Read the whole draft.** Establish its audience, purpose, main claim and requested depth of edit from the material and conversation. Read any voice sample or style guide supplied. Ask only when a missing choice would materially change the edit.
2. **Fix the argument and structure.** Check that the opening makes a promise the piece fulfils, each section advances it, concepts arrive before the reader needs them, and conclusions follow from the evidence. Remove repetition and repair transitions. Where a claim needs evidence the draft does not contain, flag the gap or ask for material; keep invented facts, examples and citations out of the rewrite.
3. **Edit the prose.** Clarify ambiguous references, replace vague wording with supported specifics, trim filler and improve sentence flow. Preserve deliberate rhythm, humour, uncertainty and the author's stance. Keep qualifications that change a claim's meaning.
4. **Compare against the source.** Account for changed or removed claims, names, numbers, quotations and citations. Keep code, commands, paths, link targets, metadata and document structure outside the requested edit intact. Re-read the result for continuity after moving or cutting material.

## Output

For pasted text, return the edited version, with a brief note only for substantive changes or unresolved gaps. If the user requests critique or suggestions, return those without applying a rewrite.

For a named file, re-read it before writing, preserve intervening user edits, and apply the edit to the requested destination. Report the changes and any unresolved gaps briefly.

For a request specifically about AI writing patterns, follow [humanize](humanize.md). When it is used as part of this editing task, use its embedded mode and return one final version.
