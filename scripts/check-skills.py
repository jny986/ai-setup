#!/usr/bin/env python3
"""Check every skills/**/SKILL.md and sub-skill file has valid frontmatter and every relative Markdown link under skills/ resolves.
Sub-skills are the Markdown files under skills/*/sub-skills/ outside `references/` folders, apart from name-table.md.
Files inside `references/` folders must carry `based_on_*` so they can be re-synced, unless listed in ORIGINAL_REFERENCES.
Also fails any `gh`/`git` command in skill Markdown that chains with `&&`, `;` or `|`.

Frontmatter: required and known keys, boolean flags, description length, and all-or-none `based_on_*` provenance
with aligned comma-separated lists. A description without a "use when"-style trigger only warns.
Files whose author is jny986 must have metadata.version equal to the latest git tag (1.0.0 when the repo has no tags).
Exits 1 on any failure.
"""
import re
import subprocess
from pathlib import Path

from skilllib import FENCE, FRONTMATTER, Report, parse_mapping, run

LINK = re.compile(r"\]\(([^)\s]+)")
TOP_KEYS = {"name", "description", "license", "metadata", "disable-model-invocation", "argument-hint"}
META_KEYS = {"version", "author", "author-url", "based_on_repo", "based_on_version", "based_on_skill", "based_on_url"}
BASED_ON = ("based_on_repo", "based_on_version", "based_on_skill")
SUB_TOP_KEYS = TOP_KEYS - {"disable-model-invocation"}
VERSION = re.compile(r"^v?\d+(\.\d+)*(\([0-9a-f]{7,40}\))?$")
# Sub-skills may name a branch or a `git describe` ref, and always pin the commit.
SUB_VERSION = re.compile(r"^[\w.-]+\([0-9a-f]{7,40}\)$")
OWN_AUTHOR = "jny986"  # files by this author must carry the latest git tag as metadata.version
DEFAULT_VERSION = "1.0.0"  # expected version while the repo has no tags
NO_FRONTMATTER ={"name-table.md"}  # index files in a sub-skills folder, not sub-skills
# References written here with no upstream, so with no `based_on_*`; paths relative to skills/.
ORIGINAL_REFERENCES = {"git/sub-skills/references/gh-review.md"}
URL_VIEWED = re.compile(r"^https://\S+ \(\d{4}-\d{2}-\d{2}\)$")  # page and the date it was viewed
REPO = re.compile(r"^[\w.-]+/[\w.-]+$")
MAX_DESCRIPTION = 1024  # agentskills.io limit
TRIGGER = re.compile(r"\b(use|invoke|trigger|when|for)\b", re.I)
CODE_SPAN = re.compile(r"```.*?```|`[^`\n]+`", re.S)
QUOTED = re.compile(r"\"[^\"]*\"|'[^']*'")  # jq filters and message bodies may hold `|` or `;`
CHAIN = re.compile(r"&&|\|\||;|\|")


def check_frontmatter(skill, rel, report, sub=False):
    """Check a SKILL.md, or with `sub` a sub-skill file, which needs no license or author and is never model-invoked."""
    m = FRONTMATTER.match(skill.read_text())
    if not m:
        report.fail(f"{rel}: missing frontmatter")
        return
    fm = parse_mapping(m.group(1))
    if not fm.get("name"):
        report.fail(f"{rel}: missing name")
    # A sub-skill's name may differ from its file name: the marketing name table aliases the old flat names.
    elif not sub and fm["name"] != skill.parent.name:
        report.fail(f"{rel}: name '{fm['name']}' != directory '{skill.parent.name}'")
    desc = fm.get("description", "")
    if not isinstance(desc, str) or not desc.strip():
        report.fail(f"{rel}: missing description")
    else:
        if len(desc) > MAX_DESCRIPTION:
            report.fail(f"{rel}: description is {len(desc)} chars, max {MAX_DESCRIPTION}")
        # User-only skills are never matched by description, so they need no trigger. Routers match sub-skills.
        if not sub and fm.get("disable-model-invocation") != "true" and not TRIGGER.search(desc):
            report.warn(f"{rel}: description has no trigger phrase (use/when/for)")
    for key in sorted(set(fm) - (SUB_TOP_KEYS if sub else TOP_KEYS)):
        report.fail(f"{rel}: unknown key '{key}'")
    if not sub and not fm.get("license"):
        report.fail(f"{rel}: missing license")
    if fm.get("disable-model-invocation", "true") not in ("true", "false"):
        report.fail(f"{rel}: disable-model-invocation must be true or false")
    meta = fm.get("metadata")
    if not isinstance(meta, dict):
        meta = {}
    # A sub-skill inherits its router's author.
    if not sub and not meta.get("author"):
        report.fail(f"{rel}: missing metadata.author")
        return
    check_provenance(meta, rel, report, sub)


def check_provenance(meta, rel, report, sub):
    """Check metadata keys and `based_on_*`; return True when all three `based_on_*` keys are present."""
    for key in sorted(set(meta) - META_KEYS):
        report.fail(f"{rel}: unknown metadata key '{key}'")
    for url in (u.strip() for u in meta.get("based_on_url", "").split(",") if u.strip()):
        if not URL_VIEWED.match(url):
            report.fail(f"{rel}: based_on_url '{url}' is not 'https://... (YYYY-MM-DD)'")
    present = [k for k in BASED_ON if meta.get(k)]
    if present and len(present) != len(BASED_ON):
        report.fail(f"{rel}: based_on_* keys must be all present or all absent, found {present}")
    if len(present) == len(BASED_ON):
        parts = {k: [p.strip() for p in meta[k].split(",")] for k in BASED_ON}
        # One version per repo; based_on_skill may name several skills from one repo, but at least one per repo.
        if len(parts["based_on_repo"]) != len(parts["based_on_version"]) or len(parts["based_on_skill"]) < len(parts["based_on_repo"]):
            report.fail(f"{rel}: based_on_repo and based_on_version must align, with at least one based_on_skill per repo")
        for repo in parts["based_on_repo"]:
            if not REPO.match(repo):
                report.fail(f"{rel}: based_on_repo '{repo}' is not owner/name")
        for version in parts["based_on_version"]:
            if not (SUB_VERSION if sub else VERSION).match(version):
                report.fail(f"{rel}: based_on_version '{version}' is not {'<ref>(hash)' if sub else 'vX.Y.Z(hash)'}")
    return len(present) == len(BASED_ON)


def check_reference(ref, rel, report):
    """A reference must record its upstream in `based_on_*` so it can be re-synced, unless it is listed as original."""
    m = FRONTMATTER.match(ref.read_text())
    fm = parse_mapping(m.group(1)) if m else {}
    meta = fm.get("metadata") if isinstance(fm.get("metadata"), dict) else {}
    for key in sorted(set(fm) - SUB_TOP_KEYS):
        report.fail(f"{rel}: unknown key '{key}'")
    if check_provenance(meta, rel, report, sub=True):
        if rel.as_posix() in ORIGINAL_REFERENCES:
            report.fail(f"{rel}: listed in ORIGINAL_REFERENCES but has based_on_*, remove it from the list")
    elif rel.as_posix() not in ORIGINAL_REFERENCES and not any(k in meta for k in BASED_ON):
        report.fail(f"{rel}: missing based_on_* metadata (add it, or list the file in ORIGINAL_REFERENCES if it has no upstream)")


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


def latest_tag(root):
    """Latest version tag on the repo, or DEFAULT_VERSION when there are no tags or git is unavailable."""
    try:
        out = subprocess.run(["git", "-C", str(root), "tag", "--list", "--sort=-v:refname"], capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return DEFAULT_VERSION
    tags = out.split()
    return tags[0] if tags else DEFAULT_VERSION


def check_versions(root, skills, report):
    """Files authored by OWN_AUTHOR must carry the repo's latest git tag as metadata.version; a sub-skill or reference inherits its router's author."""
    tag = latest_tag(root)
    for md in sorted(skills.rglob("*.md")):
        rel = md.relative_to(skills)
        m = FRONTMATTER.match(md.read_text())
        meta = parse_mapping(m.group(1)).get("metadata") if m else None
        if not isinstance(meta, dict) or "version" not in meta:
            continue
        author = meta.get("author")
        if not author and len(rel.parts) > 1:
            router = skills / rel.parts[0] / "SKILL.md"
            rm = FRONTMATTER.match(router.read_text()) if router.exists() else None
            rmeta = parse_mapping(rm.group(1)).get("metadata") if rm else None
            author = rmeta.get("author") if isinstance(rmeta, dict) else None
        if author == OWN_AUTHOR and meta["version"].lstrip("v") != tag.lstrip("v"):
            report.fail(f"{rel}: metadata.version '{meta['version']}' != latest git tag '{tag}' (author {OWN_AUTHOR})")


def check(root):
    report = Report()
    skills = Path(root) / "skills"
    check_versions(Path(root), skills, report)
    for skill in sorted(skills.rglob("SKILL.md")):
        check_frontmatter(skill, skill.relative_to(skills), report)
    for sub in sorted(skills.glob("*/sub-skills/**/*.md")):
        rel = sub.relative_to(skills)
        if "references" in rel.parts:
            check_reference(sub, rel, report)
        elif sub.name not in NO_FRONTMATTER:
            check_frontmatter(sub, rel, report, sub=True)
    check_links(skills, report)
    check_chains(skills, report)
    return report


if __name__ == "__main__":
    run(check)
