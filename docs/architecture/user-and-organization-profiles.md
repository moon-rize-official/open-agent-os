# User, Team and Organization Profiles

Open Agent OS should support multiple operating profiles without changing its canonical resource model.

| Profile | Primary user | Typical deployment | Core needs |
|---|---|---|---|
| Personal | individual | laptop / desktop | privacy, simplicity, local AI, token visibility |
| Power User | individual | workstation + server | advanced models, automation, hardware control |
| Developer | developer | workstation | code, Git, IDE, tests, agents |
| Small Team | 2–20 users | shared server | projects, shared agents, approvals, budgets |
| Startup | 10–100 users | cloud/hybrid | teams, SSO, shared knowledge, cost control |
| Organization | 100+ users | distributed | departments, policies, audit, registries |
| Enterprise | large/regulatory | isolated/hybrid/multi-region | compliance, data residency, federation |
| Research Team | researchers | shared compute | sources, provenance, experiments, reproducibility |
| Security Team | security operators | central control plane | permissions, incidents, audit, trust |
| Platform Team | infra/platform engineers | fleet | nodes, models, scheduling, observability |
| Managed SaaS | service operator | multi-tenant cloud | tenant lifecycle, billing, isolation, SLOs |
| Air-Gapped | regulated/offline operator | isolated LAN | offline registries, local models, sync packages |

## Design rule

Features should be composable.

A personal user should not have to deploy enterprise infrastructure to gain a working Agent OS.

An enterprise should not have to replace the Agent OS resource model just because it needs stronger isolation.

## Frontend personalization

The same resource may have different presentation based on role.

Example:

```text
Run
├── Personal view: result + cost + major actions
├── Developer view: tools + diff + tests + trace
├── Security view: grants + secrets + risky actions
└── Platform view: node + queue + latency + failures
```

## Organization context

A user may belong to multiple organizations.

The active organization should be explicit in:

- session;
- API request;
- authorization check;
- resource namespace;
- audit event;
- cost attribution.

Never infer tenant context only from the currently visible frontend route.
