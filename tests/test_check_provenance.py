import subprocess

from conftest import errors, load

check = load("check-provenance").check

GITMODULES = '[submodule "up"]\n\tpath = original-skills/up\n\turl = https://github.com/owner/up.git\n'


def git(repo, *args):
    subprocess.run(["git", "-C", str(repo), "-c", "user.email=a@b", "-c", "user.name=t", *args], check=True, capture_output=True)


def based_on(repo, repo_name, version):
    path = repo / "skills" / "alpha" / "SKILL.md"
    path.write_text(path.read_text().replace(
        "author: jny986", f"author: jny986\n  based_on_repo: {repo_name}\n  based_on_version: {version}\n  based_on_skill: x"
    ))


def pin_submodule(repo):
    """Commit a gitlink for original-skills/up and return its sha."""
    git(repo, "init", "-q")
    sha = "a" * 40
    git(repo, "update-index", "--add", "--cacheinfo", f"160000,{sha},original-skills/up")
    (repo / ".gitmodules").write_text(GITMODULES)
    git(repo, "add", ".gitmodules")
    git(repo, "commit", "-qm", "pin")
    return sha


def test_unknown_upstream_repo_fails(repo):
    based_on(repo, "owner/unknown", "v1.0.0(aaaaaaa)")
    (repo / ".gitmodules").write_text(GITMODULES)
    assert "no submodule" in errors(check(repo))


def test_drift_warns_by_default_and_fails_on_request(repo):
    based_on(repo, "owner/up", "v1.0.0(bbbbbbb)")
    pin_submodule(repo)
    report = check(repo)
    assert report.errors == [] and "pinned at aaaaaaa" in report.warnings[0]
    assert "pinned at aaaaaaa" in errors(check(repo, fail_on_drift=True))


def test_matching_pin_passes(repo):
    based_on(repo, "owner/up", "v1.0.0(aaaaaaa)")
    pin_submodule(repo)
    report = check(repo, fail_on_drift=True)
    assert report.errors == [] and report.warnings == []
