# Marketing

A router skill over the marketing guides for SaaS and software products. `SKILL.md` picks a guide from the task, or from a guide name you pass, and the agent follows that guide as if it were the skill.

## Install

```sh
npx skills add jny986/ai-setup --skill marketing
```

## Usage

```
/marketing [guide] [task]
```

- `/marketing copywriting rewrite the homepage hero`: run a named guide on a task.
- `/marketing cro`: old flat names still work and resolve to the current guide, here `conversion-optimization`.
- `/marketing our signups dropped after the pricing change`: with no guide name, the router picks the closest match and asks if two fit equally.
- `/marketing`: with no task either, it lists the guides and asks what you're working on.

The skill allows implicit invocation, so a plain marketing request works without `/marketing`.

### Product marketing context

Most guides read `docs/marketing/product-marketing.md` in your project for positioning, ICP and audience. Run `/marketing product-marketing` once to create it. If it's missing when a guide needs it, the router offers to create it first.

## Resources

| Path | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | The router: loads the product context, picks a guide and follows it. Its tables list every guide with a "Use when" line. |
| [`references/name-table.md`](references/name-table.md) | Every guide's name and path, where its content came from (kostja94/marketing-skills, this repo, or both), and the old names that alias to it. |
| `<category>/[<group>/]<name>/GUIDE.md` | One guide. Its own `references/` and `assets/` folders sit beside it. |
| [`agents/openai.yaml`](agents/openai.yaml) | Display metadata for OpenAI and Codex agents. |

The top-level category folders are:

| Folder | Covers |
|---|---|
| `analytics/` | Tracking, attribution, A/B tests, traffic sources, SEO monitoring |
| `channels/` | Communities, directories, app stores, events, email, SMS, partnerships, PR, referrals |
| `content/` | Copywriting, copy editing, articles, lead magnets, podcasts, video, images, translation |
| `paid-ads/` | Ad creative, ad formats, and Google, Meta, LinkedIn, Reddit, TikTok and YouTube ads |
| `platforms/` | Organic social |
| `sales/` | Cold email, prospecting, RevOps, sales enablement |
| `seo/` | Keyword and competitor research, content strategy, on-page, technical, off-page, local, entity, parasite and programmatic SEO |
| `strategies/` | Brand, pricing and offers, domains, GEO, localisation, free tools, open source, paid ads strategy, conversion, launch and growth, marketing operations, site structure |

## Hand-offs

Guides hand off to each other by name, for example "see cro", and the router resolves that name the same way it resolves yours. A hand-off written as `dev/references/...` points to the page and component build guides in `skills/dev/references/`, a reference-only tree in this repo with no router skill of its own.

## Sources

Based on [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills), [kostja94/pagina](https://github.com/kostja94/pagina) and [kostja94/bricks](https://github.com/kostja94/bricks), all MIT. See the [root README](../../README.md) for how they're kept as submodules and the structure checks.
