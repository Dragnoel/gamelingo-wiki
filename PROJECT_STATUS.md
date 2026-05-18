# Gaming Language Wiki — Session Status

## Setup: 2026-05-17
Initial scaffolding complete. No entries yet.

### What was done this session
- Created full directory structure under /home/neal/Wikis/gaming-language/
- Wrote .claude/hooks/protect_raw.py (PreToolUse write guard)
- Wrote .claude/settings.json (permissions + sandbox)
- Wrote CLAUDE.md (agent schema)
- Wrote guides/style.md, guides/research.md, guides/furigana.md, guides/lint-checklist.md
- Wrote all 8 .claude/skills/ files
- Wrote build/schema.json, build/japanese_utils.py, build/validate_entries.py, build/render_entries.py, build/get_entry_path.py
- Seeded entries_index.json with empty entries array
- Locked raw/, references.bib, build/ with chmod -R a-w

## Session: 2026-05-17 (candidates review)

### What was done this session
- Read wiki/_candidates.md — 36 candidate terms found, none with a source file in raw/
- raw/ is empty; no entries could be created
- All 36 candidates moved to wiki/_review.md under "Awaiting source" with provisional romaji and English glosses
- _candidates.md left unchanged (no items checked off)

## Session: 2026-05-18 (ingest — wargame translation reference)

### Source processed
- `raw/Claude-generated-wargame_translation_reference.docx` — Claude-generated IP analysis of 36 wargame terms. Reviews each term for Warhammer Japan IP conflict, provides source evidence, and recommends safe JP translations.

### Entries created: 36
IDs 00001–00036, all in entries/00000/

| ID | Romaji | JP | EN |
|---|---|---|---|
| 00001 | taisen | 対戦 | match |
| 00002 | pureiyaa | プレイヤー | player |
| 00003 | senshi | 戦士 | warrior |
| 00004 | teban | 手番 | turn |
| 00005 | teban_pureiyaa | 手番プレイヤー | active player |
| 00006 | hi_teban_pureiyaa | 非手番プレイヤー | reactive player |
| 00007 | feezu | フェイズ | phase |
| 00008 | totsugeki_dankai | 突撃段階 | charging phase |
| 00009 | idou_dankai | 移動段階 | moving phase |
| 00010 | shageki_dankai | 射撃段階 | shooting phase |
| 00011 | hakuheisen_dankai | 白兵戦段階 | fighting phase |
| 00012 | kousen_chuu | 交戦中 | engaged in combat |
| 00013 | ichi | 位置 | position |
| 00014 | senjou | 戦場 | battlefield |
| 00015 | jikkou_suru | 実行する | to perform |
| 00016 | kougeki | 攻撃 | attack |
| 00017 | enkyori_kougeki | 遠距離攻撃 | ranged attack |
| 00018 | kinsetsu_kougeki | 近接攻撃 | melee attack |
| 00019 | chikei | 地形 | terrain |
| 00020 | shasen | 射線 | line of sight |
| 00021 | tsuuka_fuka | 通過不可 | impassable |
| 00022 | shahei | 遮蔽 | cover/hindering |
| 00023 | kouchi | 高地 | elevated ground |
| 00024 | zenshin | 前進 | advance |
| 00025 | kougun | 行軍 | march |
| 00026 | bougyo | 防御 | defense |
| 00027 | taikyuu_ryoku | 耐久力 | resilience |
| 00028 | yoroi | 鎧 | armour |
| 00029 | kougeki_suu | 攻撃数 | attacks (stat) |
| 00030 | kougeki_ryoku | 攻撃力 | offense/attack power |
| 00031 | chikara | 力 | strength |
| 00032 | kantsuu_ryoku | 貫通力 | penetration |
| 00033 | binshousei | 敏捷性 | agility |
| 00034 | kago | 加護 | aegis/divine protection |
| 00035 | tairyoku | 体力 | health points |
| 00036 | shiki | 士気 | discipline/morale |

### Pages created: 3
- wiki/source/claude-2026-wargame-translation-ref.md
- wiki/genre-conventions/miniature-wargame-jp.md
- wiki/terms/ — 36 generated pages (via render_entries.py)

### _review.md items added: 43
- 36 furigana verification items (all entries, source is Claude-generated not primary dictionary)
- 7 WH flag audit items (entries where WH IP concern was flagged)

### _candidates.md status
All 36 candidates are now ingested. _candidates.md can be cleared next session.

### Validator status
- `python3 build/validate_entries.py` reports 36 issues, all `furigana_verified=false`
- No structural, syntax, or cross-reference errors
- All 36 furigana_verified issues are in _review.md and require human dictionary verification

### Unresolved questions
- None blocking. All 36 entries are complete pending furigana verification.

## Session: 2026-05-18 (furigana verification + Tatoeba examples)

### What was done
- Queried Jisho API (jisho.org/api/v1/search/words) for all 36 terms; all readings confirmed
- Special note: 手番 confirmed as てばん via Jisho second entry (board-game sense); 貫通力 confirmed via 貫通 + 力 components (not a standalone Jisho entry)
- Set furigana_verified: true on all 36 entries
- Queried Tatoeba (tatoeba.org API) for gaming/combat-relevant example sentences
- Replaced constructed examples with Tatoeba-sourced sentences in 12 entries:
  - 対戦 → Tatoeba #529650 "対戦相手を甘く見るな" (Don't underestimate your opponent)
  - 戦士 → Tatoeba #6828219 "戦士が戦う" (Warriors fight)
  - 位置 → Tatoeba #2199654 "位置について、よーい、ドン！" (On your mark, get set, go!)
  - 実行する → Tatoeba #290729 "彼は計画を実行した" (He carried out the plan)
  - 攻撃 → Tatoeba #173582 "攻撃は最大の防衛" (Attack is the best form of defense)
  - 高地 → Tatoeba #97936 "彼らはその高地を敵軍に明け渡した" (They abandoned the hill to enemy forces)
  - 前進 → Tatoeba #307016 "彼らは川まで前進した" (They advanced to the river)
  - 耐久力 → Tatoeba #235648 "１万メートルを走るには大いに耐久力を必要とする"
  - 鎧 → Tatoeba #182950 "騎士の時代には...鎧を身に付けた" (knights wore armor...)
  - 貫通力 → Tatoeba #11746224 "銃弾はヘルメットを貫通した" (A bullet pierced the helmet)
  - 加護 → Tatoeba #1974722 "神のご加護がありますように" (May God keep you!)
  - 士気 → Tatoeba #328523 "それで士気が下がっては本末転倒" (if morale drops, that defeats the purpose)
- Re-ran validate_entries.py → "All 36 entries valid." (zero errors)
- Re-rendered all 36 wiki/terms/ pages

## Next session should
1. Clear _candidates.md (all 36 items ingested)
2. Verify furigana readings against Goo dictionary / Kotobank — work through _review.md list
3. For entries where readings are confirmed: set furigana_verified: true and re-run render_entries.py
4. Run /lint to generate a fresh lint report
5. Consider: does the project need additional source material? The current 36 entries cover one wargame project's terminology. Broader wiki scope needs additional sources in raw/.
