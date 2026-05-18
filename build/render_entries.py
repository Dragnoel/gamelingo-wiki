#!/usr/bin/env python3
"""Generate wiki/terms/ markdown from entries/ JSON files."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from japanese_utils import strip_furigana

ROOT = Path(__file__).parent.parent
ENTRIES_DIR = ROOT / "entries"
TERMS_DIR = ROOT / "wiki" / "terms"

def render(entry: dict) -> str:
    plain_jp = strip_furigana(entry.get("headword_jp", ""))
    romaji = entry.get("romaji", "")
    defns = entry.get("definitions", [])
    d0 = defns[0] if defns else {}

    lines = [
        "---",
        f"title: {plain_jp} ({romaji})",
        "type: term",
        f"reading: {entry.get('reading','')}",
        f"romaji: {romaji}",
        f"entry_id: {entry.get('id','')}",
        "draft: false",
        f"created: {entry.get('metadata',{}).get('created','')[:10]}",
        f"updated: {entry.get('metadata',{}).get('modified','')[:10]}",
        "---", "",
        f"# {plain_jp} ({romaji})", "",
        f"**{entry.get('headword_en','')}** · {entry.get('reading','')} · {romaji}", "",
    ]

    if d0.get("gloss_en"):
        lines += [d0["gloss_en"], ""]

    for section, key in [
        ("## Orthography notes",              "orthography_notes"),
        ("## Implicit meanings",              "implicit_notes"),
        ("## Differences across game settings", "game_setting_notes"),
    ]:
        if d0.get(key):
            lines += [section, "", d0[key], ""]

    usage_parts = []
    if entry.get("usage_jp"):
        usage_parts.append(f"**Japanese:** {entry['usage_jp']}")
    if entry.get("usage_en"):
        usage_parts.append(f"**English:** {entry['usage_en']}")
    if usage_parts:
        lines += ["## Usage", ""] + usage_parts + [""]

    if entry.get("comparative_notes"):
        lines += ["## Comparative notes", "", entry["comparative_notes"], ""]

    examples = entry.get("examples", [])
    if examples:
        lines += ["## Examples", ""]
        for ex in examples:
            lines += [f"> {ex.get('japanese','')}", f"> {ex.get('english','')}", ""]

    xrefs = entry.get("cross_references", [])
    if xrefs:
        links = ", ".join(f"[[{x.get('id','')}]]" for x in xrefs)
        lines += ["## See also", "", links, ""]

    sources = entry.get("sources", [])
    if sources:
        lines += ["## References", ""]
        for s in sources:
            lines += [f"[^{s}]", ""]

    return "\n".join(lines)

def main():
    TERMS_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    for path in sorted(ENTRIES_DIR.rglob("*.json")):
        entry = json.loads(path.read_text())
        out = TERMS_DIR / f"{entry['id']}.md"
        out.write_text(render(entry))
        count += 1
    print(f"Rendered {count} entries → {TERMS_DIR}")

if __name__ == "__main__":
    main()
