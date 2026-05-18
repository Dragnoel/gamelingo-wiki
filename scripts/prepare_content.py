#!/usr/bin/env python3
"""
Prepare wiki/ content for Quartz publication.

Reads wiki/, applies two transforms per .md file, and writes to content/:
  1. Exclude files whose names start with '_' (internal tracking files).
  2. Convert {kanji|reading} furigana notation to HTML <ruby> tags.

Also normalises long-form wikilinks:
  [[wiki/terms/00004_teban.md]] -> [[00004_teban]]
  [[wiki/genre-conventions/foo.md]] -> [[foo]]
so Quartz shortest-path resolution works correctly.

Non-.md files are copied as-is (for future images/attachments).
"""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI = ROOT / "wiki"
CONTENT = ROOT / "content"

FURIGANA = re.compile(r'\{([^|{}]+)\|([^|{}]+)\}')
WIKILINK_LONGFORM = re.compile(r'\[\[wiki/[^|\]]+/([^/|\]]+?)(?:\.md)?\]\]')


def convert_furigana(text: str) -> str:
    return FURIGANA.sub(r'<ruby>\1<rt>\2</rt></ruby>', text)


def normalise_wikilinks(text: str) -> str:
    # [[wiki/terms/00004_teban.md]] -> [[00004_teban]]
    # [[wiki/genre-conventions/miniature-wargame-jp]] -> [[miniature-wargame-jp]]
    return WIKILINK_LONGFORM.sub(r'[[\1]]', text)


def process_md(src: Path, dst: Path) -> None:
    text = src.read_text(encoding="utf-8")
    text = convert_furigana(text)
    text = normalise_wikilinks(text)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text, encoding="utf-8")


def prepare() -> None:
    if CONTENT.exists():
        shutil.rmtree(CONTENT)
    CONTENT.mkdir()

    excluded = 0
    copied_md = 0
    copied_other = 0

    for src in WIKI.rglob("*"):
        if not src.is_file():
            continue

        rel = src.relative_to(WIKI)

        # Exclude internal tracking files (any _*.md at any depth)
        if src.name.startswith("_"):
            excluded += 1
            continue

        dst = CONTENT / rel

        if src.suffix == ".md":
            process_md(src, dst)
            copied_md += 1
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            copied_other += 1

    print(
        f"prepare_content: {copied_md} md files converted, "
        f"{copied_other} other files copied, "
        f"{excluded} internal files excluded → content/"
    )


if __name__ == "__main__":
    prepare()
