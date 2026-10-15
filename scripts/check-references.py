#!/usr/bin/env python3
"""Check that things skills and templates point at exist.

- Non-Markdown asset paths (`references/x.csv`, `scripts/x.sh`, ...) resolve from the file or an ancestor folder.
- `docs/agents/<file>.md` mentions resolve against this repo's docs/agents.
- Skill names (`/name`, `` `name` skill``, `skill: name`) in skills, templates and docs name a skill or marketing sub-skill that exists.
- Retired skill names appear nowhere outside frontmatter.

Slash mentions are only checked outside skills/marketing and skills/dev, where `/blog`-style URL paths are common.
Exits 1 on any failure.
"""
import re
from pathlib import Path

from skilllib import FENCE, FRONTMATTER, Report, run, skill_dirs

ASSET = re.compile(r"(?<![\w/.-])((?:\.{1,2}/)*(?:references|scripts|assets|templates)/[\w./-]+\.(?:sh|csv|ya?ml|json|html|py|txt))")
DOCS_AGENTS = re.compile(r"docs/agents/([\w-]+\.md)")
SLASH = re.compile(r"`/([a-z][a-z0-9-]+)`")
NAMED = re.compile(r"`([a-z][a-z0-9-]+)` skill\b|[Ss]kill `([a-z][a-z0-9-]+)`|^skill: *\"?([a-z][a-z0-9-]+)", re.M)
# Slash commands built into the agent, plus system paths that show up in prose.
BUILTIN = {"compact", "clear", "tmp", "help", "init", "model", "review", "config", "memory", "resume", "usr", "etc", "bin"}
# Names a skill used to have; the frontmatter `based_on_skill` still legitimately holds upstream names.
RETIRED = {"ask-matt"}


def known_names(root):
    """Skill names plus every sub-skill name (and alias) in the marketing name table."""
    names = set(skill_dirs(root))
    table = root / "skills" / "marketing" / "sub-skills" / "name-table.md"
    if table.exists():
        for line in table.read_text().splitlines():
            if line.startswith("|"):
                names |= {n for cell in line.split("|")[1:] for n in re.findall(r"`([a-z][a-z0-9-]*)`", cell)}
    return names


def body(path):
    text = path.read_text()
    return FENCE.sub("", FRONTMATTER.sub("", text, count=1))


def check(root):
    report = Report()
    root = Path(root)
    names = known_names(root)
    docs_dir = root / "docs" / "agents"
    files = sorted((root / "skills").rglob("*.md")) + sorted((root / "templates").glob("*.md")) + sorted(docs_dir.glob("*.md"))
    for md in files:
        rel = md.relative_to(root)
        text = body(md)
        in_loose_tree = len(rel.parts) > 1 and rel.parts[0] == "skills" and rel.parts[1] in ("marketing", "dev")
        for target in ASSET.findall(text):
            if re.search(r"[<>*…{}]", target):
                continue
            if not any((base / target).exists() for base in [md.parent, *md.parents]):
                report.fail(f"{rel}: missing asset {target}")
        if rel.parts[0] == "skills":
            for target in DOCS_AGENTS.findall(text):
                if not (docs_dir / target).exists():
                    report.fail(f"{rel}: docs/agents/{target} does not exist in this repo")
        if not in_loose_tree:
            for name in SLASH.findall(text):
                if name not in names and name not in BUILTIN:
                    report.fail(f"{rel}: `/{name}` is not a skill or sub-skill")
        for groups in NAMED.findall(text):
            name = next(g for g in groups if g)
            if name not in names:
                report.fail(f"{rel}: skill '{name}' does not exist")
        for old in RETIRED:
            if re.search(rf"(?<![\w-]){re.escape(old)}(?![\w-])", text):
                report.fail(f"{rel}: mentions retired skill name '{old}'")
    return report


if __name__ == "__main__":
    run(check)
