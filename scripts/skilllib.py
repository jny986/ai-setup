"""Shared helpers for the repo checks: a stdlib-only frontmatter/YAML-subset parser, skill discovery and a result report."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
FENCE = re.compile(r"```.*?```", re.S)
KEY = re.compile(r"^([A-Za-z_][\w-]*):[ \t]*(.*)$")


class Report:
    """Collects failures and non-fatal warnings for one check."""

    def __init__(self):
        self.errors = []
        self.warnings = []

    def fail(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)


def unquote(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1].replace('\\"', '"') if value[0] == '"' else value[1:-1]
    return value


def parse_mapping(text):
    """Parse the YAML subset used in this repo: top-level scalars, block scalars (`>`/`|`) and one level of nested mappings.

    Nested mappings come back as dicts, everything else as strings.
    """
    out = {}
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        m = KEY.match(lines[i])
        i += 1
        if not m:
            continue
        key, value = m.group(1), m.group(2)
        body = []
        while i < len(lines) and (lines[i].startswith((" ", "\t")) or not lines[i].strip()):
            body.append(lines[i])
            i += 1
        if value[:1] in (">", "|"):
            parts = [b.strip() for b in body if b.strip()]
            out[key] = (" " if value[0] == ">" else "\n").join(parts)
        elif not value and any(b.strip() for b in body):
            nested = {}
            for b in body:
                nm = KEY.match(b.strip())
                if nm:
                    nested[nm.group(1)] = unquote(nm.group(2))
            out[key] = nested
        else:
            out[key] = unquote(value)
    return out


def frontmatter(path):
    """Return the parsed frontmatter of a Markdown file, or None when it has none."""
    m = FRONTMATTER.match(path.read_text())
    return parse_mapping(m.group(1)) if m else None


def skill_dirs(root=ROOT):
    """Directories directly under skills/ that hold a SKILL.md, keyed by name."""
    return {p.parent.name: p.parent for p in sorted((root / "skills").glob("*/SKILL.md"))}


def run(check):
    """Run `check(ROOT)`, print the report and exit 1 on any failure."""
    report = check(ROOT)
    for w in report.warnings:
        print("WARN", w)
    for e in report.errors:
        print("FAIL", e)
    print(f"{len(report.errors)} failure(s), {len(report.warnings)} warning(s)" if report.errors or report.warnings else "ok")
    sys.exit(1 if report.errors else 0)
