# Domain 55 — API / SDK: Expanded Backend Scope

Research APIs for:

- personal/local deployments;
- internal team deployments;
- multi-organization SaaS;
- enterprise;
- offline/disconnected clients;
- plugins/extensions.

## API layers

1. Canonical Resource API
2. Runtime/Execution API
3. Query/Search API
4. Event/Streaming API
5. Administrative API
6. Extension/Plugin API
7. Backend-for-Frontend APIs
8. Compatibility/Discovery API

## Requirements

- explicit organization/namespace context;
- versioned schemas;
- idempotency keys;
- optimistic concurrency;
- pagination;
- watch/stream;
- correlation IDs;
- audit metadata;
- stable errors;
- rate limits;
- token/cost usage metadata;
- capability discovery;
- client SDK generation;
- local/offline operation.

## Compare

- REST/OpenAPI;
- gRPC/Protobuf;
- GraphQL for query aggregation where justified;
- WebSocket;
- SSE;
- event buses.

Avoid exposing internal database schemas as the platform API.
