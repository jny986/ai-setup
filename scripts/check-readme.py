#!/usr/bin/env python3
"""Check every submodule in .gitmodules appears in the README structure tree.

The skills reference is the docs site (site/); its catalogue is generated from skills/, so there is no index to sync.
Exits 1 on any failure.
"""
import re
from pathlib import Path

from skilllib import Report, run


def check_submodules(root, report):
    gitmodules, readme = root / ".gitmodules", root / "README.md"
    if not gitmodules.exists() or not readme.exists():
        return
    tree = readme.read_text()
    for path in re.findall(r"^\s*path = source-skills/(\S+)", gitmodules.read_text(), re.M):
        if f"{path}/" not in tree:
            report.fail(f"README.md: submodule source-skills/{path} missing from the structure tree")


def check(root):
    report = Report()
    check_submodules(Path(root), report)
    return report


if __name__ == "__main__":
    run(check)
