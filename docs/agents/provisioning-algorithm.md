# Resource Provisioning Algorithm

**Status:** PROPOSAL

## Composition

```text
Common baseline
+ Department pack
+ Role-family overlay
+ Project requirements
+ Task requirements
+ Live environment requirements
      ↓
Normalize capabilities
      ↓
Find approved providers
      ↓
Policy + risk filtering
      ↓
Health + compatibility filtering
      ↓
Least-privilege grant
      ↓
Workspace provisioning
      ↓
Audit + provenance
```

## Rules

1. REQUIRED resources must resolve or the run blocks/requests an alternative.
2. PREFERRED resources may use compatible fallbacks.
3. OPTIONAL resources are provisioned only when useful.
4. PROHIBITED resources are denied even when available.
5. Public packs name capabilities, not vendors.
6. Discovery never implies authorization.
7. Credentials should be scoped and short-lived where possible.
8. Live resources require freshness checks.
9. Context-heavy resources are retrieved selectively.
10. Every grant is revocable and auditable.

## Compact profiles

The 1,548 generated profile records reference shared packs instead of duplicating requirements. This reduces drift, repository size, provider lock-in, and future token/context overhead.
