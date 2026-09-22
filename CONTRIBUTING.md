# Contributing to Open Agent OS

Contributions should improve **evidence quality, interoperability, reproducibility, security, or implementation usefulness**.

## Research contributions

Substantive claims should identify an evidence class:

- `PRIMARY SOURCE`
- `SPECIFICATION`
- `SOURCE CODE`
- `PAPER`
- `SECURITY ADVISORY`
- `PRODUCTION EVIDENCE`
- `BENCHMARK`
- `SECONDARY ANALYSIS`
- `COMMUNITY EVIDENCE`

Prefer primary sources. Record versions and dates where behavior can change. If sources conflict, document the conflict instead of silently reconciling it.

## Design contributions

Use an RFC for changes to canonical contracts, kernel boundaries, or interoperability rules. Use an ADR for repository decisions that create lasting constraints.

Design text should remain marked `PROPOSAL` until accepted.

## Public-safety boundary

Do not contribute:

- credentials or tokens;
- private infrastructure details;
- customer or employee personal information;
- proprietary datasets or source code;
- private chat exports;
- third-party copyrighted documentation copied wholesale.

Summarize and cite instead.

## Pull requests

A good PR explains:

1. what changed;
2. why it matters;
3. supporting evidence;
4. security/compatibility impact;
5. whether it changes a proposal, contract, or only documentation.
