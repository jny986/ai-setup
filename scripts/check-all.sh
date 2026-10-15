#!/usr/bin/env bash
# Run every repo check in the same order as CI, then the checker tests. Exits 1 if any step failed.
cd "$(dirname "$0")/.." || exit 1

status=0
step() {
  echo "== $1"
  shift
  "$@" || status=1
}

step "Marketing router structure" python3 scripts/check-marketing-structure.py
step "Skill frontmatter and links" python3 scripts/check-skills.py
step "Index sync" python3 scripts/check-indexes.py
step "Agent yaml" python3 scripts/check-agent-yaml.py
step "References" python3 scripts/check-references.py
step "Assets" python3 scripts/check-assets.py
step "Provenance" python3 scripts/check-provenance.py
if command -v yamllint >/dev/null; then
  step "YAML lint" yamllint -c .yamllint.yaml skills/*/agents .github
fi
if command -v markdownlint-cli2 >/dev/null; then
  step "Markdown lint" markdownlint-cli2
fi
if python3 -c "import pytest" 2>/dev/null; then
  step "Checker tests" python3 -m pytest -q tests
fi
exit $status
