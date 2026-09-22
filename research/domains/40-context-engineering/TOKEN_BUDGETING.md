# Token Budgeting and Context Efficiency

**Domain:** 40 Context Engineering  
**Status:** RESEARCH IN PROGRESS

## Goal

Maximize useful information per token while preserving:

- correctness;
- safety;
- traceability;
- task state;
- user intent.

## Context sources

Tag every injected context block:

```text
platform-policy
organization-policy
agent-definition
skill
tool-schema
task
history
working-memory
persistent-memory
retrieved-knowledge
artifact
runtime-state
```

Record token contribution from each source.

## Context budget

A model request should reserve budget before assembly.

Example:

```text
Maximum context
- required output reserve
- reasoning reserve where needed
- tool-call reserve
= input context budget
```

Then allocate priority.

## Suggested priority classes

### P0 — cannot drop

- safety;
- authorization/policy;
- current task;
- required output schema.

### P1 — strongly required

- critical project state;
- accepted decisions;
- active constraints;
- necessary tool schemas.

### P2 — retrieval

- relevant knowledge;
- recent history;
- memory.

### P3 — optional

- background material;
- low-confidence memories;
- old conversation;
- unrelated tools.

## Major token-saving techniques

### Selective tool schema loading

Do not inject every tool and every MCP schema into every agent request.

Use capability routing to expose only likely-needed tools.

### Retrieval over bulk context

Search knowledge first, then inject only evidence relevant to the task.

### Hierarchical summaries

Maintain:

- full raw record;
- structured state;
- compact rolling summary.

Do not repeatedly summarize summaries without provenance because information will drift.

### Artifact references

Pass stable artifact IDs and retrieve exact slices instead of repeatedly pasting large files.

### Delta context

For iterative work, transmit state changes rather than rebuilding huge contexts where API/harness semantics allow it.

### Prompt caching

Arrange stable prefixes so provider caching can reuse them.

### Specialized models

Route easy transformations to smaller/cheaper models.

### Structured outputs

Compact structured results can reduce verbose output and downstream parsing tokens.

### Stop conditions

Bound:

- turns;
- retries;
- delegated runs;
- output length;
- research breadth.

## Token-aware delegation

Before delegating, estimate whether the child requires:

- full context;
- summary;
- artifact references;
- only a task contract.

Default should be a bounded task contract, not cloning the parent context.

## Token-aware RAG

Retrieval should optimize not simply for document relevance, but for:

```text
useful evidence / token
```

Evaluate:

- answer quality;
- citation coverage;
- tokens injected;
- duplicate chunks;
- unused chunks.

## Token-aware MCP

Tool descriptions and schemas consume context.

Research:

- lazy tool discovery;
- schema caching;
- tool subset projection;
- concise descriptions;
- structured capability indexes.

## Observability

Every ModelCall should expose a context breakdown showing token contributions by source.

Example:

```text
Policy            1,200
Agent             800
Tools             4,500
History           9,100
Retrieved docs    6,000
Task                700
-----------------------
Input            22,300
```

This makes token waste diagnosable.

## Anti-patterns

- inject entire knowledgebase;
- attach every MCP server;
- replay all chat history forever;
- copy parent context into every subagent;
- use giant verbose system prompts for simple tasks;
- let tools return unbounded output;
- summarize without preserving raw source references;
- optimize for fewer tokens when it materially harms correctness or safety.
