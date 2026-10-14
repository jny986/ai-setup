#!/usr/bin/env python3
"""Check every skills/**/SKILL.md has valid frontmatter and every relative Markdown link under skills/ resolves.

Exits 1 on any failure.
"""
import re
import sys
from pathlib import Path

SKILLS = Path(__file__).resolve().parent.parent / "skills"
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
LINK = re.compile(r"\]\(([^)\s]+)")
FENCE = re.compile(r"```.*?```", re.S)

errors = []

for skill in sorted(SKILLS.rglob("SKILL.md")):
    rel = skill.relative_to(SKILLS)
    m = FRONTMATTER.match(skill.read_text())
    if not m:
        errors.append(f"{rel}: missing frontmatter")
        continue
    fields = dict(re.findall(r"^([a-z-]+):\s*(.*)$", m.group(1), re.M))
    if fields.get("name", "").strip("\"'") != skill.parent.name:
        errors.append(f"{rel}: name '{fields.get('name')}' != directory '{skill.parent.name}'")
    # `description: >` block scalars count as present.
    if not re.search(r"^description:\s*\S", m.group(1), re.M):
        errors.append(f"{rel}: missing description")

links = 0
for md in sorted(SKILLS.rglob("*.md")):
    for target in LINK.findall(FENCE.sub("", md.read_text())):
        target = target.split("#")[0]
        # Only .md targets; skips URLs, anchors, example links like (url), and placeholders like <name>.md.
        if not target.endswith(".md") or "://" in target or re.search(r"[<>*…{}]", target):
            continue
        links += 1
        if not (md.parent / target).exists():
            errors.append(f"{md.relative_to(SKILLS)}: broken link {target}")

for e in errors:
    print("FAIL", e)
print(f"{len(list(SKILLS.rglob('SKILL.md')))} skills, {links} links: " + (f"{len(errors)} failure(s)" if errors else "ok"))
sys.exit(1 if errors else 0)
