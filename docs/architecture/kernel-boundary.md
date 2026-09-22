# Agent OS Kernel Boundary

**Status: PROPOSAL / OPEN QUESTION**

The central architectural question is not “which framework should we use?” but:

> Which semantics must remain stable when implementations are replaced?

## Candidate kernel responsibilities

The current research hypothesis considers these strong kernel candidates:

- canonical resource identity;
- execution lifecycle semantics;
- principal/identity semantics;
- capability brokerage;
- policy decision/enforcement boundaries;
- event/log contract;
- checkpoint/recovery contract;
- artifact/provenance contract;
- extension/plugin ABI or API.

## Likely userland

These are strong candidates to remain replaceable adapters:

- model providers;
- agent harnesses;
- vector databases;
- RAG implementations;
- memory backends;
- workflow engines;
- browsers;
- sandboxes;
- IDEs;
- UI frameworks;
- observability backends.

## Test for kernel inclusion

A concern should move into the kernel only if replacing it would otherwise break interoperability, security invariants, state recovery, or canonical identity across the rest of the system.

This is intentionally not frozen. Alternative boundaries should be proposed through RFCs.
