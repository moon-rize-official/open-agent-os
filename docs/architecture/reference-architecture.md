# Reference Architecture

Open Agent OS uses a six-plane reference model for research and comparison.

## 1. Experience Plane

Human and developer interfaces:

- Web/GUI
- CLI/TUI
- IDE integrations
- API/SDK
- mobile and notification surfaces

## 2. Control Plane

- orchestration
- registry
- scheduling
- routing
- identity
- authorization
- policy
- workflow coordination
- approvals

## 3. Agent Plane

- runtime
- harness adapters
- context assembly
- planning
- delegation
- memory access
- review

## 4. Capability Plane

- tools
- MCP
- browser
- computer use
- shell
- Git
- external APIs

## 5. Data Plane

- knowledge
- retrieval
- memory
- events
- artifacts
- provenance
- audit
- search

## 6. Infrastructure Plane

- models
- CPU/GPU
- nodes
- containers/VMs
- networking
- storage
- secrets
- observability
- backup/recovery

## Design objective

Components inside a plane may still be independently replaceable. The plane model is an organizational device, not a deployment requirement.
