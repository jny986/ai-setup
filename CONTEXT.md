# AI Setup

A personal collection of configuration for AI coding agents, mostly skills, adapted from upstream skill repos and published for install.

## Language

### Packaging

**Skill**:
A folder with a `SKILL.md` that an agent loads for a particular kind of task, invoked by the user or matched by its description.
_Avoid_: Plugin, command, prompt

**Router skill**:
A skill that picks among a group of related sub-skills so the user needs one entry point instead of many names.
_Avoid_: Meta-skill, umbrella skill, dispatcher

**Sub-skill**:
A member of a router skill's group. It is not itself a skill and is run through its router.
_Avoid_: Guide, child skill

**Reference-only tree**:
A set of sub-skills with no router skill, reached by hand-off from sub-skills elsewhere.
_Avoid_: Hidden skill, library

**Hand-off (between sub-skills)**:
A sub-skill naming another sub-skill, in the same or a different tree, as the next step.
_Avoid_: Link, redirect

**Name table**:
The index mapping each sub-skill's final name to its location, source and old aliases.
_Avoid_: Registry, manifest

**Alias**:
An old name for a sub-skill that still resolves to its current name.
_Avoid_: Redirect, legacy name

**Mod**:
A change to the agent's own interface or behaviour, such as a pane, status line, slash command or hook.
_Avoid_: Plugin, extension

### Provenance

**Upstream**:
An external skill repo this setup draws from, kept for reference and diffing.
_Avoid_: Vendor, source repo

**Adapted skill**:
A skill derived from an upstream skill, with its source recorded.
_Avoid_: Fork, copy

**Source tracking**:
The record on an adapted skill of which upstream repo, version and skill it came from.
_Avoid_: Attribution, credit

### Workflow

**Phase**:
A chunk of work inside a session, such as grilling, implementing or QA. It ends when you think "ok, we're done with that".
_Avoid_: Stage, step

**Phase boundary**:
The gap between two phases, the only place to decide whether to continue, clear, hand off, delegate or compact.
_Avoid_: Checkpoint, break

**Handoff**:
A document, or a fresh background agent, that carries a conversation's work to another session.
_Avoid_: Summary, transfer

**Grilling**:
A relentless interview that stress-tests a plan or design one question at a time.
_Avoid_: Brainstorm, interview

**Spec**:
A written statement of what to build, published to the issue tracker.
_Avoid_: PRD, requirements doc

**Ticket**:
One tracer-bullet slice of work, declaring the tickets that block it.
_Avoid_: Task, story

**Tracer bullet**:
A thin vertical slice that cuts through every layer and can land on its own.
_Avoid_: Horizontal slice, layer

**Wide refactor**:
One mechanical change whose blast radius spans the codebase, sequenced as expand, migrate, contract rather than sliced vertically.
_Avoid_: Big-bang change

**Agent brief**:
The structured issue comment that is the authoritative contract for an agent picking up a `ready-for-agent` issue.
_Avoid_: Ticket description, prompt

**AFK agent**:
An agent working unattended, without a human in the loop.
_Avoid_: Background bot

**Triage role**:
One of the five canonical states an issue moves through, each mapped to a label in the tracker.
_Avoid_: Status, priority

### Domain model

**Glossary**:
The `CONTEXT.md` list of the project's terms, each with the words to avoid.
_Avoid_: Dictionary, wiki

**ADR (architecture decision record)**:
A short record of a hard-to-reverse, surprising, trade-off-driven decision.
_Avoid_: Design doc, decision log

### Learning

**Teaching workspace**:
A directory holding a learner's mission, resources, lessons and learning records across sessions.
_Avoid_: Course, classroom

**Mission**:
The reason a learner cares about a topic, used to ground all teaching.
_Avoid_: Goal, syllabus

**Lesson**:
One self-contained HTML output teaching one tightly scoped thing tied to the mission.
_Avoid_: Tutorial, chapter

**Learning record**:
A numbered record of a non-obvious lesson learned, used to place the learner's next step.
_Avoid_: Notes, progress log
