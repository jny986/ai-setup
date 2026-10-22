#!/usr/bin/env python3
"""Build skills.html and the marketing, git, security, design, implement and docs sub-skill lists in SKILLS.md.

skills.html is generated from the SKILLS.md skills table plus the marketing, git, security, design, implement and docs router tables in their SKILL.md.
SKILLS.md gets the Version and Author cells of its skills table and the spans between its `marketing-sub-skills` and
`git-sub-skills`, `security-sub-skills`, `design-sub-skills`, `implement-sub-skills` and `docs-sub-skills` markers rewritten; version and author come from each file's `metadata` frontmatter. Run after adding,
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
IMPLEMENT_ROUTER = ROOT / "skills" / "implement" / "SKILL.md"
DOCS_ROUTER = ROOT / "skills" / "docs" / "SKILL.md"


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


def page(node, skill):
    out = []
    for name, sub in sorted(node["dirs"].items()):
        out.append(f'<details><summary>{html.escape(name)} <span class="count">({count(sub)})</span></summary>')
        out.extend(page(sub, skill))
        out.append("</details>")
    if node["sub_skills"]:
        out.append('<ul class="sub-skills">')
        for name, path, use, _, _ in sorted(node["sub_skills"]):
            search = " ".join([name, use, *Path(path).parts[3:-1]])
            out.append(f'<li class="sub-skill" data-search="{html.escape(search, quote=True)}">'
                       f'<h4><a href="{html.escape(path)}">{html.escape(name)}</a></h4>'
                       f'<p>{inline(use)}</p><code>/{html.escape(skill)} {html.escape(name)} &lt;task&gt;</code></li>')
        out.append("</ul>")
    return out


def splice(path, body, comment, marker):
    start, end = f"{marker}:start", f"{marker}:end"
    text = path.read_text()
    block = f"{comment(start)}\n{body}\n{comment(end)}"
    pattern = re.compile(re.escape(comment(start)) + r".*?" + re.escape(comment(end)), re.S)
    if not pattern.search(text):
        raise SystemExit(f"{path.name}: markers missing")
    path.write_text(pattern.sub(lambda _: block, text))


STYLE = """:root { color-scheme: light; --ink: #213830; --muted: #53665e; --line: #d6ddd5; --paper: #fafbf7; --accent: #285c46; }
* { box-sizing: border-box; }
[hidden] { display: none !important; }
body { margin: 0; background: var(--paper); color: var(--ink); font: 16px/1.65 system-ui, sans-serif; }
a { color: var(--accent); text-underline-offset: .2em; }
a:hover { text-decoration-thickness: 2px; }
:focus-visible { outline: 3px solid var(--accent); outline-offset: 4px; }
.wrap { max-width: 1120px; margin: auto; padding: 0 24px; }
.topbar { display: flex; justify-content: space-between; gap: 16px; padding-block: 22px; border-bottom: 1px solid var(--line); font-size: .85rem; }
.brand { font-weight: 700; letter-spacing: .04em; }
header { padding: 56px 0 32px; max-width: 780px; }
.eyebrow { color: var(--accent); font-size: .8rem; text-transform: uppercase; letter-spacing: .12em; font-weight: 700; }
h1 { font-size: clamp(2.2rem, 6vw, 3.8rem); letter-spacing: -.045em; line-height: 1.1; margin: 12px 0 20px; }
header p { font-size: 1.1rem; color: var(--muted); }
.guide { border-left: 3px solid var(--accent); padding: 4px 24px; margin: 0 0 36px; max-width: 850px; }
.guide h2 { font-size: 1.05rem; margin: 0 0 8px; }
.guide p { margin: 8px 0; color: var(--muted); }
code { font: .85rem/1.6 ui-monospace, SFMono-Regular, Consolas, monospace; overflow-wrap: anywhere; }
.guide code, .invoke code { background: #eef2eb; padding: 5px 9px; border-radius: 4px; color: var(--ink); }
.search { padding: 24px 0; border-block: 1px solid var(--line); margin-bottom: 28px; }
label { display: block; font-weight: 650; margin-bottom: 8px; }
.search-row { display: flex; gap: 12px; }
input { flex: 1; min-width: 0; padding: 13px 16px; border: 1px solid #74857a; border-radius: 6px; font: inherit; background: white; color: var(--ink); }
input::placeholder { color: var(--muted); }
button { font: inherit; border: 1px solid #74857a; background: white; color: var(--ink); padding: 10px 18px; border-radius: 6px; cursor: pointer; }
button:hover { background: #eef2eb; }
button:active { background: #dde7dc; }
.result-count { color: var(--muted); margin: 10px 0 0; font-size: .9rem; }
.layout { display: grid; grid-template-columns: 210px minmax(0, 1fr); gap: 40px; align-items: start; }
.skill-nav { position: sticky; top: 20px; max-height: calc(100vh - 40px); overflow-y: auto; padding-bottom: 20px; }
.skill-nav p { margin: 0 0 12px; font-weight: 650; }
.skill-nav a { display: block; font-size: .82rem; padding: 4px 0; overflow-wrap: anywhere; text-decoration: none; }
.skill-nav a:hover { text-decoration: underline; }
.skill { border-bottom: 1px solid var(--line); padding: 0 0 32px; margin-bottom: 32px; scroll-margin-top: 24px; }
.skill-heading { display: flex; flex-wrap: wrap; align-items: center; gap: 10px 16px; }
h2 { font-size: 1.4rem; letter-spacing: -.025em; margin: 0; overflow-wrap: anywhere; }
.badge { font-size: .72rem; font-weight: 600; padding: 3px 9px; border: 1px solid var(--line); border-radius: 4px; color: var(--muted); }
.description { margin: 14px 0 18px; }
.invoke { display: flex; flex-wrap: wrap; align-items: baseline; gap: 8px 12px; margin: 0 0 14px; font-size: .85rem; }
.read { font-size: .85rem; }
details { border: 1px solid var(--line); border-radius: 6px; margin-top: 20px; background: white; }
summary { cursor: pointer; padding: 12px 16px; font-size: .9rem; font-weight: 650; }
.count { color: var(--muted); font-weight: 400; margin-left: 6px; }
details details { margin: 10px 16px; }
.sub-skills { list-style: none; margin: 0; padding: 0 16px; }
.sub-skill { padding: 16px 0; border-top: 1px solid var(--line); }
h3 { margin: 0; font-size: .95rem; }
h4 { margin: 0; font-size: .95rem; overflow-wrap: anywhere; }
.sub-skill p { font-size: .9rem; margin: 6px 0 10px; }
.sub-skill code { color: var(--muted); }
.empty { padding: 24px; background: #eef2eb; border-radius: 6px; }
footer { border-top: 1px solid var(--line); margin-top: 40px; padding: 24px 0 40px; color: var(--muted); font-size: .85rem; }
.skip { position: absolute; top: -100px; left: 16px; padding: 12px; background: white; }
.skip:focus { top: 12px; }
@media (max-width: 760px) { .layout { grid-template-columns: minmax(0, 1fr); } .skill-nav { display: none; } header { padding-top: 32px; } .wrap { padding-inline: 18px; } .guide { padding-left: 16px; } }
@media print { .search, .skill-nav, .skip { display: none; } .layout { display: block; } details { content-visibility: visible; } }"""

SCRIPT = """const input = document.querySelector('#skill-search');
const skills = [...document.querySelectorAll('.skill')];
const words = text => text.toLowerCase().split(/\\s+/).filter(Boolean);
function filterSkills() {
  const terms = words(input.value);
  const matches = text => terms.every(term => text.toLowerCase().includes(term));
  let visible = 0;
  for (const skill of skills) {
    const parentMatch = matches(skill.dataset.search);
    const children = [...skill.querySelectorAll('.sub-skill')];
    for (const child of children) child.hidden = !matches(skill.dataset.skill) && !matches(skill.dataset.skill + ' ' + child.dataset.search);
    skill.hidden = !parentMatch && !children.some(child => !child.hidden);
    if (!skill.hidden) visible++;
    for (const folder of [...skill.querySelectorAll('details')].reverse()) {
      folder.hidden = ![...folder.querySelectorAll('.sub-skill')].some(child => !child.hidden);
      if (terms.length) {
        if (!folder.hasAttribute('data-was-open')) folder.dataset.wasOpen = String(folder.open);
        folder.open = !folder.hidden;
      } else if (folder.hasAttribute('data-was-open')) {
        folder.open = folder.dataset.wasOpen === 'true';
        delete folder.dataset.wasOpen;
      }
    }
    document.querySelector(`.skill-nav a[href="#${skill.id}"]`).hidden = skill.hidden;
  }
  document.querySelector('#result-count').textContent = `${visible} of ${skills.length} skills${terms.length ? ' match your search' : ''}.`;
  document.querySelector('#empty').hidden = visible !== 0;
}
input.addEventListener('input', filterSkills);
document.querySelector('#clear-search').addEventListener('click', () => {
  input.value = '';
  filterSkills();
  input.focus();
});
document.querySelector('.search').hidden = false;
"""
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def inline(text):
    """Render inline code from trusted catalogue descriptions, escaping all HTML."""
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", html.escape(text))


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
    """A searchable usage guide to this package, with each router's children beneath it."""
    out = ["<!doctype html>", '<html lang="en">', "<head>", '<meta charset="utf-8">', "<title>Skills</title>",
           '<meta name="viewport" content="width=device-width, initial-scale=1">',
           '<meta name="description" content="Find the skills in ai-setup, when to use them, and how to invoke each skill and sub-skill.">',
           f"<style>\n{STYLE}\n</style>", "</head>", "<body>",
           '<a class="skip" href="#catalogue">Skip to skills</a><div class="wrap">',
           '<div class="topbar"><span class="brand">ai-setup / Skills guide</span><a href="README.md">Repository guide</a></div>',
           '<header><span class="eyebrow">The skills in this package</span><h1>Find the right skill<br>for the task.</h1>',
           '<p>Browse what each skill does, when to use it, and how to ask for it. Expand a skill to explore its more specific workflows.</p>',
           f'<p>{len(rows)} skills &nbsp; / &nbsp; {sum(count(t) for t in trees.values())} sub-skills</p></header>',
           '<section class="guide" aria-labelledby="how-to"><h2 id="how-to">How to use this guide</h2>',
           '<p>After installing the skills, name the skill in your request and describe your task. In clients that support slash commands, use '
           '<code>/skill-name &lt;task&gt;</code>. Replace <code>&lt;task&gt;</code> with what you want done.</p>',
           '<p>For a specific workflow, add its sub-skill: <code>/git code-review &lt;branch or commit&gt;</code> or '
           '<code>/design audit &lt;page or interface&gt;</code>. You can also ask the parent skill to choose a workflow.</p>',
           '<p><strong>Automatic or explicit</strong> means the agent may select the skill when your request fits. '
           '<strong>Explicit request</strong> means you must ask for it. Unsure where to start? Ask <code>/what-to-use &lt;task&gt;</code>.</p></section>',
           '<section class="search" aria-label="Filter the catalogue" hidden><label for="skill-search">Find a skill or sub-skill</label>',
           '<div class="search-row"><input id="skill-search" type="search" placeholder="Try: review, pricing, debugging…" '
           'aria-controls="catalogue" aria-describedby="result-count"><button id="clear-search" type="button">Clear</button></div>',
           f'<p class="result-count" id="result-count" role="status">{len(rows)} of {len(rows)} skills.</p></section>',
           '<div class="layout"><nav class="skill-nav" aria-label="Jump to a skill"><p>All skills</p>']
    for name, *_ in sorted(rows):
        out.append(f'<a href="#skill-{html.escape(name)}">{html.escape(name)}</a>')
    out.extend(['</nav>', f'<main id="catalogue" data-skill-count="{len(rows)}">',
                '<p id="empty" class="empty" hidden>No matching skills. Try a broader term or clear the search to browse all skills.</p>'])
    for name, path, _, invokable, _, _, desc in sorted(rows):
        label = "Automatic or explicit" if invokable == "Yes" else "Explicit request"
        out.append(f'<article class="skill" id="skill-{html.escape(name)}" data-skill="{html.escape(name)}" '
                   f'data-invokable="{invokable.lower()}" data-search="{html.escape(name + " " + desc, quote=True)}">')
        out.append(f'<div class="skill-heading"><h2>{html.escape(name)}</h2><span class="badge">{label}</span></div>')
        out.append(f'<p class="description">{inline(desc)}</p>')
        out.append(f'<p class="invoke"><strong>How to ask</strong> <code>/{html.escape(name)} &lt;task&gt;</code></p>')
        out.append(f'<a class="read" href="{html.escape(path)}/SKILL.md">Read full {html.escape(name)} instructions &rarr;</a>')
        if name in trees:
            out.append(f'<h3 class="eyebrow" style="margin-top:24px">Sub-skills</h3><details>\n<summary>Explore {html.escape(name)} workflows '
                       f'<span class="count">({count(trees[name])})</span></summary>')
            out.extend(page(trees[name], name))
            out.append('</details>')
        out.append('</article>')
    out += ['</main></div><footer>Looking for the upstream collections? '
            '<a href="source-skills/skills.html">Browse the source skills index</a>. '
            'For installation, see the <a href="README.md">repository guide</a>.</footer></div>',
            f'<script>\n{SCRIPT}\n</script>', "</body>", "</html>", ""]
    return "\n".join(out)


root = tree(sub_skills())
git_root = tree(linked_sub_skills(GIT_ROUTER), "git")
security_root = tree(situation_sub_skills(SECURITY_ROUTER), "security")
design_root = tree(situation_sub_skills(DESIGN_ROUTER), "design")
implement_root = tree(linked_sub_skills(IMPLEMENT_ROUTER), "implement")
docs_root = tree(linked_sub_skills(DOCS_ROUTER), "docs")
comment = lambda m: f"<!-- {m} -->"
splice(ROOT / "SKILLS.md", "## Marketing sub-skills\n\n" + "\n".join(markdown(root)), comment, "marketing-sub-skills")
splice(ROOT / "SKILLS.md", "## Git sub-skills\n\n" + "\n".join(markdown(git_root)), comment, "git-sub-skills")
splice(ROOT / "SKILLS.md", "## Security sub-skills\n\n" + "\n".join(markdown(security_root)), comment, "security-sub-skills")
splice(ROOT / "SKILLS.md", "## Design sub-skills\n\n" + "\n".join(markdown(design_root)), comment, "design-sub-skills")
splice(ROOT / "SKILLS.md", "## Implement sub-skills\n\n" + "\n".join(markdown(implement_root)), comment, "implement-sub-skills")
splice(ROOT / "SKILLS.md", "## Docs sub-skills\n\n" + "\n".join(markdown(docs_root)), comment, "docs-sub-skills")
(ROOT / "skills.html").write_text(skills_page(skills(), {"marketing": root, "git": git_root, "security": security_root, "design": design_root, "implement": implement_root, "docs": docs_root}))
print(f"{count(root)} marketing, {count(git_root)} git, {count(security_root)} security, {count(design_root)} design, {count(implement_root)} implement, {count(docs_root)} docs sub-skills")
