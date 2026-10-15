from conftest import errors, load

check = load("check-skills").check


def edit(repo, name, old, new):
    path = repo / "skills" / name / "SKILL.md"
    path.write_text(path.read_text().replace(old, new))


def test_valid_repo_passes(repo):
    assert check(repo).errors == []


def test_name_must_match_directory(repo):
    edit(repo, "alpha", "name: alpha", "name: other")
    assert "!= directory" in errors(check(repo))


def test_unknown_key_fails(repo):
    edit(repo, "alpha", "license: MIT", "license: MIT\nlicence: MIT")
    assert "unknown key 'licence'" in errors(check(repo))


def test_description_too_long(repo):
    edit(repo, "alpha", "Does a thing. Use when", "x" * 1100 + " use when")
    assert "max 1024" in errors(check(repo))


def test_missing_trigger_only_warns(repo):
    edit(repo, "alpha", "Does a thing. Use when the user asks for a thing.", "Thing")
    report = check(repo)
    assert report.errors == [] and "trigger" in report.warnings[0]


def test_based_on_must_be_all_or_none(repo):
    edit(repo, "alpha", "author: jny986", "author: jny986\n  based_on_repo: a/b")
    assert "all present or all absent" in errors(check(repo))


def test_based_on_lists_must_align(repo):
    edit(repo, "alpha", "author: jny986", "author: jny986\n  based_on_repo: a/b, c/d\n  based_on_version: v1.0.0(abcdef1)\n  based_on_skill: x")
    assert "different lengths" in errors(check(repo))


def test_bad_version_format(repo):
    edit(repo, "alpha", "author: jny986", "author: jny986\n  based_on_repo: a/b\n  based_on_version: latest\n  based_on_skill: x")
    assert "based_on_version" in errors(check(repo))


def test_invalid_flag_value(repo):
    edit(repo, "alpha", "license: MIT", "license: MIT\ndisable-model-invocation: yes")
    assert "must be true or false" in errors(check(repo))


def test_broken_link(repo):
    (repo / "skills" / "alpha" / "doc.md").write_text("[x](missing.md)\n")
    assert "broken link missing.md" in errors(check(repo))
