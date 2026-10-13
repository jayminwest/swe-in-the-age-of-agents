---
status: draft
sources: [inbox/2026-10-13-earendil-measuring-code-sloppiness.md, inbox/2026-10-13-environment-philosophy-extract.md, inbox/interviews/2026-10-13-environment.md]
related: [agents-are-an-environment-problem, ratchets, machine-enforced-standards]
---
# Code Sloppiness

**Sloppiness** is the structural debt that working code accumulates: duplication, needless abstraction, verbosity, and complexity concentrated in a few large functions. Sloppy code passes its tests. The cost arrives later. A refactor spans more files than expected, similar logic appears in several places, and modules depend on each other in both directions. The codebase still builds, but working in it takes more effort.

## Why agents produce it

Models write correct code because correctness is verifiable: tests give a clear signal. Sloppiness gives no such signal. Measurements of agent-written code find it markedly more verbose than code in established repositories, with more of its mass in large, complex functions.

Bad decisions accumulate. When an agent works through a sequence of changes with a fresh context each time, the shortcuts of early changes constrain later ones. Agents cannot reliably clean up after themselves either. A model asked to score its own code produces scores close to random.

## Measuring it

Measure sloppiness without a model in the loop, so the same code always gets the same score. Useful signals include growth in total lines, duplicated lines, the share of code in large and complex functions, and import cycles. The question each measure answers is whether the codebase is getting worse. That question makes it a ratchet.

Measures are leads, not verdicts. Do not chase zero. Do not add indirection to improve a score. Track counts alongside densities, so a large clean addition cannot dilute a real hotspot.

## Open questions
- The rules that define "verbose" or "complex" are themselves written by humans. Is this where human taste stays in the loop, and the line between what the environment enforces and what review covers?
