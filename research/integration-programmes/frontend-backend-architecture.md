# Frontend & Backend Architecture Research Programme

**Status:** RESEARCH IN PROGRESS  
**Expanded:** 2026-09-22

## Mission

Research how one modular Agent OS can serve very different users without forcing them into the same interface or backend deployment shape.

The system should support:

1. individual / personal user;
2. power user / local-AI enthusiast;
3. individual developer;
4. small development team;
5. startup / small company;
6. medium organization;
7. enterprise / regulated organization;
8. platform engineering team;
9. security / compliance team;
10. research / knowledge team;
11. support / operations team;
12. managed Agent OS / SaaS operator;
13. offline / air-gapped operator;
14. distributed multi-site organization.

The architecture goal is:

```text
One canonical resource model
+
One policy / identity model
+
Multiple backend deployment profiles
+
Multiple frontend experience profiles
```

## Current reference evidence

Useful adjacent architecture patterns:

- Backstage architecture overview:
  https://backstage.io/docs/overview/architecture-overview/
- Backstage frontend plugin architecture:
  https://backstage.io/docs/frontend-system/architecture/plugins/
- Backstage backend plugin architecture:
  https://backstage.io/docs/backend-system/architecture/plugins/
- Backstage backend system:
  https://backstage.io/docs/backend-system/
- Kubernetes multi-tenancy:
  https://kubernetes.io/docs/concepts/security/multi-tenancy/
- OpenFGA multi-tenant SaaS:
  https://openfga.dev/docs/use-cases/multi-tenant-saas
- OpenFGA organization-context authorization:
  https://openfga.dev/docs/modeling/organization-context-authorization
- OpenFGA agent authorization:
  https://openfga.dev/docs/modeling/agents

## OBSERVED

Backstage separates app/frontend, backend, plugins, modules and shared services. Frontend plugins encapsulate UI features while backend plugins are independently deployable and communicate over network boundaries.

Backstage explicitly supports splitting one backend into multiple deployments for scale and isolation.

Kubernetes multi-tenancy distinguishes namespace-style shared-control-plane isolation from stronger virtualized/dedicated control-plane isolation.

OpenFGA demonstrates organization-scoped authorization, user membership across multiple organizations, custom roles, group membership and agent principals.

## PROPOSAL — frontends should be role-specific projections

The Agent OS should not expose one giant universal dashboard.

Instead:

```text
Canonical API
    │
    ├── Personal Cockpit
    ├── Developer Console
    ├── Team Workspace
    ├── Organization Control Deck
    ├── Security Console
    ├── Knowledge / Research Console
    ├── Platform Operations Console
    └── Marketplace / Extension Console
```

Each UI is a projection over the same resource APIs and policy engine.

## PROPOSAL — backend should support deployment profiles

### Profile A — Personal/local

Single process or modular monolith.

Possible services:

- local API;
- local SQLite/PostgreSQL;
- local model router;
- local tool/MCP broker;
- local knowledge store;
- local workspace/sandbox manager.

Primary concerns:

- simplicity;
- offline operation;
- minimal RAM/CPU;
- easy backup;
- transparent token use;
- no multi-tenant complexity.

### Profile B — Developer workstation

Adds:

- Git/worktree integration;
- coding-agent runtime;
- IDE integrations;
- local + cloud model routing;
- test/evaluation services;
- artifact store;
- trace viewer.

### Profile C — Small team/server

Adds:

- organization/group model;
- shared agent/capability registry;
- centralized authentication;
- shared knowledge;
- shared workflows;
- approvals;
- team quotas;
- remote workers.

### Profile D — Organization

Adds:

- multi-team authorization;
- department ownership;
- policy service;
- secrets broker;
- audit;
- billing/cost accounting;
- notifications;
- managed registries;
- extension allowlists.

### Profile E — Enterprise/regulated

Adds:

- stronger tenant/project isolation;
- workload identity;
- federation;
- retention policies;
- compliance evidence;
- SIEM integration;
- regional/data-residency boundaries;
- dedicated control planes where required;
- enterprise SSO/SCIM;
- formal change control.

### Profile F — Managed Agent OS / SaaS

Adds:

- tenant provisioning;
- tenant billing;
- organization-context switching;
- per-tenant quotas;
- tenant admin;
- tenant-specific extension policies;
- noisy-neighbor protections;
- tenant-aware observability.

## Backend service map

Candidate services:

```text
Edge/API Gateway
Identity Service
Organization/Tenant Service
Authorization/Policy Service
Agent Registry
Capability Registry
Discovery Service
Task Service
Run/Execution Service
Workflow Service
Scheduler
Model Router
Token/Cost Service
MCP/Tool Broker
Marketplace/Catalog Service
Workspace/Sandbox Service
Knowledge Service
Memory Service
Artifact Service
Event Service
Audit Service
Approval Service
Notification Service
Evaluation Service
Observability/Telemetry Service
Secrets Broker
Node/Compute Service
Billing/Quota Service
Search Service
```

Not every deployment should run these as separate microservices.

**PROPOSAL:** default to a modular monolith for small deployments, then split services only when scale, isolation, security or ownership requires it.

## Frontend experience map

### Personal Cockpit

Optimize for:

- goals/tasks;
- chat/command input;
- current agents;
- local models;
- token/cost meter;
- knowledge;
- approvals;
- simple activity feed.

### Developer Console

Optimize for:

- repositories/worktrees;
- issue/task context;
- code diffs;
- test results;
- agent runs;
- model routing;
- tool calls;
- token/context use;
- terminal/IDE handoff.

### Team Workspace

Optimize for:

- shared projects;
- agent assignments;
- team tasks;
- approvals;
- artifacts;
- knowledge;
- reviews;
- cost budgets;
- agent availability.

### Organization Control Deck

Optimize for:

- departments/teams;
- agent registry;
- capability registry;
- policies;
- quotas;
- spend;
- model/provider configuration;
- extension governance;
- audit;
- health.

### Security Console

Optimize for:

- permission graph;
- secrets;
- high-risk tool calls;
- approvals;
- supply-chain state;
- MCP server trust;
- policy violations;
- audit trails;
- incident investigation.

### Knowledge / Research Console

Optimize for:

- sources;
- ingestion;
- citations;
- freshness;
- contradictory claims;
- RAG quality;
- memory promotion;
- research projects.

### Platform Operations Console

Optimize for:

- nodes;
- GPU/CPU;
- model runtimes;
- queues;
- workflows;
- service health;
- storage;
- backups;
- failover;
- distributed execution.

## API boundary

Frontends should not talk directly to arbitrary backend databases or agents.

Preferred flow:

```text
Frontend
   ↓
BFF / API Gateway
   ↓
Identity + policy
   ↓
Canonical Resource APIs
   ↓
Backend services
```

For complex frontends, research a Backend-for-Frontend layer to shape data without contaminating canonical core APIs.

## Plugin model

Research:

- frontend plugins;
- backend plugins;
- paired full-stack plugins;
- schema-driven UI extensions;
- sandboxed extensions;
- organization-specific extensions.

Backstage is useful as an architecture comparison because its frontend plugins, backend plugins, modules, extension points, and package boundaries explicitly separate these concerns.

## Multi-tenancy

Research at least:

- single user;
- multi-user single organization;
- multi-organization;
- partner/cross-organization sharing;
- managed SaaS;
- isolated regulated tenant.

Authorization must support:

- user may belong to several organizations;
- active organization context;
- group/team membership;
- organization roles;
- custom roles;
- agent principals;
- task-scoped grants;
- tenant-specific policies.

## Failure modes

- one frontend exposing controls the current principal should not see;
- BFF bypassing canonical policy checks;
- tenant context confused between browser tabs;
- cached data leaking across organization switches;
- cross-tenant search;
- shared model prompts leaking data;
- plugin frontend calling unapproved backend;
- organization-level role accidentally granting global platform privilege;
- distributed services disagreeing about active policy version.

## Research deliverables

- USER_PERSONAS.md
- FRONTEND_SURFACES.md
- BACKEND_SERVICE_MAP.md
- TENANCY_MODEL.md
- BFF_API_PATTERN.md
- FRONTEND_PLUGIN_CONTRACT.md
- BACKEND_PLUGIN_CONTRACT.md
- UI_PERMISSION_MODEL.md
- DEPLOYMENT_PROFILES.md
- reference architecture diagrams
- prototype implementation matrix
