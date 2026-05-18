# Furigana notation reference — Gaming Language Wiki

## Notation format
All Japanese text in JSON entry fields uses {kanji|reading} notation:

  {手|て}{番|ばん}        → 手番 read てばん
  {行|こう}{動|どう}      → 行動 read こうどう
  {食|た}べる             → 食べる, only the kanji portion annotated

## Rules
- One {kanji|reading} block per kanji unit. Do not span multiple characters in one block unless they form a single lexical unit with a single reading.
- The reading must be hiragana only. No katakana, romaji, or mixed readings in the furigana field.
- For okurigana (kana suffixes on kanji), include only the kanji in the base, not the okurigana:
    Correct:   {食|た}べる
    Incorrect: {食べ|たべ}る
- Do not add furigana to pure kana words (hiragana or katakana only).
- Do not add furigana to romaji or numbers.

## Validation
Run python3 build/validate_entries.py to check all entries for:
- Malformed {kanji|reading} syntax (unclosed braces, non-hiragana readings)
- Furigana base with no kanji
- furigana_verified: false flag

## Kanji vs katakana analysis (required in every entry)
For every term entry, the definitions[].orthography_notes field must address:
1. Does a kanji form exist? If so, what does the character etymology contribute to meaning?
2. Does a katakana form exist? Is it a loanword, an emphasis marker, or a false friend?
3. Does the orthographic choice vary by game domain (board vs video vs TTRPG vs card)?
4. Are there hiragana forms, and do they carry a distinct register (casual, written, digital)?

## Katakana loanword handling
When katakana_form is populated:
- Document whether the katakana form is semantically equivalent, a near-miss, or a false friend.
- Note the origin language if known.
- Flag in alt_forms[].note if the loanword has drifted in meaning within the gaming domain.

## Uncertainty protocol
- If a reading cannot be confirmed from a source in raw/, set furigana_verified: false.
- Add an entry to wiki/_review.md: "Furigana unverified: [term] — needs confirmation against [source type]."
- Do not guess or infer readings from analogous kanji. Mark {{unverified}} inline.

## Game-specific terms
Proprietary card names, invented mechanics, and designer jargon may not appear in standard dictionaries.
pykakasi and JMDICT are unreliable for these. Always require a primary source (manual, official site,
designer statement) before setting furigana_verified: true.
