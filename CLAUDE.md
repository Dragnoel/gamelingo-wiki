# Gaming Language Wiki — agent schema

## Before doing anything in a session, read (in order):
1. PROJECT_STATUS.md — what happened last session and what to do first
2. CLAUDE.md (this file)
3. guides/style.md and guides/research.md
4. The relevant .claude/skills/ file for the task type

## At the end of every session, update PROJECT_STATUS.md:
- Entries created/edited (with counts)
- Pages created/edited
- Items added to _review.md and _candidates.md
- Any unresolved questions
- What the next session should start with

## Purpose
This wiki documents the language of play in board games, video games, TTRPGs,
and related forms, with focus on Japanese↔English comparative usage. Emphasis
on implicit meanings, orthographic choices (kanji vs katakana vs hiragana), and
how the same concept differs across game settings. It is a reference, not an essay.

## Two-track structure
- **Terms (JSON source):** All JP↔EN term pages live as JSON in entries/.
  The agent writes JSON; build/render_entries.py generates wiki/terms/ markdown.
  Never edit wiki/terms/ directly.
- **Entity pages (freeform markdown):** games/, mechanics/, genre-conventions/,
  comparisons/, source/ are written as markdown directly in wiki/.

## Folder rules
- raw/ — read allowed, writes blocked. Never write to it.
- references.bib — read-only.
- build/ — read and run allowed, edits blocked.
- entries/ — agent writes JSON term entries here.
- wiki/ — agent writes entity pages here.
  wiki/terms/ is generated; do not edit directly.
- queries/ — saved Q&A and _cleanup.sh.
- PROJECT_STATUS.md and PROJECT_CONTEXT_BRIEF.md — agent updates these.
- entries_index.json — update whenever an entry is added or removed.

## Numeric entry IDs
Every term entry: 5-digit zero-padded ID + romanized reading.
  00001_teban, 00002_tempo, 00003_tsu_tsumu, …
Directory: IDs 00000–00499 → entries/00000/, 00500–00999 → entries/00500/, etc.
Use: python3 build/get_entry_path.py <entry_id>

## JSON entry schema (see build/schema.json for machine-readable version)

```json
{
  "id": "00001_teban",
  "headword_jp": "{手|て}{番|ばん}",
  "headword_en": "turn / one's turn to act",
  "reading": "てばん",
  "romaji": "teban",
  "kanji_form": "手番",
  "katakana_form": null,
  "alt_forms": [
    {
      "form": "テンポ",
      "reading": "てんぽ",
      "note": "False friend: テンポ is a loanword meaning pace or momentum, not turn."
    }
  ],
  "part_of_speech": "noun",
  "register": ["in-game", "rulebook"],
  "domain": ["board", "card", "ttrpg"],
  "definitions": [
    {
      "sense_number": 1,
      "gloss_en": "one's turn to act; the right and responsibility to move",
      "gloss_jp": "自分が行動できる順番",
      "explanation_en": "The period in which a player exercises agency.",
      "implicit_notes": "...",
      "orthography_notes": "...",
      "game_setting_notes": "..."
    }
  ],
  "usage_jp": "...",
  "usage_en": "...",
  "comparative_notes": "...",
  "examples": [
    {
      "id": "00001_teban_ex1",
      "japanese": "あなたの{手|て}{番|ばん}です。",
      "english": "It is your turn.",
      "source": "raw/manuals/some-rulebook.pdf",
      "sense_numbers": [1]
    }
  ],
  "cross_references": [
    { "type": "contrast", "id": "00002_turn", "note": "ターン (loanword variant)" }
  ],
  "sources": ["costikyan-2013-uncertainty"],
  "metadata": {
    "created": "YYYY-MM-DDTHH:MM:SSZ",
    "modified": "YYYY-MM-DDTHH:MM:SSZ",
    "furigana_verified": false,
    "reviewed": false
  }
}
```

## Generated wiki/terms/ page structure (for reference — do not write by hand)
1. Lead (≤ 80 words): headword in JP with furigana, romaji, plain EN gloss.
2. ## Orthography notes
3. ## Implicit meanings
4. ## Differences across game settings
5. ## Usage in Japanese
6. ## Usage in English
7. ## False friends and near-misses
8. ## Examples (from sources only)
9. ## See also
10. ## References

## Freeform entity page structure (games/, mechanics/, etc.)
1. Lead paragraph (≤ 80 words).
2. Body sections as needed.
3. ## See also
4. ## References

## Furigana notation
{kanji|reading} in all JP text fields.
  {食|た}べる, {手|て}{番|ばん}, {行|こう}{動|どう}
Run python3 build/validate_entries.py after writing entries to check syntax.
See guides/furigana.md and .claude/skills/furigana-guide.md.

## Kanji vs katakana analysis (required for every term entry)
For every term, explicitly document in the entry:
- Does a kanji form exist? What does the etymology reveal?
- Does a katakana form exist? Loanword, emphasis, or false friend?
- Does the orthographic choice differ by game domain?
- Are there hiragana forms with different register?
Uncertainty: {{unverified}} + flag in wiki/_review.md.

## Wikilink conventions
- Title Case always. JP term pages: primary at romanization, stub at JP form.
- Cross-link alt forms to the primary with a semantic note.

## Sourcing rules
- Every non-trivial claim has a footnote.
- Unlocatable: {{unverified}} + wiki/_review.md.
- Quotes ≤ 15 words; one per source per page.

## What the slash commands do
- /ingest: Create source/ pages from raw/ files. Extract terms → write JSON
  in entries/ (use build/get_entry_path.py for correct directory) → run
  python3 build/render_entries.py. Write game/mechanic entity pages as markdown.
  Update entries_index.json and PROJECT_STATUS.md.
- /query: Answer using wiki/ + references.bib only. Offer to file back.
- /lint: Run guides/lint-checklist.md. Run python3 build/validate_entries.py.
  Regenerate PROJECT_CONTEXT_BRIEF.md. Output to wiki/_lint-report.md. Propose only.
- /cleanup: Write proposed deletions to queries/_cleanup.sh. Do not run it.
  Format: #!/usr/bin/env bash / set -euo pipefail / rm "path"   # reason

## Hard prohibitions
- Do not write to raw/, references.bib, CLAUDE.md, guides/, or build/.
- Do not edit wiki/terms/ directly — always edit entries/ JSON, then re-render.
- Do not run chmod, chflags, rm, mv, git push, sudo, curl, or wget.
- Do not delete files — use /cleanup for a reviewed script.
- Do not invent JP terms, readings, or furigana — mark {{unverified}}.
- Do not assert a kanji reading without a source or validate_entries.py confirmation.
- Do not write in first person or essay style.

## _review.md vs _candidates.md
- wiki/_review.md: unverified claims, furigana needing dictionary verification,
  contested cross-references, disputed orthographic notes. Human resolves.
- wiki/_candidates.md: terms, games, mechanics, or comparisons to create in a
  future session. Format:
  - [ ] テンポ (tempo) — video-game pace sense; raw/articles/video-game-tempo.pdf
  - [ ] アクション vs 行動 — domain-split analysis (board vs video)

## Open questions flagged in _review.md
- Term canonicalization when JP/EN communities use the same loanword differently.
- Game-internal terms existing only in localization (e.g. "PSI" in MOTHER 2 / EarthBound).
- Katakana loanwords with drifted meanings: スキル vs 技.
