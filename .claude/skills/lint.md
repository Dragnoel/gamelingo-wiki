# /lint — Gaming Language Wiki

## Purpose
Full audit of the vault. Produces wiki/_lint-report.md. Proposes changes only — does not edit entries or wiki pages. Regenerates PROJECT_CONTEXT_BRIEF.md at the end.

## Procedure

### 1. Run automated validation
```
python3 build/validate_entries.py
```
Record all errors in the report.

### 2. Work through guides/lint-checklist.md
Execute every item in order. For each failure, record:
- Which file(s) are affected
- What the problem is
- What the proposed fix is (do not apply it)

### 3. Write wiki/_lint-report.md
Format:
```
# Lint report — YYYY-MM-DD

## Automated validation
[output of validate_entries.py]

## Checklist results
### Passed
- [item]

### Failed — proposed fixes
- [item]: [file] — [problem] → [proposed fix]

## Summary
- Entries: N total, N with furigana_verified: false, N cross-ref errors
- Pages: N source, N games, N mechanics, N genre-conventions, N comparisons
- _review.md open items: N
- _candidates.md open items: N
```

### 4. Regenerate PROJECT_CONTEXT_BRIEF.md
Write a short machine-readable primer with current vault state:
- Date regenerated
- Entry count (total, verified, unverified)
- Page counts by type
- Open _review.md items (count + brief list)
- Open _candidates.md items (count + brief list)
- Last ingest date (from PROJECT_STATUS.md)
Keep it under 60 lines — it is a token-efficient session orientation, not documentation.

### 5. Update PROJECT_STATUS.md
Record that a lint session was run, the date, and summary counts.

## Hard prohibitions during /lint
- Do not edit entries/ JSON files. Propose fixes only.
- Do not edit wiki/ pages (except _lint-report.md and PROJECT_CONTEXT_BRIEF.md).
- Do not run render_entries.py during lint — read-only pass only.
