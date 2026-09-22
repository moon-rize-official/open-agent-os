# Domain 72 — Multi-Tenancy: Expanded Scope

## Profiles

Research isolation for:

- multiple local users;
- one organization / many teams;
- users in several organizations;
- partners/shared projects;
- managed SaaS tenants;
- highly regulated tenants;
- dedicated enterprise control planes.

## Current references

- Kubernetes multi-tenancy:
  https://kubernetes.io/docs/concepts/security/multi-tenancy/
- OpenFGA multi-tenant SaaS:
  https://openfga.dev/docs/use-cases/multi-tenant-saas
- OpenFGA organization context:
  https://openfga.dev/docs/modeling/organization-context-authorization

## Isolation dimensions

- identity;
- authorization;
- API namespace;
- task/run state;
- knowledge;
- memory;
- artifact storage;
- secrets;
- model prompts;
- vector/search indexes;
- logs/traces;
- cost/billing;
- compute;
- network;
- extensions.

## Tenant context

A principal may belong to several organizations.

The request should carry explicit organization context and backend authorization should verify that the principal is entitled to act in that context.

## Isolation patterns

### Shared control plane

Lowest operational overhead.

Requires strong logical isolation.

### Namespace/per-tenant partition

Stronger boundaries in data and operations.

### Virtual control plane

Useful when tenants need stronger API/resource isolation.

### Dedicated control plane

Highest isolation and operational cost.

## Failure tests

- cross-tenant search;
- cache key collision;
- shared vector index leakage;
- organization switch in another browser tab;
- logs missing tenant ID;
- model cache reused across unauthorized tenants;
- cost charged to wrong organization;
- background task survives tenant offboarding.
