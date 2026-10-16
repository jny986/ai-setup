#!/usr/bin/env python3
"""Build skills.html and the marketing, git, security and design sub-skill lists in SKILLS.md.

skills.html is generated from the SKILLS.md skills table plus the marketing, git, security and design router tables in their SKILL.md.
SKILLS.md gets the Version and Author cells of its skills table and the spans between its `marketing-sub-skills` and
`git-sub-skills`, `security-sub-skills` and `design-sub-skills` markers rewritten; version and author come from each file's `metadata` frontmatter. Run after adding,
moving or renaming a skill or router sub-skill, or bumping a version.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROUTER = ROOT / "skills" / "marketing" / "SKILL.md"
GIT_ROUTER = ROOT / "skills" / "git" / "SKILL.md"
SECURITY_ROUTER = ROOT / "skills" / "security" / "SKILL.md"
DESIGN_ROUTER = ROOT / "skills" / "design" / "SKILL.md"


def meta(path):
    """(version, author) from the `metadata:` frontmatter of a markdown file; "—" where absent."""
    m = re.match(r"---\n(.*?)\n---", path.read_text(), re.S)
    front = m.group(1) if m else ""
    found = []
    for key in ("version", "author"):
        v = re.search(rf"^  {key}: *\"?([^\"\n]+)\"?\s*$", front, re.M)
        found.append(v.group(1) if v else "—")
    return tuple(found)


def sub_skills():
    """(name, path, use when) for each router row that points at a marketing sub-skill file."""
    out = []
    for line in ROUTER.read_text().splitlines():
        m = re.match(r"\| `([^`]+)` \| `(sub-skills/[^`]+\.md)` \| (.*) \|$", line)
        if m:
            out.append(m.groups())
    return out


def linked_sub_skills(router):
    """Same shape as sub_skills(), for a router's `| [`name`](sub-skills/x.md) | use when |` rows."""
    out = []
    for line in router.read_text().splitlines():
        m = re.match(r"\| \[`([^`]+)`\]\((sub-skills/[^)]+\.md)\) \| (.*) \|$", line)
        if m:
            out.append(m.groups())
    return out


def situation_sub_skills(router):
    """Same shape as sub_skills(), for a router whose rows read `| situation | [`name`](sub-skills/x.md) |`."""
    out = []
    for line in router.read_text().splitlines():
        m = re.match(r"\| (.*) \| \[`([^`]+)`\]\((sub-skills/[^)]+\.md)\) \|$", line)
        if m:
            out.append((m[2], m[3], m[1]))
    return out


def tree(rows, skill="marketing"):
    root = {"dirs": {}, "sub_skills": []}
    for name, path, use in rows:
        node = root
        for part in Path(path).parts[1:-1]:
            node = node["dirs"].setdefault(part, {"dirs": {}, "sub_skills": []})
        node["sub_skills"].append((name, f"skills/{skill}/{path}", use, *meta(ROOT / "skills" / skill / path)))
    return root


def count(node):
    return len(node["sub_skills"]) + sum(count(d) for d in node["dirs"].values())


def markdown(node, depth=0):
    pad = "  " * depth
    out = []
    for name, sub in sorted(node["dirs"].items()):
        out.append(f"{pad}- **{name}** ({count(sub)})")
        out.extend(markdown(sub, depth + 1))
    out.extend(f"{pad}- [{n}]({p}) (v{v}, {a}): {u}" for n, p, u, v, a in sorted(node["sub_skills"]))
    return out


def page(node):
    out = []
    for name, sub in sorted(node["dirs"].items()):
        out.append(f'<details><summary>{html.escape(name)} <span class="count">({count(sub)})</span></summary>')
        out.extend(page(sub))
        out.append("</details>")
    if node["sub_skills"]:
        out.append("<table><thead><tr><th>Sub-skill</th><th>Version</th><th>Author</th><th>Use when</th></tr></thead><tbody>")
        out.extend(f'<tr><td><a href="{html.escape(p)}">{html.escape(n)}</a></td><td>{html.escape(v)}</td>'
                   f'<td>{html.escape(a)}</td><td>{html.escape(u)}</td></tr>' for n, p, u, v, a in sorted(node["sub_skills"]))
        out.append("</tbody></table>")
    return out


def splice(path, body, comment, marker):
    start, end = f"{marker}:start", f"{marker}:end"
    text = path.read_text()
    block = f"{comment(start)}\n{body}\n{comment(end)}"
    pattern = re.compile(re.escape(comment(start)) + r".*?" + re.escape(comment(end)), re.S)
    if not pattern.search(text):
        raise SystemExit(f"{path.name}: markers missing")
    path.write_text(pattern.sub(lambda _: block, text))


STYLE = """body { font: 15px/1.5 system-ui, sans-serif; max-width: 1100px; margin: 2rem auto; padding: 0 1rem; color: #222; }
details { border: 1px solid #ddd; border-radius: 6px; margin-bottom: .75rem; }
summary { cursor: pointer; padding: .75rem 1rem; font-weight: 600; font-size: 1.1rem; }
summary span { color: #777; font-weight: normal; }
summary a { font-size: .85rem; font-weight: normal; margin-left: .5rem; }
details details { margin: .5rem 1rem; }
details details summary { font-size: 1rem; }
table { border-collapse: collapse; width: 100%; }
th, td { text-align: left; vertical-align: top; padding: .5rem 1rem; border-top: 1px solid #eee; }
td:first-child { white-space: nowrap; font-family: ui-monospace, monospace; }
td.inv-yes, td.inv-no { white-space: nowrap; }
td.inv-yes { color: #1a7f37; }
td.inv-no { color: #b42318; }"""
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def skills():
    """(name, path, based-on links, invokable, version, author, description) per row of the SKILLS.md table.

    Rewrites each row's Version and Author cells from the skill's SKILL.md so the table cannot drift.
    """
    rows = []
    lines = (ROOT / "SKILLS.md").read_text().splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| ["):
            name_cell, based, invokable, _, _, desc = (c.strip() for c in line.strip().strip("|").split("|", 5))
            name, path = LINK.match(name_cell).groups()
            version, author = meta(ROOT / path / "SKILL.md")
            lines[i] = f"| {name_cell} | {based} | {invokable} | {version} | {author} | {desc} |"
            rows.append((name, path, LINK.findall(based), invokable, version, author, desc))
    (ROOT / "SKILLS.md").write_text("\n".join(lines) + "\n")
    return rows


def skills_page(rows, trees):
    """Skills grouped by upstream (Original first), then one section per router's sub-skill tree.

    scripts/check-indexes.py reads the skill rows and the `<span>(N)</span>` group counts, so keep both shapes.
    """
    groups = {}
    for row in rows:
        groups.setdefault(tuple(row[2]), []).append(row)
    ordered = sorted(groups.items(), key=lambda kv: (bool(kv[0]), [t for t, _ in kv[0]]))
    out = ["<!doctype html>", '<html lang="en">', "<head>", '<meta charset="utf-8">', "<title>Skills</title>",
           f"<style>\n{STYLE}\n</style>", "</head>", "<body>", "<h1>Skills</h1>"]
    for based, members in ordered:
        label = "Original" if not based else "Based on " + ", ".join(html.escape(t) for t, _ in based)
        links = "".join(f' <a href="{html.escape(u)}">{html.escape(u)}</a>' for _, u in based)
        out.append(f'<details>\n<summary>{label} <span>({len(members)})</span>{links}</summary>')
        out.append("<table><thead><tr><th>Name</th><th>Agent invokable</th><th>Version</th><th>Author</th>"
                   "<th>Description</th></tr></thead><tbody>")
        for name, path, _, invokable, version, author, desc in sorted(members):
            out.append(f'<tr><td><a href="{html.escape(path)}">{html.escape(name)}</a></td>'
                       f'<td class="inv-{invokable.lower()}">{html.escape(invokable)}</td><td>{html.escape(version)}</td>'
                       f"<td>{html.escape(author)}</td><td>{html.escape(desc)}</td></tr>")
        out += ["</tbody></table>", "</details>"]
    for name, tree_root in trees.items():
        out.append(f'<details>\n<summary>{html.escape(name.capitalize())} sub-skills <span class="count">({count(tree_root)})</span></summary>')
        out.extend(page(tree_root))
        out.append("</details>")
    out += ["</body>", "</html>", ""]
    return "\n".join(out)


root = tree(sub_skills())
git_root = tree(linked_sub_skills(GIT_ROUTER), "git")
security_root = tree(situation_sub_skills(SECURITY_ROUTER), "security")
design_root = tree(situation_sub_skills(DESIGN_ROUTER), "design")
comment = lambda m: f"<!-- {m} -->"
splice(ROOT / "SKILLS.md", "## Marketing sub-skills\n\n" + "\n".join(markdown(root)), comment, "marketing-sub-skills")
splice(ROOT / "SKILLS.md", "## Git sub-skills\n\n" + "\n".join(markdown(git_root)), comment, "git-sub-skills")
splice(ROOT / "SKILLS.md", "## Security sub-skills\n\n" + "\n".join(markdown(security_root)), comment, "security-sub-skills")
splice(ROOT / "SKILLS.md", "## Design sub-skills\n\n" + "\n".join(markdown(design_root)), comment, "design-sub-skills")
(ROOT / "skills.html").write_text(skills_page(skills(), {"marketing": root, "git": git_root, "security": security_root, "design": design_root}))
print(f"{count(root)} marketing, {count(git_root)} git, {count(security_root)} security, {count(design_root)} design sub-skills")
