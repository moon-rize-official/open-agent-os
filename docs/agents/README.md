# Agent Organization Model

**Status:** OBSERVED + INFERENCE + PROPOSAL  
**Source class:** AI-FLEET PRIOR RESEARCH

This document captures the reusable organizational knowledge distilled from the earlier AI-FLEET agent-company research. It is intentionally generalized for public use.

## 1. Historical corpus

**OBSERVED:** the prior generated corpus contained:

- **43 departments**
- **228 subdepartments**
- **1,332 role/person workspaces**
- **25,901 files**

Each role workspace was designed as more than a prompt. It had separate surfaces for agent definition, tools, MCP, knowledge, memory, permissions, workflows, prompts, reviews, audit, inbox, and outputs.

The exact historical registry is not reproduced here. This public repository instead preserves the architecture and turns it into reusable schemas, examples, and generators.

## 2. Matrix organization

**OBSERVED:** the earlier organization used five layers:

```text
ORGANIZATION
    ↓
DEPARTMENTS
    ↓
TEAM LEADS
    ↓
SPECIALIST POOLS
    ↓
TEMPORARY TASK TEAMS
```

Permanent departments own capabilities. Leads coordinate. Specialists provide narrow expertise. Temporary teams are assembled for a task.

The operating rule is:

> Use the smallest competent team capable of completing the task safely.

That rule is more important than maximizing agent count.

## 3. Durable lead archetypes

The source organization used durable named leads as examples:

| Archetype | Primary role |
|---|---|
| Hermes | Chief coordinator / task router |
| Themis | Governance and policy authority |
| Athena | Engineering architecture / product strategy |
| Hephaestus | Implementation and automation lead |
| Daedalus | Systems/platform architecture |
| Atlas | Read-mostly infrastructure inventory |
| Aegis | Security engineering lead |
| Argus | Independent verification and audit |
| Mnemosyne | Knowledge/memory governance |
| Apollo | Research and external intelligence |
| Calliope | Documentation and structured communication |
| Orpheus | Creative direction |

**PROPOSAL:** implementations should treat these as examples of durable role identities, not required names.

## 4. Specialist pools

Specialists should be capability workers, not elaborate personalities.

Examples from the prior organization include:

- Engineering: backend, frontend, API, database, Python, TypeScript, Go, Rust, testing, performance, integration, mobile.
- Platform: deploy, CI, image building, configuration management, infrastructure-as-code, containers, Kubernetes, network, DNS, backup, observability.
- Security: application security, cloud security, host security, network security, IAM, secrets, vulnerability, threat modeling, forensics, incident security.
- Knowledge: research, source validation, curation, documentation, taxonomy, knowledge graph, RAG, embeddings, archiving, summarization.
- Product/creative: product, UX, UI, brand, content, copy, video, audio, graphics, accessibility.

## 5. Independent verification

**OBSERVED:** the creator of a consequential artifact should normally not be the final authority declaring it correct.

A typical flow:

```text
Architecture/Plan
      ↓
Implementation
      ↓
Independent Verification
      ↓
Security Review
      ↓
Governance Check
      ↓
Completion
```

Open Agent OS treats independent review as a reusable orchestration pattern.

## 6. Capability levels

The source model separated capability/seniority into six levels:

| Level | Meaning |
|---|---|
| L0 | Utility worker |
| L1 | Specialist |
| L2 | Senior specialist |
| L3 | Team lead |
| L4 | Department lead |
| L5 | Executive coordinator |

Higher capability can affect task complexity, delegation, context budget, and review responsibility.

It **must not automatically grant infrastructure privilege**.

## 7. Authority is separate from capability

An architect may be highly capable but read-only. A narrower deployment worker may have controlled mutation rights.

This gives two independent dimensions:

```text
Capability Level
+
Operational Authority
```

See [Capability, Authority and Risk](capability-authority-risk.md).

## 8. Dynamic task teams

Useful patterns include:

### Feature team
- Lead: architecture/product role
- Builder: implementation role
- Specialists: domain-specific workers
- Verifier: independent review role

### Infrastructure change team
- Lead: systems/platform role
- Inventory: read-only state collector
- Builder: automation/deployment role
- Security: security reviewer
- Verifier: independent reviewer
- Governance: policy authority

### Research team
- Lead: research role
- Members: researchers/source validators
- Synthesis: architecture/domain expert
- Knowledge: curator/provenance role

### Incident team
- Coordinator
- Incident lead
- Diagnostics
- Security
- Verification
- Timeline/knowledge
- Governance

## 9. Public archetype library

The historical corpus verified a 1,332-workspace organization. Open Agent OS adds a separate **PROPOSAL** generator that produces **1,548 public agent archetypes** from:

- 43 public department archetypes
- 6 role families
- 6 capability levels

This is a design-space catalog, **not a recommendation to run 1,548 agents at once**.

See [Public Agent Archetype Library](archetype-library.md).
