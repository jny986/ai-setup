from conftest import errors, load

check = load("check-readme").check


def test_valid_repo_passes(repo):
    assert check(repo).errors == []


def test_submodule_missing_from_readme(repo):
    (repo / ".gitmodules").write_text('[submodule "x"]\n\tpath = source-skills/x\n\turl = https://github.com/a/x.git\n')
    (repo / "README.md").write_text("└── source-skills/\n")
    assert "source-skills/x missing" in errors(check(repo))
