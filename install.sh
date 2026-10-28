#!/usr/bin/env bash
# Install the repository's agent definitions and personal configuration templates.
set -eu

root=''
if [ -n "${BASH_SOURCE[0]:-}" ]; then
  root=$(CDPATH='' cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
fi
checkout=''
workdir=''

cleanup() {
  if [ -n "$checkout" ]; then rm -rf "$checkout"; fi
  if [ -n "$workdir" ]; then rm -rf "$workdir"; fi
}

update_template() {
  local source=$1 destination=$2 candidate="$workdir/template" state=''
  if [ -L "$destination" ] || { [ -e "$destination" ] && [ ! -f "$destination" ]; }; then
    printf 'Skipping non-regular destination: %s\n' "$destination" >&2
    return
  fi
  if [ "${source##*.}" = json ]; then
    state="$(dirname "$destination")/.ai-setup-settings-template.json"
    if [ -L "$state" ] || { [ -e "$state" ] && [ ! -f "$state" ]; }; then
      printf 'Cannot update template history: %s\n' "$state" >&2
      return 1
    fi
  fi
  python3 - "$source" "$destination" "$candidate" "$state" "$workdir/settings-history" <<'PY'
import json
import sys
from pathlib import Path

source, destination, candidate = map(Path, sys.argv[1:4])
template = source.read_text(encoding="utf-8")
existing = destination.read_text(encoding="utf-8") if destination.exists() else ""

if source.suffix == ".json":
    def remove_owned(old, previous):
        if isinstance(old, dict) and isinstance(previous, dict):
            return {key: remove_owned(value, previous.get(key)) for key, value in old.items()}
        if isinstance(old, list) and isinstance(previous, list):
            return [value for value in old if value not in previous]
        return old

    def merge(old, new, previous):
        if isinstance(old, dict) and isinstance(new, dict):
            result = dict(old)
            owned = {}
            if isinstance(previous, dict):
                for key in previous.keys() - new.keys():
                    if key in result:
                        result[key] = remove_owned(result[key], previous[key])
            for key, value in new.items():
                prior = previous.get(key) if isinstance(previous, dict) else None
                result[key], owned[key] = merge(old.get(key), value, prior)
            return result, owned
        if isinstance(old, list) and isinstance(new, list):
            previous = previous if isinstance(previous, list) else []
            kept = [value for value in old if value not in previous or value in new]
            added = [value for value in new if value not in kept]
            return kept + added, [value for value in previous if value in new and value in kept] + added
        if isinstance(new, dict):
            return merge({}, new, previous)
        if isinstance(new, list):
            return list(new), list(new)
        return new, None

    old = json.loads(existing) if destination.exists() else {}
    new = json.loads(template)
    if not isinstance(old, dict) or not isinstance(new, dict):
        raise ValueError("Settings must be JSON objects")
    state = Path(sys.argv[4])
    previous = json.loads(state.read_text(encoding="utf-8")) if state.exists() else {}
    merged, owned = merge(old, new, previous)
    result = json.dumps(merged, indent=2, ensure_ascii=False) + "\n"
    Path(sys.argv[5]).write_text(json.dumps(owned, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
else:
    start = "<!-- BEGIN ai-setup template -->"
    end = "<!-- END ai-setup template -->"
    section = start + "\n" + template.rstrip("\n") + "\n" + end
    if (existing.count(start) != existing.count(end) or existing.count(start) > 1
            or (start in existing and existing.index(start) > existing.index(end))):
        raise ValueError(f"Invalid template markers in {destination}")
    if start in existing:
        before, remainder = existing.split(start, 1)
        _, after = remainder.split(end, 1)
        result = before + section + after
    elif not existing or existing == template:
        result = section + "\n"
    elif template and existing.count(template) == 1:
        result = existing.replace(template, section + "\n", 1)
    else:
        result = existing + ("\n" if existing.endswith("\n") else "\n\n") + section + "\n"
candidate.write_text(result, encoding="utf-8")
PY
  install_file "$candidate" "$destination" update
  if [ -n "$state" ]; then
    chmod 600 "$workdir/settings-history"
    mv "$workdir/settings-history" "$state"
  fi
}
trap cleanup EXIT

# A piped script uses stdin for its source, so read answers from the terminal.
if [ -t 0 ]; then
  exec 3<&0
elif [ -t 1 ] && { exec 3</dev/tty; } 2>/dev/null; then
  :
else
  printf 'An interactive terminal is required to answer installation prompts.\n' >&2
  exit 1
fi

ask() {
  local prompt=$1 answer
  while :; do
    printf '%s' "$prompt"
    if ! IFS= read -r answer <&3; then
      printf '\nInput ended; installation cancelled.\n' >&2
      exit 1
    fi
    case "$answer" in
      y|Y|yes|YES) return 0 ;;
      n|N|no|NO|'') return 1 ;;
      *) printf 'Please enter y or n.\n' ;;
    esac
  done
}

install_file() {
  local source=$1 destination=$2 mode=${3:-prompt} backup suffix
  if [ -L "$destination" ] || { [ -e "$destination" ] && [ ! -f "$destination" ]; }; then
    printf 'Skipping non-regular destination: %s\n' "$destination" >&2
    return
  fi
  if [ -e "$destination" ] || [ -L "$destination" ]; then
    if [ -f "$destination" ] && cmp -s "$source" "$destination"; then
      printf 'Already up to date: %s\n' "$destination"
      return
    fi
    if [ "$mode" = prompt ] && ! ask "Replace $destination? A backup will be created. [y/N] "; then
      printf 'Skipped: %s\n' "$destination"
      return
    fi
    backup="$destination.bak"
    suffix=1
    while [ -e "$backup" ] || [ -L "$backup" ]; do
      backup="$destination.bak.$suffix"
      suffix=$((suffix + 1))
    done
    cp -p "$destination" "$backup"
    printf 'Backup: %s\n' "$backup"
  fi
  mkdir -p "$(dirname "$destination")"
  cp "$source" "$destination"
  printf 'Installed: %s\n' "$destination"
}

printf 'Checking home directories:\n'
for dir in .agents .claude .codex; do
  if [ -d "$HOME/$dir" ]; then
    printf '  Found %s\n' "$HOME/$dir"
  else
    printf '  Not found: %s\n' "$HOME/$dir"
  fi
done

claude=no
codex=no
if [ -d "$HOME/.claude" ] && ask 'Install for Claude Code? [y/N] '; then claude=yes; fi
if [ -d "$HOME/.codex" ] && ask 'Install for Codex? [y/N] '; then codex=yes; fi
if [ "$claude" = no ] && [ "$codex" = no ]; then
  printf 'No available client selected; nothing to install.\n'
  exit 0
fi

printf 'What would you like to install or update?\n  1) Agents\n  2) Config templates\n  3) Both\n'
printf 'Config templates update managed content and preserve other settings; changed files are backed up.\n'
while :; do
  printf 'Choose 1, 2 or 3: '
  if ! IFS= read -r choice <&3; then
    printf '\nInput ended; installation cancelled.\n' >&2
    exit 1
  fi
  case "$choice" in 1|2|3) break ;; *) printf 'Please choose 1, 2 or 3.\n' ;; esac
done

if [ -z "$root" ] || [ ! -d "$root/agents" ] || [ ! -d "$root/templates" ]; then
  if ! command -v git >/dev/null 2>&1; then
    printf 'Git is required to download the agents and templates.\n' >&2
    exit 1
  fi
  checkout=$(mktemp -d "${TMPDIR:-/tmp}/ai-setup-install.XXXXXXXX")
  printf 'Downloading agents and templates from GitHub...\n'
  git clone --quiet --depth 1 https://github.com/jny986/ai-setup.git "$checkout/repo"
  root="$checkout/repo"
fi

if [ "$choice" = 2 ] || [ "$choice" = 3 ]; then
  if ! command -v python3 >/dev/null 2>&1; then
    printf 'Python 3 is required to merge config templates.\n' >&2
    exit 1
  fi
  workdir=$(mktemp -d "${TMPDIR:-/tmp}/ai-setup-templates.XXXXXXXX")
fi

if [ "$choice" = 1 ] || [ "$choice" = 3 ]; then
  for agent in "$root"/agents/*; do
    [ -d "$agent" ] || continue
    name=${agent##*/}
    if [ "$claude" = yes ] && [ -f "$agent/agent.md" ]; then
      install_file "$agent/agent.md" "$HOME/.claude/agents/$name.md"
    fi
    if [ "$codex" = yes ] && [ -f "$agent/$name.toml" ]; then
      install_file "$agent/$name.toml" "$HOME/.codex/agents/$name.toml"
    fi
  done
fi

if [ "$choice" = 2 ] || [ "$choice" = 3 ]; then
  if [ "$claude" = yes ]; then
    update_template "$root/templates/claude/AGENTS.md" "$HOME/.claude/AGENTS.md"
    update_template "$root/templates/claude/CLAUDE.md" "$HOME/.claude/CLAUDE.md"
    printf '\nThe Claude settings template contains personal paths, hooks, permissions and plugin choices. Review templates/claude/settings.json before applying it.\n'
    if ask 'Merge the Claude settings template? [y/N] '; then
      update_template "$root/templates/claude/settings.json" "$HOME/.claude/settings.json"
    fi
  fi
  if [ "$codex" = yes ]; then
    update_template "$root/templates/codex/AGENTS.md" "$HOME/.codex/AGENTS.md"
  fi
fi
printf 'Done. Review installed templates and agent models for your environment.\n'
