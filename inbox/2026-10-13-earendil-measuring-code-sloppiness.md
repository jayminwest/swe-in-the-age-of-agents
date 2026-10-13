source: link dropped by Jaymin in interview Q2, 2026-10-13
url: https://earendil.com/posts/measuring-code-sloppiness/
touches (guess): gen/ Ch6, Agents are an Environment Problem
note: AGENT SUMMARY, not verbatim. Fetch tool truncated quotes at ~125 chars; text in "quotes" is exact, the rest is paraphrase. Model names in the post are snapshot material and stay out of prose.

# "Measuring the Sloppiness of Code" (Earendil, likely Sebastian; Thu, 10 Sep 2026)

## Core argument
LLMs write near-correct code because correctness is verifiable ("checked by hidden tests, which results in a clear reward signal"). Sloppiness (needless abstractions, duplicates, bad decisions, LOC explosion) has no such signal and "often requires human intuition and taste." Agents can't clean it up either: "bad coding decisions accumulate over time." Conclusion: "human intuition and taste are still either implicitly or explicitly baked into the evaluation."

## Measures considered
- AI judge: "from my observations it rarely works"; 1-10 scoring "is basically equivalent to a random number generator"; pairwise judging flips preference when solutions are renamed. "Asking LLMs to judge the code they write is not a substitute for a proper evaluation."
- Human judge: best for readability, not scalable.
- Delta LOC: "surprisingly effective metric for sloppiness", but Goodhart's law applies.
- Verbosity (SlopCodeBench): |AST-Grep flagged lines ∪ clone lines| / LOC. Rules are handcrafted heuristics, "the human aspect of it all."
- Erosion (SlopCodeBench): "how much of a codebase's mass is concentrated in a few large and complex functions." mass(f) = CC(f)·sqrt(SLOC(f)); erosion = mass of functions with CC > 10 / total mass.

## Results
- Established repos: verbosity 0.15 ± 0.06, erosion 0.31 ± 0.17. Agent code: 0.33 ± 0.10, 0.68 ± 0.20. "roughly twice as verbose and eroded as human code."
- Iterative benchmark (context wiped between checkpoints, mimicking real use): strict solve rate 0% even for frontier models.
- Future directions: "coupledness of functions, code churn, cohesion."

## Gaps relative to Jaymin's Q1/Q2
- No file-level size discussion; consolidation measured only at function level (erosion).
- No environment-side prevention described; the post measures, it doesn't ratchet.

Linked, not fetched: SlopCodeBench (arxiv 2603.24755), judge-bias paper (arxiv 2604.16790).
