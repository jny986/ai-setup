#!/usr/bin/env python3
"""Check that the marketing router, its sub-skills and the name table resolve.

Strict: no flat sub-skills, router rows are final names with nested paths, every old name aliases to a final name,
and every `dev/references/...` hand-off in marketing resolves. Also checks the dev references against the name table.
Exits 1 on any failure.
"""
import re
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent / "skills" / "marketing"
SPAN = re.compile(r"`([^`]+)`")
LINK = re.compile(r"\]\((?:\./)?((?:references|assets)/[^)\s#]*)|`(?:\./)?((?:references|assets)/[^`\s]*)`")

# The 50 flat sub-skill names before the restructure; each must alias to a final name.
# ponytail: one-time migration list, drop it once upstream syncs no longer need the alias check.
OLD_NAMES = """ab-testing ad-creative ads ai-seo analytics aso attribution churn-prevention co-marketing cold-email
community-marketing competitor-profiling competitors content-strategy copy-editing copywriting cro customer-research
directory-submissions emails events free-tools image influencer-marketing launch lead-magnets marketing-council
marketing-ideas marketing-loops marketing-plan marketing-psychology offers onboarding paywalls popups pricing
product-marketing programmatic-seo prospecting public-relations referrals revops sales-enablement schema seo-audit
signup site-architecture sms social video""".split()
BANNED = ("contextus", "When invoking")  # sub-skills load the product marketing context and drop kostja's preamble
MD_LINK = re.compile(r"\]\(([^)\s#]+)")
HANDOFF = re.compile(r"dev/references/[A-Za-z0-9_./-]*[A-Za-z0-9_]")

errors = []


def check_banned(rel, text):
    for bad in BANNED:
        if bad.lower() in text.lower():
            errors.append(f"{rel}: contains '{bad}'")


def rows(lines):
    """Code spans per cell for each table row whose first cell is a code span."""
    for line in lines:
        if line.startswith("| `"):
            yield [SPAN.findall(cell) for cell in line.strip().strip("|").split("|")]


def sub_skill_file(path):
    """Router paths point straight at the sub-skill file."""
    return SKILL / path


# Router table rows: | `name` | `path` | use when |.
router = {}
for line in (SKILL / "SKILL.md").read_text().splitlines():
    if line.startswith("| `") and line.count("|") != 4:
        errors.append(f"router: row has stray '|': {line[:60]}")
for cells in rows((SKILL / "SKILL.md").read_text().splitlines()):
    if len(cells) < 2 or not cells[1]:
        errors.append(f"router: row without a path: {cells[0]}")
        continue
    name, path = cells[0][0], cells[1][0]
    if "/" not in path:
        errors.append(f"router: {name} -> {path} is not a nested path")
    if name in router:
        errors.append(f"router: duplicate name {name}")
    router[name] = path
    if not sub_skill_file(path).is_file():
        errors.append(f"router: {name} -> {sub_skill_file(path).relative_to(SKILL)} missing")

# Sub-skill files: every .md under sub-skills/<category>/ outside a nested references/ or assets/ folder.
sub_skills = sorted(
    p.relative_to(SKILL).as_posix() for p in (SKILL / "sub-skills").rglob("*.md")
    if p.name != "name-table.md" and not {"references", "assets"} & set(p.relative_to(SKILL / "sub-skills").parts[:-1])
)

# Name table: Marketing rows are name | path | source | aliases; Dev rows are name | path | source.
sections, current = {}, None
for line in (SKILL / "sub-skills" / "name-table.md").read_text().splitlines():
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

for g in sorted(set(sub_skills) - set(router.values())):
    errors.append(f"router: sub-skill {g} not listed")
for name in sorted(set(marketing_names) - set(router)):
    errors.append(f"router: final name {name} not listed")
for old in OLD_NAMES:
    if old not in aliases:
        errors.append(f"name table: old name {old} has no alias")
for d in sorted(p for p in SKILL.iterdir() if p.is_dir() and p.name != "sub-skills"):
    if (d / "references").is_dir() or (d / "assets").is_dir():
        errors.append(f"flat sub-skill folder left: {d.name}")

for alias, target in aliases.items():
    if alias in marketing_names and alias != target:
        errors.append(f"name table: alias {alias} -> {target} shadows final name {alias}")
for name, path in router.items():
    if marketing_names.get(name) != path:
        errors.append(f"router: {name} -> {path} disagrees with name table")
for g in sub_skills:
    if g.count("/") < 2:
        errors.append(f"flat sub-skill {g}")

# Sub-skill bodies.
for g in sub_skills:
    gf = sub_skill_file(g)
    text = gf.read_text()
    for m in LINK.finditer(text):
        target = m.group(1) or m.group(2)
        # Placeholder paths like references/<name>.md are prose, not links.
        if not re.search(r"[<>*…{}]", target) and not (gf.parent / target).exists():
            errors.append(f"{g}: broken link {target}")
    check_banned(g, text)

# Every relative markdown link anywhere in marketing must resolve (placeholders and URLs are prose).
for md in sorted(SKILL.rglob("*.md")):
    for target in MD_LINK.findall(md.read_text()):
        if "://" not in target and not re.search(r"[<>{}*]", target) and target.endswith(".md") \
                and not (md.parent / target).exists():
            errors.append(f"{md.relative_to(SKILL)}: broken link {target}")

# Dev sub-skills: no router yet, so the name table's Dev section is the index.
DEV = SKILL.parent / "dev"
dev_paths = {cells[1][0] for cells in rows(sections.get("Dev", []))}
dev_guides = {p.parent.relative_to(SKILL.parent).as_posix() for p in DEV.rglob("GUIDE.md")}
for p in sorted(dev_paths - dev_guides):
    errors.append(f"name table (Dev): {p}/GUIDE.md missing")
for g in sorted(dev_guides - dev_paths):
    errors.append(f"name table (Dev): guide {g}/GUIDE.md not listed")
for p in DEV.rglob("SKILL.md"):
    errors.append(f"dev: unexpected {p.relative_to(SKILL.parent)}")
for md in sorted(DEV.rglob("*.md")):
    rel, text = md.relative_to(SKILL.parent), md.read_text()
    for target in MD_LINK.findall(text):
        if "://" not in target and not (md.parent / target).exists():
            errors.append(f"{rel}: broken link {target}")
    check_banned(rel, text)

# Marketing hand-offs to dev references must resolve to a guide folder or a reference file.
handoffs = 0
for md in sorted(SKILL.rglob("*.md")):
    if md.name == "name-table.md":
        continue
    for target in HANDOFF.findall(md.read_text()):
        handoffs += 1
        path = SKILL.parent / target
        if not ((path / "GUIDE.md").is_file() or path.is_file()):
            errors.append(f"{md.relative_to(SKILL)}: hand-off {target} does not resolve")

# Prose cross-references must use final names: "<old> skill/guide/sub-skill" or a bolded "**<old>**" entry.
stale = [o for o in OLD_NAMES if o not in marketing_names]
STALE = re.compile(r"(?<![\w-])(?<!former )(?:%s)\s+(?:skill|guide|sub-skill)\b|\*\*(?:%s)\b(?:\s*/|\*\*)" % (("|".join(stale),) * 2))
for md in sorted(SKILL.rglob("*.md")):
    if md.name in ("name-table.md",) or md == SKILL / "SKILL.md":
        continue
    for m in STALE.finditer(md.read_text()):
        errors.append(f"{md.relative_to(SKILL)}: old sub-skill name in '{m.group(0)}'")

for e in errors:
    print("FAIL", e)
print(f"{len(sub_skills)} sub-skills, {len(router)} router rows, {len(marketing_names)} final names, {len(aliases)} aliases, "
      f"{len(dev_guides)} dev references, {handoffs} dev hand-offs: "
      + (f"{len(errors)} failure(s)" if errors else "ok"))
sys.exit(1 if errors else 0)
