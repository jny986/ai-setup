#!/usr/bin/env python3
"""Generate the docs catalogue from shipped files, without modifying those files.

Markdown stays data: the theme renders it with HTML and Vue execution disabled.
Only the website source registry is editorial; repository sources come from all
Markdown provenance under each shipped package, including reference documents.
"""
import hashlib
import importlib.util
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

from skilllib import FRONTMATTER, frontmatter, skill_dirs

ROOT = Path(__file__).resolve().parent.parent
GITHUB = "https://github.com/jny986/ai-setup/blob/main/"


def load_index(root):
    spec = importlib.util.spec_from_file_location("site_index", ROOT / "scripts/build-index.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ROOT = root
    module.ROUTER = root / "skills/marketing/SKILL.md"
    return module


def body(path):
    return FRONTMATTER.sub("", path.read_text(), count=1).lstrip("\n")


def file_fields(path, root):
    relative = path.relative_to(root).as_posix()
    return {"path": relative, "url": GITHUB + relative, "body": body(path)}


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def normalize_repository(value):
    value = value.strip().removesuffix("/").removesuffix(".git")
    value = re.sub(r"^(?:https?://github\.com/|git@github\.com:)", "", value, flags=re.I)
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", value):
        raise ValueError(f"Invalid based_on_repo: {value!r}")
    return value.lower()


def normalize_website(value):
    parts = urlsplit(value.strip())
    if parts.scheme not in ("http", "https") or not parts.netloc or parts.username or parts.password:
        raise ValueError(f"Invalid website source URL: {value!r}")
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), parts.query, parts.fragment))


def router_tree(index, name):
    path = index.ROOT / "skills" / name / "SKILL.md"
    if name == "marketing":
        rows = index.sub_skills()
    elif name in ("git", "implement", "plan"):
        rows = index.linked_sub_skills(path)
    elif name in ("security", "design"):
        rows = index.situation_sub_skills(path)
    else:
        rows = []

    def convert(node):
        return {
            "dirs": {key: convert(child) for key, child in sorted(node["dirs"].items())},
            "subSkills": [
                {"id": "subskill-" + slug(path), "name": child_name, "description": description,
                 "invocation": f"/{name} {child_name} <task>", "path": path,
                 "url": GITHUB + path, "version": version, "author": author}
                for child_name, path, description, version, author in sorted(node["sub_skills"])
            ],
        }
    return convert(index.tree(rows, name))


def sources(root, skills):
    repositories = {}
    for skill in skills:
        folder = root / Path(skill["path"]).parent
        for path in sorted(folder.rglob("*.md")):
            metadata = (frontmatter(path) or {}).get("metadata", {})
            if not isinstance(metadata, dict):
                continue
            for value in metadata.get("based_on_repo", "").split(","):
                if value.strip():
                    repositories.setdefault(normalize_repository(value), set()).add(skill["name"])
    output = [{"name": repo, "type": "repository", "url": "https://github.com/" + repo,
               "skills": sorted(names)} for repo, names in sorted(repositories.items())]
    known = {skill["name"] for skill in skills}
    websites = {}
    registry = root / "site/data/website-sources.json"
    for entry in json.loads(registry.read_text()):
        if not isinstance(entry.get("title"), str) or not entry["title"].strip():
            raise ValueError("Website source requires a descriptive title")
        names = entry.get("skills")
        if not isinstance(names, list) or not names or any(name not in known for name in names):
            raise ValueError(f"Website source {entry['title']!r} has invalid skill mappings: {names!r}")
        url = normalize_website(entry["url"])
        item = websites.setdefault(url, {"name": entry["title"], "type": "website", "url": url, "skills": set()})
        item["skills"].update(names)
    output.extend({**item, "skills": sorted(item["skills"])} for _, item in sorted(websites.items()))
    for item in output:
        item["id"] = "source-" + slug(item["name"]) + "-" + hashlib.sha256(item["url"].encode()).hexdigest()[:10]
    return output


def build(root=ROOT):
    root = Path(root)
    index = load_index(root)
    rows = {row[0]: row for row in index.skills(update=False)}
    skills = []
    for folder_name, folder in skill_dirs(root).items():
        path = folder / "SKILL.md"
        meta = frontmatter(path) or {}
        name = meta.get("name", folder_name)
        if name not in rows:
            raise ValueError(f"Skill {name!r} is missing from SKILLS.md")
        invocation = rows[name][3]
        skills.append({
            "id": "skill-" + name, "name": name, "description": meta.get("description", ""),
            "invocationLabel": "Automatic or explicit" if invocation == "Yes" else "Explicit request",
            "invocation": f"/{name} <task>", "metadata": meta.get("metadata", {}),
            "tree": router_tree(index, folder_name), **file_fields(path, root),
        })
    skills.sort(key=lambda skill: skill["name"])
    agents = []
    for folder in sorted((root / "agents").iterdir()):
        if not folder.is_dir():
            continue
        files = sorted(path for path in folder.rglob("*") if path.is_file())
        primary = next((path for path in files if path.name == "agent.md"), None)
        meta = frontmatter(primary) or {} if primary else {}
        agents.append({"id": "agent-" + slug(folder.name), "name": meta.get("name", folder.name),
                       "description": meta.get("description", ""),
                       "formats": [{"name": "Claude agent" if path.name == "agent.md" else "Codex configuration" if path.suffix == ".toml" else path.name,
                                    "language": "markdown" if path.suffix == ".md" else path.suffix.lstrip("."),
                                    **file_fields(path, root),
                                    "configuration": (FRONTMATTER.match(path.read_text()).group(0)
                                                      if FRONTMATTER.match(path.read_text()) else "")}
                                   for path in files]})
    templates = [{"id": "template-" + slug(path.relative_to(root / "templates").as_posix()),
                  "name": path.relative_to(root / "templates").as_posix(), "description": "",
                  "language": "markdown" if path.suffix == ".md" else path.suffix.lstrip("."),
                  **file_fields(path, root)}
                 for path in sorted((root / "templates").rglob("*")) if path.is_file()]
    catalogue = {"skills": skills, "agents": agents, "templates": templates, "sources": sources(root, skills)}
    for section, items in catalogue.items():
        ids = [item["id"] for item in items]
        if len(ids) != len(set(ids)):
            raise ValueError(f"Duplicate anchors in {section}")
    return catalogue


def main():
    catalogue = build()
    destination = ROOT / "site/.vitepress/catalogue.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(catalogue, ensure_ascii=False, indent=2) + "\n")
    print(", ".join(f"{len(items)} {name}" for name, items in catalogue.items()))


if __name__ == "__main__":
    main()
