# jp-en-comparison — auto-loaded for JP↔EN comparative analysis

## When this guide applies
Auto-load whenever writing or editing pages in wiki/comparisons/, or when a /query session produces a comparative answer to be filed back.

## Comparison page (wiki/comparisons/<slug>.md)

### Frontmatter
```yaml
---
title: <Comparison Title — e.g. "Randomization: JP vs EN board-game rulebooks">
type: comparison
draft: false
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - <bib-key-or-filename>
---
```

### Body structure
1. Lead (≤ 80 words): what is being compared, which sources inform the comparison, what the key finding is.
2. ## In Japanese — how the concept is expressed in JP sources, with wikilinks to term entries and cited examples.
3. ## In English — how the concept is expressed in EN sources, with wikilinks and cited examples.
4. ## Points of divergence — specific differences in register, orthography, implicit meaning, or domain usage.
5. ## Points of convergence — where JP and EN usage aligns (if applicable).
6. ## Unresolved questions — claims that require additional sources to confirm; add each to _candidates.md.
7. ## See also
8. ## References

## Standards for comparative claims
- Every comparative claim ("JP rulebooks prefer X while EN rulebooks use Y") requires at least one sourced example from each language.
- Do not assert a claim about one language's usage based solely on the other's absence.
- Domain scope must be stated: "in board game rulebooks", "in TCG card text", "in video game UI", etc.
- Do not infer general cultural meaning from game-domain evidence. State the evidence and its scope.

## Handling asymmetry
If a concept exists in one language but lacks a direct equivalent in the other:
- Document the gap explicitly ("English has no direct equivalent to 手番's obligation connotation").
- Link to the closest approximations with a note on the semantic distance.
- Do not supply an invented translation — flag in _review.md if a translation choice is contested.

## Wikilinks in comparison pages
- Every JP term referenced should link to its term entry: [[Teban]] or [[手番]].
- Every EN term with a term entry should be linked similarly.
- Game titles link to wiki/games/ pages; mechanics link to wiki/mechanics/ pages.
