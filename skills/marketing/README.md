# Marketing

A router skill over the marketing sub-skills for SaaS and software products. `SKILL.md` picks a sub-skill from the task, or from a sub-skill name you pass, and the agent follows that sub-skill as if it were the skill.

## Install

```sh
npx skills add jny986/ai-setup --skill marketing
```

## Usage

```
/marketing [sub-skill] [task]
```

- `/marketing copywriting rewrite the homepage hero`: run a named sub-skill on a task.
- `/marketing cro`: old flat names still work and resolve to the current sub-skill, here `conversion-optimization`.
- `/marketing our signups dropped after the pricing change`: with no sub-skill name, the router picks the closest match and asks if two fit equally.
- `/marketing`: with no task either, it lists the sub-skills and asks what you're working on.

The skill allows implicit invocation, so a plain marketing request works without `/marketing`.

### Product marketing context

Most sub-skills read `docs/marketing/product-marketing.md` in your project for positioning, ICP and audience. Run `/marketing product-marketing` once to create it. If it's missing when a sub-skill needs it, the router offers to create it first.

## Resources

| Path | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | The router: loads the product context, picks a sub-skill and follows it. Its tables list every sub-skill with a "Use when" line. |
| [`sub-skills/name-table.md`](sub-skills/name-table.md) | Every sub-skill's name and path, where its content came from (kostja94/marketing-skills, this repo, or both), and the old names that alias to it. |
| `sub-skills/<category>/[<group>/]<name>.md` | One sub-skill. Supporting `references/` and `assets/` folders sit beside it, shared by the sub-skills in the same folder. |
| [`agents/openai.yaml`](agents/openai.yaml) | Display metadata for OpenAI and Codex agents. |

The category folders, all under `sub-skills/`, are:

| Folder | Covers |
|---|---|
| `sub-skills/analytics/` | Tracking, attribution, A/B tests, traffic sources, SEO monitoring |
| `sub-skills/channels/` | Communities, directories, app stores, events, email, SMS, partnerships, PR, referrals |
| `sub-skills/content/` | Copywriting, copy editing, articles, lead magnets, podcasts, video, images, translation |
| `sub-skills/paid-ads/` | Ad creative, ad formats, and Google, Meta, LinkedIn, Reddit, TikTok and YouTube ads |
| `sub-skills/platforms/` | Organic social |
| `sub-skills/sales/` | Cold email, prospecting, RevOps, sales enablement |
| `sub-skills/seo/` | Keyword and competitor research, content strategy, on-page, technical, off-page, local, entity, parasite and programmatic SEO |
| `sub-skills/strategies/` | Brand, pricing and offers, domains, GEO, localisation, free tools, open source, paid ads strategy, conversion, launch and growth, marketing operations, site structure |

## Hand-offs

Sub-skills hand off to each other by name, for example "see cro", and the router resolves that name the same way it resolves yours. A hand-off written as `implement/sub-skills/references/...` points to the page and component build guides packaged with the implement router. Install `implement` alongside `marketing` for these build hand-offs.

## Sources

Based on [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills), [kostja94/pagina](https://github.com/kostja94/pagina) and [kostja94/bricks](https://github.com/kostja94/bricks), all MIT. See the [root README](../../README.md) for how they're kept as submodules and the structure checks.
