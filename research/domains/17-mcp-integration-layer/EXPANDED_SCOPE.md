# Domain 17 — MCP / Integration Layer: Expanded Scope

**Status:** RESEARCH IN PROGRESS

## Current references

- MCP project: https://modelcontextprotocol.io/
- Official MCP Registry: https://registry.modelcontextprotocol.io/docs
- Registry source: https://github.com/modelcontextprotocol/registry

## Research beyond protocol basics

Research:

- MCP server architecture;
- local vs remote servers;
- stdio vs HTTP transports;
- server lifecycle;
- health;
- authentication;
- authorization;
- secrets;
- registry/discovery;
- private registries;
- organization allowlists;
- marketplaces/aggregators;
- trust;
- package provenance;
- security scanning;
- compatibility;
- schema caching;
- offline registry snapshots;
- gateways/brokers.

## Registry vs marketplace

The official MCP Registry is a metadata/discovery layer. Downstream aggregators can add richer curation, ratings, security scanning, search and installation experiences.

Open Agent OS should research both separately.

## MCP capability broker

**PROPOSAL:** agents should normally reach MCP servers through a capability broker rather than each connecting directly.

Potential broker responsibilities:

- discover;
- launch/connect;
- authenticate;
- authorize;
- inject scoped credentials;
- enforce tool policy;
- log/audit;
- rate-limit;
- cache schemas;
- monitor health;
- terminate compromised servers.

## Deliverables

- MCPServer resource schema;
- MCPRegistry adapter;
- private registry profile;
- trust/provenance record;
- capability projection;
- installation manifest;
- health model;
- compatibility tests;
- policy examples.
