#!/usr/bin/env python3
"""PreToolUse guardrail. Blocks writes to raw/, build/, guides/, references.bib,
CLAUDE.md, .claude/. Blocks dangerous Bash. Exits 0 to allow, 2 to block."""
import json
import re
import sys

PROTECTED_WRITE_PATTERNS = [
    re.compile(r"(^|/)raw(/|$)"),
    re.compile(r"(^|/)references\.bib$"),
    re.compile(r"(^|/)CLAUDE\.md$"),
    re.compile(r"(^|/)guides(/|$)"),
    re.compile(r"(^|/)build(/|$)"),
    re.compile(r"\.claude(/|$)"),
]

DANGEROUS_BASH = re.compile(
    r"\b(chmod|chflags|chown|rm\s+-rf|mv\s+.*\s+raw|"
    r"git\s+push|sudo|curl|wget|dd\s|>\s*raw)\b"
)

def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    tool = payload.get("tool_name", "")
    inp  = payload.get("tool_input", {}) or {}

    if tool in ("Edit", "Write", "MultiEdit"):
        path = str(inp.get("file_path", ""))
        for pat in PROTECTED_WRITE_PATTERNS:
            if pat.search(path):
                print(
                    f"BLOCKED: writes to '{path}' are protected. "
                    f"Writable: entries/, wiki/ (not wiki/terms/), queries/, "
                    f"PROJECT_STATUS.md, PROJECT_CONTEXT_BRIEF.md, entries_index.json.",
                    file=sys.stderr,
                )
                return 2

    if tool == "Bash":
        cmd = str(inp.get("command", ""))
        if DANGEROUS_BASH.search(cmd):
            print(f"BLOCKED: '{cmd[:80]}' is forbidden by vault policy.", file=sys.stderr)
            return 2

    return 0

if __name__ == "__main__":
    sys.exit(main())
