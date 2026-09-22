# Agent Resource Requirements Model

**Status:** PROPOSAL

An AgentDefinition should declare what it needs without requiring a specific vendor.

## Example

```yaml
resources:
  knowledge:
    - capability: software-architecture
      required: true

  data:
    - capability: project-issue-data
      access: read-write

  tools:
    - capability: version-control
      access: read-write
    - capability: test-execution
      access: execute

  integrations:
    - capability: issue-tracker

  compute:
    sandbox: isolated-shell

  models:
    - capability: code-reasoning

  communication:
    - capability: task-inbox

  observability:
    - capability: run-tracing
    - capability: token-accounting
```

## Why capability-based requirements?

A public Agent OS should not require one product.

For example:

```text
version-control
    ├── GitHub
    ├── GitLab
    ├── Gitea
    └── local Git
```

The role requests `version-control`; the organization chooses an approved provider.

## Requirement states

- REQUIRED
- PREFERRED
- OPTIONAL
- PROHIBITED

## Access modes

- metadata
- read
- write
- execute
- administer
- approve

## Runtime provisioning

```text
AgentDefinition
     ↓
Resource requirements
     ↓
Organization policy
     ↓
Resource inventory
     ↓
Provider compatibility
     ↓
Least-privilege grant
     ↓
Workspace provisioning
```

## Missing resources

If a required resource cannot be provided:

- block;
- find alternative provider;
- request installation;
- request approval;
- delegate to a different agent;
- continue in degraded mode only if explicitly allowed.

## Audit

Provisioning should record:

- requirement;
- selected provider;
- granted scope;
- credential identity;
- grant duration;
- approving policy;
- revocation event.
