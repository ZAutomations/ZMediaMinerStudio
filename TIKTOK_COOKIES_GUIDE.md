# How to Export TikTok Cookies

TikTok profile scanning requires cookies to work properly (a full cookie export works even without logging in). Follow these steps:

## Method 1: Using "Get cookies.txt LOCALLY" Extension (Recommended)

### Step 1: Install Browser Extension
- **Chrome/Edge**: [Get cookies.txt LOCALLY](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)
- **Firefox**: [cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)

### Step 2: Open TikTok (Login Optional)
1. Open your browser
2. Go to https://www.tiktok.com
3. **Login with your TikTok account** (recommended, but not required — a plain visit is enough)
4. Make sure the page loads

### Step 3: Export Cookies
1. **Stay on tiktok.com** (don't navigate away)
2. Click the extension icon in your browser toolbar
3. Click "Export" or "Download"
4. A `cookies.txt` file will be downloaded

### Step 4: Move to Data Folder
1. Find your downloaded `cookies.txt` file (usually in Downloads folder)
2. Copy or move it to one of these locations:
   ```
   D:\MyFinalAutomations\VideoTextExtractor\data\cookies.txt
   ```
   OR for multi-account support:
   ```
   D:\MyFinalAutomations\VideoTextExtractor\data\cookies\tiktok\account1.txt
   ```

## Multi-Account Support

For managing multiple TikTok accounts:
1. Create a folder: `data\cookies\tiktok\`
2. Export each account's cookies to separate files:
   - `account1.txt`
   - `account2.txt`
   - etc.
3. The app will automatically rotate between valid cookies

## Troubleshooting

### "No TikTok cookies found" Error
This means:
- Your cookies are missing or expired
- The cookies.txt file is not in the correct location

**Solution**: Export fresh cookies and try again

### "Profile not found" Error
- Make sure you're logged into the correct TikTok account
- Export cookies while on the profile page you want to scrape

### Cookies Expire
- TikTok cookies expire after a few days/weeks
- If scraping stops working, export fresh cookies
- Don't logout from TikTok after exporting cookies

## Important Notes

✅ **DO:**
- Stay logged into TikTok in your browser
- Re-export cookies if they expire
- Keep cookies.txt file safe (it contains your login session)

❌ **DON'T:**
- Share your cookies.txt file with anyone
- Logout from TikTok after exporting cookies
- Use old/expired cookies

## Test Your Cookies

After placing cookies.txt, try scanning a TikTok profile:
1. Go to the Metadata Scan tab
2. Enter a TikTok profile URL (e.g., https://www.tiktok.com/@username)
3. Click "Start Scan"
4. If it works - your cookies are valid!

---

**Need Help?** Make sure you:
1. Are logged into TikTok in browser
2. Export cookies while ON tiktok.com
3. Place cookies.txt in the correct `data` folder
4. The file is named exactly `cookies.txt`
