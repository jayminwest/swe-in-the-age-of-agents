# Book Spine

The living plan for this book. Nothing gets drafted as prose until the layer above it is locked.

**Status:** Layer 2 in progress. Layers 3–6 blocked.

---

## How this document works

Planning proceeds top-down in layers. A layer is *locked* when it stops changing; work never starts on a layer whose parent is still open. This is deliberate — the failure mode of the previous version was accumulating good sections that no spine held together.

| Layer | Contents | Status |
|-------|----------|--------|
| 0 | Inputs and governing rules | locked |
| 1 | Title and thesis | open |
| 2 | The ladder skeleton — name, change, binding constraint, unlock | **in progress** |
| 3 | Chapter theses (one sentence each) | blocked on 2 |
| 4 | Destination map — every candidate source → home / kill / reference | blocked on 3 |
| 5 | Per-chapter section outlines | blocked on 4 |
| 6 | Prose | blocked on 5 |

`chapters/` does not exist and should not be created until Layer 3 is locked.

---

## Layer 0 — Inputs

Source material lives in the predecessor repo, which is frozen for reading only:

- `~/Projects/agentic-engineering-knowledge-base/` — 204,000 words of authored prose across 12 chapters. Treat as a quarry, not a baseline. Reuse is a deliberate act, recorded in the Layer 4 destination map.
- `08052026-editorial-pass.md` — the human read-through that started this.
- `08052026-spine-rework.md` — the structural outline this document supersedes.

### Governing rules (locked)

1. Spine chapters carry zero model names, zero version numbers, zero "as of" claims, zero pricing, zero benchmarks.
2. Reference material may be dated, and must be labeled as a snapshot with `last_verified`.
3. Assume frontier models throughout. A better model should raise the system's capacity for free. The book outlives model generations.
4. The agentic loop — trigger → model → tool calls → results → repeat until stop — is the durable concept. Never dressed up in fad terminology.
5. Skills, subagents, workflows, and vendor features are abstractions composed from the primitives. They are classified, never added to the foundation.
6. Hard rules live in code, not in prompts. Anything a prompt begs an agent not to do is a check that was not written.
7. Durability test, applied per paragraph: mentally delete every proper noun, version number, and date. The argument must still stand.

See `STYLE_GUIDE.md` for voice, evidence standards, and the three-tier claim classification. The style guide predates this rework and needs one editing pass against these rules — tracked in Open Questions.

### Reader precondition (locked)

The reader already uses AI in some capacity. Everyone in software engineering does. "Never used an agent" is not a rung and gets no chapter — at most a short on-ramp section early in Part II for readers arriving from casual use.

---

## Layer 1 — Title and thesis

**Title:** TBD. Working candidates, decision deferred (blocks nothing):

- Software Engineering in the Age of Agents — *From Conversation to Delegation*
- Engineering for Agents
- Working Effectively with Agents

**Thesis:** TBD. One sentence the whole book proves.

Candidate residue carried over from the predecessor: *leverage increases as reliance shifts from the prompt to the environment.* If this is the thesis, every rung must demonstrate the shift. If it is not, the ladder needs a different engine.

---

## Layer 2 — The ladder skeleton

Two ladders. The individual ladder is treated first and lays the foundation; the organizational ladder expands beyond the single engineer. Both audiences are first-class.

Each rung answers four questions. The third is the hard one — the binding constraint at a rung is the entire reason the next rung exists.

- **What changes** — what the engineer does differently here.
- **What binds** — the constraint that caps this rung no matter how well it is executed.
- **What unlocks** — the practice or shift that breaks the binding constraint.
- **Chapter thesis** — deferred to Layer 3.

### Part I — Foundations

Two chapters, short. Not a component tour.

#### Ch 1 — The Worldview

- Defines the agentic loop. First concept in the book.
- One paragraph on next-token prediction. Shared mental model, nothing more.
- Working analogy: intelligence on tap. Capability is provisioned; the system controls the flow.
- Thesis: agents are an environment problem. Trust the environment, not the model.
- Map of the book: two ladders. The reader locates themselves.

#### Ch 2 — The Primitives

Five primitives, durable definitions only.

| Primitive | Question it answers |
|-----------|---------------------|
| Trigger (Prompt) | What begins the loop? Human messages are one kind; hooks, schedules, CI events, and other agents are others. |
| Model | How much intelligence does this task require? |
| Context | What tokens does the model see on each iteration? |
| Tools | What actions can the model take? |
| Harness | How do the other four operate together? |

Closes with the primitives-versus-abstractions taxonomy.

**Open:** the harness foundation is roughly 9,700 words in the predecessor and cannot fit here alongside four other primitives. Either Part I is three chapters, or most of the harness material moves down the ladder to where it is used. Unresolved.

### Part II — The Individual Ladder

Rung names are placeholders. Naming them is part of Layer 2.

#### Rung 1 — Single Conversation

- **What changes:**
- **What binds:**
- **What unlocks:**

#### Rung 2 — Parallel Sessions

- **What changes:**
- **What binds:**
- **What unlocks:**

#### Rung 3 — Orchestration

- **What changes:**
- **What binds:**
- **What unlocks:**

#### Rung 4 — Non-Conversational Delegation

The chat pattern disappears. Triggers replace prompts. Success is the only destination: gates, tests, lint, and checks make incorrect work unable to land.

Stated plainly at this rung: a strict environment guarantees *built correctly*, not *worth building*. Design becomes the bottleneck.

- **What changes:**
- **What binds:**
- **What unlocks:** — or: this is the top of the individual ladder and what it unlocks is Part III.

### Part III — The Organizational Ladder

#### Stage 1 — Adoption

- **What changes:**
- **What binds:**
- **What unlocks:**

#### Stage 2 — Environment Readiness

The codebase as the product surface for agents. Trust and permissions at team scale; security enforced by the harness, never by prompts.

- **What changes:**
- **What binds:**
- **What unlocks:**

#### Stage 3 — Automated SDLC

- **What changes:**
- **What binds:**
- **What unlocks:** — or: this is the end state.

### Part IV — Reference

Dated content permitted, labeled with `last_verified`. Cross-indexed by rung and stage. Nothing here is load-bearing for the spine.

---

## Layer 3 — Chapter theses

Blocked. One sentence per chapter, stating what it argues rather than what it covers.

## Layer 4 — Destination map

Blocked. Every candidate source section gets exactly one line: destination, and reuse policy (lift / heavy edit / rewrite from the thesis down).

Known orphans from the predecessor outline — material with no assigned home, roughly 35,000 words:

| Source | Words | Note |
|--------|------:|------|
| Harness foundation (what is a harness, stack, categories, control system) | 9,765 | See the Ch 2 open question. |
| Tool design, tool selection | 2,387 | Candidate for Ch 2. |
| Model evaluation | 5,782 | Overlaps evaluation material at Rung 2. |
| Model limitations and workarounds | 2,802 | Much of it version-bound; may not survive rule 1. |
| Specs as source code, context as code | 4,093 | Rung 4 or the reference catalog. |
| ReAct, multi-agent collaboration | 4,326 | Rung 3, or lineage-framed per the style guide. |
| Prompt structuring, prompt language | 6,361 | More than Rung 1 can absorb as written. |

## Layers 5–6

Blocked.

---

## Kill list

Removed from the spine entirely. Recorded here so the decisions are not relitigated.

- The twelve leverage points, as concept and as framing. Durable residue only: leverage increases as reliance shifts from prompt to environment.
- ADW terminology, everywhere.
- "Loop Engineering" as a named discipline. The agentic loop stays; the label goes.
- Model routing tables, provider behavioral profiles, and benchmark tables in spine chapters. Reference or delete.
- If/then prompting and prompt-embedded checklists as recommended practice.
- Heavy attribution to any single external site.

---

## Open questions

- The thesis sentence (Layer 1).
- Rung and stage names — these become chapter titles.
- Whether Part I is two chapters or three, driven by where the harness foundation lands.
- Target length. The predecessor is 204,000 words. Unstated target means unbounded scope.
- What grounds claims once vendor names, benchmarks, prices, and dates are gone. Three evidence categories remain — observable behavior, documented patterns, reproducible examples — and they have to carry the whole book. This constrains what can be claimed, not just how it is cited.
- One editing pass on `STYLE_GUIDE.md` against the governing rules above.
- Publishing and repository cutover from the predecessor. Deferred; not blocking.

---

## Decision log

| Date | Decision |
|------|----------|
| 2026-08-05 | Ladder is the spine; primitives are a short foundation, not a component tour. |
| 2026-08-10 | "Never used an agent" is a precondition, not a rung. Short on-ramp section at most. |
| 2026-08-10 | New repository. Predecessor stays readable and unfrozen for now; retirement deferred. |
| 2026-08-10 | Carry-over limited to the style guide, markdown lint config, and the frontmatter validator. No agent machinery. |
