from conftest import errors, load

module = load("check-skills")
check = module.check


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
    assert "must align" in errors(check(repo))


def test_several_skills_from_one_repo_pass(repo):
    edit(repo, "alpha", "author: jny986", "author: jny986\n  based_on_repo: a/b\n  based_on_version: v1.0.0(abcdef1)\n  based_on_skill: x, y")
    assert check(repo).errors == []


def test_bad_version_format(repo):
    edit(repo, "alpha", "author: jny986", "author: jny986\n  based_on_repo: a/b\n  based_on_version: latest\n  based_on_skill: x")
    assert "based_on_version" in errors(check(repo))


def test_invalid_flag_value(repo):
    edit(repo, "alpha", "license: MIT", "license: MIT\ndisable-model-invocation: yes")
    assert "must be true or false" in errors(check(repo))


def write_sub(repo, body, name="step.md"):
    folder = repo / "skills" / "alpha" / "sub-skills"
    folder.mkdir(exist_ok=True)
    (folder / name).write_text(body)


SUB = "---\nname: step\ndescription: Does a step.\nmetadata:\n  version: \"1.0.0\"\n{extra}---\n\nBody.\n"


def test_valid_sub_skill_passes(repo):
    write_sub(repo, SUB.format(extra="  based_on_repo: a/b\n  based_on_version: main(abcdef1)\n  based_on_skill: x\n"))
    assert check(repo).errors == []


def test_sub_skill_needs_frontmatter(repo):
    write_sub(repo, "# Step\n")
    assert "missing frontmatter" in errors(check(repo))


def test_sub_skill_needs_description(repo):
    write_sub(repo, SUB.format(extra="").replace("description: Does a step.\n", ""))
    assert "missing description" in errors(check(repo))


def test_sub_skill_unknown_key_fails(repo):
    write_sub(repo, SUB.format(extra="").replace("metadata:", "licence: MIT\nmetadata:"))
    assert "unknown key 'licence'" in errors(check(repo))


def test_sub_skill_rejects_model_invocation_flag(repo):
    write_sub(repo, SUB.format(extra="").replace("metadata:", "disable-model-invocation: true\nmetadata:"))
    assert "unknown key 'disable-model-invocation'" in errors(check(repo))


def test_sub_skill_version_needs_hash(repo):
    write_sub(repo, SUB.format(extra="  based_on_repo: a/b\n  based_on_version: main\n  based_on_skill: x\n"))
    assert "<ref>(hash)" in errors(check(repo))


def test_sub_skill_legacy_based_on_key_fails(repo):
    write_sub(repo, SUB.format(extra="  based_on: a/b@abcdef1\n"))
    assert "unknown metadata key 'based_on'" in errors(check(repo))


def test_name_table_needs_no_frontmatter(repo):
    write_sub(repo, "# Names\n", name="name-table.md")
    assert check(repo).errors == []


REF = "---\nmetadata:\n  version: \"1.0.0\"\n{extra}---\n\n# Guide\n"
REF_BASED_ON = "  based_on_repo: a/b\n  based_on_version: main(abcdef1)\n  based_on_skill: x\n"


def write_ref(repo, body):
    folder = repo / "skills" / "alpha" / "sub-skills" / "references"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "guide.md").write_text(body)


def test_reference_with_based_on_passes(repo):
    write_ref(repo, REF.format(extra=REF_BASED_ON))
    assert check(repo).errors == []


def test_reference_without_based_on_fails(repo):
    write_ref(repo, REF.format(extra=""))
    assert "missing based_on_*" in errors(check(repo))


def test_reference_without_frontmatter_fails(repo):
    write_ref(repo, "# Guide\n")
    assert "missing based_on_*" in errors(check(repo))


def test_reference_partial_based_on_fails(repo):
    write_ref(repo, REF.format(extra="  based_on_repo: a/b\n"))
    assert "all present or all absent" in errors(check(repo))


def test_reference_legacy_based_on_key_fails(repo):
    write_ref(repo, REF.format(extra="  based_on: a/b@abcdef1\n"))
    assert "unknown metadata key 'based_on'" in errors(check(repo))


def test_original_reference_needs_no_based_on(repo, monkeypatch):
    monkeypatch.setattr(module, "ORIGINAL_REFERENCES", {"alpha/sub-skills/references/guide.md"})
    write_ref(repo, "# Guide\n")
    assert check(repo).errors == []


def test_original_reference_with_based_on_fails(repo, monkeypatch):
    monkeypatch.setattr(module, "ORIGINAL_REFERENCES", {"alpha/sub-skills/references/guide.md"})
    write_ref(repo, REF.format(extra=REF_BASED_ON))
    assert "ORIGINAL_REFERENCES" in errors(check(repo))


def test_broken_link(repo):
    (repo / "skills" / "alpha" / "doc.md").write_text("[x](missing.md)\n")
    assert "broken link missing.md" in errors(check(repo))


def test_chained_command_fails(repo):
    (repo / "skills" / "alpha" / "doc.md").write_text("Run `git add . && git commit`.\n")
    assert "chained command" in errors(check(repo))


def test_chained_command_in_fenced_block_fails(repo):
    (repo / "skills" / "alpha" / "doc.md").write_text("```bash\ngit diff | grep x\n```\n")
    assert "chained command" in errors(check(repo))


def test_pipe_inside_quotes_passes(repo):
    (repo / "skills" / "alpha" / "doc.md").write_text("Run `gh api x --jq '.[] | .id'`.\n")
    assert check(repo).errors == []


def test_version_defaults_to_1_0_0_without_tags(repo):
    edit(repo, "alpha", "author: jny986", "author: jny986\n  version: \"1.0.0\"")
    assert check(repo).errors == []


def test_version_must_match_latest_tag(repo, monkeypatch):
    monkeypatch.setattr(module, "latest_tag", lambda root: "v2.0.0")
    edit(repo, "alpha", "author: jny986", "author: jny986\n  version: \"1.0.0\"")
    assert "!= latest git tag 'v2.0.0'" in errors(check(repo))


def test_version_ignores_tag_v_prefix(repo, monkeypatch):
    monkeypatch.setattr(module, "latest_tag", lambda root: "v2.0.0")
    edit(repo, "alpha", "author: jny986", "author: jny986\n  version: \"2.0.0\"")
    assert check(repo).errors == []


def test_version_not_enforced_for_other_authors(repo, monkeypatch):
    monkeypatch.setattr(module, "latest_tag", lambda root: "v2.0.0")
    edit(repo, "alpha", "author: jny986", "author: someone\n  version: \"1.0.0\"")
    assert check(repo).errors == []


def test_latest_tag_defaults_outside_a_repo(tmp_path):
    assert module.latest_tag(tmp_path) == "1.0.0"
