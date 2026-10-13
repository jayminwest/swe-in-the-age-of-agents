---
status: draft
sources: [inbox/interviews/2026-10-13-environment.md, inbox/2026-10-13-environment-philosophy-extract.md, BOOK_SPINE.md]
related: [agents-are-an-environment-problem, verification-gate, code-sloppiness]
---
# Machine-Enforced Standards

A standard is real when a machine enforces it. Linting keeps code consistent, style rules keep it readable, and type checks keep contracts honest. A standard written only in a prompt or a document is a request, and an agent can ignore a request. Anything a prompt asks an agent not to do is a check that was not written.

Unenforced standards drift. An agent follows written guidance on one change and misses it on the next. Across hundreds of changes the codebase becomes inconsistent. A check applies the same rule to every change, whichever agent or human made it.

## Exceptions carry reasons

Every exception to a rule states why it exists. A suppression without a reason is forbidden. A debt marker in the code cites a tracked issue. The codebase never carries an exception nobody can explain.

## Tooling does not offset debt

Having the checks is different from passing them. A repository with complete tooling and sloppy code is sloppy. A measure of the environment that rewards the presence of tools hides the state of the code those tools protect.

## The limit of enforcement

The gates enforce what they can. Review enforces the rest. The work is to move as much judgment as possible into checks and to know what remains outside them.

## Open questions
- What specifically remains for review? This is the same question as the limit of the environment in [agents-are-an-environment-problem].
