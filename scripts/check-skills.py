#!/usr/bin/env python3
"""Check every skills/**/SKILL.md has valid frontmatter and every relative Markdown link under skills/ resolves.
Also fails any `gh`/`git` command in skill Markdown that chains with `&&`, `;` or `|`.

Frontmatter: required and known keys, boolean flags, description length, and all-or-none `based_on_*` provenance
with aligned comma-separated lists. A description without a "use when"-style trigger only warns.
Exits 1 on any failure.
"""
import re
from pathlib import Path

from skilllib import FENCE, FRONTMATTER, Report, parse_mapping, run

LINK = re.compile(r"\]\(([^)\s]+)")
TOP_KEYS = {"name", "description", "license", "metadata", "disable-model-invocation", "argument-hint"}
META_KEYS = {"version", "author", "author-url", "based_on_repo", "based_on_version", "based_on_skill"}
BASED_ON = ("based_on_repo", "based_on_version", "based_on_skill")
VERSION = re.compile(r"^v?\d+(\.\d+)*(\([0-9a-f]{7,40}\))?$")
REPO = re.compile(r"^[\w.-]+/[\w.-]+$")
MAX_DESCRIPTION = 1024  # agentskills.io limit
TRIGGER = re.compile(r"\b(use|invoke|trigger|when|for)\b", re.I)
CODE_SPAN = re.compile(r"```.*?```|`[^`\n]+`", re.S)
QUOTED = re.compile(r"\"[^\"]*\"|'[^']*'")  # jq filters and message bodies may hold `|` or `;`
CHAIN = re.compile(r"&&|\|\||;|\|")


def check_frontmatter(skill, rel, report):
    m = FRONTMATTER.match(skill.read_text())
    if not m:
        report.fail(f"{rel}: missing frontmatter")
        return
    fm = parse_mapping(m.group(1))
    if fm.get("name") != skill.parent.name:
        report.fail(f"{rel}: name '{fm.get('name')}' != directory '{skill.parent.name}'")
    desc = fm.get("description", "")
    if not isinstance(desc, str) or not desc.strip():
        report.fail(f"{rel}: missing description")
    else:
        if len(desc) > MAX_DESCRIPTION:
            report.fail(f"{rel}: description is {len(desc)} chars, max {MAX_DESCRIPTION}")
        # User-only skills are never matched by description, so they need no trigger.
        if fm.get("disable-model-invocation") != "true" and not TRIGGER.search(desc):
            report.warn(f"{rel}: description has no trigger phrase (use/when/for)")
    for key in sorted(set(fm) - TOP_KEYS):
        report.fail(f"{rel}: unknown key '{key}'")
    if not fm.get("license"):
        report.fail(f"{rel}: missing license")
    if fm.get("disable-model-invocation", "true") not in ("true", "false"):
        report.fail(f"{rel}: disable-model-invocation must be true or false")
    meta = fm.get("metadata")
    if not isinstance(meta, dict) or not meta.get("author"):
        report.fail(f"{rel}: missing metadata.author")
        return
    for key in sorted(set(meta) - META_KEYS):
        report.fail(f"{rel}: unknown metadata key '{key}'")
    present = [k for k in BASED_ON if meta.get(k)]
    if present and len(present) != len(BASED_ON):
        report.fail(f"{rel}: based_on_* keys must be all present or all absent, found {present}")
    if len(present) == len(BASED_ON):
        parts = {k: [p.strip() for p in meta[k].split(",")] for k in BASED_ON}
        if len({len(v) for v in parts.values()}) != 1:
            report.fail(f"{rel}: based_on_* lists have different lengths")
        for repo in parts["based_on_repo"]:
            if not REPO.match(repo):
                report.fail(f"{rel}: based_on_repo '{repo}' is not owner/name")
        for version in parts["based_on_version"]:
            if not VERSION.match(version):
                report.fail(f"{rel}: based_on_version '{version}' is not vX.Y.Z(hash)")


def check_links(skills, report):
    links = 0
    for md in sorted(skills.rglob("*.md")):
        for target in LINK.findall(FENCE.sub("", md.read_text())):
            target = target.split("#")[0]
            # Only .md targets; skips URLs, anchors, example links like (url), and placeholders like <name>.md.
            if not target.endswith(".md") or "://" in target or re.search(r"[<>*…{}]", target):
                continue
            links += 1
            if not (md.parent / target).exists():
                report.fail(f"{md.relative_to(skills)}: broken link {target}")
    return links


def check_chains(skills, report):
    """Fail on a `gh`/`git` command that chains with `&&`, `;` or `|`; agents run one command per call."""
    for md in sorted(skills.rglob("*.md")):
        for span in CODE_SPAN.findall(md.read_text()):
            # A fence holds one command per line (after the info string); an inline span is one command.
            lines = span.split("\n")[1:-1] if span.startswith("```") else [span.strip("`")]
            for line in lines:
                line = line.strip()
                if line.startswith(("gh ", "git ")) and CHAIN.search(QUOTED.sub("''", line)):
                    report.fail(f"{md.relative_to(skills)}: chained command `{line}`, split into one command per call")


def check(root):
    report = Report()
    skills = Path(root) / "skills"
    for skill in sorted(skills.rglob("SKILL.md")):
        check_frontmatter(skill, skill.relative_to(skills), report)
    check_links(skills, report)
    check_chains(skills, report)
    return report


if __name__ == "__main__":
    run(check)
