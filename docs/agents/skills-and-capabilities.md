# Skills and Capability Knowledge

**Status:** OBSERVED + PROPOSAL  
**Source class:** AI-FLEET PRIOR RESEARCH

The saved AI-FLEET Skills Index reports **440 skills**.

Six platform-level skills were marked tested:

- `aifleet-delegate`
- `aifleet-handoff`
- `aifleet-ingest-knowledge`
- `aifleet-orchestrate`
- `aifleet-review-gate`
- `aifleet-skill-improve`

The wider index contained department-specific and shared skills spanning engineering, strategy, facilities, trust & safety, knowledge, security, operations and other functions.

## Reusable design lessons

A skill should be:

- uniquely identified;
- versioned;
- bounded by explicit inputs/outputs;
- associated with risk;
- testable;
- discoverable;
- portable across supported harnesses;
- independently reviewable;
- promotable/rollbackable.

Shared skills from the earlier corpus included categories such as:

- task decomposition;
- agent delegation and handoff;
- capability discovery;
- approval-gate enforcement;
- artifact validation;
- audit event authoring;
- citation and provenance management;
- context budgeting;
- cross-model review;
- fact verification;
- freshness checking;
- knowledge ingestion/retrieval;
- least-privilege checks;
- MCP capability routing;
- memory conflict detection;
- regression-risk analysis;
- run checkpoint/resume planning;
- secret redaction;
- skill evaluation, versioning, release and rollback;
- source-quality assessment and triangulation;
- tool discovery/routing;
- uncertainty labeling;
- unsafe-action escalation;
- web research.

**PROPOSAL:** Open Agent OS should treat skills as first-class, independently versioned capability packages rather than embedding every procedure inside agent prompts.
