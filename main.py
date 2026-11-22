#!/usr/bin/env python3
"""Write the plan entry to /output/entry.txt.

Stdlib only, no network. The entry text is hardcoded and deterministic.
"""

import os

ENTRY = (
    "Day 1: build 3 Notion wedding-budget templates (planner, vendors, "
    "guests), list at $19 on Etsy, SEO titles brides search. Spend "
    "$100: Etsy Ads, 10 pins/day. Buyers: brides. Edge: 1,000 agents sell "
    "generic AI art; one high-intent niche compounds. Day 30: ~20 sales, $300-$500 net."
)


def validate_entry(text: str) -> str:
    """Check a candidate entry and return it cleaned, or explain why not.

    A valid entry is non-empty after trimming, at most 280 characters,
    and written as plain text with no control characters in it. Any
    problem raises a ValueError naming the exact rule that failed, so a
    caller can fix the text instead of guessing what went wrong.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry must not be empty after trimming")
    if len(cleaned) > 280:
        raise ValueError(f"entry is {len(cleaned)} chars, over the 280 limit")
    if any(ord(ch) < 32 and ch not in "\n\t" for ch in cleaned):
        raise ValueError("entry must not contain control characters")
    return cleaned


def write_entry(path: str, text: str) -> int:
    """Write one validated entry to path and report how many chars landed.

    The parent folder is created when missing, the file is written as
    UTF-8, and the returned count lets the caller confirm the file holds
    exactly the text that was validated — no silent truncation, no extra
    trailing newline sneaking in after the fact.
    """
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return len(text)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise ValueError("ENTRY must not be empty")
    if not 1 <= len(text) <= 280:
        raise ValueError(f"ENTRY must be 1-280 characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
