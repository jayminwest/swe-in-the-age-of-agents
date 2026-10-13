source: Jaymin's own repos, pointed at in interview Q2 (2026-10-13): ~/Projects/scaffold-project, ~/Projects/os-eco/trellis
touches (guess): gen/ Ch6, Agents are an Environment Problem
note: AGENT EXTRACTION. Text in "quotes" is Jaymin's own writing, with file:line. Everything else is the agent's paraphrase. Altitude rule (Jaymin, Q2): mindset and philosophy, never a tool checklist. The Trellis name stays out of prose.

Abbreviations: PHIL = scaffold-project/templates/common/docs/PHILOSOPHY.md, SP = scaffold-project, TR = os-eco/trellis

## His own origin phrasing
- "Agents are not a hiring problem. They're an environment problem." (TR `git show f1b3165:SPEC.md`:47-48)
- "An AI-ready codebase is one where (a) any change is verifiable in under 60 seconds, (b) the repo answers its own onboarding questions, (c) every standard is enforced by a machine, (d) every action is reversible, and (e) the team treats agents as users they're designing for." (same file :41-45, quoting his ai-readiness-principles.md)

## Principles
- Complexity is the root enemy: "Complexity is anything that makes the system hard to understand or change… change amplification… cognitive load… unknown unknowns" (PHIL:10-14). "The rules apply to humans and agents alike. The quality gates enforce what they can. Review enforces the rest." (PHIL:4-6)
- Strategic, not tactical: "'Just get it working' is how complexity piles up, and it piles up one reasonable shortcut at a time." (PHIL:39-40)
- Ratchets only tighten: "Coverage floors rise, and size, debt and duplication budgets fall. Loosening one is a deliberate, reviewed commit with a reason. Nothing is grandfathered at birth." (PHIL:80-82). "loosening requires an explicit commit by a human" (SP/templates/ts/base/budgets/coverage-budgets.json:2). "To grow past the ceiling: refactor first; do NOT raise the number — that would defeat the guard." (SP/templates/ts/base/scripts/check-file-sizes.ts:16-17). Floors start at reality: "Coverage floors start at what the first green run observed, rounded down." (SP/scripts/bootstrap.sh:30)
- One verify gate, hook = CI: "`verify` runs every gate, locally, in the pre-commit hook and in CI, which run the same thing. If a gate is too slow for the hook, make it faster. Do not skip it." (PHIL:86-88). Parity enforced: "a gate can never silently vanish from (or never reach) CI" (check-ci-parity.ts:12-14)
- Hard rules in code: "every standard is enforced by a machine" (original SPEC:43). "Never commit or push red." (SP/SKILL.md:21). "A red gate is fixed, never explained away." (PHIL:95-96). Exceptions carry reasons, never bare allows (SP/templates/common/AGENTS.md:49)
- One core, thin front ends: "Domain logic lives in a core library… The CLI, GUI and service only translate input into calls and results into output, so each capability has one implementation." (PHIL:47-50). "A front end that reimplements logic is a bug." (ARCHITECTURE.md:22-23). "Parity is mechanical (deep-equal tests), not aspirational." (TR/SPEC.md:36-37)
- Deep modules, not short files: "A shallow module… costs more than it gives. Do not split code just to make files or functions short." (PHIL:20-21). "Add an abstraction… when the second implementation arrives, not on speculation." (PHIL:75-76)
- Define errors out of existence: "Design the API so the error cannot happen (deleting a missing key succeeds, an empty range is a valid range) before you add a code path for it. Each error that remains gets a stable code and a hint that tells the caller what to do." (PHIL:32-35)
- Docs current, machine-checked: "Update it in the same commit as any change to a contract." (AGENTS.md:25). Agent-doc commands/paths validated to exist. "Every TODO/FIXME/HACK/XXX cites a tracker id… on the same line." (AGENTS.md:55)
- One agent doc for every harness (AGENTS.md:5).
- Evidence: "'All gates green' is necessary, not sufficient: refactors also check paths the tests do not import" (PHIL:89-91)
- Standard lives in one place: "The templates are the standard. Edit them here, never in a generated project" (SP/SKILL.md:69-70)

## What the sloppiness tool is for (unnamed in prose)
- Problem: "A refactor spans more files than expected. Similar logic starts appearing in several places. Modules depend on each other in both directions. The codebase still builds, but working in it takes more effort." (TR/README.md:17-19)
- Approach: deterministic, no model. "how sloppy is this TypeScript tree, where exactly, and is it getting worse?" (TR/SPEC.md:39-40)
- "A repo with perfect tooling and sloppy code scores sloppy" (SPEC.md:163-166). "Large clean additions cannot erase hotspot findings" (SPEC.md:168-171)
- Anti-gaming: "Do not add indirection merely to improve metrics." "An unchanged score can accompany a useful change; a lower score can accompany a worse design." "Do not chase zero." "Treat rankings as leads, not a mandate" (TR/src/guides/cleanup.ts)
- Pivot (Sep 2026): from an LLM-assisted readiness rubric (does the repo have the right tooling) to deterministic code measurement. "Combining safeguard configuration with structural score is rejected because tooling must not offset code debt." (plan pl-b2ea)

## Mechanism categories (illustrations only)
Size budgets; coverage floors; debt-marker accountability; duplication budgets; dead-code checks; strict typing with reasoned exceptions; gate parity; doc-truth checks; structural-debt baselines (complexity, erosion, cycles); output/error contracts; canonical template standard.

## Tensions (candidate interview questions)
1. Size budgets vs deep modules ("Do not split code just to make files or functions short").
2. Goodhart: every ratchet can be gamed by an agent; metrics are leads, not verdicts.
3. "Every standard enforced by a machine" vs "Review enforces the rest".
4. Is the environment the cause of good code or its scaffolding? (the tooling-must-not-offset-debt pivot)
5. "Only a human loosens a ratchet" when agents write the commits: enforcement unclear.
6. Provisional score used as a CI gate.
7. "Verifiable in under 60 seconds" with no gate-runtime budget.
