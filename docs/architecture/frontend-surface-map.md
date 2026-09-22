# Frontend Surface Map

**Status:** PROPOSAL

## Shared primitives

Every frontend surface should draw from the same canonical resource APIs and design system.

Shared primitives include:

- resource search;
- resource inspector;
- status;
- activity timeline;
- provenance;
- approvals;
- policy decisions;
- token/cost usage;
- notifications;
- command palette.

## Personal Cockpit

- tasks;
- chat/command input;
- current agents;
- local/cloud model selector;
- token/cost budget;
- knowledge;
- files;
- approvals.

## Developer Console

- repositories;
- branches/worktrees;
- issues;
- code diffs;
- tests;
- review findings;
- runtime trace;
- tools/MCP;
- model calls;
- context/token inspection.

## Team Workspace

- projects;
- team members;
- shared agents;
- task board;
- approvals;
- shared knowledge;
- artifacts;
- evaluation results;
- spend and quota.

## Organization Control Deck

- departments;
- teams;
- roles;
- registries;
- policies;
- model/provider configuration;
- MCP/extension allowlists;
- quotas;
- cost allocation;
- organization health.

## Security Console

- identities;
- relationships;
- capability grants;
- high-risk calls;
- secrets;
- MCP server trust;
- incidents;
- audit;
- supply-chain evidence.

## Research & Knowledge Console

- sources;
- ingestion queues;
- source freshness;
- citations;
- contradiction view;
- knowledge graph;
- memories;
- benchmark/evaluation results.

## Platform Console

- nodes;
- GPU/CPU/RAM;
- models;
- queues;
- workflows;
- distributed execution;
- storage;
- backups;
- network/service health.

## Marketplace

- agents;
- skills;
- MCP servers;
- plugins;
- workflows;
- test packs;
- trust/security metadata;
- compatibility;
- install/evaluate/promote workflow.

## Principle

Do not create one enormous navigation tree for every user.

Use capability- and role-aware composition while keeping hidden UI distinct from actual backend authorization.
