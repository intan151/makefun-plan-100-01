#!/usr/bin/env python3
"""Write the plan entry to /output/entry.txt.

Stdlib only, no network. The entry text is hardcoded and deterministic.
"""

import os

ENTRY = (
    "Day 1: build 3 Notion wedding-budget templates (planner, vendors, "
    "guests), list at $19 on Etsy, SEO titles brides search. Spend "
    "$100: Etsy Ads, 10 pins/day. Buyers: brides. Edge: 1,000 agents sell "
    "generic AI art; few own one niche that compounds. Day 30: ~20 sales, $300-$500."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
