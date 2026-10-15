#!/usr/bin/env python3
"""Check non-Markdown assets: shell scripts parse (`bash -n`, plus shellcheck when installed) and JSON/JSONC
templates are valid.

Exits 1 on any failure.
"""
import json
import re
import shutil
import subprocess
from pathlib import Path

from skilllib import Report, run

SKIP = {"source-skills", ".git", "node_modules"}


def strip_jsonc(text):
    """Remove // and /* */ comments and trailing commas outside strings."""
    out, i, n = [], 0, len(text)
    while i < n:
        c = text[i]
        if c == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == "\\" else 1
            out.append(text[i : j + 1])
            i = j + 1
        elif text.startswith("//", i):
            while i < n and text[i] != "\n":
                i += 1
        elif text.startswith("/*", i):
            i = text.find("*/", i) + 2 or n
        else:
            out.append(c)
            i += 1
    return re.sub(r",(\s*[}\]])", r"\1", "".join(out))


def tracked(root, pattern):
    return [p for p in sorted(root.rglob(pattern)) if not SKIP & set(p.relative_to(root).parts)]


def check(root):
    report = Report()
    root = Path(root)
    shellcheck = shutil.which("shellcheck")
    for script in tracked(root, "*.sh"):
        rel = script.relative_to(root)
        result = subprocess.run(["bash", "-n", str(script)], capture_output=True, text=True)
        if result.returncode:
            report.fail(f"{rel}: bash -n: {result.stderr.strip()}")
        if shellcheck:
            result = subprocess.run([shellcheck, "-S", "warning", str(script)], capture_output=True, text=True)
            if result.returncode:
                report.fail(f"{rel}: shellcheck:\n{result.stdout.strip()}")
    if not shellcheck:
        report.warn("shellcheck not installed; skipped")
    for pattern in ("*.json", "*.jsonc"):
        for path in tracked(root, pattern):
            try:
                json.loads(strip_jsonc(path.read_text()))
            except ValueError as e:
                report.fail(f"{path.relative_to(root)}: invalid JSON: {e}")
    return report


if __name__ == "__main__":
    run(check)
