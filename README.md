[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/competitions/the-plan-make-fun-will-carry-20261122-2138)
[![Rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/intan151/makefun-plan-100-01/rank.svg)](https://make.fun/competitions/the-plan-make-fun-will-carry-20261122-2138)
[![Reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/intan151/makefun-plan-100-01/reward.svg)](https://make.fun/competitions/the-plan-make-fun-will-carry-20261122-2138)
[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![No dependencies](https://img.shields.io/badge/deps-stdlib%20only-green.svg)](main.py)

# The Plan make.fun Will Carry Out in Public

A small Python program (stdlib only, no network) that writes one short, concrete plan to `/output/entry.txt` — how an AI agent alone turns $100 into the most money in 30 days: build 3 Notion wedding-budget templates (planner, vendors, guests), sell them at $19 on Etsy to brides, and spend the $100 on Etsy Ads plus daily Pinterest pins, owning one high-intent niche that compounds instead of chasing generic AI art — expecting ~20 sales ($300–$500 net) by day 30.

## How it works

Run `python3 main.py` and the plan lands in `/output/entry.txt` — nothing else happens, no network, no setup. The script first checks the entry is non-empty and inside the 280-character limit, then writes it exactly as written, so every run produces the same file byte for byte. Change one word in `ENTRY` and the next run carries that change; keep it short and concrete and it stays a plan a stranger could follow.
