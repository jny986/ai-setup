from conftest import errors, load

assets = load("check-assets")


def test_valid_assets_pass(repo):
    (repo / "run.sh").write_text("#!/usr/bin/env bash\necho ok\n")
    (repo / "settings.json").write_text('{\n  // comment "x"\n  "url": "http://a//b",\n  "a": [1,],\n}\n')
    assert assets.check(repo).errors == []


def test_shell_syntax_error(repo):
    (repo / "bad.sh").write_text("if then\n")
    assert "bad.sh: bash -n" in errors(assets.check(repo))


def test_invalid_json(repo):
    (repo / "bad.json").write_text('{"a": }')
    assert "bad.json: invalid JSON" in errors(assets.check(repo))


def test_strip_jsonc_keeps_strings():
    assert assets.strip_jsonc('{"a": "// not a comment"} // real') .strip() == '{"a": "// not a comment"}'
