---
status: reviewed
sources: [inbox/interviews/2026-10-13-environment.md, inbox/2026-10-13-environment-philosophy-extract.md, inbox/2026-10-13-earendil-measuring-code-sloppiness.md, inbox/2026-10-12.md]
related: [ratchets, verification-gate, machine-enforced-standards, self-documenting-repository, agents-as-users, code-sloppiness]
---
# Agents Are an Environment Problem

The quality of an agent's work depends on the environment it works in. The **environment** is everything around the agentic loop that shapes and checks its output: the codebase, its structure, its documentation, and the automated checks that run against every change. Reliable agent work comes from trusting the environment, not the model.

## Failure in an unprepared environment

An unchecked agent produces code that works today and fails the test of durability. The code is short-sighted and hacky. Tests ignore the project's lint rules and style. Functionality consolidates into large files and functions that do everything, where a maintainable design would split it. Each change is locally reasonable. Across many changes the codebase grows inconsistent, because nothing holds the agent to one standard.

The cause is a missing check. An agent free to complete a task however it wants completes it in a way the environment does not verify. Better models shrink this effect. They do not remove it in codebases too large to fit in context, where the agent works against legacy code it can only partly see.

## Correctness and durability

Correctness is easy to verify: tests pass or fail. Durability is not. Duplication, needless abstraction, and concentrated complexity pass every test, and judging them has required human taste. A prepared environment converts as much of that taste as possible into checks a machine runs on every change.

## Properties of a prepared environment

- **Fast verification:** any change is verifiable in under a minute.
- **Self-documenting:** the repository answers its own onboarding questions.
- **Machine-enforced standards:** every standard is enforced by a machine.
- **Reversibility:** every action can be undone.
- **Agents as users:** the team designs the codebase for agents as its users.

These properties serve humans and agents alike. Agents expose their absence sooner, because agents produce changes faster than humans can review them.

## Open questions
- Where does the environment's guarantee stop? A strict environment guarantees work is built correctly, not that it was worth building. Your material says "The quality gates enforce what they can. Review enforces the rest." What does review cover that no check can?
- Reversibility has one line of source material. What does it look like in practice, and does it need its own concept?
- The 2026-10-12 memo calls this "arguably a thesis for the book." Does this concept stay in Ch6 or move earlier?
