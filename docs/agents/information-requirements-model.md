# Agent Information Requirements Model

**Status:** PROPOSAL

An agent should receive the **minimum sufficient information** required for the current task.

## Context assembly

```text
Principal
   ↓
AgentDefinition
   ↓
Department Pack
   ↓
Role Pack
   ↓
Project Pack
   ↓
Task Contract
   ↓
Policy Filter
   ↓
Freshness Filter
   ↓
Token Budgeter
   ↓
Effective Context
```

## Universal information every agent needs

Usually required:

- identity;
- role;
- mission;
- current task;
- authority boundary;
- risk class;
- available capabilities;
- expected output;
- applicable policy;
- escalation path;
- provenance requirements;
- resource/token budget.

## Information every agent does NOT automatically need

Examples:

- all organization secrets;
- all customer records;
- all HR data;
- unrestricted production credentials;
- complete conversation history;
- full knowledgebase dumps;
- every tool schema;
- unrelated project memory;
- raw legal files unrelated to the task.

## Freshness classes

| Class | Example | Guidance |
|---|---|---|
| F0 Static | definitions, historical standards | refresh on version change |
| F1 Slow | architecture, policies | hours/days |
| F2 Active | project state, issue status | minutes/hours |
| F3 Live | deployments, incidents, permissions | seconds/minutes |
| F4 Transactional | balances, authorization decisions | fetch at action time |

## Sensitivity classes

| Class | Meaning |
|---|---|
| S0 | public |
| S1 | internal |
| S2 | confidential |
| S3 | restricted |
| S4 | highly restricted / regulated |

Access to information is determined by policy, not by role name alone.

## Token priority

| Priority | Meaning |
|---|---|
| P0 | must fit |
| P1 | strongly relevant |
| P2 | retrieve when relevant |
| P3 | omit unless explicitly needed |

## Failure behavior

If required information is unavailable, the agent should not invent it.

Possible outcomes:

- block;
- ask for retrieval;
- fetch live;
- escalate;
- continue with explicitly degraded confidence.

## Context manifest

Every ModelCall should be able to explain where context came from:

```text
Task            P0   720 tokens
Policy          P0   910
Role            P1   400
Project state   P1 1,100
Knowledge       P2 2,400
Memory          P2   500
Tools           P1 1,800
```

This enables token optimization and information-governance audits.
