# furigana-guide — auto-loaded when furigana is involved

## When this guide applies
Auto-load whenever writing or editing headword_jp, reading, or examples[].japanese fields in any entry JSON,
or whenever a session involves Japanese text annotation.

## Quick reference

| Correct | Incorrect |
|---|---|
| {手|て}{番|ばん} | {手番|てばん} |
| {食|た}べる | {食べ|たべ}る |
| てばん (reading field) | テバン, teban |
| {行|こう}{動|どう} | {行動|こうどう} |

## Rules (summary — full reference in guides/furigana.md)
1. One {kanji|reading} block per kanji unit.
2. Reading must be hiragana only.
3. Okurigana stays outside the braces.
4. Do not annotate pure kana, romaji, or numbers.
5. Do not guess readings — mark {{unverified}} and add to _review.md.

## Validation command
```
python3 build/validate_entries.py
```
Run after writing any entry. Fix all errors before ending the session.

## furigana_verified field
- false (default): reading is present in the entry but has not been confirmed against a primary source.
- true: reading confirmed from game manual, official publisher material, or designer statement in raw/.

Never set furigana_verified: true based on dictionary lookup alone for game-specific or invented terms.

## Common errors to watch for
- Compound kanji split incorrectly: {手番|てばん} should be {手|て}{番|ばん}
- Katakana in reading field: ターン should be たーん in reading, ターン in katakana_form
- Mixed script in headword_jp: the field should contain only the Japanese form with furigana notation, not romaji
- Missing furigana on rare or obscure kanji: if uncertain, mark {{unverified}}

## Katakana false friends (examples requiring orthography_notes)
- テンポ (loanword: tempo/pace) vs {手|て}{番|ばん} (native: one's turn)
- スキル (loanword: skill/ability slot) vs {技|わざ} (native: technique/move)
- ターン (loanword: turn) vs {手|て}{番|ばん} (native: turn, with obligation connotation)
Document all such pairs in alt_forms[].note and orthography_notes.
