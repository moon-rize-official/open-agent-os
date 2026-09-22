# Backend Service Map

**Status:** PROPOSAL

Open Agent OS should define service boundaries without requiring each boundary to become a separately deployed microservice.

## Control-plane services

- Identity
- Organization / Tenant
- Authorization
- Policy
- Registry
- Discovery
- Scheduler
- Workflow
- Approval
- Configuration

## Agent/runtime services

- Agent Runtime
- Harness Adapter Manager
- Run / Execution
- Session
- Workspace
- Sandbox
- Tool / MCP Broker
- Model Router
- Node / Compute

## Data/intelligence services

- Knowledge
- Ingestion
- Search
- RAG
- Memory
- Artifact
- Provenance
- Context Assembly

## Operations services

- Event Bus / Event Store
- Audit
- Observability
- Evaluation
- Token / Cost Accounting
- Quota / Budget
- Notification
- Backup / Restore

## Ecosystem services

- Marketplace / Catalog
- Plugin Manager
- MCP Registry Adapter
- Skill Registry
- Schema Registry
- Compatibility Service

## Deployment rule

```text
Small system:
modular monolith

Growing team:
split high-load / high-risk services

Enterprise:
isolate by trust, scale, data residency and ownership
```

Avoid microservices by default. Service boundaries are architectural contracts; deployment boundaries are operational choices.
