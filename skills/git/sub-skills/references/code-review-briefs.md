---
metadata:
  version: "1.0.0"
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: code-review, retro
---

# Code-review reviewer briefs

The coordinator supplies the reviewed diff command, commit list and sources from steps 1–3 of [code-review](../code-review.md). Both reviewers assess changed lines only; surrounding code supplies context.

## Reviewer prompts

**Standards sub-agent prompt** should include:

- The full diff command and commit list, with the instruction to report only on lines changed in the diff.
- The standards-source files and automated checks identified by the coordinator, **plus the smell baseline below** pasted in full.
- The brief: "Report, per file/hunk where relevant, (a) every place the diff violates a documented standard: cite the standard (file + the rule); and (b) any baseline smell you spot: name it and quote the hunk. Distinguish hard violations from judgement calls: documented-standard breaches can be hard, but baseline smells are always judgement calls, and a documented repo standard overrides the baseline. Skip anything the listed automated checks enforce. Tag each hard breach that is a fixed syntactic pattern, banned API, import shape or file-location rule as mechanical (a lint rule or hook could catch it); leave judgement calls untagged. After the findings, add a separate Notes list of documented standards you found vague, contradictory or stale while applying them, and say if no CODING_STANDARDS.md exists; Notes are not findings. Under 400 words."

**Spec sub-agent prompt** should include:

- The diff command and commit list, with the instruction to judge only what the diff changes.
- The path or fetched contents of the spec.
- The brief: "Report: (a) requirements the spec asked for that are missing or partial; (b) behaviour in the diff that wasn't asked for (scope creep); (c) requirements that look implemented but where the implementation looks wrong. Quote the spec line for each finding. Under 400 words."

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

