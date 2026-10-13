---
status: draft
sources: [inbox/2026-10-13-environment-philosophy-extract.md, inbox/interviews/2026-10-13-environment.md, human/chapter-1.md]
related: [agents-are-an-environment-problem, ratchets, machine-enforced-standards]
---
# The Verification Gate

The **verification gate** is the single command that decides whether a change is done. It runs every check the project has. The same gate runs inside the agent's loop, in the pre-commit hook, and in CI, so "done" means one thing everywhere.

One gate removes a class of failure: work that passes locally and fails later. The agent runs the gate as a tool call. A failing check returns as a tool result, and the agent acts on it before any human sees the change. The gate turns the environment's standards into input for the agentic loop.

## Rules for the gate

- **Fast.** Any change is verifiable in under a minute. An agent runs the gate many times per task, and a slow gate invites skipping. When a check is too slow for the hook, make it faster. Do not remove it.
- **Never skipped.** Red work is never committed. A red gate is fixed, never explained away.
- **Parity is checked.** A check that runs locally and not in CI, or in CI and not locally, is a defect. A machine verifies the parity.
- **Necessary, not sufficient.** A green gate shows the tested paths work. A refactor still needs evidence for paths the tests do not exercise.

## Open questions
- What happens when the gate cannot stay under a minute as the codebase grows? Is there a budget for gate runtime?
