from conftest import errors, load

check = load("check-references").check


def write(repo, rel, text):
    path = repo / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def test_valid_repo_passes(repo):
    write(repo, "skills/alpha/notes.md", "Run `/beta` then the `alpha` skill. See docs/agents/issue-tracker.md and `/compact`.\n")
    assert check(repo).errors == []


def test_unknown_slash_name(repo):
    write(repo, "skills/alpha/notes.md", "Try `/nope`.\n")
    assert "`/nope` is not a skill" in errors(check(repo))


def test_slash_paths_ignored_in_marketing(repo):
    write(repo, "skills/marketing/guide.md", "Link to `/blog` and `/pricing`.\n")
    assert check(repo).errors == []


def test_unknown_named_skill(repo):
    write(repo, "skills/alpha/notes.md", "Use the `nope` skill.\n")
    assert "skill 'nope' does not exist" in errors(check(repo))


def test_marketing_guide_names_resolve(repo):
    write(repo, "skills/marketing/references/name-table.md", "| `video` | `content/video` | ours | |\n")
    write(repo, "skills/alpha/notes.md", "Use the `video` skill.\n")
    assert check(repo).errors == []


def test_missing_asset(repo):
    write(repo, "skills/alpha/notes.md", "Run `scripts/run.sh`.\n")
    assert "missing asset scripts/run.sh" in errors(check(repo))
    write(repo, "skills/alpha/scripts/run.sh", "echo hi\n")
    assert check(repo).errors == []


def test_missing_docs_agents_file(repo):
    write(repo, "skills/alpha/notes.md", "See docs/agents/domain.md.\n")
    assert "docs/agents/domain.md does not exist" in errors(check(repo))


def test_retired_name_outside_frontmatter(repo):
    write(repo, "skills/alpha/notes.md", "Ask ask-matt.\n")
    assert "retired skill name 'ask-matt'" in errors(check(repo))
    write(repo, "skills/alpha/notes.md", "---\nbased_on_skill: ask-matt\n---\nbody\n")
    assert check(repo).errors == []
