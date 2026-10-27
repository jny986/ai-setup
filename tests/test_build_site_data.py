"""Catalogue coverage and provenance aggregation, including reference-only sources."""
import json
from pathlib import Path

import pytest

import skilltree
from conftest import load
from skilllib import FRONTMATTER, frontmatter, skill_dirs

site_data = load("build-site-data")
ROOT = Path(__file__).resolve().parent.parent


def test_catalogue_covers_shipped_items_and_preserves_bodies():
    catalogue = site_data.build(ROOT)
    skills = catalogue["skills"]
    assert [item["name"] for item in skills] == sorted(skill_dirs(ROOT))
    for skill in skills:
        path = ROOT / skill["path"]
        assert skill["body"] == FRONTMATTER.sub("", path.read_text(), count=1).lstrip("\n")
        assert skill["description"] == frontmatter(path)["description"]
        assert skill["id"] == "skill-" + skill["name"]
    assert {item["path"] for item in catalogue["templates"]} == {
        path.relative_to(ROOT).as_posix() for path in (ROOT / "templates").rglob("*") if path.is_file()
    }
    agents = {item["id"]: item for item in catalogue["agents"]}
    explore = agents["agent-explore"]
    assert explore["name"] == "Explore"
    assert {item["path"] for item in explore["formats"]} == {
        "agents/explore/agent.md", "agents/explore/explore.toml"
    }
    review = agents["agent-review"]
    assert {item["path"] for item in review["formats"]} == {
        "agents/review/agent.md", "agents/review/review.toml"
    }


def test_router_trees_match_router_tables():
    items = {item["name"]: item for item in site_data.build(ROOT)["skills"]}

    def flatten(node):
        return node["subSkills"] + [item for child in node["dirs"].values() for item in flatten(child)]

    for name, rows in (
        ("marketing", skilltree.sub_skills(ROOT / "skills/marketing/SKILL.md")),
        ("git", skilltree.linked_sub_skills(ROOT / "skills/git/SKILL.md")),
        ("security", skilltree.situation_sub_skills(ROOT / "skills/security/SKILL.md")),
        ("design", skilltree.situation_sub_skills(ROOT / "skills/design/SKILL.md")),
        ("implement", skilltree.linked_sub_skills(ROOT / "skills/implement/SKILL.md")),
        ("grill", skilltree.linked_sub_skills(ROOT / "skills/grill/SKILL.md")),
        ("writing", skilltree.linked_sub_skills(ROOT / "skills/writing/SKILL.md")),
    ):
        actual = flatten(items[name]["tree"])
        assert {(item["name"], item["path"], item["description"]) for item in actual} == {
            (child, f"skills/{name}/{path}", description) for child, path, description in rows
        }
    # A plain skill must not acquire all its references as catalogue children.
    assert flatten(items["tdd"]["tree"]) == []


def test_provenance_includes_reference_only_repositories_and_normalizes(tmp_path):
    folder = tmp_path / "skills/alpha/references"
    folder.mkdir(parents=True)
    (folder / "reference.md").write_text('---\nmetadata:\n  based_on_repo: "https://github.com/Example/Repo.git, Other/Source"\n---\n')
    (folder / "another.md").write_text('---\nmetadata:\n  based_on_repo: example/repo\n---\n')
    registry = tmp_path / "site/data"
    registry.mkdir(parents=True)
    (registry / "website-sources.json").write_text(json.dumps([
        {"title": "A source", "url": "https://EXAMPLE.com/article/", "skills": ["alpha"]},
        {"title": "Repeated source", "url": "https://example.com/article", "skills": ["beta"]},
    ]))
    result = site_data.sources(tmp_path, [
        {"name": "alpha", "path": "skills/alpha/SKILL.md"},
        {"name": "beta", "path": "skills/beta/SKILL.md"},
    ])
    repos = {item["name"]: item["skills"] for item in result if item["type"] == "repository"}
    assert repos == {"example/repo": ["alpha"], "other/source": ["alpha"]}
    websites = [item for item in result if item["type"] == "website"]
    assert len(websites) == 1
    assert websites[0]["skills"] == ["alpha", "beta"]
    assert websites[0]["url"] == "https://example.com/article"


def test_unknown_website_skill_fails(tmp_path):
    registry = tmp_path / "site/data"
    registry.mkdir(parents=True)
    (registry / "website-sources.json").write_text(json.dumps([
        {"title": "Source", "url": "https://example.com", "skills": ["typo"]},
    ]))
    with pytest.raises(ValueError, match="invalid skill mappings"):
        site_data.sources(tmp_path, [])


def test_generation_is_read_only_and_deterministic():
    watched = sorted((ROOT / "skills").rglob("*.md"))
    before = [path.read_bytes() for path in watched]
    first = site_data.build(ROOT)
    assert first == site_data.build(ROOT)
    assert before == [path.read_bytes() for path in watched]
    for section in first.values():
        assert len({item["id"] for item in section}) == len(section)


def test_invocation_label_follows_disable_model_invocation(tmp_path):
    for name, extra in (("open", ""), ("closed", "disable-model-invocation: true\n")):
        folder = tmp_path / "skills" / name
        folder.mkdir(parents=True)
        (folder / "SKILL.md").write_text(f"---\nname: {name}\ndescription: Does a thing.\n{extra}---\n")
    (tmp_path / "agents").mkdir()
    (tmp_path / "templates").mkdir()
    (tmp_path / "site/data").mkdir(parents=True)
    (tmp_path / "site/data/website-sources.json").write_text("[]")
    labels = {item["name"]: item["invocationLabel"] for item in site_data.build(tmp_path)["skills"]}
    assert labels == {"open": "Automatic or explicit", "closed": "Explicit request"}
