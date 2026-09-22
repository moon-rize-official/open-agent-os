# Domain 30 — Capability Registry: Initial Findings

**Status:** RESEARCH IN PROGRESS  
**Date:** 2026-09-22

## Reference patterns

- MCP tool/resource/prompt capability surfaces
- A2A Agent Cards and skills
- Backstage catalog entity metadata
- Kubernetes discovery and versioned API resources
- OpenTelemetry semantic conventions and entity naming

## OBSERVED

MCP 2026-07-28 keeps capability surfaces such as tools/resources/prompts and adds stronger caching and extension semantics while moving toward a stateless protocol core.

A2A Agent Cards describe identity, capabilities, skills and supported interfaces for discovery.

## PROPOSAL

Capability should be a first-class **declaration**, separate from the object that provides it.

```text
Capability
   ↑
providedBy
   ├── AgentDefinition
   ├── Tool
   ├── MCP Server
   ├── Model
   ├── Node
   └── Environment
```

### Capability fields

- ID / namespace / version
- human description
- input/output schema
- side-effect classification
- risk class
- required authority
- required environment
- data classifications accepted/produced
- latency/cost hints
- model/context requirements
- deterministic/non-deterministic flag
- idempotency expectations
- availability/health source
- provenance
- compatibility constraints

## Design rule

**Discovery must not imply authorization.**

A principal may discover that a capability exists but still be denied execution after policy evaluation.

## V1

Support:

- machine-readable capability descriptors;
- exact + semantic/tag search;
- provider relationships;
- version constraints;
- policy metadata;
- health projection;
- local caching for offline use.

## FAILURE MODES

- ambiguous capability names;
- stale provider mappings;
- incompatible schema versions;
- capability inflation/overclaiming;
- semantic search returning unsafe near-matches;
- hidden side effects;
- cost/latency metadata becoming stale.

## OPEN QUESTIONS

- How much behavioral semantics belong in the capability descriptor versus the Skill?
- Should capability compatibility use semantic versioning, schema hashes, or both?
- How should confidence in observed capability quality be represented?
