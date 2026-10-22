import pytest

from conftest import errors, load

check = load("check-indexes").check


@pytest.fixture
def catalogue(repo):
    (repo / "skills.html").write_text(
        '<main data-skill-count="2">'
        '<article class="skill" id="skill-alpha" data-skill="alpha" data-invokable="yes"></article>'
        '<article class="skill" id="skill-beta" data-skill="beta" data-invokable="no"></article>'
        '</main>'
    )
    return repo


def test_usage_catalogue_passes(catalogue):
    assert check(catalogue).errors == []


def test_usage_catalogue_invocation_policy(catalogue):
    path = catalogue / "skills.html"
    path.write_text(path.read_text().replace('data-invokable="no"', 'data-invokable="yes"'))
    assert "agent-invokable column disagrees" in errors(check(catalogue))


def test_usage_catalogue_count(catalogue):
    path = catalogue / "skills.html"
    path.write_text(path.read_text().replace('data-skill-count="2"', 'data-skill-count="3"'))
    assert "catalogue count does not match" in errors(check(catalogue))


def test_usage_catalogue_order(catalogue):
    path = catalogue / "skills.html"
    text = path.read_text().replace('alpha', 'temporary').replace('beta', 'alpha').replace('temporary', 'beta')
    text = text.replace('data-invokable="yes"', 'data-invokable="temporary"').replace('data-invokable="no"', 'data-invokable="yes"').replace('data-invokable="temporary"', 'data-invokable="no"')
    path.write_text(text)
    assert "not sorted alphabetically" in errors(check(catalogue))


def test_valid_repo_passes(repo):
    assert check(repo).errors == []


def test_unlisted_skill(repo):
    (repo / "skills" / "gamma").mkdir()
    (repo / "skills" / "gamma" / "SKILL.md").write_text("---\nname: gamma\n---\n")
    out = errors(check(repo))
    assert "SKILLS.md: skill 'gamma' not listed" in out and "skills.html: skill 'gamma' not listed" in out


def test_row_for_missing_skill(repo):
    path = repo / "SKILLS.md"
    path.write_text(path.read_text() + "| [ghost](skills/ghost) | Original | Yes | Boo. |\n")
    assert "lists 'ghost'" in errors(check(repo))


def test_unsorted_rows(repo):
    path = repo / "SKILLS.md"
    lines = path.read_text().splitlines()
    path.write_text("\n".join(lines[:4] + [lines[5], lines[4]]) + "\n")
    assert "not sorted" in errors(check(repo))


def test_invokable_column_must_match_frontmatter(repo):
    path = repo / "SKILLS.md"
    path.write_text(path.read_text().replace("| Original | No |", "| Original | Yes |"))
    assert "agent-invokable column disagrees" in errors(check(repo))


def test_html_group_count(repo):
    path = repo / "skills.html"
    path.write_text(path.read_text().replace("(2)", "(5)"))
    assert "says 5 but lists 2" in errors(check(repo))


def test_nested_sub_skills_preserve_group_checks(repo):
    path = repo / "skills.html"
    nested = (
        '<tr><td colspan="5"><details><summary>Alpha sub-skills <span class="count">(1)</span></summary>'
        '<details><summary>Category</summary><table><tbody>'
        '<tr><td><a href="skills/alpha/sub-skills/example.md">example</a></td></tr>'
        '</tbody></table></details></details></td></tr>\n'
    )
    text = path.read_text().replace('<tr><td><a href="skills/beta">', nested + '<tr><td><a href="skills/beta">')
    path.write_text(text)
    assert check(repo).errors == []
    path.write_text(text.replace("<span>(2)</span>", "<span>(5)</span>"))
    assert "says 5 but lists 2" in errors(check(repo))


def test_submodule_missing_from_readme(repo):
    (repo / ".gitmodules").write_text('[submodule "x"]\n\tpath = source-skills/x\n\turl = https://github.com/a/x.git\n')
    (repo / "README.md").write_text("└── source-skills/\n")
    assert "source-skills/x missing" in errors(check(repo))
