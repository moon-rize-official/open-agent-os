# Information Selection for Agent Context

**Domain:** 40 Context Engineering  
**Status:** RESEARCH IN PROGRESS

## Research question

Given everything the organization knows, what is the smallest set of information that lets this agent complete this task correctly and safely?

## Proposed selector

```text
Task
  ↓
Required capabilities
  ↓
Agent / department profile
  ↓
Policy filter
  ↓
Source discovery
  ↓
Freshness filter
  ↓
Relevance ranking
  ↓
Sensitivity check
  ↓
Token budget
  ↓
Context package
```

## Scoring dimensions

Candidate information may be ranked by:

- task relevance;
- role relevance;
- source authority;
- freshness;
- confidence;
- dependency relationship;
- sensitivity;
- token size;
- expected value;
- duplication.

## Useful metric

Research an approximate:

```text
Information Value Density
=
Expected task utility
/
Tokens injected
```

This should not override mandatory safety/policy context.

## Department + role composition

A backend engineer should receive:

```text
Engineering department pack
+ implementation role pack
+ project architecture
+ relevant repository slices
+ issue/task contract
+ tests
+ required tools
```

not the full company corpus.

A security reviewer should receive a different projection over the same task.

## Dynamic information discovery

Agents should be able to identify missing information and request it explicitly.

Research:

- self-declared information gaps;
- retrieval plans;
- source authority constraints;
- uncertainty thresholds;
- escalation when information is inaccessible;
- preventing agents from broadening access simply because they request more context.

## Tests

- missing mandatory context;
- stale operational state;
- poisoned retrieval;
- sensitive overexposure;
- irrelevant context overload;
- duplicated information;
- contradictory sources;
- token budget exhaustion.
