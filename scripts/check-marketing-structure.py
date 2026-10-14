#!/usr/bin/env python3
"""Check that the marketing router, its guides and the name table resolve.

Hand-offs to Pagina/Bricks/dev paths are not checked yet. Exits 1 on any failure.
"""
import re
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent / "skills" / "marketing"
SPAN = re.compile(r"`([^`]+)`")
LINK = re.compile(r"\]\((?:\./)?((?:references|assets)/[^)\s#]*)|`(?:\./)?((?:references|assets)/[^`\s]*)`")

errors = []


def rows(lines):
    """Code spans per cell for each table row whose first cell is a code span."""
    for line in lines:
        if line.startswith("| `"):
            yield [SPAN.findall(cell) for cell in line.strip().strip("|").split("|")]


# Router table: first span is the name, second (if any) the path; else flat.
router = {}
for line in (SKILL / "SKILL.md").read_text().splitlines():
    if line.startswith("| `") and line.count("|") != 3:
        errors.append(f"router: row has stray '|': {line[:60]}")
for cells in rows((SKILL / "SKILL.md").read_text().splitlines()):
    spans = cells[0]
    name, path = spans[0], spans[1] if len(spans) > 1 else spans[0]
    if name in router:
        errors.append(f"router: duplicate name {name}")
    router[name] = path
    if not (SKILL / path / "GUIDE.md").is_file():
        errors.append(f"router: {name} -> {path}/GUIDE.md missing")

guides = sorted(p.parent.relative_to(SKILL).as_posix() for p in SKILL.rglob("GUIDE.md"))

def superseded(g):
    """Old flat guide kept until the contract ticket, whose aliased nested guide is routed."""
    for line in (SKILL / "references" / "name-table.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.startswith("| `") and len(cells) > 3 and f"`{g}`" in cells[3]:
            return cells[1].strip("`") in router.values()
    return False


for g in sorted(set(guides) - set(router.values())):
    if "/" in g or not superseded(g):
        errors.append(f"router: guide {g}/GUIDE.md not listed")

# Name table: Marketing rows are name | path | source | aliases; Dev rows are name | path | source.
sections, current = {}, None
for line in (SKILL / "references" / "name-table.md").read_text().splitlines():
    if line.startswith("## "):
        current = sections.setdefault(line[3:].strip(), [])
    elif current is not None:
        current.append(line)

aliases, marketing_names, seen = {}, {}, {}
for section, lines in sections.items():
    names = {}
    for cells in rows(lines):
        name, path = cells[0][0], cells[1][0]
        if name in names:
            errors.append(f"name table ({section}): duplicate name {name}")
        names[name] = path
        if name in seen and seen[name] != section:
            errors.append(f"name table: {name} in both {seen[name]} and {section}")
        seen[name] = section
        for alias in cells[3] if len(cells) > 3 else []:
            if alias in aliases:
                errors.append(f"name table: alias {alias} -> {aliases[alias]} and {name}")
            aliases[alias] = name
    if section == "Marketing":
        marketing_names = names

for alias, target in aliases.items():
    if alias in marketing_names and alias != target:
        errors.append(f"name table: alias {alias} -> {target} shadows final name {alias}")
for name, path in router.items():
    if name not in marketing_names and name not in aliases:
        errors.append(f"router: {name} is neither a final name nor an alias")
    elif "/" in path and marketing_names.get(aliases.get(name, name)) != path:
        errors.append(f"router: {name} -> {path} disagrees with name table")
for g in guides:
    if "/" not in g and g not in aliases:
        errors.append(f"name table: flat guide {g} has no alias")

# Guide bodies.
for g in guides:
    text = (SKILL / g / "GUIDE.md").read_text()
    for m in LINK.finditer(text):
        target = m.group(1) or m.group(2)
        # Placeholder paths like references/<name>.md are prose, not links.
        if not re.search(r"[<>*…{}]", target) and not (SKILL / g / target).exists():
            errors.append(f"{g}/GUIDE.md: broken link {target}")
    # Migrated guides load the product marketing context, not Contextus, and drop kostja's preamble.
    if "/" in g:
        for bad in ("contextus.md", "When invoking"):
            if bad.lower() in text.lower():
                errors.append(f"{g}/GUIDE.md: contains '{bad}'")

for e in errors:
    print("FAIL", e)
print(f"{len(guides)} guides, {len(router)} router rows, {len(marketing_names)} final names, {len(aliases)} aliases: "
      + (f"{len(errors)} failure(s)" if errors else "ok"))
sys.exit(1 if errors else 0)
