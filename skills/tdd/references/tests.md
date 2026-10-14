# Good and Bad Tests

## Good Tests

**Integration-style**: Test through real interfaces, not mocks of internal parts.

Characteristics:

- Tests behavior users/callers care about
- Uses public API only
- Survives internal refactors
- Describes WHAT, not HOW
- One logical assertion per test

## Bad Tests

**Implementation-detail tests**: Coupled to internal structure.

Red flags:

- Mocking internal collaborators
- Testing private methods
- Asserting on call counts/order
- Test breaks when refactoring without behavior change
- Test name describes HOW not WHAT
- Verifying through external means instead of interface (e.g. querying the database directly instead of going through the public API)

**Tautological tests**: Expected value restates the implementation, so the test passes by construction. Expected values must come from an independent source of truth: a known-good literal, a worked example, the spec — never a value recomputed the way the code computes it.

See the `examples/` directory for these patterns worked in a specific stack (e.g. [typescript.md](examples/typescript.md), [laravel.md](examples/laravel.md)).
