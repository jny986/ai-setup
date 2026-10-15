#!/usr/bin/env python3
"""Build skills.html and the marketing and git guide lists in SKILLS.md.

skills.html is generated from the SKILLS.md skills table plus the marketing and git router tables in their SKILL.md.
SKILLS.md gets the Version and Author cells of its skills table and the spans between its `marketing-references` and
`git-references` markers rewritten; version and author come from each file's `metadata` frontmatter. Run after adding,
moving or renaming a skill or router guide, or bumping a version.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROUTER = ROOT / "skills" / "marketing" / "SKILL.md"
GIT_ROUTER = ROOT / "skills" / "git" / "SKILL.md"


def meta(path):
    """(version, author) from the `metadata:` frontmatter of a markdown file; "—" where absent."""
    m = re.match(r"---\n(.*?)\n---", path.read_text(), re.S)
    front = m.group(1) if m else ""
    found = []
    for key in ("version", "author"):
        v = re.search(rf"^  {key}: *\"?([^\"\n]+)\"?\s*$", front, re.M)
        found.append(v.group(1) if v else "—")
    return tuple(found)


def guides():
    """(name, path, use when) for each router row that points at a marketing guide file."""
    out = []
    for line in ROUTER.read_text().splitlines():
        m = re.match(r"\| `([^`]+)` \| `(references/[^`]+\.md)` \| (.*) \|$", line)
        if m:
            out.append(m.groups())
    return out


def git_guides():
    """Same shape as guides(), for the git router's `[`name`](references/x.md)` rows."""
    out = []
    for line in GIT_ROUTER.read_text().splitlines():
        m = re.match(r"\| \[`([^`]+)`\]\((references/[^)]+\.md)\) \| (.*) \|$", line)
        if m:
            out.append(m.groups())
    return out


def tree(rows, skill="marketing"):
    root = {"dirs": {}, "guides": []}
    for name, path, use in rows:
        node = root
        for part in Path(path).parts[1:-1]:
            node = node["dirs"].setdefault(part, {"dirs": {}, "guides": []})
        node["guides"].append((name, f"skills/{skill}/{path}", use, *meta(ROOT / "skills" / skill / path)))
    return root


def count(node):
    return len(node["guides"]) + sum(count(d) for d in node["dirs"].values())


def markdown(node, depth=0):
    pad = "  " * depth
    out = []
    for name, sub in sorted(node["dirs"].items()):
        out.append(f"{pad}- **{name}** ({count(sub)})")
        out.extend(markdown(sub, depth + 1))
    out.extend(f"{pad}- [{n}]({p}) (v{v}, {a}): {u}" for n, p, u, v, a in sorted(node["guides"]))
    return out


def page(node):
    out = []
    for name, sub in sorted(node["dirs"].items()):
        out.append(f"<details><summary>{html.escape(name)} <span>({count(sub)})</span></summary>")
        out.extend(page(sub))
        out.append("</details>")
    if node["guides"]:
        out.append("<table><thead><tr><th>Guide</th><th>Version</th><th>Author</th><th>Use when</th></tr></thead><tbody>")
        out.extend(f'<tr><td><a href="{html.escape(p)}">{html.escape(n)}</a></td><td>{html.escape(v)}</td>'
                   f'<td>{html.escape(a)}</td><td>{html.escape(u)}</td></tr>' for n, p, u, v, a in sorted(node["guides"]))
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
details { border: 1px solid #ddd; border-radius: 6px; margin-bottom: .5rem; }
summary { cursor: pointer; padding: .6rem 1rem; font-weight: 600; }
summary span { color: #777; font-weight: normal; }
summary .inv-yes, summary .inv-no { float: right; font-size: .85rem; font-weight: normal; }
summary .inv-yes { color: #1a7f37; }
summary .inv-no { color: #b42318; }
details > p, details > ul { margin: .25rem 1rem .75rem; }
details details { margin: .5rem 1rem; }
table { border-collapse: collapse; width: calc(100% - 2rem); margin: 0 1rem .75rem; }
th, td { text-align: left; vertical-align: top; padding: .5rem 1rem; border-top: 1px solid #eee; }
td:first-child { white-space: nowrap; font-family: ui-monospace, monospace; }"""
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
    out = ["<!doctype html>", '<html lang="en">', "<head>", '<meta charset="utf-8">', "<title>Skills</title>",
           f"<style>\n{STYLE}\n</style>", "</head>", "<body>", "<h1>Skills</h1>"]
    for name, path, based, invokable, version, author, desc in rows:
        out.append(f'<details><summary><a href="{html.escape(path)}">{html.escape(name)}</a>'
                   f'<span class="inv-{invokable.lower()}">Agent invokable: {html.escape(invokable)}</span></summary>')
        out.append(f"<p>{html.escape(desc)}</p>")
        out.append(f"<p>Version: {html.escape(version)} · Author: {html.escape(author)}</p>")
        if based:
            links = ", ".join(f'<a href="{html.escape(u)}">{html.escape(t)}</a>' for t, u in based)
            out.append(f"<p>Based on: {links}</p>")
        else:
            out.append("<p>Original</p>")
        if name in trees:
            out.extend(page(trees[name]))
        out.append("</details>")
    out += ["</body>", "</html>", ""]
    return "\n".join(out)


root = tree(guides())
git_root = tree(git_guides(), "git")
comment = lambda m: f"<!-- {m} -->"
splice(ROOT / "SKILLS.md", "## Marketing references\n\n" + "\n".join(markdown(root)), comment, "marketing-references")
splice(ROOT / "SKILLS.md", "## Git references\n\n" + "\n".join(markdown(git_root)), comment, "git-references")
(ROOT / "skills.html").write_text(skills_page(skills(), {"marketing": root, "git": git_root}))
print(f"{count(root)} marketing guides, {count(git_root)} git guides")
