# Open Agent OS

> **Vendor-neutral research, specifications, reference architectures, and implementation guides for building modular Agent OS / AI OS platforms.**

Open Agent OS is an open-source knowledgebase for engineers, researchers, and teams designing systems where **models, agents, harnesses, tools, memory, knowledge, workflows, sandboxes, compute, storage, policies, and user interfaces can evolve independently behind stable contracts**.

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Research Domains](https://img.shields.io/badge/research%20domains-80-6f42c1)](research/domains/README.md)
[![Status](https://img.shields.io/badge/status-research%20foundation-orange)](ROADMAP.md)

## Why this exists

The agent ecosystem is moving quickly, but most projects optimize for a particular framework, model provider, runtime, or workflow. Open Agent OS asks a different question:

**What stable abstractions are needed to build an Agent OS whose components remain replaceable?**

The project studies the full stack:

- canonical resources and lifecycle semantics;
- agent runtimes and harness adapters;
- model abstraction and routing;
- multi-agent orchestration and durable workflows;
- eventing, checkpoints, recovery, and provenance;
- memory, knowledge, RAG, ingestion, and context engineering;
- skills, tools, MCP, browser/computer use, and coding agents;
- identity, authorization, policy, secrets, sandboxing, and governance;
- registries, discovery, scheduling, compute fabric, networking, and storage;
- observability, evaluation, testing, benchmarking, and cost;
- APIs, SDKs, plugins, CLI/TUI, GUI, IDEs, and marketplaces;
- offline-first, high-availability, multi-tenant, and distributed deployments.

## Start here

- **Build your own Agent OS:** [Getting Started](docs/getting-started/build-your-own-agent-os.md)
- **Architecture:** [Reference Architecture](docs/architecture/reference-architecture.md)
- **Kernel boundary:** [What belongs in the Agent OS kernel?](docs/architecture/kernel-boundary.md)
- **Research:** [80-domain programme](research/domains/README.md)
- **Wiki:** [Wiki source](wiki/Home.md)
- **Roadmap:** [ROADMAP.md](ROADMAP.md)
- **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md)


## Agent organization knowledge

Open Agent OS includes a public, reusable agent-organization corpus derived from earlier pre-public research and clearly separated from new proposals.

- **Pre-public verified corpus:** 43 departments, 228 subdepartments, and **1,332 role/person workspaces**
- **Public archetype registry:** **1,548 generated agent archetypes**
- **Capability model:** L0–L5 capability levels kept separate from operational authority
- **Risk model:** R0–R4 action classes
- **Organization model:** permanent departments + leads + specialist pools + temporary task teams
- **Skills knowledge:** prior corpus reports **440 reusable skills**

Start here:

- [Agent Organization Model](docs/agents/README.md)
- [Role Workspace Contract](docs/agents/role-workspace-contract.md)
- [Capability, Authority and Risk](docs/agents/capability-authority-risk.md)
- [Skills and Capabilities](docs/agents/skills-and-capabilities.md)
- [Public 1,548-Agent Archetype Library](docs/agents/archetype-library.md)
- [Generated JSON Registry](generated/agent-archetypes.json)
- [Generated CSV Registry](generated/agent-archetypes.csv)

The 1,548-entry registry is a **design-space catalog**, not a recommendation to run 1,548 agents simultaneously. The default operating principle remains: use the smallest competent team that can complete the task safely.

## Research discipline

Important statements are classified as:

| Label | Meaning |
|---|---|
| **OBSERVED** | Directly supported by a cited implementation, specification, paper, source repository, benchmark, or production report |
| **INFERENCE** | Synthesis derived from multiple observations |
| **PROPOSAL** | A design recommendation for Open Agent OS |
| **ALTERNATIVE** | A credible competing design |
| **REJECTED** | A considered design that is not currently recommended |
| **OPEN QUESTION** | Evidence is insufficient or experimentation is still required |
| **V1** | Proposed minimum baseline |
| **FUTURE** | Intentionally deferred |

Marketing claims are not treated as observed implementation evidence.

## Working architecture

```text
Human / Organization
        |
        v
   Control Plane
        |
  +-----+--------------------------+
  |     |            |             |
Registry Scheduler  Policy      Workflow
  |     |            |             |
  +-----+------------+-------------+
        |
        v
    Agent Runtime
        |
 +------+------+------+-------+---------+
 |      |      |      |       |         |
Harness Model Skills Tools  Memory   Knowledge
 |      |      |      |       |         |
 +------+------+------+-------+---------+
        |
        v
 Workspace / Sandbox
        |
        v
   Compute Fabric
        |
        v
 Events + Artifacts + Provenance
        |
        v
 Evaluation + Approval + Audit
```

The architecture is intentionally a **research hypothesis**, not a frozen standard.

## Public-safety boundary

This repository is for generalizable public research and specifications. Do **not** publish credentials, private infrastructure details, customer information, proprietary source material, exported private chats, or third-party copyrighted documentation.

## License

Original project content is intended to be licensed under **Apache-2.0**. Third-party projects, specifications, models, data, and trademarks remain under their own licenses and terms.
