#!/usr/bin/env python3
"""Validate all JSON entries: schema, furigana syntax, cross-reference integrity."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from japanese_utils import validate_furigana_syntax

ROOT = Path(__file__).parent.parent
ENTRIES_DIR = ROOT / "entries"
INDEX_FILE = ROOT / "entries_index.json"

def load_known_ids() -> set[str]:
    if not INDEX_FILE.exists():
        return set()
    return {e["id"] for e in json.loads(INDEX_FILE.read_text()).get("entries", [])}

def validate_entry(path: Path, known_ids: set[str]) -> list[str]:
    errors = []
    try:
        entry = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        return [f"{path.name}: invalid JSON: {e}"]

    for field in ("headword_jp",):
        for err in validate_furigana_syntax(entry.get(field, "")):
            errors.append(f"{path.name} [{field}]: {err}")
    for ex in entry.get("examples", []):
        for err in validate_furigana_syntax(ex.get("japanese", "")):
            errors.append(f"{path.name} [example {ex.get('id','')}]: {err}")

    for xref in entry.get("cross_references", []):
        xid = xref.get("id")
        if xid and xid not in known_ids:
            errors.append(f"{path.name}: cross_reference id '{xid}' not in index.")

    if not entry.get("metadata", {}).get("furigana_verified"):
        errors.append(f"{path.name}: furigana_verified=false — verify readings.")

    return errors

def main():
    known_ids = load_known_ids()
    all_errors = []
    entry_paths = sorted(ENTRIES_DIR.rglob("*.json"))
    for p in entry_paths:
        all_errors.extend(validate_entry(p, known_ids))

    if all_errors:
        print(f"\n{len(all_errors)} validation issue(s):\n")
        for e in all_errors:
            print(f"  {e}")
        sys.exit(1)
    else:
        print(f"All {len(entry_paths)} entries valid.")

if __name__ == "__main__":
    main()
