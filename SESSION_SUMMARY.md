# Session Summary — TikTok Fix + Torch-Free Migration

Date: 2026-08-19 · Branch: `main` · Python 3.11.9

Short record of what was done and how it works, so a future session can pick
up quickly.

## 1. TikTok profile scanning (FIXED — no Playwright)

TikTok was blocking profile enumeration (WAF / X-Bogus). The working fix is a
small scraper in `platforms/tiktok.py` (class `TikTokScraper`):

1. **Find cookies** — `data/cookies.txt` (legacy) then `data/cookies/tiktok/*.txt`
   (multi-account). Only files containing real tiktok.com cookies count
   (`_check_tiktok_cookie`).
2. **Get secUid** — fetch `https://www.tiktok.com/@user` and parse
   `__UNIVERSAL_DATA_FOR_REHYDRATION__` (or `SIGI_STATE`) from the HTML.
3. **List videos** — in-process `yt_dlp.YoutubeDL` with `extract_flat=True`,
   `cookiefile=<found file>`, `http_headers={'Referer': 'https://www.tiktok.com/'}`,
   extractor `tiktokuser:{secUid}`.

### The key gotcha (why old code failed)
- A **cookie-authenticated** request to the profile page often gets a ~12KB
  anti-bot "login shell" page with **no secUid**.
- A fresh **anonymous** request returns the full ~394KB SSR page WITH the secUid.
- Fix: `_get_user_info()` tries the cookie session first, then falls back to an
  anonymous `requests.Session()` (`platforms/tiktok.py`). This was added AFTER
  the redesign port because a real run hit "Could not fetch user info".
- The **subprocess** yt-dlp path (`python -m yt_dlp ... tiktokuser:...`) fails
  ("Failed to parse JSON") — only the **in-process** `yt_dlp.YoutubeDL` path works.
- Don't re-add a Playwright/CDP fallback; it's unnecessary.

Wiring on main:
- `core/metadata_scanner.py` → `scan_tiktok_profile()` delegates to
  `TikTokScraper.scrape_profile_entries()`.
- `core/downloader.py` → `_pick_tiktok_cookie()` + TikTok branch in cookie
  selection (mirrors Instagram rotation).

## 2. Torch-free migration (faster-whisper + RapidOCR)

Replaced the heavy ML stack (no `torch` anywhere):

| Before (heavy `venv`) | After (light `venv_light`) |
|---|---|
| `openai-whisper` (needs torch) | `faster-whisper` (CTranslate2, int8 CPU) |
| `easyocr` (pulls torch) | `rapidocr-onnxruntime` (~15MB ONNX) |

Changed files:
- `core/extractor.py` — `load_whisper()` uses `WhisperModel(WHISPER_MODEL, device="cpu", compute_type="int8", download_root=models/whisper)`; `load_ocr()` uses `RapidOCR()`; OCR call is `ocr_result, _ = self.ocr_reader(frame_np)` (returns `(result, elapse)`, result = list of `[box, text, score]` — same shape as EasyOCR, so the sort/clean code is unchanged); `extract_speech()` joins the segment generator (`" ".join(seg.text ...)`). The user's error guards were preserved (`_has_audio_stream`, reload-on-failure, try/except model load).
- `core/downloader.py` — `_detect_voice_in_audio()` uses `WhisperModel("tiny", ...)`.
- `requirements.txt` — torch-free deps.
- `run.bat` — runs `venv_light\Scripts\python.exe`, errors print to console.

### Current environment
- `venv_light\` — the ACTIVE torch-free env (deps installed, everything verified).
- `venv\` — OLD heavy env (still on disk as fallback). Delete once happy:
  `venv\`, `models\whisper\*.pt` (openai-whisper format).
- The faster-whisper base model auto-downloaded to `models/whisper` (HF cache
  layout, `models--Systran--faster-whisper-base`), NOT `.pt` format.

### How to verify quickly (from project root)
```
venv_light\Scripts\python.exe -c "import torch"          # must FAIL (torch-free)
venv_light\Scripts\python.exe -c "import faster_whisper, rapidocr_onnxruntime, yt_dlp"   # OK
venv_light\Scripts\python.exe -c "import sys; sys.path.insert(0,'.'); from core.metadata_scanner import MetadataScanner; r=MetadataScanner().scan_tiktok_profile('https://www.tiktok.com/@rescue3animal', max_videos=3); print(len(r['videos']))"
```

## 3. Merge status vs `redesign/phase-1-lightweight`
- Ported into main: TikTok scraper + cookie rotation + simplified scanner
  (plus the anonymous-secUid fallback the redesign lacks).
- Did NOT port (design would LOSE main features): nothing else was merged —
  the redesign drops bilibili scan, CTA parsing/column, bracket-tolerant
  clip parsing, and cookies in generic playlist scanning. Keep main's versions.
- `run.bat` error visibility and `.gitignore` entries were adopted.
- The redesign's `case_commentary_animal_story` niche was NOT ported (main has
  its own upgraded animal + relationship niches).

## 4. Notes / gotchas
- Console output with emojis: pipe with `PYTHONIOENCODING=utf-8` or run from the
  app (cmd uses cp1252 otherwise).
- HF Hub warns about symlinks / unauthenticated requests — benign; set
  `HF_HUB_DISABLE_SYMLINKS_WARNING=1` to silence.
- TikTok cookies expire (days–weeks). If scans start failing, re-export fresh
  cookies to `data/cookies.txt` while on tiktok.com.