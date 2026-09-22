# Domain 60 — Organizational Model: Initial Findings

**Status:** RESEARCH IN PROGRESS  
**Date:** 2026-09-22

## Source-derived design input

Pre-public research verified:

- 43 departments;
- 228 subdepartments;
- 1,332 structured role/person workspaces;
- a matrix model of departments, leads, specialist pools, and temporary task teams.

## PROPOSAL

Represent organization as a **graph with optional hierarchy**, not a rigid tree.

Useful relationship types:

- belongsTo
- reportsTo
- manages
- owns
- reviews
- approves
- delegatesTo
- supports
- providesCapabilityTo
- memberOf
- temporaryMemberOf

A hierarchy is one projection of this graph.

## Role vs instance

```text
OrganizationRoleDefinition
        ↓
AgentDefinition / HumanRole
        ↓
AgentInstance / HumanPrincipal
```

Permanent roles describe responsibility and authority boundaries. Runtime instances execute work.

## Separation of dimensions

Do not merge these concepts:

- capability — what an actor can do;
- authority — what an actor may do;
- responsibility — what an actor is expected to own;
- accountability — who answers for the result;
- assignment — what work is currently allocated.

## Mixed human/agent organization

The same organizational graph should support both humans and agents as Principals while preserving different execution and accountability semantics.

## V1

Support:

- Organization
- Department/Group
- RoleDefinition
- Principal membership
- reporting relationships
- ownership relationships
- review/approval relationships
- temporary task-team membership

Do not encode all organization semantics only in prompts.

## FAILURE MODES

- circular reporting/delegation;
- orphaned ownership;
- excessive hierarchy slowing work;
- responsibility without authority;
- authority without accountability;
- permanent giant swarms;
- agents self-promoting into higher-authority roles.

## OPEN QUESTIONS

- Which organizational relationships need enforcement versus documentation only?
- Should Department and Group be separate canonical kinds?
- How should temporary task teams be represented: Group resources, Run scopes, or both?
