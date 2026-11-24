// news-image-20261123 — a program/v1 entry for make.fun.
//
// The image is drawn by generate_image.py (Pillow, from Monday 23 November
// 2026's reported world news) and shipped in this repository as entry.png.
// This program's only job is to copy that image to the output directory
// the grader provides. Node 22, standard library only, no network.
//
// Local check:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
//   # out/entry.png should be byte-identical to entry.png

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(
  new URL('./entry.png', import.meta.url),
  join(outDir, 'entry.png'),
);
