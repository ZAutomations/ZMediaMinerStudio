"""
Phase 1 smoke test — verifies the torch-free migration works end to end.
Run with the NEW venv_light python:
    venv_light\Scripts\python.exe _phase1_smoke_test.py
Checks:
  1. torch is NOT importable (proves torch-free)
  2. extractor imports (RapidOCR + faster-whisper load)
  3. OCR runs on a real video frame
  4. Speech transcription runs on a real video
This file is a temporary dev tool — safe to delete after Phase 1 sign-off.
"""
import sys
from pathlib import Path

REPO = Path(__file__).parent
sys.path.insert(0, str(REPO))

# Pick a small real test video that exists in the repo
CANDIDATES = [
    REPO / "channels/_general_downloads/tiktok/_processed_done/7660755154446257431.mp4",
    REPO / "channels/_general_downloads/youtube/videos/9YQTc_969jo.mp4",
    REPO / "channels/_general_downloads/youtube/videos/XulN4FZCqJ4.mp4",
]
video = next((str(p) for p in CANDIDATES if p.exists()), None)

print("=" * 60)
print("PHASE 1 SMOKE TEST — torch-free OCR + STT")
print("=" * 60)

# 1. torch must be gone
print("\n[1] torch-free check...")
try:
    import torch  # noqa
    print("  ❌ FAIL: torch is still importable — not torch-free!")
except ImportError:
    print("  ✅ PASS: torch is NOT installed (torch-free)")

# 2. import the migrated module
print("\n[2] import core.extractor...")
from core.extractor import MediaExtractor
ex = MediaExtractor()
print("  ✅ PASS: MediaExtractor imported")

if not video:
    print("\n⚠️  No test video found — skipping OCR/STT run.")
    sys.exit(0)

print(f"\n  Using test video: {video}")

# 3. OCR
print("\n[3] OCR (RapidOCR) on video frames...")
try:
    overlay = ex.extract_overlay_text(video, "test_id")
    print("  ✅ PASS: OCR ran")
    print("  --- overlay text (first 300 chars) ---")
    print("  " + (overlay[:300].replace("\n", "\n  ") if overlay else "(no overlay text detected)"))
except Exception as e:
    import traceback
    print("  ❌ FAIL: OCR crashed")
    traceback.print_exc()

# 4. STT
print("\n[4] Speech (faster-whisper) transcription...")
try:
    speech = ex.extract_speech(video)
    print("  ✅ PASS: transcription ran")
    print("  --- speech text (first 300 chars) ---")
    print("  " + (speech[:300] if speech else "(no speech detected / no audio)"))
except Exception as e:
    import traceback
    print("  ❌ FAIL: transcription crashed")
    traceback.print_exc()

print("\n" + "=" * 60)
print("SMOKE TEST DONE")
print("=" * 60)
