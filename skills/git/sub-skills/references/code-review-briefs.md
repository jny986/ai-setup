---
metadata:
  version: "1.0.0"
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: code-review, retro
---

# Code-review reviewer briefs

## Shared dispatch contract

Use one installed `review` instance per applicable axis. Each receives:

- **Scope:** resolved base/head SHAs, captured diff command, changed-file and commit lists, and intended pending/untracked-file scope. Surrounding code supplies context; findings concern the captured change set.
- **Axis context:** its brief below, relevant source text or exact paths, applicable prior findings, and available shared-check results. Inspect needed code directly; reuse supplied discovery and fetched history.
- **Boundary:** inspect and report only. The coordinator owns questions, fixes, commits and publication. Use an approved browser for inspection and place evidence outside reviewed files. Return blocking questions to the coordinator; do not invoke the whole `git code-review` workflow or redispatch its axes.
- **Output:** axis, findings with severity, precise file/line evidence, impact and remedy; files covered and exclusions; limitations and unresolved questions. Keep Notes separate. An incomplete or failed review is not a clean result.

## Reviewer prompts

**Code review (Standards) prompt** should include:

- The standards-source files and automated checks identified by the coordinator, **plus the smell baseline below** pasted in full.
- The brief: "Report, per file/hunk where relevant, (a) every place the diff violates a documented standard: cite the standard (file + the rule); and (b) any baseline smell you spot: name it and quote the hunk. Distinguish hard violations from judgement calls: documented-standard breaches can be hard, but baseline smells are always judgement calls, and a documented repo standard overrides the baseline. Skip anything the listed automated checks enforce. Tag each hard breach that is a fixed syntactic pattern, banned API, import shape or file-location rule as mechanical (a lint rule or hook could catch it); leave judgement calls untagged. After the findings, add a separate Notes list of documented standards you found vague, contradictory or stale while applying them, and say if no CODING_STANDARDS.md exists; Notes are not findings. Under 400 words."

**Spec review prompt** should include:

- The path or fetched contents of the spec.
- The brief: "Report: (a) requirements the spec asked for that are missing or partial; (b) behaviour in the diff that wasn't asked for (scope creep); (c) requirements that look implemented but where the implementation looks wrong. Quote the spec line for each finding. Under 400 words."

**UI/UX review prompt**, dispatched only when the diff changes user-facing UI (templates, components, styles, copy, front-end assets), should include:

- The spec source from step 2 (its user task and acceptance criteria), plus `PRODUCT.md`, `DESIGN.md` and the brand kit when they exist.
- The instruction to read the **Review lenses** table in `design audit` and treat each lens as a checklist of what to look for. Apply the lenses the diff touches; skip the rest.
- When the coordinator's browser pre-flight passed: the URL, the browser tool and the states to exercise from the spec's acceptance criteria. Brief it to use its own browser session, stay on local or staging, use test data and read-only actions, and take a snapshot after each navigation. It captures desktop and narrow widths, walks the primary flow, does a keyboard-only pass, reads console errors, and cites the screenshot or element per finding.
- The brief: "Review the changed UI against the design audit lenses. Walk the affected user task step by step and name the step that fails or slows the user. Judge from the diff and source, and confirm in the browser when one is provided. Under Limits, list what you could not verify and separate what you verified in the browser from what you inferred from source. Report each finding as `[P0-P3] problem — file:line or state; evidence; user impact; specific fix`, using the design audit priorities. Report supported defects only, and say when the diff has no UI/UX issues. Skip anything the listed automated checks enforce. Under 400 words."

**Security review prompt** must include:

- Account for every changed file, explaining exclusions. Keep the same fixed point across re-reviews.
- The instruction: "Read the installed `security` router and its `sub-skills/review-code.md`, then perform the full applicable analysis: load every matching guide, trace suspect patterns through surrounding code to attacker-controlled sources, classify findings and needs-verification items, and produce the workflow's security report. Prior reports and checks of earlier fixes are context, not a substitute for reviewing the current complete diff."
- The report-only boundary: "Report confirmed vulnerabilities, needs-verification items and suggested remedies to the coordinator. Keep them open; do not apply fixes, commit, push or publish. Return questions requiring a user decision. The coordinator handles the fix/review loop."
- The required coverage record: resolved base/head SHAs, diff command, reviewed pending changes and untracked files, changed files covered, applied guides, exclusions and limitations. Report missing dependencies or incomplete analysis explicitly; distinguish them from a completed clean review. Preserve the security workflow's severity and evidence requirements without truncating the coverage record to fit the other axes' word limits.

## Standards smell baseline

Apply these Fowler code smells (_Refactoring_, ch.3) even when the repo documents no standards:

- **The repo overrides.** A documented repo standard always wins; where it endorses something the baseline would flag, suppress the smell.
- **Always a judgement call.** Each smell is a labelled heuristic ("possible Feature Envy"), never a hard violation. Like any standard here, skip anything tooling already enforces.

Each smell reads *what it is* → *how to fix*; match it against the diff:

- **Mysterious Name**: a function, variable, or type whose name doesn't reveal what it does or holds. → rename it; if no honest name comes, the design's murky.
- **Duplicated Code**: the same logic shape appears in more than one hunk or file in the change. → extract the shared shape, call it from both.
- **Feature Envy**: a method that reaches into another object's data more than its own. → move the method onto the data it envies.
- **Data Clumps**: the same few fields or params keep travelling together (a type wanting to be born). → bundle them into one type, pass that.
- **Primitive Obsession**: a primitive or string standing in for a domain concept that deserves its own type. → give the concept its own small type.
- **Repeated Switches**: the same `switch`/`if`-cascade on the same type recurs across the change. → replace with polymorphism, or one map both sites share.
- **Shotgun Surgery**: one logical change forces scattered edits across many files in the diff. → gather what changes together into one module.
- **Divergent Change**: one file or module is edited for several unrelated reasons. → split so each module changes for one reason.
- **Speculative Generality**: abstraction, parameters, or hooks added for needs the spec doesn't have. → delete it; inline back until a real need shows.
- **Message Chains**: long `a.b().c().d()` navigation the caller shouldn't depend on. → hide the walk behind one method on the first object.
- **Middle Man**: a class or function that mostly just delegates onward. → cut it, call the real target direct.
- **Refused Bequest**: a subclass or implementer that ignores or overrides most of what it inherits. → drop the inheritance, use composition.

