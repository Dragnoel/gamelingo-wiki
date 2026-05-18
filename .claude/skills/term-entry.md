# term-entry — auto-loaded when writing JSON term entries

## When this guide applies
Auto-load whenever creating or editing a file in entries/. This supplements the schema in CLAUDE.md.

## ID assignment
- Check entries_index.json for the highest existing ID number.
- Assign the next available integer, zero-padded to 5 digits.
- Run python3 build/get_entry_path.py <id_with_romaji> to confirm the correct subdirectory.
- Never reuse or skip IDs.

## Required field discipline
Every entry must have all required fields populated before the session ends:
- headword_jp: {kanji|reading} notation; no plain kanji without furigana.
- reading: hiragana only.
- romaji: Hepburn romanization, lowercase, underscores for spaces.
- kanji_form: the standard kanji spelling, or null if none.
- katakana_form: the katakana loanword form if one exists, or null.
- definitions: at least one sense; each sense must have gloss_en, gloss_jp, orthography_notes, implicit_notes, game_setting_notes.
- examples: at least one, with source traced to a file in raw/.
- sources: at least one bib key from references.bib.
- metadata.furigana_verified: false until confirmed from a primary source.

## orthography_notes (required per sense)
Must address all four orthography questions:
1. Kanji form etymology — what the characters contribute to meaning.
2. Katakana form — loanword origin, semantic relationship, false-friend risk.
3. Domain-specific orthographic variation — which game types use which form.
4. Hiragana register — casual, digital, or children's text usage if applicable.
If any question cannot be answered from sources, add {{unverified}} and a _review.md item.

## implicit_notes (required per sense)
Document what the term implies beyond its dictionary gloss:
- Social or ludic obligations encoded in the term.
- Connotations absent from the English equivalent.
- Cultural framing (failure, stewardship, competition, cooperation).

## game_setting_notes (required per sense)
State how usage differs across: board games, card games (TCGs), video/mobile games, TTRPGs.
If a domain is unknown, say so and add a _candidates.md item for a source that would resolve it.

## After writing an entry
1. Add to entries_index.json.
2. Run python3 build/render_entries.py.
3. Run python3 build/validate_entries.py.
4. Fix any reported errors before ending the session.
