# Navigation Menu

## Scope

A navigation menu exposes the destinations and actions users need to move through a product or site. Its structure follows information architecture and user priority, not the organization's internal chart.

## Decisions

Define primary destinations, active state, hierarchy, authenticated variations, mobile behavior, overflow, and whether a disclosure, menu, or navigation list matches the interaction.

## Constraints

- Use links for destinations and buttons for disclosures or commands.
- Do not apply application-menu ARIA semantics to ordinary website navigation.
- Preserve keyboard access, visible focus, active-page indication, and escape from overlays.
- Avoid hiding essential destinations behind hover-only interaction.

## Acceptance criteria

Every destination and active state is correct across authentication states. Keyboard and pointer interaction, mobile opening/dismissal, focus restoration, long labels, and resizing an open menu preserve access.
