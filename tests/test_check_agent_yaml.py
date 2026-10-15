from conftest import errors, load

check = load("check-agent-yaml").check


def test_valid_repo_passes(repo):
    assert check(repo).errors == []


def test_missing_yaml(repo):
    (repo / "skills" / "alpha" / "agents" / "openai.yaml").unlink()
    assert "alpha/agents/openai.yaml: missing" in errors(check(repo))


def test_missing_interface_key(repo):
    path = repo / "skills" / "alpha" / "agents" / "openai.yaml"
    path.write_text(path.read_text().replace('  short_description: "Does a thing"\n', ""))
    assert "missing interface.short_description" in errors(check(repo))


def test_user_only_skill_must_disable_implicit(repo):
    path = repo / "skills" / "beta" / "agents" / "openai.yaml"
    path.write_text(path.read_text().replace("false", "true"))
    assert "must be false" in errors(check(repo))


def test_invokable_skill_must_not_disable_implicit(repo):
    path = repo / "skills" / "alpha" / "agents" / "openai.yaml"
    path.write_text(path.read_text() + "policy:\n  allow_implicit_invocation: false\n")
    assert "does not set disable-model-invocation" in errors(check(repo))
