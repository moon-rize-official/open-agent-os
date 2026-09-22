# Domain 61 — Digital Employees: Initial Findings

**Status:** RESEARCH IN PROGRESS  
**Date:** 2026-09-22

## Terminology caution

**OPEN QUESTION:** "Digital Employee" is a useful organizational metaphor but can mislead if treated as equivalent to a human employment relationship.

For Open Agent OS, use it narrowly for a **persistent role-bound agent identity with durable organizational state**, not as a legal or moral claim of personhood/employment status.

## PROPOSAL — persistent role surface

A persistent digital-worker-style agent may have:

- AgentDefinition
- persistent Principal identity
- organizational RoleDefinition
- manager/reporting references
- inbox/work queue
- goals/objectives
- schedule/availability policy
- project memberships
- memory scope
- knowledge scopes
- skills/capabilities
- tools
- permissions
- authority ceiling
- budget
- evaluation history
- audit history

## Distinguish from task agent

```text
Persistent role agent
  identity survives tasks
  organization membership persists
  memory/knowledge scopes persist
  has inbox and goals

Ephemeral task agent
  created for bounded work
  limited context/authority
  disposed after task/run
```

## Lifecycle

V1 lifecycle should support:

- provision
- activate
- suspend
- restrict
- reassign
- rotate credentials
- deprecate
- archive/offboard

Offboarding must revoke:

- workload credentials;
- tool grants;
- secret access;
- task leases;
- organization memberships;
- active sessions;
- delegated capabilities.

## Separation of duties

Persistent agents should not automatically review or approve their own consequential work.

## V1

Treat persistent agents as a composition of existing canonical resources rather than inventing a special privileged "employee" super-resource.

## FAILURE MODES

- memory leaking across role changes;
- stale permissions after reassignment;
- indefinite unattended inbox execution;
- goals persisting after policy changes;
- manager loops;
- misleading anthropomorphic UX hiding actual machine authority;
- inactive agents retaining credentials.

## OPEN QUESTIONS

- Should persistent agents have an explicit schedule resource or policy?
- How should role changes affect memory retention?
- Which lifecycle events require human approval?
