# Domain 29 — Agent Registry: Initial Findings

**Status:** RESEARCH IN PROGRESS  
**Date:** 2026-09-22

## Reference patterns

- Backstage Software Catalog: centralized ownership/metadata catalog with versioned entities and relations.
- Kubernetes API resources: declarative objects plus observed status and watch semantics.
- A2A Agent Cards: discoverable server identity, capabilities, skills and supported interfaces.
- SPIFFE: verifiable runtime workload identity.

## OBSERVED

Backstage separates declarative entity metadata from runtime systems and scales the catalog pattern to large software estates.

A2A defines an Agent Card as the discovery surface for an agent server and supports well-known URI, curated registry/catalog, and direct configuration discovery.

## PROPOSAL

The Agent Registry should store **definitions and discoverable metadata**, not live process state as its sole source of truth.

Separate:

```text
AgentDefinition
    ↓
AgentInstance(s)
    ↓
Health / lease / runtime status
```

### Registry fields

- canonical ID
- version
- name
- owner
- organization/department/team
- role family
- declared capabilities
- required capabilities
- supported protocols/interfaces
- model/harness constraints
- knowledge/memory scopes
- authority ceiling
- risk classification
- cost/latency metadata
- compatibility constraints
- provenance
- attestation/signature metadata
- lifecycle state
- deprecation state

### Runtime projection

Live instances should publish:

- instance ID
- definition/version
- node
- current health
- availability
- active task count
- current model/harness
- last heartbeat
- lease expiry
- observed capabilities
- runtime policy state

## V1

Use a local-first registry capable of:

- file-backed declarative definitions;
- API-backed indexing/search;
- offline operation;
- signed/versioned definitions;
- runtime instance leases;
- health/availability separated from definition;
- export/import for federation later.

## FAILURE MODES

- stale registrations;
- version drift between definition and instance;
- healthy registry / dead runtime;
- duplicate IDs;
- capability overclaiming;
- revoked agent still cached by clients;
- registry poisoning;
- unauthorized edits to authority metadata.

## OPEN QUESTIONS

- Should an AgentDefinition be immutable per version?
- How should registries federate without trusting remote capability claims blindly?
- What attestation is required before a runtime instance can claim a definition?
