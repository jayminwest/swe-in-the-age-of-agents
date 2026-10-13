---
status: draft
sources: [inbox/2026-10-13-environment-philosophy-extract.md, human/PLANNING.md]
related: [agents-are-an-environment-problem, self-documenting-repository, verification-gate]
---
# Agents as Users

A codebase prepared for agents treats them as users the team designs for. Build commands, error messages, and module boundaries all have an agent as a consumer, and each is designed for that consumer.

## One core, thin front ends

Each capability has one implementation, in a core library. Command-line tools, interfaces, and services only translate input into calls and results into output. An agent changing a behavior has one place to change it and no second copy to fall out of sync. A front end that reimplements logic is a bug.

## Define errors out of existence

Design the interface so the error cannot happen: deleting a missing key succeeds, and an empty range is a valid range. Each error that remains gets a stable code and a hint that tells the caller what to do. The agent receives the hint as a tool result and acts on it. Callers never parse error messages.

## Deep modules

A **deep module** hides a large amount of behavior behind a small interface. A shallow module costs more than it gives. Code is never split only to make files or functions short. An abstraction is added when the second implementation arrives, not on speculation.

## Open questions
- PLANNING lists "agent ergonomics" under Tools in Ch2. Is that the same idea at the tool level, and should the two concepts merge or reference each other?
