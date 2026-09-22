# Provider Selection Policy

**Status:** PROPOSAL

## Goal

Translate portable resource requirements into approved concrete providers without hard-coding vendors into agent definitions.

## Selection pipeline

```text
Resource requirement
      ↓
Capability registry
      ↓
Provider candidates
      ↓
Organization allowlist
      ↓
Compatibility
      ↓
Security / trust
      ↓
Deployment locality
      ↓
Health / availability
      ↓
Cost / resource fit
      ↓
Selected provider
      ↓
Least-privilege grant
```

## Example

An agent asks for:

```yaml
capability: version-control
access: write
network: private-network
```

Possible candidates may include GitLab Self-Managed, Gitea or another approved internal forge. GitHub Cloud could be excluded if the organization's task policy requires private-network-only operation.

## Selection criteria

- capability completeness;
- deployment mode;
- offline/local requirement;
- organization approval;
- identity integration;
- authorization granularity;
- secrets handling;
- multi-tenancy;
- audit;
- security history;
- current health;
- latency;
- cost;
- resource footprint;
- API stability;
- export/migration support;
- version compatibility.

## Provider lock-in rule

Agent definitions should reference providers only when a task specifically depends on provider-specific behavior.

Otherwise use portable capabilities and resolve providers at provisioning time.
