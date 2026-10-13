---
status: draft
sources: [inbox/2026-10-13-environment-philosophy-extract.md, inbox/2026-10-13-earendil-measuring-code-sloppiness.md]
related: [agents-are-an-environment-problem, agents-as-users, machine-enforced-standards]
---
# The Self-Documenting Repository

A **self-documenting repository** answers its own onboarding questions. An agent starts each task with an empty context. The conventions, the architecture, and the commands that verify a change must all be readable from the repository itself.

## Rules

- **One agent document.** A single document serves every harness. Different tools read the same file.
- **Principles first.** The agent document points to the project's design philosophy before any design change.
- **Docs change with the code.** A change to a contract updates its documentation in the same commit.
- **Docs are checked.** Every command and path the agent document names must exist. A machine verifies this on every change.
- **One standard, one place.** A standard shared across projects lives in a template. Projects are generated from the template. They are never edited to match it.

## Open questions
- What belongs in the agent document itself, and what should it only point to?
- Context injection and just-in-time retrieval (PLANNING, Ch2) overlap with this. Where is the boundary?
