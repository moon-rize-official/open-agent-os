# Department Knowledge Requirements Map

**Status:** INITIAL PROPOSAL

This map describes typical information classes. Specific organizations should override it.

| Department | Core information needs |
|---|---|
| Executive & Strategy | strategy, goals, KPIs, portfolio, financial summaries, major risks, market intelligence |
| Product | roadmap, requirements, customer feedback, product analytics, experiments, competitive research |
| Research & Innovation | papers, standards, experiments, evidence, datasets, prior research, citations |
| Engineering | repositories, architecture, ADRs, issues, dependencies, APIs, tests, build/release state |
| AI & Agent Systems | models, prompts, evals, skills, tools, MCP, agent definitions, routing, token/cost data |
| Data & Analytics | schemas, lineage, datasets, metrics definitions, quality, pipelines, access policies |
| Design & User Experience | design system, user research, journeys, accessibility, prototypes, product requirements |
| Platform & Infrastructure | topology, inventory, deployments, service health, runbooks, capacity, backups |
| Security | assets, identities, permissions, threats, vulnerabilities, incidents, policies, security telemetry |
| IT & Internal Systems | users, endpoints, software inventory, support tickets, identity systems, internal services |
| Knowledge & Documentation | source inventory, taxonomy, provenance, freshness, documentation, knowledge graph |
| Operations | procedures, schedules, SLAs/SLOs, inventories, incidents, operational dashboards |
| Quality & Reliability | test plans, quality gates, defects, incidents, SLOs, release criteria |
| Sales | CRM/account data, product information, pricing, proposals, pipeline, approved collateral |
| Marketing & Growth | brand rules, campaigns, analytics, audience research, approved claims, content calendar |
| Partnerships & Business Development | partners, agreements, opportunities, integration requirements, relationship history |
| Customer Success | account goals, product usage, health scores, renewals, open risks, support history |
| Customer Support | tickets, product docs, troubleshooting, customer context, escalation procedures |
| Professional Services | SOWs, customer environment, implementation plans, deliverables, acceptance criteria |
| Finance & Accounting | budgets, invoices, ledger, forecasts, policies, cost allocations, approvals |
| People & HR | org structure, policies, role definitions, approved employee data only as required |
| Legal | contracts, laws, regulatory guidance, disputes, IP, approved templates, jurisdiction context |
| Compliance & Governance | control framework, evidence, policies, audits, regulatory obligations, exceptions |
| Risk Management | risk register, controls, incidents, dependencies, scenarios, mitigations |
| Procurement & Vendor Management | vendors, contracts, licenses, security reviews, pricing, renewal dates |
| Corporate Development | market research, strategic targets, financial models, diligence data |
| Communications & PR | approved messaging, media context, brand policy, public statements, crisis plans |
| Program & Project Management | plans, milestones, dependencies, risks, status, owners, decisions |
| Facilities & Workplace | sites, access, maintenance, assets, safety procedures, schedules |
| Supply Chain & Logistics | suppliers, inventory, orders, routes, lead times, quality, disruptions |
| Manufacturing & Production | BOM, process specs, QA, equipment state, schedules, safety |
| Regulatory Affairs | applicable regulations, submissions, evidence, deadlines, regulator communications |
| Trust & Safety | policies, abuse patterns, reports, enforcement rules, escalation criteria |
| Internal Audit | controls, evidence, logs, policy versions, findings, remediation status |
| Business Continuity & Crisis Management | continuity plans, dependencies, contacts, recovery procedures, incidents |
| Developer Experience | SDKs, templates, build systems, docs, developer feedback, internal platform state |
| Architecture | system maps, ADRs, standards, dependencies, constraints, roadmaps |
| Cloud & Network Engineering | cloud inventory, network topology, IAM, DNS, traffic, capacity, incidents |
| Developer Platform | platform APIs, templates, environments, CI/CD, service catalog, developer metrics |
| Data Platform | storage, pipelines, schemas, governance, access, lineage, capacity |
| AI Platform | model inventory, inference runtimes, GPUs, routing, quotas, evals, safety controls |
| Automation & Integration Platform | workflows, connectors, credentials references, queues, API contracts, failures |
| Enterprise Architecture & Shared Services | capability maps, application portfolio, standards, dependencies, governance |

## Important

Sensitive information should be represented as **requirements**, not automatically injected data.

For example:

- HR agent may require "approved employee record fields" rather than all employee data.
- Security agent may require "credential status" rather than plaintext credentials.
- Finance agent may require "authorized balance view" rather than unrestricted banking access.
