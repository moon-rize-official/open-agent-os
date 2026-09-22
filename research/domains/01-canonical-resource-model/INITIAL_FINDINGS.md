# Domain 01 — Canonical Resource Model: Initial Findings

**Status:** RESEARCH IN PROGRESS  
**Date:** 2026-09-22

## Evidence reviewed

Primary/reference sources in this initial pass:

- Kubernetes Objects and API Concepts: https://kubernetes.io/docs/concepts/overview/working-with-objects/
- Kubernetes Custom Resources: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
- Backstage Catalog entity model: https://backstage.io/docs/features/software-catalog/descriptor-format/
- Backstage entity references: https://backstage.io/docs/features/software-catalog/references/
- OpenTelemetry Resource identity: https://opentelemetry.io/docs/specs/otel/resource/
- SPIFFE identity: https://spiffe.io/docs/latest/spiffe-specs/spiffe-id/
- MCP 2026-07-28 release notes/spec changes: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- A2A Agent Card specification: https://github.com/a2aproject/A2A/blob/main/docs/specification.md

## OBSERVED

Kubernetes models persistent API resources using versioned kinds, metadata, desired-state `spec`, and observed-state `status`. Objects have stable names and UIDs, support watch/list semantics, and can expose subresources for finer authorization.

Backstage adapts a Kubernetes-like entity shape for catalog objects and uniquely identifies entities by kind, namespace, and name.

OpenTelemetry treats resource identity as the pivot for correlating telemetry from the same observed entity.

SPIFFE separates human-readable/runtime resource naming from cryptographically verifiable workload identity.

## INFERENCE

An Agent OS benefits from separating:

1. **declarative resources** — desired state and policy;
2. **runtime resources** — observed instances and health;
3. **execution records** — individual attempts, calls, turns and events;
4. **artifacts** — durable outputs;
5. **security principals** — authenticated actors/workloads.

Trying to make every runtime event a first-class mutable resource would make the API noisy and harder to reason about.

## PROPOSAL — V1 first-class resources

The following should be first-class, addressable, versioned resources:

- Organization
- Principal
- AgentDefinition
- AgentInstance
- Session
- Task
- Run
- Artifact
- Approval
- Workspace
- Capability
- Workflow
- Node
- KnowledgeSource
- Skill
- Policy

## PROPOSAL — records/subresources

These are better represented as immutable or append-oriented records/subresources in V1:

- Turn
- Event
- ToolCall
- ModelCall
- MemoryRecord
- Checkpoint

A Checkpoint may later become a first-class resource if cross-run retention, migration, or lifecycle management requires independent ownership.

## PROPOSED common envelope

```yaml
apiVersion: agentos.dev/v1alpha1
kind: AgentDefinition
metadata:
  id: 01J...
  name: backend-specialist
  namespace: default
  labels: {}
  annotations: {}
  generation: 7
spec:
  # desired state
status:
  # observed state
```

## Design requirements

Every first-class resource should define:

- globally stable identity;
- human-readable name;
- namespace/scope;
- owner/parent references;
- API version;
- schema version;
- desired vs observed state where meaningful;
- lifecycle state;
- creation/update timestamps;
- deletion/finalization semantics where external cleanup exists;
- provenance;
- authorization boundary;
- observability identity.

## OPEN QUESTIONS

- Should Session own Task, or should both belong directly to a Project/Workspace?
- Should Approval bind to Run, Event, Action, or a specific proposed state transition?
- Should Checkpoint be a first-class resource in V1?
- Is MemoryRecord always append-only, or can promoted memories become independently versioned resources?
- What is the minimum canonical relationship graph required before implementation?
