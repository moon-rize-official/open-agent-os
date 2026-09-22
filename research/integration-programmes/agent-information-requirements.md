# Agent & Department Information Requirements Research Programme

**Status:** RESEARCH IN PROGRESS  
**Date:** 2026-09-22

## Mission

Determine what information each agent, role family, department, team, and task actually needs in order to perform safely and effectively.

The system should answer:

- What information is required?
- Who is allowed to access it?
- Where does it come from?
- How authoritative is it?
- How fresh must it be?
- How long may it be retained?
- Should it enter context, memory, retrieval, or only be fetched on demand?
- What must never be exposed by default?
- How many tokens should be spent carrying it?

## Core principle

Do **not** give every agent the entire organization knowledgebase.

Use composable information profiles:

```text
Universal Baseline
      +
Department Knowledge Pack
      +
Role-Family Knowledge Pack
      +
Project Context
      +
Task Contract
      +
Live Operational Data
      +
Authorized Memory
      =
Effective Agent Context
```

## Information classes

Research and formalize at least:

1. **Identity & role**
   - role definition
   - department/team
   - manager/owner
   - capability level
   - authority ceiling
   - responsibilities

2. **Task contract**
   - objective
   - constraints
   - acceptance criteria
   - deadline
   - dependencies
   - expected output
   - risk class

3. **Project context**
   - project goals
   - architecture
   - current state
   - issues
   - milestones
   - decisions
   - artifacts

4. **Organization context**
   - strategy
   - policies
   - departments
   - reporting relationships
   - terminology
   - approved standards

5. **Domain knowledge**
   - technical documentation
   - regulations
   - procedures
   - product knowledge
   - research sources
   - customer context

6. **Operational state**
   - service health
   - queues
   - inventories
   - deployments
   - incidents
   - workloads
   - current environment

7. **Tool & capability knowledge**
   - available tools
   - MCP servers
   - APIs
   - schemas
   - side effects
   - permissions
   - usage constraints

8. **Memory**
   - prior decisions
   - lessons learned
   - user preferences
   - project memory
   - role memory
   - organization memory

9. **Evidence & provenance**
   - sources
   - citations
   - source freshness
   - confidence
   - contradictions

10. **Security/compliance**
    - applicable policy
    - data classification
    - legal/regulatory constraints
    - approval requirements
    - retention rules

11. **Resource/budget**
    - token budget
    - model budget
    - compute budget
    - time budget
    - monetary budget

## Information profile metadata

Every information requirement should support:

```yaml
id:
required: true
source:
source_authority:
sensitivity:
freshness:
max_age:
retention:
access_policy:
provenance_required:
token_priority:
delivery:
  - always
  - retrieve
  - fetch-live
  - memory
  - artifact-reference
update_trigger:
fallback_behavior:
```

## Delivery modes

### Always-in-context

Only for small, critical information such as:

- current task;
- safety policy;
- authorization constraints;
- output schema.

### Retrieve-on-demand

Use for:

- documentation;
- historical decisions;
- large knowledge collections;
- standards;
- previous incidents.

### Fetch-live

Use when stale data is dangerous:

- infrastructure state;
- prices;
- schedules;
- service health;
- permissions;
- regulations that may have changed.

### Memory

Use only for information that is genuinely useful across tasks and allowed to persist.

### Artifact reference

Prefer stable IDs/paths over copying large files into every prompt.

## Research dimensions

For every agent/department profile research:

- required knowledge;
- optional knowledge;
- prohibited-by-default information;
- source systems;
- freshness SLA;
- confidence/source quality;
- privacy classification;
- retention;
- token cost;
- failure if missing;
- failure if stale;
- failure if overexposed.

## Deliverables

- InformationProfile schema
- DepartmentKnowledgePack schema
- RoleKnowledgePack schema
- Agent context assembly rules
- freshness policy
- token-priority model
- sensitivity model
- 43-department information map
- role-family information overlays
- example profiles
- tests for overexposure, staleness and missing context
