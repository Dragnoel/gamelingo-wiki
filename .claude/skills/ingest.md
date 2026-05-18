# /ingest — Gaming Language Wiki

## Purpose
Process every file in raw/ that does not yet have a wiki/source/ page. For each:
1. Create a wiki/source/ page summarising the file's content and listing terms and claims found.
2. Extract JP↔EN terms → write a JSON entry to entries/ → run python3 build/render_entries.py.
3. Write game, mechanic, or genre-convention entity pages in wiki/ as freeform markdown.
4. Update entries_index.json after each new entry.
5. Update PROJECT_STATUS.md at the end of the session.

## Step-by-step procedure

### Before starting
- Read PROJECT_STATUS.md.
- Read CLAUDE.md.
- Run: `find raw/ -type f | sort` — list all raw files.
- Run: `find wiki/source/ -type f | sort` — list already-ingested files.
- The difference is the work queue.

### For each raw file not yet ingested

**1. Create wiki/source/ page**
Filename: `wiki/source/<bib-key-or-filename>.md`
Frontmatter: title, type: source, draft: false, created, updated, sources: [bib-key].
Body: 1–3 paragraph summary. Bullet list of key terms found. Bullet list of key claims.
Do not analyse or evaluate — describe what the file contains.

**2. Extract terms**
For each JP↔EN term found in the source:
- Check entries_index.json — if the term already has an entry, add the source to its sources[] array and update modified.
- If new: assign the next available 5-digit ID. Run `python3 build/get_entry_path.py <id>` to get the correct directory.
- Write the JSON entry to `entries/<dir>/<id>_<romaji>.json` following the full schema in CLAUDE.md.
- Required fields for every entry: id, headword_jp (with furigana), headword_en, reading, romaji, part_of_speech, register, domain, definitions (at least one sense with gloss_en, gloss_jp, orthography_notes, implicit_notes, game_setting_notes), examples (at least one from the source), sources, metadata.
- Set furigana_verified: false unless the reading is confirmed by the source document.
- Add {{unverified}} and a wiki/_review.md item for any reading or orthographic claim not supported by the source.

**3. Run the renderer**
After each entry (or batch):
  python3 build/render_entries.py
Confirm the output count matches entries_index.json.

**4. Write entity pages**
For named games, mechanics, or genre conventions found in the source, create or update pages in:
- wiki/games/<game-title>.md
- wiki/mechanics/<mechanic-name>.md
- wiki/genre-conventions/<convention-name>.md
Use the freeform entity page structure from CLAUDE.md. Cite only claims traceable to raw/.

**5. Update entries_index.json**
Add each new entry as: {"id": "<id>", "romaji": "<romaji>", "headword_jp": "<plain>", "headword_en": "<gloss>"}

### After all files processed
- Run python3 build/validate_entries.py — fix any reported errors before ending.
- Update PROJECT_STATUS.md: list entries created, pages created, _review.md items added, next session guidance.

## Hard prohibitions during /ingest
- Do not write to raw/, build/, guides/, CLAUDE.md, references.bib, or wiki/terms/.
- Do not invent furigana readings — mark {{unverified}}.
- Do not create entries without at least one sourced example.
