# Compliance Obligation Taxonomy

Every rule should have explicit metadata.

## Source type

- law
- regulation
- treaty
- regulator-guidance
- technical-standard
- contractual
- license
- platform-terms
- internal-policy
- best-practice

## Obligation type

- prohibit
- require
- disclose
- document
- assess
- approve
- retain
- delete
- secure
- notify
- report
- monitor
- test
- train
- provide-human-review
- provide-remedy

## Actor role

Possible examples:

- provider
- deployer
- importer
- distributor
- manufacturer
- developer
- processor
- controller
- employer
- researcher
- open-source steward
- marketplace operator
- end user

## Applicability status

- applies
- likely-applies
- does-not-apply
- unknown
- needs-counsel
- superseded

## Freshness

Legal sources require stronger freshness controls than ordinary documentation.

Every legal rule should record:

- source URL;
- jurisdiction;
- publication date;
- effective/application date;
- last verified date;
- superseded-by;
- official/non-official status.

## Agent behavior

Agents may retrieve and summarize applicable rules.

They should not silently convert uncertain applicability into an asserted legal conclusion.

For high-impact decisions, the system should support escalation to qualified human review.
