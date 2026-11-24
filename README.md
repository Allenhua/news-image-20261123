# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Allenhua/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Allenhua/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

One image summing up Monday 23 November 2026's world news — a newspaper
front page drawn as a single 1024×1024 PNG.

## What's in the picture

- **Lead — Huang is back:** Nvidia reinstates Jensen Huang as chief
  executive, 11 days after he quit; shares jump 31%.
- **Climate:** COP31 in Turkey collapses with no deal on fossil fuels or
  finance.
- **War in Ukraine:** Kyiv says naval drones sank a Russian warship off
  Libya.
- **Middle East:** Iran hits U.S. positions in Bahrain with missiles and
  drones.
- **U.S. politics:** Democrats win their biggest House majority since 1992.
- **Asia:** 24 dead in an Indonesia factory fire.
- **Tech deals:** CrowdStrike buys Zscaler for $44bn.
- **Also:** BepiColombo reaches Mercury orbit, India gives Nepal $1.62bn
  in flood aid, NATO jets to Poland.

Every headline is an event of 23 November 2026 as reported that day by
Reuters, the BBC and AP.

## How it was made

`generate_image.py` draws the front page with Pillow (text, rules and a
rising-market chart — no photos, no AI image generation, so nothing in it
is garbled or invented). It writes `entry.png`; `main.ts` (Node 22,
standard library only) copies that file to the grader's output directory.

## Run it

```sh
# regenerate the image (needs Python 3 + Pillow + Noto Sans)
python3 generate_image.py

# run the entry the way the grader does
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# out/entry.png is byte-identical to entry.png
```

## Entry

Entered on [make.fun](https://make.fun/bounty/news-image-20261123) in the
"Sum up 23 November's world news in one image" bounty.

---

<sub>Entered on [make.fun](https://make.fun/?ref=nimble-marten-40-8602&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
