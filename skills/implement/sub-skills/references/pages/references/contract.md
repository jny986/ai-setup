# Page contract

A page owns one route's user task and its content composition. Whole-site navigation, publishing architecture, and product planning remain project-level decisions.

## Contract fields

| Concern | Required decision |
|---|---|
| Purpose | Audience, arrival context, primary task, and continuation path |
| Truth | Authoritative claims, evidence, assets, content, and data sources; unavailable facts stay explicit |
| Behavior | Inputs, outputs, actions, reachable states, permissions, and recovery |
| Composition | Information needed to recognize, evaluate, act, and verify; section order follows these needs |
| Integration | Route and canonical identity, shared layout, rendering and data conventions, metadata, and existing components |
| Release | Supported origins, locales, markets, and unavailable variants; see [delivery and localization](delivery-localization.md) |

Visible sections and source component boundaries are independent. Existing layout, controls, tokens, and content primitives remain authoritative; a new component needs an unmet responsibility.

## Reference conventions

**Core content** is the page's essential responsibility. **Common** and **conditional** content depend on the actual task and available evidence. Primary component candidates cover the main interaction; common and conditional candidates depend on context. Existing project components can fulfill the same responsibility. A discouraged pattern is a poor default, not a prohibition when the task justifies it.

For references with several modes, use the requested mode's contract and cases. **Acceptance coverage** names verification dimensions: derive the expected result from the page contract and authoritative data, then exercise each applicable case. Missing product capability is a dependency, rather than permission to invent a working state.

## Supporting capability

A page-local handler, adapter, schema, content source, query, cache, or submission endpoint may supply a required page behavior. Existing infrastructure takes precedence. Broader monitoring, search, notification, identity, moderation, or publishing changes belong to the coordinating feature/ticket scope rather than the page sub-skill. Return those dependencies to the coordinator so required non-UI work can be completed. Sample data cannot establish that an operational capability exists.

## Acceptance

The primary task works through the actual route. Page-type acceptance cases and [page quality gates](quality-gates.md) define the required evidence; unsupported claims or unavailable dependencies remain explicit.
