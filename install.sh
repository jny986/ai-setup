#!/usr/bin/env bash
# Install the repository's agent definitions and personal configuration templates.
set -eu

root=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
checkout=''

cleanup() {
  if [ -n "$checkout" ]; then rm -rf "$checkout"; fi
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
  local source=$1 destination=$2 backup suffix
  if [ -L "$destination" ] || { [ -e "$destination" ] && [ ! -f "$destination" ]; }; then
    printf 'Skipping non-regular destination: %s\n' "$destination" >&2
    return
  fi
  if [ -e "$destination" ] || [ -L "$destination" ]; then
    if [ -f "$destination" ] && cmp -s "$source" "$destination"; then
      printf 'Already up to date: %s\n' "$destination"
      return
    fi
    if ! ask "Replace $destination? A backup will be created. [y/N] "; then
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
while :; do
  printf 'Choose 1, 2 or 3: '
  if ! IFS= read -r choice <&3; then
    printf '\nInput ended; installation cancelled.\n' >&2
    exit 1
  fi
  case "$choice" in 1|2|3) break ;; *) printf 'Please choose 1, 2 or 3.\n' ;; esac
done

if [ ! -d "$root/agents" ] || [ ! -d "$root/templates" ]; then
  if ! command -v git >/dev/null 2>&1; then
    printf 'Git is required to download the agents and templates.\n' >&2
    exit 1
  fi
  checkout=$(mktemp -d "${TMPDIR:-/tmp}/ai-setup-install.XXXXXXXX")
  printf 'Downloading agents and templates from GitHub...\n'
  git clone --quiet --depth 1 https://github.com/jny986/ai-setup.git "$checkout/repo"
  root="$checkout/repo"
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
    install_file "$root/templates/AGENTS.md" "$HOME/.claude/AGENTS.md"
    install_file "$root/templates/CLAUDE.md" "$HOME/.claude/CLAUDE.md"
    printf '\nThe Claude settings template contains personal paths, hooks, permissions and plugin choices. Review templates/settings.json before applying it.\n'
    if ask 'Install the entire Claude settings template? [y/N] '; then
      install_file "$root/templates/settings.json" "$HOME/.claude/settings.json"
    fi
  fi
  if [ "$codex" = yes ]; then
    install_file "$root/templates/AGENTS.md" "$HOME/.codex/AGENTS.md"
  fi
fi
printf 'Done. Review installed templates and agent models for your environment.\n'
