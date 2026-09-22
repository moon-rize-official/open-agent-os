# Agent & Department Resource Requirements Research Programme

**Status:** RESEARCH IN PROGRESS  
**Date:** 2026-09-22

## Mission

Research what every department, role family, agent archetype, and task needs to perform real work.

This programme covers more than legal rules or context documents.

For every agent/department, research:

- information and knowledge;
- structured datasets;
- live operational data;
- files and repositories;
- applications and software;
- tools and commands;
- MCP servers;
- APIs;
- databases;
- search systems;
- communication systems;
- credentials and secrets;
- compute and sandbox requirements;
- models;
- skills;
- memory;
- artifacts;
- workflows;
- approvals;
- observability;
- expected outputs.

## Resource layers

```text
Organization baseline
      +
Department resource pack
      +
Role-family pack
      +
Project pack
      +
Task-specific requirements
      +
Live environment discovery
      =
Provisioned Agent Workspace
```

## Requirement dimensions

Every resource requirement should answer:

- what is needed?
- why is it needed?
- required or optional?
- read or write?
- source/system?
- local or remote?
- sensitivity?
- freshness?
- trust level?
- network requirement?
- credential requirement?
- token/context impact?
- cost?
- allowed risk class?
- audit requirement?
- fallback if unavailable?

## Resource categories

### Knowledge

Examples:

- procedures;
- architecture;
- standards;
- product docs;
- customer docs;
- runbooks;
- research;
- policies;
- decisions;
- regulations.

### Structured data

Examples:

- CRM entities;
- project records;
- metrics;
- inventories;
- financial records;
- asset databases;
- issue trackers;
- HR records.

### Live data

Examples:

- system health;
- incidents;
- deployments;
- account status;
- service availability;
- current prices;
- current permissions;
- queue state.

### Files and artifacts

Examples:

- repositories;
- documents;
- spreadsheets;
- contracts;
- datasets;
- images;
- logs;
- builds;
- binaries;
- reports.

### Tools/software

Examples:

- shell;
- Git;
- IDE;
- browser;
- database client;
- test runner;
- infrastructure CLI;
- design software;
- analytics tools.

### Integrations

Examples:

- MCP servers;
- REST/GraphQL/gRPC APIs;
- webhooks;
- message queues;
- database connectors;
- SaaS connectors.

### Compute

Examples:

- local process;
- container;
- microVM;
- GPU;
- browser;
- remote workstation;
- build runner;
- isolated network environment.

### Models

Examples:

- general LLM;
- reasoning model;
- coding model;
- vision model;
- embedding model;
- reranker;
- image model;
- speech model.

### Skills

Examples:

- delegation;
- code review;
- research;
- deployment;
- incident response;
- citation;
- data analysis.

### Memory

Examples:

- project memory;
- user preferences;
- past decisions;
- prior incidents;
- long-running role state.

### Communication

Examples:

- inbox;
- chat;
- email;
- issue tracker;
- ticket queue;
- notification systems.

### Observability

Examples:

- logs;
- traces;
- metrics;
- token usage;
- cost;
- tool calls;
- security audit.

## Required outputs

Each role should define what it is expected to produce.

Examples:

- code;
- review;
- architecture decision;
- report;
- ticket;
- deployment;
- approval;
- design;
- incident timeline;
- dataset;
- knowledge entry.

## Provisioning model

A role profile should not hard-code all possible tools.

Preferred flow:

```text
Role requirements
      ↓
Capability registry
      ↓
Policy filter
      ↓
Available tools/services
      ↓
Compatibility filter
      ↓
Provision workspace
```

This lets different organizations satisfy the same role requirement with different software stacks.

## Example

A backend engineer may require:

```text
Needs:
- repository access
- issue tracker
- architecture/ADR knowledge
- language/build toolchain
- test runner
- database/schema access
- API specs
- Git
- isolated shell
- code search
- review workflow

Implementation A:
GitHub + PostgreSQL + JetBrains + local shell

Implementation B:
GitLab + MySQL + VS Code + remote dev container
```

The requirement remains portable even though the products differ.

## Deliverables

- resource requirement schema;
- department resource matrix;
- role-family resource overlays;
- provisioning algorithm;
- tool/integration taxonomy;
- output contract taxonomy;
- 1,548-archetype resource projection;
- compatibility mapping;
- missing-resource detection;
- resource-request workflow;
- least-privilege provisioning tests.
