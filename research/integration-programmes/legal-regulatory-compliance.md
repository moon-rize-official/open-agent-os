# Legal, Regulatory, Compliance & Responsible-AI Research Programme

**Status:** RESEARCH IN PROGRESS  
**Date:** 2026-09-22

> This repository is an engineering research resource, not legal advice. Applicability must be verified for the actual jurisdiction, entity, product, data, sector and use case.

## Mission

Research the legal, regulatory, standards, contractual and governance obligations that can affect an Agent OS used by:

- freelancers / sole developers;
- researchers / universities;
- open-source maintainers;
- startups / SMEs;
- large companies;
- managed Agent OS / SaaS providers;
- employers;
- regulated industries;
- public-sector organizations;
- cross-border/distributed organizations.

## Obligation taxonomy

Never collapse these into a single "compliance" bucket:

```text
LAW / REGULATION
REGULATOR GUIDANCE
TECHNICAL STANDARD
INDUSTRY CODE
CONTRACTUAL OBLIGATION
OPEN-SOURCE LICENSE
PLATFORM TERMS
INTERNAL POLICY
BEST PRACTICE
```

Every requirement should record which category it belongs to and whether it is binding for the current actor.

## Current high-priority research families

### AI-specific regulation

Research:

- EU AI Act;
- national implementation/enforcement;
- Germany KI-MIG;
- Council of Europe AI Framework Convention;
- UK regulator-led AI governance;
- US federal/state/local AI rules;
- sector-specific AI rules;
- transparency/disclosure;
- prohibited uses;
- high-risk systems;
- GPAI/foundation-model obligations;
- human oversight;
- impact assessments;
- AI literacy/training.

### Privacy and data protection

Research:

- GDPR;
- national implementations;
- UK GDPR and current UK reforms;
- controller/processor roles;
- lawful basis;
- data minimization;
- special-category data;
- DPIAs;
- international transfers;
- automated decision-making/profiling;
- employee/workplace data;
- children;
- biometrics;
- logs/telemetry;
- model/memory deletion and access rights.

### Cybersecurity

Research:

- EU Cyber Resilience Act;
- NIS2;
- DORA;
- national cybersecurity laws;
- incident reporting;
- vulnerability handling;
- secure development;
- SBOMs;
- product security maintenance;
- open-source software steward rules;
- breach notification.

### Consumer and commercial law

Research:

- unfair/deceptive AI claims;
- transparency;
- subscriptions;
- refunds;
- dark patterns;
- warranties;
- product/service liability;
- advertising;
- marketplace responsibilities.

### Employment and workplace AI

Research:

- hiring/recruiting automation;
- worker profiling;
- employee monitoring;
- automated employment decisions;
- bias audits;
- notices;
- human review;
- worker representation/works-council requirements where applicable.

### Copyright, licensing and IP

Research:

- software licenses;
- model licenses;
- dataset licenses;
- training-data rights;
- text/data-mining rules;
- generated-output rights;
- attribution;
- trademarks;
- patents;
- trade secrets;
- proprietary-code context.

### Open-source law and governance

Research:

- Apache/MIT/BSD/GPL/AGPL/MPL compatibility;
- DCO/CLA;
- contributor provenance;
- SBOMs;
- license scanning;
- EU AI Act open-source treatment;
- CRA open-source treatment;
- software-steward obligations;
- commercial/non-commercial distinctions.

### Research and academia

Research:

- scientific-research exclusions/derogations;
- ethics review;
- human-subject data;
- research-data governance;
- publication/reproducibility;
- model/dataset licensing;
- dual-use concerns.

## Current official reference points

### European Union AI Act

European Commission AI Act overview:
https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

As of September 2026, Commission materials state:

- the AI Act entered into force on 1 August 2024;
- prohibited practices and AI-literacy obligations apply from 2 February 2025;
- governance and GPAI obligations apply from 2 August 2025;
- broader enforcement/transparency provisions apply from 2 August 2026;
- high-risk dates have been adjusted in the 2026 simplification process and must be tracked from current Commission/EUR-Lex sources rather than hard-coded indefinitely.

Enforcement overview:
https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act

### Germany

Germany adopted the KI-Marktüberwachungs-und-Innovationsförderungs-Gesetz (KI-MIG) in July 2026 to implement/enforce Regulation (EU) 2024/1689.

Official legal text:
https://www.gesetze-im-internet.de/ki-mig/

The Bundesnetzagentur acts as a central market-surveillance/coordinating authority for broad areas, with sector authorities retaining responsibilities in specified areas.

### Cyber Resilience Act

Official Commission open-source guidance:
https://digital-strategy.ec.europa.eu/en/policies/cra-open-source

Official consolidated regulation:
https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng

Research must distinguish:

- manufacturers;
- non-commercial open-source contributors;
- open-source software stewards;
- commercially supplied open-source products.

### NIS2

Official text:
https://eur-lex.europa.eu/eli/dir/2022/2555

Research national transposition and entity scope instead of assuming the directive itself maps identically to every organization.

### DORA

Official EU financial-sector regulation:
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554

Research is required for financial entities and relevant ICT third-party providers, including contractual, resilience, incident and third-party-risk obligations.

### Data protection / AI models

EDPB Opinion 28/2024:
https://www.edpb.europa.eu/documents/opinion-of-the-board-art-64/opinion-282024-on-certain-data-protection-aspects-related-to_en

It addresses data-protection issues around AI models, including anonymity, legitimate interests and unlawfully processed personal data.

### United Kingdom

ICO technology/AI guidance tracker:
https://ico.org.uk/about-the-ico/what-we-do/our-plans-for-new-and-updated-guidance/technology/

Research must record guidance status: draft, consultation, final or superseded. For example, ICO agentic-AI guidance is still a developing guidance area as of 2026 rather than a statute.

### United States / voluntary frameworks

NIST AI RMF:
https://www.nist.gov/itl/ai-risk-management-framework

NIST Generative AI Profile:
https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

These are voluntary risk-management frameworks, not federal AI statutes.

### International

Council of Europe Framework Convention on AI:
https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence

Track ratification/entry-into-force status per jurisdiction before treating treaty obligations as directly applicable.

## Engineering deliverables

- jurisdiction registry;
- obligation registry;
- applicability engine;
- legal-source freshness tracker;
- compliance evidence schema;
- AI-system classification worksheet;
- sector overlays;
- privacy/data-processing inventory;
- software-license inventory;
- risk/impact-assessment templates;
- transparency/disclosure requirements;
- audit/evidence retention rules;
- incident-reporting matrix;
- open-source compliance profile;
- freelancer/research/startup/enterprise applicability profiles.

## Failure modes

- treating voluntary guidance as binding law;
- using outdated application dates;
- assuming EU law applies identically outside the EU;
- assuming open source means exempt;
- failing to distinguish provider/deployer/importer/distributor roles;
- giving an agent legal conclusions without jurisdiction context;
- silently changing compliance rules when sources update;
- collecting excessive data "for compliance";
- treating compliance evidence as authorization to perform risky actions.
