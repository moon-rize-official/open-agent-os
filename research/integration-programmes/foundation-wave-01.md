# Foundation Wave 01 — Resource, Registry and Organization Synthesis

**Domains:** 01, 29, 30, 31, 60, 61  
**Status:** RESEARCH IN PROGRESS  
**Date:** 2026-09-22

## Current synthesis

The first wave points toward a layered model:

```text
Organization Graph
      │
      ├── RoleDefinition
      │      │
      │      └── AgentDefinition
      │              │
      │              └── AgentInstance
      │
      ├── Principal
      └── Group / Task Team

Capability Registry
      │
      ├── provided by AgentDefinition
      ├── provided by Tool
      ├── provided by Model
      ├── provided by Node
      └── provided by Environment

Task
  ↓
Agent Discovery
  ↓
Policy Filter
  ↓
Health / Compatibility Filter
  ↓
Ranking
  ↓
AgentInstance lease
  ↓
Run
```

## Initial architecture position

### V1

- Use versioned, metadata-rich canonical resources.
- Use desired/observed state only where a controller/reconciler meaningfully exists.
- Keep definitions separate from runtime instances.
- Keep capability declaration separate from providers.
- Keep discovery separate from authorization.
- Keep organizational role separate from runtime identity.
- Model persistent digital-worker-style agents as composition, not a privileged special case.
- Use functional public role names.
- Prefer local-first registries with federation later.

## Cross-domain invariants

1. Stable identity must survive process restart.
2. Runtime identity must be cryptographically verifiable where crossing trust boundaries.
3. Registry metadata must not be treated as proof of health.
4. Capability discovery must not grant authority.
5. Organizational seniority must not imply infrastructure privilege.
6. Every selection/delegation should be explainable and auditable.
7. Persistent role agents must support clean offboarding.
8. The system should instantiate the smallest competent team, not the largest available swarm.

## Next experiments

- Build JSON Schemas for AgentDefinition, AgentInstance, Capability, OrganizationRole and Principal.
- Prototype deterministic agent discovery against the 1,548 public archetype registry.
- Add policy filtering and explainable selection records.
- Simulate stale registry data and expired leases.
- Test temporary team formation for software, infrastructure and research tasks.
- Add OpenTelemetry-compatible resource identity to Run/AgentInstance traces.
- Evaluate SPIFFE-compatible workload identity mapping for distributed instances.
