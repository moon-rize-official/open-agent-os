# Token Economics and Usage

**Domain:** 68 Cost Management  
**Status:** RESEARCH IN PROGRESS

## Why tokens need their own research area

For model-backed systems, token use affects:

- price;
- latency;
- memory/context capacity;
- cache efficiency;
- model routing;
- throughput;
- rate limits;
- user quotas.

An Agent OS should understand token use as an observable resource, similar to CPU, RAM or GPU time.

## What is a token?

A token is a model-specific unit produced by a tokenizer.

A token may represent:

- part of a word;
- whole word;
- punctuation;
- whitespace;
- code fragments;
- non-text modality units depending on the provider/model.

Different model families use different tokenizers and therefore the same text can have different token counts.

Google's Gemini documentation describes tokenization explicitly and provides token-counting APIs. It notes a rough English heuristic of around four characters per token, but this is not a portable guarantee.

Reference:
https://ai.google.dev/gemini-api/docs/tokens

## Token categories to research

A unified Agent OS usage schema should support:

- input tokens;
- output tokens;
- cached input tokens;
- cache-write tokens where provider exposes them;
- reasoning/internal tokens where provider exposes them;
- tool/schema tokens;
- multimodal input units;
- context-retained tokens;
- retrieval-injected tokens;
- system/developer instruction tokens;
- conversation-history tokens.

## Where tokens are spent

A request may include:

```text
System instructions
+ policy
+ agent definition
+ skill instructions
+ tool/MCP schemas
+ conversation history
+ task
+ retrieved knowledge
+ memory
+ artifacts
+ user files
+ generated output
```

Long-lived agents often spend more tokens repeatedly resending context than on the user's immediate request.

## Provider differences

Research each provider/model for:

- tokenizer;
- context window;
- token-count endpoint;
- usage response fields;
- caching;
- reasoning token reporting;
- rate limits;
- input/output prices.

Do not normalize away provider-specific usage metadata. Preserve raw provider usage alongside canonical normalized fields.

## Prompt/context caching

Caching can reduce repeated computation and cost when prompts share long stable prefixes.

References:

- OpenAI prompt caching:
  https://openai.com/index/api-prompt-caching/
- Gemini context caching:
  https://ai.google.dev/gemini-api/docs/caching

Design implications:

- stable instructions should appear early;
- frequently changing task content should appear later;
- giant dynamic prefixes destroy cache reuse;
- cache identity must respect security/tenant boundaries.

## Token accounting schema

**PROPOSAL:**

```yaml
usage:
  provider: example
  model: example-model
  input_tokens: 12000
  output_tokens: 900
  cached_input_tokens: 8000
  reasoning_tokens: null
  total_tokens: 12900
  estimated_cost:
    currency: USD
    amount: 0.00
  context_window:
    max_tokens: 0
    utilization_ratio: 0.0
```

Keep raw provider payload for audit.

## Budget dimensions

Allow limits per:

- user;
- organization;
- department;
- team;
- project;
- task;
- run;
- agent;
- model;
- provider;
- day/month.

## Cost controls

- model routing;
- context trimming;
- caching;
- summarization;
- retrieval instead of full corpus injection;
- tool-schema filtering;
- shorter structured outputs;
- local models;
- batch/background execution;
- max-output tokens;
- stopping conditions;
- per-run budgets.

## Metrics

Track:

- tokens per successful task;
- tokens per run;
- tokens by context source;
- cache hit ratio;
- output/input ratio;
- cost per completed task;
- token waste from failed/retried runs;
- token waste from unused retrieved context;
- token spend by agent/skill/tool;
- token spend by tenant/team/project.

## Failure modes

- invisible runaway loops;
- retries resend giant contexts;
- one agent consumes organization quota;
- cache leaks across tenant boundaries;
- token counter differs from provider billing;
- context fills and truncates critical instructions;
- massive MCP schemas dominate prompts;
- unnecessary full conversation replay.
