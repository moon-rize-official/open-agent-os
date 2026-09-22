# Compliance Applicability Profiles

**Status:** PROPOSAL

The legal/compliance system should determine applicable requirements from facts, not from one global checklist.

## Applicability inputs

```text
jurisdiction
organization type
organization size
sector
product/service type
commercial status
AI role
data processed
affected persons
decision type
deployment location
model/provider
open-source status
risk class
```

## Example profiles

### Freelancer / sole developer

Research:

- privacy/data protection if processing personal data;
- contract/client confidentiality;
- software/model licenses;
- tax/business obligations outside this project's technical scope;
- AI transparency where applicable;
- product/cybersecurity obligations if distributing software commercially.

Avoid imposing enterprise-only controls without evidence they apply.

### Researcher / university

Research:

- research ethics;
- personal-data rules;
- scientific research provisions;
- dataset/model licenses;
- publication and reproducibility;
- institutional policy;
- export/dual-use rules where relevant.

### Open-source maintainer

Research:

- software license obligations;
- contributor provenance;
- dependency licenses;
- security/vulnerability handling;
- CRA open-source distinctions;
- AI Act open-source distinctions;
- trademark/governance.

### Startup / SME

Research:

- same substantive laws as applicable to activity;
- SME/startup support/sandboxes where available;
- privacy;
- employment;
- consumer;
- cybersecurity;
- AI Act role/classification;
- contractual/security requirements from customers.

### Enterprise

Research:

- group-level governance;
- data residency;
- vendor management;
- employment/workplace AI;
- audit;
- third-party risk;
- internal controls;
- sector-specific overlays;
- multi-jurisdiction applicability.

### Managed Agent OS / SaaS provider

Research:

- controller/processor/subprocessor roles;
- tenant isolation;
- data-processing agreements;
- security obligations;
- incident reporting;
- marketplace/plugin responsibilities;
- provider/deployer roles under AI law;
- customer audit evidence;
- cross-border transfers.

### Financial organization

Add:

- DORA;
- financial supervisory rules;
- model risk;
- ICT third-party registers/contracts;
- resilience testing;
- incident reporting.

### Public sector

Add:

- public-law requirements;
- procurement;
- accessibility;
- transparency;
- fundamental-rights impact obligations;
- records/public-information duties where applicable.

## Output

An applicability engine should return:

```yaml
requirements:
  - id:
    source_type: law
    jurisdiction:
    applies: true
    rationale:
    actor_role:
    effective_date:
    evidence_required:
    agent_context_policy:
```
