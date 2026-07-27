#!/usr/bin/env python
"""Generate the app icon (assets/app_icon.ico) for MediaMiner Studio.

A modern rounded-tile icon: a teal->blue diagonal gradient with subtle film-
strip perforations down the sides and a faceted white gem in the centre —
"mining" media (video + text + speech + metadata) for valuable data. Saved as
a multi-resolution .ico (16/32/48/64/128/256) so it stays crisp everywhere.

Run once (checked-in result travels with the repo)::

    venv\\Scripts\\python.exe setup\\make_icon.py
"""
from pathlib import Path
from PIL import Image, ImageDraw

S = 256  # master render size


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def render(size=S):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))

    # --- diagonal gradient background (teal -> deep blue) ---------------
    top = (20, 201, 179)    # #14C9B3 teal
    bot = (37, 71, 232)     # #2547E8 blue
    grad = Image.new("RGB", (size, size), top)
    gd = ImageDraw.Draw(grad)
    for y in range(size):
        gd.line([(0, y), (size, y)], fill=_lerp(top, bot, y / (size - 1)))

    radius = int(size * 0.22)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [0, 0, size - 1, size - 1], radius=radius, fill=255)
    img.paste(grad, (0, 0), mask)

    # Semi-transparent details go on an overlay so they COMPOSITE.
    overlay = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)

    # --- film-strip perforations down both sides ------------------------
    strip_w = int(size * 0.11)
    hole_w = int(size * 0.055)
    hole_h = int(size * 0.075)
    gap = int(size * 0.045)
    y = gap
    while y + hole_h < size - gap:
        lx = int(strip_w / 2 - hole_w / 2)
        od.rounded_rectangle([lx, y, lx + hole_w, y + hole_h],
                             radius=int(hole_w * 0.35), fill=(255, 255, 255, 85))
        rx = size - strip_w // 2 - hole_w // 2
        od.rounded_rectangle([rx, y, rx + hole_w, y + hole_h],
                             radius=int(hole_w * 0.35), fill=(255, 255, 255, 85))
        y += hole_h + gap

    # soft glow disc behind the gem
    cx, cy = size / 2, size / 2
    r = size * 0.29
    od.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255, 55))
    img = Image.alpha_composite(img, overlay)

    # --- faceted gem (white, opaque, on top) ----------------------------
    d = ImageDraw.Draw(img)
    w = size * 0.20           # gem half-width at the girdle
    y0 = cy - size * 0.135    # table (top edge) y
    y1 = cy - size * 0.035    # girdle y
    y2 = cy + size * 0.215    # bottom point y
    tw = w * 0.55             # half table width

    outline = [
        (cx - tw, y0), (cx + tw, y0),
        (cx + w, y1), (cx, y2), (cx - w, y1),
    ]
    d.polygon(outline, fill=(255, 255, 255, 255))

    # facet lines in a soft blue so the gem looks cut, not flat
    fac = (120, 165, 220, 255)
    lw = max(1, int(size * 0.012))
    d.line([(cx - w, y1), (cx + w, y1)], fill=fac, width=lw)          # girdle
    d.line([(cx - tw, y0), (cx - w, y1)], fill=fac, width=lw)         # crown L
    d.line([(cx + tw, y0), (cx + w, y1)], fill=fac, width=lw)         # crown R
    d.line([(cx - tw, y0), (cx, y2)], fill=fac, width=lw)             # long L
    d.line([(cx + tw, y0), (cx, y2)], fill=fac, width=lw)             # long R
    d.line([(cx - w, y1), (cx, y2)], fill=fac, width=lw)             # pavilion L
    d.line([(cx + w, y1), (cx, y2)], fill=fac, width=lw)             # pavilion R
    d.line([(cx, y0 - size * 0.001), (cx, y1)], fill=fac, width=lw)   # table mid

    return img


def main():
    here = Path(__file__).resolve().parent
    assets = here.parent / "assets"
    assets.mkdir(exist_ok=True)
    out = assets / "app_icon.ico"

    master = render(S)
    sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
    master.save(out, format="ICO", sizes=sizes)
    master.save(assets / "app_icon.png", format="PNG")
    print(f"[OK] wrote {out} ({out.stat().st_size} bytes) + app_icon.png")


if __name__ == "__main__":
    main()
