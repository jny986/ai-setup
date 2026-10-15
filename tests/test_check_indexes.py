from conftest import errors, load

check = load("check-indexes").check


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


def test_submodule_missing_from_readme(repo):
    (repo / ".gitmodules").write_text('[submodule "x"]\n\tpath = original-skills/x\n\turl = https://github.com/a/x.git\n')
    (repo / "README.md").write_text("└── original-skills/\n")
    assert "original-skills/x missing" in errors(check(repo))
