---
name: setup
description: "Set up a project to use jny986/ai-setup skills. Use to prepare AGENTS.md or CLAUDE.md, configure engineering workflows, migrate domain glossaries, or check project readiness."
license: MIT
metadata:
  version: "1.0.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: setup-matt-pocock-skills
---

Prepare the target project to use this collection. Resolve the project directory from the request, using the current directory when none is given. Configure the skills already available to the target agents. Resolve bundled references relative to this skill's directory.

Follow the steps below for a general setup. For a narrower request, perform only the relevant work. A readiness-only request runs the inspection and verification steps without modifying files or creating labels. Preserve established conventions and resolved choices on repeat runs. Gather missing information, draft the proposed changes, and obtain approval before applying them.

## 1. Inspect the project

Read existing AGENTS.md and CLAUDE.md files, following imports to the authoritative instructions. Inspect installed skills, `docs/agents/`, git remotes, and existing domain docs. Identify the requested agents and workflows. Read the available skills' descriptions and hand-offs to establish their configuration needs. Report missing skill dependencies for the user to handle separately.

Done when the target, requested workflows and existing configuration are identified, with unresolved choices made explicit.

## 2. Ask about the project

Summarise what inspection established, then ask focused questions for the decisions still needed to prepare the setup. Cover the requested agents and workflows, project conventions that are not recorded, issue tracker, triage vocabulary when applicable, and domain doc layout or migration conflicts.

Use the project and prior answers to avoid repeating questions. Give a recommended choice and its consequence where useful. Ask one topic at a time and wait for the answer before resolving dependent choices. Readily discoverable facts are the agent's job; preferences and unresolved decisions are the user's.

Done when each decision needed for the setup is supported by existing configuration or the user's answer. Answers establish the draft's contents; approval of file changes happens in step 5.

## 3. Draft project instructions

Prepare the following changes for review, keeping drafts in the conversation until approved.

Draft updates to the authoritative instructions found during inspection. Where CLAUDE.md imports AGENTS.md, target the shared file; preserve separate files' existing responsibilities.

If neither exists, propose AGENTS.md for shared project instructions. For a Claude-only request, propose CLAUDE.md; when both agents are requested, propose shared instructions in AGENTS.md and a CLAUDE.md import using `@AGENTS.md`.

Include only conventions an agent cannot cheaply discover: non-obvious commands or constraints and conditional pointers to maintained docs. Merge into existing sections and keep each policy in one authoritative place. Personal machine paths, hooks, plugins and permission settings need a separate request.

Done when the proposed instructions preserve existing policies and identify every file and pointer to add or change.

## 4. Draft engineering configuration

Prepare this part of the proposal when the selected skills rely on issue tracking, triage or domain documentation. Reuse existing configuration unless the user requested a change. The operations below describe the changes to draft; apply them only in step 6.

### Issue tracker

Resolve where the project tracks work. When no tracker is established, recommend GitHub for a GitHub remote, GitLab for a GitLab remote, or local markdown for a project without a remote. Ask for the unresolved choice before writing tracker configuration. For another tracker, collect the user's workflow and record it as prose.

Draft `docs/agents/issue-tracker.md` using the matching seed template for missing configuration; merge required changes into existing docs:

- [GitHub](references/issue-tracker-github.md)
- [GitLab](references/issue-tracker-gitlab.md)
- [Local markdown](references/issue-tracker-local.md)

New GitHub and GitLab configuration leaves the template's PR request-surface flag off. Preserve an existing value.

### Triage labels

When `triage` is installed, preserve its existing label mapping. If no mapping is settled, ask whether to use the defaults in the [triage label template](references/triage-labels.md); collect overrides only when needed. Draft `docs/agents/triage-labels.md` with all five canonical roles mapped.

For GitHub or GitLab, read existing labels and include only missing configured labels in the proposal for creation with the appropriate CLI. Preserve existing names and colors. If remote access is unavailable, mark label verification or creation as pending in the proposal. When triage is absent, skip new triage configuration and retain existing user-maintained mappings.

### Domain documentation

Plan the migration of existing domain glossaries:

1. Find the project's root `CONTEXT.md`, any `CONTEXT-MAP.md`, and the per-context glossaries the map identifies. Propose renaming them to `GLOSSARY.md` and `GLOSSARY-MAP.md` in their existing directories, preserving content and context boundaries. Limit the migration to the target project's domain docs; leave dependencies and upstream checkouts untouched.
2. If both old and new files exist in a directory, compare their contents and draft a merged result before proposing retirement of the old file. Preserve unique entries and ask about conflicting definitions rather than overwriting either version.
3. Include active reference updates in AGENTS.md, CLAUDE.md, domain docs, glossary maps and other project files in the proposal. Check that each proposed link or import targets the planned path; verify resolution after applying the changes. Historical records can retain the old names.

Done when the proposal lists every glossary rename, merge and active reference update. On a readiness-only request, report the required migration without making changes.

For new configuration, default to one root GLOSSARY.md plus `docs/adr/`. Offer a multi-context layout only when inspection finds genuine multi-package boundaries and the user chooses it.

Use the [domain documentation template](references/domain.md) to draft `docs/agents/domain.md` for the selected layout. GLOSSARY.md and ADRs are created lazily as terms and decisions are resolved, following [the modeling procedure](references/modeling.md); setup writes the consumer rules rather than inventing domain content.

### Instruction pointers

Draft short issue tracker, conditional triage label and domain doc pointers to merge into the authoritative instructions' `## Agent skills` section. Each pointer names what the doc supplies and when to read it. Preserve surrounding instructions and update existing entries in place.

Done when the tracker, domain rules, conditional triage mapping, migrations and instruction pointers are ready for review, with pending remote work identified.

## 5. Review and approve changes

Present a concrete proposal before changing project files:

- List every file to create, edit, rename or remove, with its purpose.
- Show the proposed contents for new files and the relevant diffs for existing files, including glossary migrations and reference updates.
- Identify any remote changes, such as missing tracker labels to create, separately from file changes.

Ask the user to approve this proposal or request revisions. Wait for explicit approval; a request to run setup or an answer to a discovery question does not approve an unseen set of changes. If the user requests revisions, update the proposal before seeking approval. Existing approval of this exact proposal in the conversation remains valid.

Done when the user has approved the concrete changes to apply. Until then, keep the target files unchanged.

## 6. Apply approved changes

Apply only the approved proposal, preserving unrelated content and existing user edits. Complete approved glossary renames and reference updates together. Perform remote changes only within the approved scope; report unavailable access as pending.

If implementation reveals an additional file change or a conflict requiring a different result, prepare the revised proposal and obtain approval for that addition before applying it.

Done when every approved change is applied or explicitly reported as blocked, with no unapproved additions.

## 7. Verify readiness

Use read-only checks for the requested workflows, or the installed workflows when no selection was given:

- Selected SKILL.md files, supporting resources and companion skills are readable through each target agent's installation.
- Each requested agent reaches its project instructions, and imports and doc pointers resolve without duplicate policy blocks.
- Existing domain glossaries have migrated to GLOSSARY.md / GLOSSARY-MAP.md, with active references updated; a readiness-only check reports any migration still needed.
- For engineering workflows, the tracker doc identifies the actual tracker and target. Its required CLI is available and authenticated where applicable; local markdown needs no remote service. Check remote labels when triage is installed, and verify that its mapping covers all five canonical roles. The domain rules describe the selected layout and are reachable from project instructions. GLOSSARY.md and ADRs may be absent.

Report each relevant area as ready, missing or unverified, with evidence and the smallest next action. Failed authentication or an unavailable service is unverified. For repairs beyond the approved proposal, return to step 5 with the proposed changes. After approved repairs, repeat the affected checks.

Done when every selected workflow has an evidenced status and each gap has a concrete next action. Report changed files, configured workflows and remaining work; claim completion only for verified areas.
