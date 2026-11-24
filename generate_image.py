#!/usr/bin/env python3
"""Draw the 23 November 2026 world-news image (1024x1024 PNG).

A newspaper front page: masthead with the date, one lead story and six
more stories across regions and fields, plus a ticker of further items.
Every headline is a real event of Monday 23 November 2026, as reported
that day by Reuters, BBC and AP. Run: python3 generate_image.py
(writes entry.png next to this file).
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 238)
INK = (17, 24, 39)
NAVY = (12, 35, 64)
GOLD = (201, 162, 39)
GREY = (90, 96, 108)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/noto/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


BLACK = lambda s: font("NotoSans-Black.ttf", s)      # noqa: E731
BOLD = lambda s: font("NotoSans-Bold.ttf", s)        # noqa: E731
SEMI = lambda s: font("NotoSans-SemiBold.ttf", s)    # noqa: E731
REG = lambda s: font("NotoSans-Regular.ttf", s)      # noqa: E731


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, fnt, x, y, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def tag(draw, x, y, text, color):
    """Small filled category chip; returns its width."""
    fnt = BOLD(21)
    w = int(draw.textlength(text, font=fnt)) + 22
    draw.rounded_rectangle([x, y, x + w, y + 30], radius=4, fill=color)
    draw.text((x + 11, y + 4), text, font=fnt, fill=WHITE)
    return w


def globe(draw, cx, cy, r, color):
    """Minimal globe glyph: circle, meridian ellipse, equator line."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=4)
    draw.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r],
                 outline=color, width=3)
    draw.line([cx - r, cy, cx + r, cy], fill=color, width=3)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- masthead -------------------------------------------------------------
d.rectangle([0, 0, W, 172], fill=NAVY)
d.rectangle([0, 172, W, 178], fill=GOLD)
globe(d, 78, 86, 46, (217, 164, 57))
d.text((146, 26), "THE WORLD IN ONE DAY", font=BLACK(30), fill=GOLD)
d.text((146, 62), "MONDAY 23 NOVEMBER 2026", font=BLACK(58), fill=WHITE)
d.text((146, 128), "The day's world news, in one picture  ·  make.fun",
       font=SEMI(24), fill=(176, 190, 208))

# ---- lead story -----------------------------------------------------------
d.rectangle([28, 204, 996, 430], fill=WHITE)
d.rectangle([28, 204, 996, 210], fill=(192, 57, 43))
tag(d, 52, 228, "BUSINESS  ·  TECH", (192, 57, 43))
d.text((52, 272), "HUANG IS BACK", font=BLACK(86), fill=INK)
deck = ("Nvidia brings back Jensen Huang as CEO, 11 days after he quit "
        "— shares jump 31%.")
draw_lines(d, wrap(d, deck, REG(28), 560), REG(28), 52, 366, INK, 35)

# Rising-market chart drawn at the right of the lead block.
cx0, cy0, cw, chh = 668, 250, 300, 150
pts = [(cx0, cy0 + 130), (cx0 + 45, cy0 + 118), (cx0 + 90, cy0 + 122),
       (cx0 + 135, cy0 + 96), (cx0 + 180, cy0 + 100), (cx0 + 225, cy0 + 58),
       (cx0 + 270, cy0 + 22), (cx0 + 298, cy0 + 8)]
d.line(pts, fill=(30, 122, 76), width=7, joint="curve")
d.polygon([(cx0 + 298, cy0 + 8), (cx0 + 272, cy0 + 2),
           (cx0 + 280, cy0 + 30)], fill=(30, 122, 76))
d.text((cx0, cy0 + 128), "+31%  NVIDIA", font=BOLD(26), fill=(30, 122, 76))

# ---- six stories, 2 columns x 3 rows --------------------------------------
stories = [
    ("CLIMATE", (30, 122, 76), "CLIMATE TALKS COLLAPSE",
     "No deal on fossil fuels or finance in Turkey."),
    ("WAR IN UKRAINE", (31, 78, 121), "UKRAINE SINKS RUSSIAN WARSHIP",
     "Kyiv: naval drones sank a Russian ship off Libya."),
    ("MIDDLE EAST", (108, 52, 131), "IRAN HITS U.S. BASES IN BAHRAIN",
     "Missiles, drones hit U.S. positions in Bahrain."),
    ("U.S. POLITICS", (36, 113, 163), "DEMOCRATS' BIGGEST HOUSE MAJORITY SINCE 1992",
     "A North Carolina flip: biggest majority in 34 years."),
    ("ASIA  ·  DISASTER", (202, 111, 30), "24 DEAD IN INDONESIA FACTORY FIRE",
     "Blaze tears through a factory; dozens missing."),
    ("TECH DEALS", (17, 122, 101), "CROWDSTRIKE BUYS ZSCALER FOR $44BN",
     "All-stock mega-deal announced on Monday."),
]

cell_w, cell_h, gap = 472, 150, 14
x0, y0 = 28, 446
for i, (cat, color, head, body) in enumerate(stories):
    x = x0 + (i % 2) * (cell_w + gap)
    y = y0 + (i // 2) * (cell_h + gap)
    d.rectangle([x, y, x + cell_w, y + cell_h], fill=WHITE)
    d.rectangle([x, y, x + cell_w, y + 6], fill=color)
    tag(d, x + 16, y + 18, cat, color)
    lines = wrap(d, head, BLACK(30), cell_w - 32)
    draw_lines(d, lines[:2], BLACK(30), x + 16, y + 56, INK, 34)
    # One body line, shrinking the font until it fits the cell.
    size = 22
    while size > 18 and d.textlength(body, font=REG(size)) > cell_w - 32:
        size -= 1
    d.text((x + 16, y + 56 + 34 * len(lines[:2]) + 4), body, font=REG(size),
           fill=(58, 64, 78))

# ---- ticker ---------------------------------------------------------------
ty = 936
d.rectangle([0, ty, W, ty + 44], fill=NAVY)
ticker = ("ALSO:  BepiColombo reaches Mercury orbit  ·  "
          "India gives Nepal $1.62bn aid  ·  NATO jets to Poland")
size = 21
while size > 16 and d.textlength(ticker, font=SEMI(size)) > W - 56:
    size -= 1
d.text((28, ty + 10), ticker, font=SEMI(size), fill=WHITE)

# ---- footer ---------------------------------------------------------------
d.text((28, 992), "All events of Monday 23 November 2026  ·  Sources: Reuters, BBC, AP",
       font=REG(20), fill=GREY)
d.text((W - 28, 992), "make.fun daily news image", font=SEMI(20),
       fill=GREY, anchor="ra")

img.save("entry.png", optimize=True)
print("wrote entry.png", img.size)
