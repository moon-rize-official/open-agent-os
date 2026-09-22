# Provider Mapping Research

**Status:** INITIAL VERIFIED MAP  
**Date:** 2026-09-22

This directory maps portable Agent OS capability requirements to real implementations.

The mapping is intentionally **non-exclusive** and **non-prescriptive**. A provider appearing here means it is a concrete implementation worth testing, not that Open Agent OS endorses it as the default.

## Design rule

Public agent packs request capabilities:

```text
version-control
secrets-manager
workflow-engine
observability
vector-search
model-serving
developer-portal
component-explorer
mcp-registry
```

Organizations map those capabilities to approved providers.

## Initial verified examples

### Version control / software collaboration

- **GitHub** — hosted repositories, Issues, Actions and organization collaboration.
  - Repositories: https://docs.github.com/en/repositories
  - Issues: https://docs.github.com/en/issues
  - Actions: https://docs.github.com/en/actions/get-started/understand-github-actions

- **GitLab Self-Managed** — self-managed source collaboration, administration and runners.
  - https://docs.gitlab.com/
  - https://docs.gitlab.com/administration/

- **Gitea** — self-hosted Git service with code review, collaboration, package registry and CI/CD.
  - https://docs.gitea.com/1.23/

- **Local Git** — offline-capable baseline when no remote forge is required.

### Secrets management

- **OpenBao** — identity-based secrets/encryption system; supports authentication, authorization and auditing.
  - https://openbao.org/docs/what-is-openbao/
  - https://openbao.org/docs/

- **HashiCorp Vault** — centralized secrets, dynamic credentials, identity/authentication and audit.
  - https://developer.hashicorp.com/vault/docs

### Workflow / durable execution

- **Temporal** — open-source durable execution platform designed to resume workflow execution across crashes and outages.
  - https://docs.temporal.io/

Additional workflow systems should be researched and benchmarked separately rather than treated as equivalent to durable execution engines.

### Observability

- **OpenTelemetry** — vendor-neutral telemetry framework for traces, metrics and logs.
  - https://opentelemetry.io/docs/

- **Grafana ecosystem** — visualization/observability tooling across metrics, logs, traces and incident workflows.
  - https://grafana.com/docs/

### Catalog / developer portal

- **Backstage** — open-source developer portal framework with centralized catalog, documentation, templates and plugin architecture.
  - https://backstage.io/docs/overview/what-is-backstage/
  - https://backstage.io/docs/features/software-catalog/

### Design system / component explorer

- **Storybook** — component development/documentation environment supporting design-system documentation and component testing.
  - https://storybook.js.org/docs/

### Relational data

- **PostgreSQL** — general-purpose relational database suitable for canonical metadata, configuration and transactional state depending on architecture.
  - https://www.postgresql.org/docs/

### Vector / semantic search

- **Qdrant** — vector and semantic search engine with local/self-hosted operation and edge/offline options.
  - https://qdrant.tech/documentation/

### Model serving

- **vLLM** — open-source LLM inference and serving engine with production/deployment, tool-calling, structured output and observability examples.
  - https://docs.vllm.ai/en/stable/

Local model runtimes should be compared on model compatibility, hardware support, batching, KV-cache behavior, tool calling, structured output, observability and operational complexity.

### MCP registry

- **Official MCP Registry** — community-driven metadata/discovery registry for MCP servers.
  - https://registry.modelcontextprotocol.io/docs

## Mapping dimensions

Each provider mapping should eventually record:

- capability;
- provider/project;
- deployment: local / self-hosted / cloud / hybrid;
- open-source status and license;
- offline capability;
- API/protocol;
- authentication;
- authorization;
- multi-tenancy;
- HA options;
- observability;
- backup/restore;
- extension/plugin model;
- resource requirements;
- compatibility constraints;
- security notes;
- maintenance/release freshness;
- migration/export support;
- pricing class where relevant;
- source URLs and last verification date.

## Next step

Build provider matrices per capability and test them against the 43 department packs and 1,548 generated profiles.
