# Security Model

Agent systems connect probabilistic models to deterministic systems with real side effects.

The baseline security model therefore assumes that model output, retrieved content, plugins, tools, MCP servers, generated code, browser state, downloads, and persistent memory may be untrusted.

Core controls:

- explicit identity;
- least privilege;
- scoped capabilities;
- policy enforcement;
- sandboxing;
- secret isolation;
- approval gates;
- provenance;
- audit;
- bounded budgets;
- recoverability.
