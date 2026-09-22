# Domain 73 — UI Component System / Design System: Expanded Scope

## References

- Storybook docs: https://storybook.js.org/docs/
- Storybook component documentation: https://storybook.js.org/docs/writing-docs
- Storybook testing: https://storybook.js.org/docs/writing-tests
- Storybook accessibility: https://storybook.js.org/docs/writing-tests/accessibility-testing
- Storybook MCP server: https://storybook.js.org/docs/ai/mcp/overview

## Research areas

### Design tokens

- color;
- typography;
- spacing;
- radius;
- motion;
- density;
- status;
- risk;
- confidence;
- run state.

### Generic primitives

- forms;
- tables;
- trees;
- graphs;
- timelines;
- dialogs;
- command palettes;
- logs;
- diffs;
- code viewers.

### Agent-specific components

- Agent Card
- Task Card
- Run Timeline
- Tool Call
- Model Call
- Approval Card
- Policy Decision
- Artifact Viewer
- Provenance Graph
- Knowledge Citation
- Memory Inspector
- Capability Browser
- MCP Server Card
- Node Card
- Workflow Graph
- Cost Meter
- Token Meter
- Context Budget Meter
- Evaluation Panel

### Component explorer

Research Storybook-style isolated development, documentation, component tests, accessibility tests and visual regression.

Storybook's MCP capability is also relevant because it lets agents discover design-system components and documentation.

### Design-system distribution

Research:

- package distribution;
- source-owned components;
- frontend plugin component packs;
- organization themes;
- compatibility/versioning;
- visual/accessibility regression gates.

## Critical semantic distinction

UI must visually distinguish:

- user instruction;
- model inference;
- retrieved evidence;
- proposed action;
- approved action;
- executed action;
- observed result;
- policy decision.
