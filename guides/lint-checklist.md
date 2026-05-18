# Lint checklist — Gaming Language Wiki

Run this checklist in full during every /lint session. Output results to wiki/_lint-report.md.
Propose changes only — do not make edits during a lint session.

## 1. Entry validation
- [ ] Run python3 build/validate_entries.py — record all errors.
- [ ] All entries in entries_index.json have a corresponding JSON file in entries/.
- [ ] All JSON files in entries/ are listed in entries_index.json.
- [ ] No duplicate entry IDs.
- [ ] All cross_reference IDs resolve to known entries.

## 2. Furigana audit
- [ ] All entries with furigana_verified: false are listed in _review.md.
- [ ] No entry has a katakana_form without documentation in alt_forms[].note or orthography_notes.
- [ ] No entry has an empty reading field.

## 3. wiki/terms/ currency
- [ ] Run python3 build/render_entries.py — confirm rendered count matches entries_index.json count.
- [ ] No .md files in wiki/terms/ that do not correspond to a JSON entry (orphan renders).

## 4. Source page coverage
- [ ] Every file in raw/ has a corresponding page in wiki/source/.
- [ ] Every wiki/source/ page has a bib key in references.bib.
- [ ] No orphan bib keys (bib entries not cited by any wiki page or entry).

## 5. Cross-link integrity
- [ ] All [[Wikilinks]] in wiki/ pages resolve to existing pages or entries.
- [ ] All {{unverified}} markers have a corresponding item in wiki/_review.md.

## 6. Frontmatter audit (freeform pages)
- [ ] All pages in wiki/games/, wiki/mechanics/, wiki/genre-conventions/, wiki/comparisons/, wiki/source/ have valid frontmatter (title, type, draft, created, updated, sources).
- [ ] No page has draft: true unless intentionally staged.

## 7. _review.md and _candidates.md
- [ ] _review.md items are still unresolved (remove any that have been addressed).
- [ ] _candidates.md items link to a raw/ source where applicable.

## 8. PROJECT_CONTEXT_BRIEF.md regeneration
After completing the checklist, regenerate PROJECT_CONTEXT_BRIEF.md with current counts:
- Total entries (entries_index.json length)
- Pages by type (wiki/games/, wiki/mechanics/, etc.)
- Open _review.md items (count)
- Open _candidates.md items (count)
- Last lint date
