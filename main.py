#!/usr/bin/env python3
"""Write the plan entry to /output/entry.txt.

Stdlib only, no network. The entry text is hardcoded and deterministic.
"""

import os

ENTRY = (
    "Day 1: make 3 Notion wedding-budget templates, list at $19 on Etsy "
    "with SEO titles brides search. Spend $100 on Etsy Ads + 10 pins/day. "
    "Buyers: brides. Edge: 1,000 agents sell generic AI art; almost none "
    "own one boring niche whose search compounds. Day 30: $300-$500."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
