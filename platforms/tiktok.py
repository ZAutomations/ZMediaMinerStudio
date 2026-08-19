import re
import requests
import http.cookiejar
from pathlib import Path
from urllib.parse import urlparse

# Multi-cookie support: store extra cookie files in data/cookies/tiktok/
# The legacy data/cookies.txt is always checked first.
COOKIES_DIR = Path(__file__).parent.parent / "data" / "cookies" / "tiktok"


def _check_tiktok_cookie(cookies_path):
    """Check a single Netscape cookie file for valid TikTok session cookies.

    Returns a dict with keys: logged_in, reason, file.
    """
    cookies_path = Path(cookies_path)
    if not cookies_path.exists():
        return {"logged_in": False, "reason": "file not found",
                "file": cookies_path}
    if cookies_path.stat().st_size == 0:
        return {"logged_in": False, "reason": "empty file",
                "file": cookies_path}

    try:
        jar = http.cookiejar.MozillaCookieJar(str(cookies_path))
        jar.load(ignore_discard=True, ignore_expires=True)
    except Exception as e:
        return {"logged_in": False,
                "reason": f"unreadable ({e})", "file": cookies_path}

    # Check for a real TikTok session: only cookies on a tiktok.com domain
    # count (other sites also use a cookie named "sessionid", e.g. capcut).
    # yt-dlp works with a logged-out TikTok session too (ttwid + msToken),
    # so any tiktok.com cookie marks the file as usable.
    has_session = False
    for c in jar:
        domain = (c.domain or '').lower()
        if 'tiktok.com' not in domain:
            continue
        if c.name in ('sessionid', 'sid_tt', 'sessionid_ss', 'sid_guard', 'uid_tt',
                      'ttwid', 'tt_csrf_token', 's_v_web_id', 'msToken', 'tt_chain_token'):
            has_session = True
            break

    if not has_session:
        return {"logged_in": False,
                "reason": "no TikTok cookies", "file": cookies_path}

    return {"logged_in": True, "reason": "ok", "file": cookies_path}


def find_tiktok_cookies():
    """Return list of all cookie files with valid TikTok session.

    Scans the legacy data/cookies.txt first, then data/cookies/tiktok/*.txt.
    Each element is (Path, status_dict).
    """
    from config import VIDEOS_DIR
    data_dir = VIDEOS_DIR.parent
    results = []

    legacy = data_dir / "cookies.txt"
    if legacy.exists():
        status = _check_tiktok_cookie(legacy)
        if status["logged_in"]:
            results.append((legacy, status))

    if COOKIES_DIR.exists():
        for f in sorted(COOKIES_DIR.glob("*.txt")):
            status = _check_tiktok_cookie(f)
            if status["logged_in"]:
                results.append((f, status))

    return results


def tiktok_session_status(cookies_path=None):
    """Check TikTok session status.

    If no path is given, checks legacy data/cookies.txt first, then scans
    data/cookies/tiktok/*.txt for valid sessions.
    """
    from config import VIDEOS_DIR
    data_dir = VIDEOS_DIR.parent

    if cookies_path is not None:
        return _check_tiktok_cookie(cookies_path)

    # Check legacy
    legacy = data_dir / "cookies.txt"
    if legacy.exists():
        status = _check_tiktok_cookie(legacy)
        if status["logged_in"]:
            return status

    # Check multi-account dir
    valid = find_tiktok_cookies()
    if valid:
        return valid[0][1]

    return {"logged_in": False, "reason": "no cookie files found",
            "file": None}


class TikTokScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def extract_video_id(self, url):
        patterns = [
            r'tiktok.com/@[\w.-]+/video/(\d+)',
            r'tiktok.com/.*[?&]v=(\d+)',
            r'vm.tiktok.com/(\w+)',
            r'vt.tiktok.com/(\w+)',
        ]
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)

        # Try to extract from shortened URL
        if 'vm.tiktok.com' in url or 'vt.tiktok.com' in url:
            try:
                response = requests.head(url, headers=self.headers, allow_redirects=True, timeout=10)
                return self.extract_video_id(response.url)
            except:
                pass

        return None

    def get_post_metadata(self, url):
        video_id = self.extract_video_id(url)
        if not video_id:
            return None, "", ""

        try:
            # Basic metadata extraction - captions/hashtags would require TikTok API or scraping
            # For now, return empty strings (yt-dlp will handle download)
            return video_id, "", ""
        except Exception:
            return video_id, "", ""

    def get_all_videos_from_profile(self, username, progress_callback=None):
        """Scrape all video URLs from a TikTok profile.

        Gets the user's secUid from the profile HTML, then uses yt-dlp's
        built-in TikTok user extractor (which handles TikTok's X-Bogus
        request signatures) with the saved cookies to list every video.
        Returns a list of video URLs.
        """
        entries = self.scrape_profile_entries(username, progress_callback=progress_callback)
        return [e["url"] for e in entries]

    def scrape_profile_entries(self, username, progress_callback=None):
        """Scrape all video entries from a TikTok profile.

        Returns a list of dicts with keys: video_id, title, url, duration,
        view_count, description. Uses yt-dlp's tiktok:user extractor with
        cookies (which handles TikTok's X-Bogus request signatures).
        """
        import time
        import yt_dlp

        # Find valid TikTok cookies
        cookies_path = self._find_tiktok_cookie()
        if not cookies_path:
            raise RuntimeError(
                "❌ No TikTok cookies found!\n\n"
                "TikTok profile scraping requires cookies.\n\n"
                "To fix this:\n"
                "1. Install 'Get cookies.txt LOCALLY' browser extension\n"
                "2. Visit tiktok.com in your browser (login is optional)\n"
                "3. Export cookies while on tiktok.com\n"
                "4. Save to one of these locations:\n"
                "   • data/cookies.txt (legacy)\n"
                "   • data/cookies/tiktok/*.txt (multi-account)\n"
            )

        if progress_callback:
            progress_callback(f"🔑 Using cookies from: {cookies_path.name}")

        # Build a requests session with cookies to fetch user info (secUid)
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        })
        jar = http.cookiejar.MozillaCookieJar(str(cookies_path))
        jar.load(ignore_discard=True, ignore_expires=True)
        for cookie in jar:
            session.cookies.set(cookie.name, cookie.value, domain=cookie.domain, path=cookie.path)

        user_info = self._get_user_info(session, username)
        if not user_info:
            # TikTok occasionally serves a thin login-shell page on early
            # requests (anti-bot) before returning the full SSR page. Retry
            # a few times with a short pause.
            import time
            for _ in range(5):
                time.sleep(1.5)
                user_info = self._get_user_info(session, username)
                if user_info:
                    break
        if not user_info:
            raise Exception(f"Could not fetch user info for @{username}")
        sec_uid = user_info.get('secUid', '')
        if not sec_uid:
            raise Exception(f"Could not get secUid for @{username}")
        video_count = user_info.get('videoCount', '?')
        if progress_callback:
            progress_callback(f"📡 Found user: {user_info.get('nickname', username)} ({video_count} videos)")

        # Use yt-dlp's TikTok user extractor to list all videos.
        # Passing the secUid directly ("tiktokuser:{secUid}") avoids the
        # "Unable to extract secondary user ID" failure that can happen
        # when yt-dlp re-parses the profile page itself.
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True,
            'cookiefile': str(cookies_path),
            'http_headers': {'Referer': 'https://www.tiktok.com/'},
        }
        entries = []
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(f"tiktokuser:{sec_uid}", download=False)
                raw_entries = info.get('entries') or []
                for entry in raw_entries:
                    video_id = entry.get('id')
                    if not video_id:
                        continue
                    entries.append({
                        "video_id": video_id,
                        "title": entry.get('title', '') or '',
                        "url": f"https://www.tiktok.com/@{username}/video/{video_id}",
                        "duration": entry.get('duration', 0) or 0,
                        "view_count": entry.get('view_count', 0) or 0,
                        "description": entry.get('description') or entry.get('title', '') or '',
                    })
                if progress_callback:
                    progress_callback(
                        f"📄 Found {len(entries)} videos (total: {len(entries)})"
                    )
        except Exception as e:
            if progress_callback:
                progress_callback(f"⚠️ yt-dlp user extraction error: {str(e)[:100]}")

        return entries

    def _find_tiktok_cookie(self):
        """Find a valid TikTok cookie file."""
        from config import VIDEOS_DIR
        data_dir = VIDEOS_DIR.parent

        # Check legacy location
        legacy = data_dir / "cookies.txt"
        if legacy.exists():
            status = _check_tiktok_cookie(legacy)
            if status["logged_in"]:
                return legacy

        # Check multi-account directory
        if COOKIES_DIR.exists():
            for f in sorted(COOKIES_DIR.glob("*.txt")):
                status = _check_tiktok_cookie(f)
                if status["logged_in"]:
                    return f

        return None

    def _get_user_info(self, session, username):
        """Get TikTok user info including secUid."""
        try:
            # Try the web profile page first
            resp = session.get(
                f"https://www.tiktok.com/@{username}",
                timeout=15
            )

            if resp.status_code == 200:
                # Look for SIGI_STATE or __NEXT_DATA__ in the HTML
                text = resp.text

                # Try to find user data in SIGI_STATE (newer TikTok)
                match = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>', text, re.DOTALL)
                if match:
                    import json
                    data = json.loads(match.group(1))
                    user = data.get('__DEFAULT_SCOPE__', {}).get('webapp.user-detail', {}).get('userInfo', {}).get('user', {})
                    if user:
                        stats = data.get('__DEFAULT_SCOPE__', {}).get('webapp.user-detail', {}).get('userInfo', {}).get('stats', {})
                        return {
                            'secUid': user.get('secUid', ''),
                            'nickname': user.get('nickname', ''),
                            'videoCount': stats.get('videoCount', 0),
                        }

                # Try SIGI_STATE (older format)
                match = re.search(r'<script id="SIGI_STATE"[^>]*>(.*?)</script>', text, re.DOTALL)
                if match:
                    import json
                    data = json.loads(match.group(1))
                    user = data.get('UserModule', {}).get('users', {})
                    if user:
                        for uid, udata in user.items():
                            return {
                                'secUid': udata.get('secUid', ''),
                                'nickname': udata.get('nickname', ''),
                                'videoCount': udata.get('stats', {}).get('videoCount', 0),
                            }

            # Fallback: try the API directly
            resp = session.get(
                "https://www.tiktok.com/api/user/detail/",
                params={'uniqueId': username, 'language': 'en'},
                timeout=15
            )
            if resp.status_code == 200:
                data = resp.json()
                user = data.get('userInfo', {}).get('user', {})
                if user:
                    return {
                        'secUid': user.get('secUid', ''),
                        'nickname': user.get('nickname', ''),
                        'videoCount': user.get('stats', {}).get('videoCount', 0),
                    }

        except Exception as e:
            pass

        return None
