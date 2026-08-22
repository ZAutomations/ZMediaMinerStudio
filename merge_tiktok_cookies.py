#!/usr/bin/env python
"""Merge TikTok cookies (exported by a browser extension) into data/cookies.txt.

Why: Chrome 127+ encrypts cookies with App-Bound Encryption, so yt-dlp cannot
read them via --cookies-from-browser.  A cookie-export extension (e.g.
'Get cookies.txt LOCALLY') reads cookies through Chrome's own extension API and
writes a Netscape cookies.txt, which bypasses that encryption entirely.

How to use:
  1. Log into TikTok in Chrome, then open the extension.
  2. Export cookies for  tiktok.com  (Netscape format) to a file, e.g.
     C:\\Temp\\tiktok_export.txt.
  3. Run:  python merge_tiktok_cookies.py C:\\Temp\\tiktok_export.txt
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COOKIES = ROOT / "data" / "cookies.txt"

SESSION_KEYS = ("sessionid", "sessionid_ss", "sid_tt", "ttwid", "odin_tt", "sid_guard")


def _pairs(path):
    out = []
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line or line.startswith("#") or "\t" not in line:
            continue
        parts = line.split("\t")
        if len(parts) >= 7:
            out.append(parts)
    return out


def main():
    if len(sys.argv) < 2:
        print("Usage: python merge_tiktok_cookies.py <exported_cookies.txt>")
        return 1
    src = Path(sys.argv[1])
    if not src.exists():
        print(f"Export file not found: {src}")
        return 1

    new_tiktok = [p for p in _pairs(src) if "tiktok.com" in p[0]]
    if not new_tiktok:
        print("No tiktok.com cookies found in the export. Make sure you exported for tiktok.com.")
        return 1

    existing = _pairs(COOKIES)
    kept = [p for p in existing if "tiktok.com" not in p[0]]

    merged = {}
    for p in kept + new_tiktok:
        key = (p[0], p[2], p[5])
        merged[key] = p
    lines = [p for p in merged.values()]

    header = "# Netscape HTTP Cookie File\n"
    body = "\n".join("\t".join(p) for p in lines) + "\n"
    COOKIES.write_text(header + body, encoding="utf-8")

    names = {p[5] for p in merged.values() if "tiktok.com" in p[0]}
    good = sorted(n for n in names if n in SESSION_KEYS)
    print(f"TikTok cookies merged: {len(names)}  (session keys present: {good or ['NONE']})")
    if any(n in SESSION_KEYS for n in names):
        print("OK: valid TikTok session merged. Retry the metadata scan.")
        return 0
    print("Warning: no TikTok session cookie found. Ensure you are logged into TikTok "
          "in Chrome before exporting.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
