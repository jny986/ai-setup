"""Fixtures: a minimal valid repo tree that each test breaks in one way, and a loader for the hyphenated check scripts."""
import importlib.util
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))

SKILL = """---
name: {name}
description: Does a thing. Use when the user asks for a thing.
{extra}license: MIT
metadata:
  author: jny986
---

# {name}
"""

YAML = """interface:
  display_name: "{name}"
  short_description: "Does a thing"
{policy}"""

def load(script):
    """Import scripts/<script>.py (names contain hyphens, so plain import will not do)."""
    spec = importlib.util.spec_from_file_location(script.replace("-", "_"), SCRIPTS / f"{script}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def repo(tmp_path):
    """A valid repo with skills alpha (model-invocable) and beta (user-only)."""
    for name, extra, policy in (
        ("alpha", "", ""),
        ("beta", "disable-model-invocation: true\n", "policy:\n  allow_implicit_invocation: false\n"),
    ):
        folder = tmp_path / "skills" / name
        (folder / "agents").mkdir(parents=True)
        (folder / "SKILL.md").write_text(SKILL.format(name=name, extra=extra))
        (folder / "agents" / "openai.yaml").write_text(YAML.format(name=name, policy=policy))
    (tmp_path / "docs" / "agents").mkdir(parents=True)
    (tmp_path / "docs" / "agents" / "issue-tracker.md").write_text("# Tracker\n")
    return tmp_path


def errors(report):
    return "\n".join(report.errors)
