# Security Policy

Agent systems combine untrusted model output with privileged tools, external content, credentials, browsers, filesystems, APIs, and persistent memory. Open Agent OS therefore treats security as a cross-cutting architectural requirement.

## Baseline assumptions

Treat the following as potentially untrusted:

- model output;
- retrieved documents and webpages;
- memory entries;
- plugins and connectors;
- MCP servers and tools;
- generated code;
- downloaded files;
- browser/computer-use environments;
- third-party models and packages.

## Baseline controls

Guidance in this repository should default toward:

- explicit identity;
- least privilege;
- scoped capabilities;
- policy enforcement;
- sandboxing for untrusted execution;
- bounded budgets and rate limits;
- provenance and audit trails;
- approval gates for high-impact actions;
- secret isolation;
- recoverable and replayable workflows where practical.

Do not publish active exploit details for vulnerabilities in code shipped by this project in a public issue. Use GitHub private vulnerability reporting when it is enabled.
