#!/usr/bin/env python3
"""Check SKILLS.md and skills.html list exactly the skills under skills/, agree with each other and with the
`disable-model-invocation` frontmatter flag, and are sorted within each group. Also checks that every submodule in
.gitmodules appears in the README structure tree.

Exits 1 on any failure.
"""
import re
from pathlib import Path

from skilllib import Report, frontmatter, run, skill_dirs

MD_ROW = re.compile(r"^\| \[([^\]]+)\]\(skills/([^)]+)\) \| (.*?) \| (Yes|No) \| .* \|$", re.M)
HTML_ROW = re.compile(r'<tr><td><a href="skills/([^"]+)">([^<]+)</a></td><td class="inv-(yes|no)">(Yes|No)</td>')
HTML_SKILL = re.compile(r'<article class="skill" id="skill-([^"]+)" data-skill="([^"]+)" data-invokable="(yes|no)"')
HTML_GROUP = re.compile(r"<details>\s*<summary>(.*?)</summary>(.*)</details>", re.S)


def html_groups(text):
    """Yield upstream summaries and bodies, keeping nested sub-skill details intact."""
    depth = 0
    start = 0
    for tag in re.finditer(r"<details>|</details>", text):
        if tag.group() == "<details>":
            if depth == 0:
                start = tag.start()
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                yield HTML_GROUP.fullmatch(text[start:tag.end()]).groups()


def sorted_runs(rows, key_of_group):
    """Yield (group, names) runs of consecutive rows sharing a group."""
    run_group, names = object(), []
    for row in rows:
        group = key_of_group(row)
        if group != run_group and names:
            yield run_group, names
            names = []
        run_group = group
        names.append(row[0])
    if names:
        yield run_group, names


def check_submodules(root, report):
    gitmodules, readme = root / ".gitmodules", root / "README.md"
    if not gitmodules.exists() or not readme.exists():
        return
    tree = readme.read_text()
    for path in re.findall(r"^\s*path = source-skills/(\S+)", gitmodules.read_text(), re.M):
        if f"{path}/" not in tree:
            report.fail(f"README.md: submodule source-skills/{path} missing from the structure tree")


def check(root):
    report = Report()
    root = Path(root)
    skills = skill_dirs(root)
    invokable = {n: (frontmatter(d / "SKILL.md") or {}).get("disable-model-invocation", "false") != "true" for n, d in skills.items()}

    md_rows = []  # (name, based-on group, invokable)
    for name, path, based_on, yes in MD_ROW.findall((root / "SKILLS.md").read_text()):
        if name != path:
            report.fail(f"SKILLS.md: link text '{name}' != path 'skills/{path}'")
        md_rows.append((name, based_on, yes == "Yes"))
    html_text = (root / "skills.html").read_text()
    html_rows = []
    for path, name, cls, label in HTML_ROW.findall(html_text):
        if (cls == "yes") != (label == "Yes"):
            report.fail(f"skills.html: {name} class and label disagree")
        html_rows.append((name, None, label == "Yes"))
    catalogue = HTML_SKILL.findall(html_text)
    for anchor, name, invokable_label in catalogue:
        if anchor != name:
            report.fail(f"skills.html: skill '{name}' has mismatched anchor '{anchor}'")
        html_rows.append((name, None, invokable_label == "yes"))
    if catalogue:
        names = [row[1] for row in catalogue]
        if names != sorted(names):
            report.fail("skills.html: catalogue skills are not sorted alphabetically")
        total = re.search(r'data-skill-count="(\d+)"', html_text)
        if not total or int(total[1]) != len(catalogue):
            report.fail("skills.html: catalogue count does not match listed skills")

    md_names, html_names = [r[0] for r in md_rows], [r[0] for r in html_rows]
    for label, names in (("SKILLS.md", md_names), ("skills.html", html_names)):
        for dup in sorted({n for n in names if names.count(n) > 1}):
            report.fail(f"{label}: {dup} listed more than once")
        for n in sorted(set(skills) - set(names)):
            report.fail(f"{label}: skill '{n}' not listed")
        for n in sorted(set(names) - set(skills)):
            report.fail(f"{label}: lists '{n}' but skills/{n}/SKILL.md does not exist")
    if set(md_names) != set(html_names):
        report.fail("SKILLS.md and skills.html list different skills")

    for label, rows in (("SKILLS.md", md_rows), ("skills.html", html_rows)):
        for name, _, listed in rows:
            if name in invokable and listed != invokable[name]:
                report.fail(f"{label}: {name} agent-invokable column disagrees with disable-model-invocation")

    for group, names in sorted_runs(md_rows, lambda r: r[1]):
        if names != sorted(names):
            report.fail(f"SKILLS.md: rows for '{group}' are not sorted alphabetically")
    for summary, body in html_groups(html_text):
        names = [m[0] for m in HTML_ROW.findall(body)]
        label = re.sub(r"<[^>]+>.*", "", summary).strip()
        if names != sorted(names):
            report.fail(f"skills.html: group '{label}' is not sorted alphabetically")
        count = re.search(r"<span>\((\d+)\)</span>", summary)
        if count and int(count.group(1)) != len(names):
            report.fail(f"skills.html: group '{label}' says {count.group(1)} but lists {len(names)}")

    check_submodules(root, report)
    return report


if __name__ == "__main__":
    run(check)
