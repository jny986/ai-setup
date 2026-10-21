#!/usr/bin/env python3
"""Check skill provenance against the upstream submodules.

Always fails when a skill's `based_on_repo` has no submodule in .gitmodules.
With --fail-on-drift, also fails when `based_on_version`'s commit hash differs from the pinned submodule commit.
With --remote, also compares the pinned commit to the upstream default branch (network); implies --fail-on-drift.

Reads the pinned commit from the git tree, so submodules need not be checked out.
"""
import re
import subprocess
import sys
from pathlib import Path

from skilllib import Report, frontmatter, run, skill_dirs

SUBMODULE = re.compile(r'\[submodule "[^"]+"\]\s+path = (\S+)\s+url = (\S+)')


def repo_slug(url):
    return re.sub(r"(\.git)?/?$", "", url).split("github.com/")[-1]


def git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)


def check(root, fail_on_drift=False, remote=False):
    report = Report()
    root = Path(root)
    gitmodules = root / ".gitmodules"
    modules = {repo_slug(url): path for path, url in SUBMODULE.findall(gitmodules.read_text())} if gitmodules.exists() else {}
    drift = report.fail if fail_on_drift or remote else report.warn
    pinned = {}
    drifted = {}

    def pin(repo):
        if repo not in pinned:
            out = git(root, "ls-tree", "HEAD", modules[repo]).stdout.split()
            pinned[repo] = out[2] if len(out) >= 3 and out[1] == "commit" else None
        return pinned[repo]

    # Every skill file: SKILL.md, sub-skills and references each record their own upstream.
    files = {str(md.relative_to(root / "skills")): md for folder in skill_dirs(root).values() for md in sorted(folder.rglob("*.md"))}
    for name, md in files.items():
        meta = (frontmatter(md) or {}).get("metadata", {})
        if not isinstance(meta, dict) or not meta.get("based_on_repo"):
            continue
        repos = [r.strip() for r in meta["based_on_repo"].split(",")]
        versions = [v.strip() for v in meta.get("based_on_version", "").split(",")]
        for repo, version in zip(repos, versions):
            if repo not in modules:
                report.fail(f"{name}: based_on_repo '{repo}' has no submodule in .gitmodules")
                continue
            sha, recorded = pin(repo), re.search(r"\(([0-9a-f]+)\)", version)
            if sha and recorded and not sha.startswith(recorded.group(1)):
                drifted.setdefault((repo, version), []).append(name)

    # One line per stale (repo, version), not per file: hundreds of files can share one upstream bump.
    for (repo, version), names in drifted.items():
        shown = ", ".join(names[:3]) + (", ..." if len(names) > 3 else "")
        drift(f"{len(names)} file(s) record based_on_version {version} but {modules[repo]} is pinned at {pin(repo)[:7]}: {shown}")

    if remote:
        for repo, path in modules.items():
            url = f"https://github.com/{repo}.git"
            head = subprocess.run(["git", "ls-remote", url, "HEAD"], capture_output=True, text=True).stdout.split()
            sha = pin(repo)
            if head and sha and head[0] != sha:
                report.fail(f"{path}: pinned {sha[:7]}, upstream HEAD is {head[0][:7]}")
    return report


if __name__ == "__main__":
    flags = sys.argv[1:]
    run(lambda root: check(root, "--fail-on-drift" in flags, "--remote" in flags))
