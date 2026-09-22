# Domain 31 — Agent Discovery: Initial Findings

**Status:** RESEARCH IN PROGRESS  
**Date:** 2026-09-22

## Evidence

A2A's Agent Card defines discovery metadata and supports well-known URLs, curated catalogs/registries, and direct configuration.

Backstage demonstrates a large-scale searchable metadata catalog model.

OpenFGA-style relationship models show why authorization should be evaluated independently from search/discovery.

## PROPOSAL

Agent selection should be a pipeline:

```text
Task requirements
      ↓
Capability candidate search
      ↓
Compatibility filtering
      ↓
Policy / authorization filtering
      ↓
Health / availability filtering
      ↓
Cost / latency / locality ranking
      ↓
Candidate selection
      ↓
Lease / reservation
```

## Ranking inputs

- capability match
- required skill match
- policy eligibility
- risk ceiling
- data-access eligibility
- health
- current load
- locality
- model availability
- context requirements
- historical evaluation quality
- latency
- expected cost
- trust/attestation
- user/project preferences

## Design rule

**Ranking and authorization are separate systems.**

A high-ranked agent that is not authorized must never be selected.

## Local/offline mode

The discovery service should work from a local registry snapshot and local health data without cloud access.

## FAILURE MODES

- stale health;
- cached permissions after revocation;
- ranking loops;
- overfitting to past benchmark scores;
- cheapest-agent bias degrading quality;
- selection of agents with incompatible tool/model versions;
- federation importing untrusted claims.

## V1

Start with deterministic filtering + transparent weighted ranking before introducing model-based discovery.

Every selection should emit an explainable decision record containing:

- candidates considered;
- filters applied;
- ranking factors;
- selected agent;
- rejected alternatives;
- policy decision references.

## OPEN QUESTIONS

- Should selection be deterministic by default?
- When should semantic matching be allowed to broaden declared capabilities?
- How should multi-agent team formation differ from single-agent discovery?
