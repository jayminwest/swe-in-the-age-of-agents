---
status: draft
sources: [inbox/interviews/2026-10-13-environment.md, inbox/2026-10-13-environment-philosophy-extract.md]
related: [agents-are-an-environment-problem, verification-gate, code-sloppiness]
---
# Ratchets

A **ratchet** is a quality measure that only moves in one direction. Test coverage only rises. File size, duplication, and debt only fall. A change that moves a ratchet the wrong way fails verification.

Ratchets target the main way codebases decay under agents. Complexity accumulates one reasonable shortcut at a time. No single change is the problem, so no single review catches it. A ratchet catches the sum: whatever the codebase achieved yesterday is the floor for today.

## How ratchets work

- **Start at reality.** A new ratchet records the codebase's current value. It demands no immediate cleanup. It forbids getting worse.
- **Loosening is a human act.** Raising a floor is routine. Lowering one is a deliberate, reviewed commit with a stated reason.
- **Fix the code, not the number.** A file at its size ceiling is refactored before it grows. Raising the ceiling defeats the ratchet.
- **New work starts compliant.** A new project begins inside every budget. Nothing is grandfathered at birth.

## Gaming

A ratchet is a metric, and an agent optimizing against a metric can satisfy it without improving the code. A file split into shallow fragments meets a size budget and worsens the design. Indirection added to move a score adds complexity. Ratchet values are leads that point at problems. An unchanged score can accompany a useful change, and a lower score can accompany a worse design.

## Open questions
- Who loosens a ratchet when agents write the commits? Is "a human commits it" enforced or trusted?
- Size budgets push toward splitting. The deep-module rule says "Do not split code just to make files or functions short." How does the book reconcile the two?
