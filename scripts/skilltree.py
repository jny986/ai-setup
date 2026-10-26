"""Router sub-skill parsers shared by the site catalogue builder: read each router's SKILL.md table into a folder tree."""
import re
from pathlib import Path

from skilllib import FRONTMATTER, parse_mapping


def meta(path):
    """(version, author) from the `metadata:` frontmatter of a markdown file; "—" where absent."""
    m = FRONTMATTER.match(path.read_text())
    metadata = (parse_mapping(m.group(1)) if m else {}).get("metadata", {})
    return tuple(metadata.get(key, "—") for key in ("version", "author"))


def sub_skills(router):
    """(name, path, use when) for each marketing router row that points at a sub-skill file."""
    out = []
    for line in router.read_text().splitlines():
        m = re.match(r"\| `([^`]+)` \| `(sub-skills/[^`]+\.md)` \| (.*) \|$", line)
        if m:
            out.append(m.groups())
    return out


def linked_sub_skills(router):
    """Same shape as sub_skills(), for a router's `| [`name`](sub-skills/x.md) | use when |` rows."""
    out = []
    for line in router.read_text().splitlines():
        m = re.match(r"\| \[`([^`]+)`\]\(((?:sub-skills|references)/[^)]+\.md)\) \| (.*) \|$", line)
        if m:
            out.append(m.groups())
    return out


def situation_sub_skills(router):
    """Same shape as sub_skills(), for a router whose rows read `| situation | [`name`](sub-skills/x.md) |`."""
    out = []
    for line in router.read_text().splitlines():
        m = re.match(r"\| (.*) \| \[`([^`]+)`\]\(((?:sub-skills|references)/[^)]+\.md)\) \|$", line)
        if m:
            out.append((m[2], m[3], m[1]))
    return out


def tree(root, rows, skill):
    node_root = {"dirs": {}, "sub_skills": []}
    for name, path, use in rows:
        node = node_root
        for part in Path(path).parts[1:-1]:
            node = node["dirs"].setdefault(part, {"dirs": {}, "sub_skills": []})
        node["sub_skills"].append((name, f"skills/{skill}/{path}", use, *meta(root / "skills" / skill / path)))
    return node_root


def rows_for(root, skill):
    """Sub-skill rows for a router skill; none for skills without a router table."""
    router = root / "skills" / skill / "SKILL.md"
    if skill == "marketing":
        return sub_skills(router)
    if skill in ("git", "implement", "grill", "writing"):
        return linked_sub_skills(router)
    if skill in ("security", "design"):
        return situation_sub_skills(router)
    return []
