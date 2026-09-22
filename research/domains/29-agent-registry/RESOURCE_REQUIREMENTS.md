# Resource Requirements in the Agent Registry

**Domain:** 29 Agent Registry  
**Status:** RESEARCH IN PROGRESS

The Agent Registry should describe more than an agent's name and capabilities.

An AgentDefinition should be able to declare:

- what it knows;
- what data it needs;
- what live systems it needs;
- what tools it needs;
- what integrations it needs;
- what compute it needs;
- what models it supports/requires;
- what skills it requires;
- what it may write;
- what outputs it produces.

## Proposed relationship

```text
AgentDefinition
      │
      ├── providesCapability
      └── requiresResource
                 │
                 ▼
          Capability Registry
                 │
                 ▼
          Approved Provider
```

This allows a public agent archetype to remain portable across organizations.

## Example

```yaml
id: backend-engineer
requires:
  - category: tool
    capability: version-control
    necessity: REQUIRED
    access: write

  - category: tool
    capability: test-runner
    necessity: REQUIRED
    access: execute

  - category: knowledge
    capability: project-architecture
    necessity: REQUIRED
    access: read
```

One organization may map these to GitHub + pytest. Another may map them to GitLab + Maven.

## Discovery impact

Agent Discovery must check not only whether an agent claims the capability to perform a task, but whether the required resources can actually be provisioned in the current environment.
