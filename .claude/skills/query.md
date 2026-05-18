# /query — Gaming Language Wiki

## Purpose
Research a specific question using only existing wiki/ pages and references.bib.
Do not use raw/ files directly — raw/ knowledge enters the wiki only through /ingest.
At the end, offer to file the answer as a new wiki/ page.

## Procedure

### 1. Understand the question
Restate the question in neutral, encyclopedic terms. Identify what type of wiki page the answer would produce:
- A comparison/ page (JP vs EN usage, two terms, two game domains)
- A mechanic/ page (a specific game mechanic)
- An addition to an existing page

### 2. Research using wiki/ only
Search:
  grep -r "<term>" wiki/
  grep -r "<term>" entries_index.json
Do not read raw/ files. Do not use training-data knowledge as a source.
Cite every claim with the wiki page or bib key it comes from.

### 3. Draft the answer
Write the answer in encyclopedic prose. Follow guides/style.md.
Mark any claim that cannot be sourced to an existing wiki page as {{unverified}}.
If important claims are missing from the wiki, note: "This question requires an /ingest session to add [source] before a full answer is possible."

### 4. Offer to file back
After the answer, ask:
"File this as wiki/comparisons/<slug>.md? (yes / no / suggest different path)"
If yes, write the page using freeform entity page structure from CLAUDE.md.
If the answer contains {{unverified}} markers, add items to wiki/_candidates.md for the next /ingest.

## Hard prohibitions during /query
- Do not read or cite raw/ files.
- Do not use training-data knowledge as a citation.
- Do not write to entries/ or run build scripts.
