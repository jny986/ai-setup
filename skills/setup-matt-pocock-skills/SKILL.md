---
name: setup-matt-pocock-skills
description: "Compatibility entry point for project setup. Requires the setup skill."
disable-model-invocation: true
license: MIT
metadata:
  version: "1.1.0"
  author: jny986
  author-url: https://jny986.com
  based_on_repo: mattpocock/skills
  based_on_version: v1.3.1(49dd158)
  based_on_skill: setup-matt-pocock-skills
---

# Engineering setup compatibility entry point

Engineering setup now lives in `/setup`.

Locate the installed `setup` skill through the available-skills list or a sibling skill folder. Read its SKILL.md and follow it to configure engineering workflows for the target project. Its references resolve relative to the setup skill directory.

If `setup` is unavailable, tell the user to install it with `npx skills add jny986/ai-setup --skill setup` for their agent, then run `/setup`. Report the missing dependency instead of claiming setup is complete.
