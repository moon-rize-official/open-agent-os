# Agent Role Workspace Contract

**Status:** PROPOSAL derived from prior role-workspace structure

A reusable agent role should be modeled as a structured workspace rather than one monolithic prompt.

## Workspace surfaces

```text
Role/
├── README.md
├── agent/
│   ├── agent.md
│   └── agent.yaml
├── tools/
│   ├── TOOLS.md
│   └── tools.yaml
├── mcp/
│   ├── MCP.md
│   └── mcp-servers.yaml
├── knowledge/
│   ├── KNOWLEDGE.md
│   └── sources.yaml
├── memory/
│   ├── MEMORY.md
│   └── memory-policy.yaml
├── permissions/
│   ├── PERMISSIONS.md
│   └── permissions.yaml
├── workflows/
├── prompts/
├── reviews/
├── audit/
├── inbox/
└── outputs/
```

## Why split the workspace?

The separation allows independent versioning and policy for:

- identity and role intent;
- tools and side effects;
- MCP/integration surfaces;
- knowledge sources;
- memory retention/promotion;
- permissions;
- workflows;
- prompt projections;
- review requirements;
- audit evidence;
- incoming work;
- durable outputs.

## Canonical role record

```yaml
id: agent-example
version: 1.0.0
organization:
  department: Engineering
  team: Backend
role:
  family: implementation-delivery
  capability_level: L2
mission: Implement bounded backend changes with tests and evidence.
capabilities:
  - code-generation
  - debugging
  - testing
authority:
  max_risk: R2
  production_mutation: false
tools:
  allow: [git, test-runner]
mcp:
  allow: []
knowledge:
  sources: []
memory:
  scope: project
  retention: bounded
permissions:
  default: deny
reviews:
  independent_review_required: true
audit:
  required: true
```

The role record should be declarative enough to project into multiple harnesses.
