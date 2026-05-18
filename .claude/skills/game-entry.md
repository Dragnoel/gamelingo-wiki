# game-entry — auto-loaded when writing game entity pages

## When this guide applies
Auto-load whenever creating or editing a page in wiki/games/ or wiki/mechanics/ or wiki/genre-conventions/.

## Game entity page (wiki/games/<slug>.md)

### Frontmatter
```yaml
---
title: <Game Title>
type: game
draft: false
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - <bib-key-or-filename>
---
```

### Body structure
1. Lead (≤ 80 words): full title in original language and English, publisher, year, platform(s), genre. No evaluative language.
2. ## Language context — how the game's language is relevant to this wiki (JP release, localization, bilingual edition, etc.)
3. ## Terms — wikilinks to all term entries sourced from this game
4. ## Localization notes — where JP and EN versions differ in terminology or phrasing (sourced only)
5. ## See also — related games, mechanics, comparisons
6. ## References

### Constraints
- Do not summarise gameplay beyond what is needed to contextualise the language.
- Do not evaluate game quality.
- All localization claims must be sourced to a file in raw/.

## Mechanic entity page (wiki/mechanics/<slug>.md)

### Frontmatter
```yaml
---
title: <Mechanic Name>
type: mechanic
draft: false
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - <bib-key-or-filename>
---
```

### Body structure
1. Lead (≤ 80 words): mechanic name in JP and EN, game domain(s) where it appears.
2. ## JP terminology — terms used in Japanese for this mechanic, with wikilinks.
3. ## EN terminology — terms used in English, with wikilinks.
4. ## Cross-domain variation — how the mechanic and its name differ across board/card/video/TTRPG.
5. ## See also
6. ## References

## Genre-convention entity page (wiki/genre-conventions/<slug>.md)
Follow mechanic page structure. Replace "mechanic" with "convention" throughout.
