#!/usr/bin/env python3
"""Check every skill has agents/openai.yaml with the required interface keys, and that its
`policy.allow_implicit_invocation` agrees with `disable-model-invocation` in the SKILL.md.

A skill with `disable-model-invocation: true` must set `allow_implicit_invocation: false`; any other skill must not.
Exits 1 on any failure.
"""
from pathlib import Path

from skilllib import Report, frontmatter, parse_mapping, run, skill_dirs


def check(root):
    report = Report()
    for name, folder in skill_dirs(Path(root)).items():
        path = folder / "agents" / "openai.yaml"
        rel = f"{name}/agents/openai.yaml"
        if not path.exists():
            report.fail(f"{rel}: missing")
            continue
        data = parse_mapping(path.read_text())
        interface = data.get("interface")
        if not isinstance(interface, dict):
            report.fail(f"{rel}: missing interface")
        else:
            for key in ("display_name", "short_description"):
                if not interface.get(key):
                    report.fail(f"{rel}: missing interface.{key}")
        policy = data.get("policy", {})
        implicit = policy.get("allow_implicit_invocation") if isinstance(policy, dict) else None
        if implicit not in (None, "true", "false"):
            report.fail(f"{rel}: allow_implicit_invocation must be true or false")
            continue
        user_only = (frontmatter(folder / "SKILL.md") or {}).get("disable-model-invocation") == "true"
        if user_only and implicit != "false":
            report.fail(f"{rel}: SKILL.md sets disable-model-invocation, so allow_implicit_invocation must be false")
        if not user_only and implicit == "false":
            report.fail(f"{rel}: allow_implicit_invocation is false but SKILL.md does not set disable-model-invocation")
    return report


if __name__ == "__main__":
    run(check)
