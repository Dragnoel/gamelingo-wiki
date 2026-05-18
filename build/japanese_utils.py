"""Furigana parsing and kana utilities for the Gaming Language Wiki."""
import re
from typing import Iterator

FURIGANA_PATTERN = re.compile(r'\{([^|{}]+)\|([^|{}]+)\}')

def parse_furigana(text: str) -> Iterator[tuple[str, str]]:
    """Yield (kanji_base, reading) pairs from {kanji|reading} notation."""
    for m in FURIGANA_PATTERN.finditer(text):
        yield m.group(1), m.group(2)

def strip_furigana(text: str) -> str:
    """Return plain text with furigana notation removed (keeps kanji base)."""
    return FURIGANA_PATTERN.sub(lambda m: m.group(1), text)

def is_hiragana(text: str) -> bool:
    return all('ぁ' <= c <= 'ゟ' or c in ' ・' for c in text if not c.isspace())

def has_kanji(text: str) -> bool:
    return any('一' <= c <= '鿿' for c in text)

def validate_furigana_syntax(text: str) -> list[str]:
    """Return list of error strings for malformed {kanji|reading} notation."""
    errors = []
    for kanji, reading in parse_furigana(text):
        if not has_kanji(kanji):
            errors.append(f"Furigana base '{kanji}' contains no kanji.")
        if not is_hiragana(reading):
            errors.append(f"Reading '{reading}' for '{kanji}' is not hiragana.")
    depth = 0
    for ch in text:
        if ch == '{': depth += 1
        elif ch == '}': depth -= 1
        if depth < 0:
            errors.append("Unmatched '}' in furigana notation.")
            break
    if depth > 0:
        errors.append("Unmatched '{' in furigana notation.")
    return errors
