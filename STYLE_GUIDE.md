# Style Guide

How `gen/` prose is written. Reference voice: `human/chapter-1.md`, `human/chapter-2.md`. The
governing rules in `BOOK_SPINE.md` Layer 0 override this file where they conflict.

**Target:** tight, information-dense, terse. Every sentence carries a fact, a definition, or a
consequence. Anything else is cut.

---

## Voice

- Third person by default. Occasional "we" and "this book" are allowed, as in ch1 ("we must understand", "this book will not").
- No "I", no "you". Direct guidance uses the imperative: "Validate tool outputs."
- Active voice. Name the actor. Passive only when the actor is unknown or irrelevant.
- Plain and declarative. Define, then state the consequence.
- Confident. Hedge only when the uncertainty is real, and then say what is uncertain.

## Density

- One idea per paragraph. 2-4 sentences.
- Definition first. The first 1-2 sentences of a concept answer "what is this and why does it matter".
- Say a thing once. No summaries of what was just said, no previews of what comes next.
- Prefer one precise sentence to two approximate ones.
- No markdown tables. Use a list or prose. Numbered lists for steps, bullets for attributes and taxonomies.

## Evidence

Claims rest on Jaymin's experience (from interviews), sources he drops in `inbox/`, observable model
behavior, or a reproducible example. Nothing else.

- Write experience as third-person observation of a recurring behavior: "Agents in an unprepared codebase tend to...", not "In my work...".
- Cite only sources in `inbox/`. No outside citations.
- If a claim needs support that the sources do not give, it goes to the concept's `## Open questions`, not into prose.

## Durability

The test: mentally delete every proper noun, version number, and date. The argument must still stand.

- **Law:** rooted in information theory, economics, control theory, or human factors. Outlasts any model. Write it as plain, load-bearing prose.
- **Heuristic:** a current rule of thumb whose exact value drifts ("keep the toolset small"). State the rule and the force beneath it.
- **Snapshot:** models, tools, vendors, prices, benchmarks, dates. Not in concept prose.

- No temporal superlatives: "cutting-edge", "state-of-the-art", "the latest", "currently the best".
- Prefer the force to the figure. When a number appears, give the reason behind it.
- Dead ends are durable. Why an approach failed is permanent data.

## Terms

- **Bold** a term where it is defined. Define it before using it.
- One term per concept. Once "context" is defined, never switch to "window contents" or "memory".
- Expand jargon on first use.

## Concept files

```markdown
---
status: draft | reviewed | yours
sources: [human/PLANNING.md, inbox/interviews/2026-10-13-environment.md]
related: [context, harness]
---
# Concept Name

Definition. Why it matters.

How it works / how to apply it.

## Open questions
- Things the sources do not settle. Optional.
```

- 200-800 words of prose.
- H1 is the concept name. H2 for sections, rarely H3.
- Examples only when they carry the point. Keep them minimal. Contrast fragile vs robust when that is the point.
- Links between concepts live in `related:`. No "Connections" section.
- `make validate` checks the frontmatter, em-dashes, and tables.

## Cut on sight

- Adverbs that add nothing ("really", "basically", "simply", "fundamentally").
- Em-dashes. Use a period, colon, or parentheses.
- Throat-clearing: "here's what", "it's worth noting", "it is important to understand".
- "Not X, it's Y" contrasts. State Y.
- Meta-joiners: "the rest of this section", "as we will see", "in this chapter".
- Vague declaratives: "the implications are significant". Name the implication.
- Inanimate things doing human verbs ("the decision emerges"). Name the actor.
- Rhetorical questions, colloquialisms, marketing adjectives.
- Paragraphs that end on a punchy one-liner for effect.
- Three consecutive sentences of the same length.
