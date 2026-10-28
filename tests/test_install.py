"""Exercise interactive template updates with an isolated home directory."""
import json
import os
import pty
import select
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run_installer(repo, home):
    master, slave = pty.openpty()
    env = {**os.environ, "HOME": str(home)}
    process = subprocess.Popen([str(repo / "install.sh")], stdin=slave, stdout=slave, stderr=slave, env=env)
    os.close(slave)
    output = b""
    prompts = [
        (b"Install for Claude Code?", b"y\n"),
        (b"Choose 1, 2 or 3:", b"2\n"),
        (b"Merge the Claude settings template?", b"y\n"),
    ]
    sent = set()
    try:
        while process.poll() is None:
            ready, _, _ = select.select([master], [], [], 5)
            if not ready:
                raise AssertionError(f"Installer stalled: {output!r}")
            try:
                output += os.read(master, 4096)
            except OSError:
                break
            for index, (prompt, answer) in enumerate(prompts):
                if index not in sent and prompt in output:
                    os.write(master, answer)
                    sent.add(index)
        assert process.wait(timeout=5) == 0, output.decode(errors="replace")
    finally:
        if process.poll() is None:
            process.kill()
            process.wait()
        os.close(master)


def test_updates_templates_preserving_user_content_and_owned_list_entries(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    shutil.copy(ROOT / "install.sh", repo / "install.sh")
    shutil.copytree(ROOT / "templates", repo / "templates")
    shutil.copytree(ROOT / "agents", repo / "agents")
    home = tmp_path / "home"
    claude = home / ".claude"
    claude.mkdir(parents=True)
    template = (repo / "templates/claude/AGENTS.md").read_text()
    (claude / "AGENTS.md").write_text(template + "\nCustom instructions\n")
    (claude / "settings.json").write_text(json.dumps({
        "custom": 42, "permissions": {"allow": ["Bash(custom:*)", "Bash(git commit:*)"]}
    }))

    run_installer(repo, home)
    instructions = (claude / "AGENTS.md").read_text()
    assert instructions.count("## Shell commands") == 1
    assert "Custom instructions" in instructions

    settings_template = repo / "templates/claude/settings.json"
    new_template = json.loads(settings_template.read_text())
    allow = new_template["permissions"]["allow"]
    allow.remove("Bash(git commit:*)")  # Already present before installation: user-owned.
    allow.remove("Bash(git push:*)")  # Added by installer: template-owned.
    allow.append("Bash(new:*)")
    settings_template.write_text(json.dumps(new_template))
    run_installer(repo, home)
    settings = json.loads((claude / "settings.json").read_text())
    assert settings["custom"] == 42
    assert "Bash(custom:*)" in settings["permissions"]["allow"]
    assert "Bash(git commit:*)" in settings["permissions"]["allow"]
    assert "Bash(git push:*)" not in settings["permissions"]["allow"]
    assert "Bash(new:*)" in settings["permissions"]["allow"]
    before = (claude / "settings.json").read_bytes()
    run_installer(repo, home)
    assert (claude / "settings.json").read_bytes() == before

    del new_template["permissions"]["allow"]
    settings_template.write_text(json.dumps(new_template))
    run_installer(repo, home)
    allow = json.loads((claude / "settings.json").read_text())["permissions"]["allow"]
    assert allow == ["Bash(custom:*)", "Bash(git commit:*)"]
