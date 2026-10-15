# Security

A router skill for security work, organised by situation. `SKILL.md` picks a sub-skill from the task, or from a sub-skill name you pass, and the agent follows it as if it were the skill.

## Install

```sh
npx skills add jny986/ai-setup --skill security
```

## Usage

```
/security [sub-skill] [task]
```

- `/security review-code`: audit the current changes for vulnerabilities.
- `/security build-securely`: design a feature with its controls in place.
- `/security harden-deployment`: secure Dockerfiles, CI/CD, cloud, secrets and dependencies.
- `/security release-gate`: final check before merge or deploy.

## Resources

| Path | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | The router: chooses a sub-skill and loads it. |
| [`sub-skills/review-code.md`](sub-skills/review-code.md) | Audit sub-skill: scope, load guides by code type, trace source to sink, report high-confidence findings only. |
| [`sub-skills/build-securely.md`](sub-skills/build-securely.md) | Build sub-skill: threat model, then controls chosen by feature type. |
| [`sub-skills/harden-deployment.md`](sub-skills/harden-deployment.md) | Docker, CI/CD, cloud, secrets and dependency hardening. |
| [`sub-skills/release-gate.md`](sub-skills/release-gate.md) | One pass/fail checklist before merge or deploy. |
| `sub-skills/references/` (including `languages/` and `infrastructure/`) | Per-topic, per-language and per-platform guides, hardening controls, patterns and checklist, review rules and report template, privacy, LLM, dependency and Solana guides, loaded on demand. Content adapted from [getsentry/skills](https://github.com/getsentry/skills) (Apache-2.0), [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (MIT) and [affaan-m/ECC](https://github.com/affaan-m/ECC) (MIT); each file's `based_on_*` metadata records its source. |
| [`agents/openai.yaml`](agents/openai.yaml) | Display metadata for OpenAI and Codex agents. |
