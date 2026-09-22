# Capability, Authority and Risk

**Status:** OBSERVED + PROPOSAL

## Capability and authority are independent

A high-capability agent should not implicitly become a privileged agent.

Example:

```yaml
capability:
  level: L4

authority:
  infrastructure: read
  production_mutation: false
  secrets: none
  git_write: proposal
```

A narrower operational agent may have controlled write rights:

```yaml
capability:
  level: L2

authority:
  infrastructure: controlled-write
  production_mutation: R2
  secrets: scoped
```

## Risk classes

The source organization used this reusable scale:

| Class | Meaning | Typical execution |
|---|---|---|
| R0 | Read / information | autonomous |
| R1 | Non-mutating diagnostic | autonomous |
| R2 | Reversible limited mutation | policy-controlled |
| R3 | Privileged/significant mutation | human approval |
| R4 | Destructive/security-critical | explicit multi-party approval |

Examples:

```text
read logs             → R0
run tests             → R1
restart dev service   → R2
change production IAM → R3
wipe disk             → R4
```

## Design rule

Authorization decisions should evaluate at least:

```text
principal
+ capability level
+ requested action
+ target resource
+ risk class
+ environment
+ policy
+ approval state
```

Do not encode authority only in prompt text.
