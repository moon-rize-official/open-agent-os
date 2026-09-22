# Public Agent Archetype Library

**Status:** PROPOSAL

The historical AI-FLEET research verified a separate corpus of **1,332 role/person workspaces**. That exact registry is not currently available as a public-safe source artifact.

To preserve the useful design space without pretending to reproduce the original registry, Open Agent OS provides a deterministic public archetype generator.

## Generator size

The generator combines:

- **43 department archetypes**
- **6 role families**
- **6 capability levels**

```text
43 × 6 × 6 = 1,548 agent archetypes
```

This exceeds the requested 1,400+ role knowledge target while remaining transparent about provenance.

## Role families

1. strategy-planning
2. analysis-research
3. implementation-delivery
4. operations-reliability
5. verification-governance
6. knowledge-coordination

## Capability levels

- L0 utility worker
- L1 specialist
- L2 senior specialist
- L3 team lead
- L4 department lead
- L5 executive coordinator

## Important warning

This is a **catalog**, not a swarm-size recommendation.

A production Agent OS should instantiate only the smallest competent set of agents required for a task.

Run:

```bash
python scripts/generate-agent-archetypes.py
```

The script writes JSON, CSV and summary outputs under `generated/`.
