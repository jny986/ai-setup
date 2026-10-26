---
name: review
description: Review and improve documents consumed by agents, including skills, routers, references, AGENTS.md and CLAUDE.md.
argument-hint: "Document or skill path and review scope; defaults to project AGENTS.md or CLAUDE.md"
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
---

# Review agent documents

Review how an agent discovers, reads and follows the requested documents. Use [agents](agents.md) as the shared writing reference; for skills, also read [skill mechanics](references/skill-mechanics.md). Apply those principles here rather than duplicating them.

## Process

1. **Resolve scope and consumers.** Read the named documents or skill package and applicable project instructions. With no named target, use the project's AGENTS.md or CLAUDE.md; when one imports the other, follow the import to the authoritative source. Follow relevant imports, links, router entries and callers to understand the actual reading path. Review supporting documents when the target depends on them, without expanding into unrelated documentation.

   Done when the target, its intended behavior, consumers and authoritative sources are identified. Report inaccessible sources as coverage gaps.

2. **Find actionable problems.** Trace each finding to a passage and explain how it could change agent behavior. Use the shared writing reference to assess:

   - Contradictory instructions, unclear authority and duplicated policies that can drift.
   - Missing context pointers, broken links and guidance placed where its consumers will not find it.
   - Vague steps or completion criteria, unnecessary instructions and details the project already exposes cheaply.
   - Structure that obscures the workflow: misplaced reference material, unrelated branches and excessive always-loaded content.

   For AGENTS.md and CLAUDE.md, keep project-wide essentials in the root and move conditional guidance behind links with clear reading cues. Preserve working imports and established project conventions.

   For skills, check that the name and description select the intended tasks, routing reaches the right workflow, supporting resources are discoverable, and invocation policy and agent metadata agree. Check that instructions preserve the user's scope and authorization. Propose consolidation only when workflows share a useful entry point; preserve distinct triggers and explicit invocation requirements.

   Done when each finding has evidence, an expected consequence and a concrete correction. Distinguish demonstrated problems from hypotheses; prioritize behavioral problems over stylistic preferences.

3. **Report or improve within the request.** For a review-only request, present findings in severity order with file locations and proposed corrections. For a request to improve or refactor, apply the supported corrections within the authorized scope. Resolve contradictions from authoritative project instructions and settled user decisions; ask about unresolved choices before making changes that depend on them. Continue independent improvements where possible.

   Preserve useful constraints and unique information. Keep each policy in one authoritative place, update its consumers and links together, and retain provenance for adapted content. A skill review does not authorize running the workflow being reviewed.

   Done when the requested report is delivered or the requested improvements are applied, with unresolved decisions identified.

4. **Verify the reading path.** Check changed links, imports, router entries and caller references. For skills, run applicable package or repository validation and update public indexes or documentation when discovery or behavior changes. Use a realistic example when needed to assess ambiguous routing or instructions; structural checks alone do not establish behavioral correctness.

   Report what changed or was recommended, verification evidence and any remaining coverage gaps. If there are no actionable findings, say so.
