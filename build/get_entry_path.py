#!/usr/bin/env python3
"""Print the correct entries/ subdirectory for a given entry ID."""
import sys

def get_dir(entry_id: str) -> str:
    num = int(entry_id.split("_")[0])
    base = (num // 500) * 500
    return f"entries/{base:05d}/"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: get_entry_path.py <entry_id>  e.g. 00501_aruku")
        sys.exit(1)
    print(get_dir(sys.argv[1]))
