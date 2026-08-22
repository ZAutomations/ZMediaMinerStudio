import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('D:\GitHub\pythonprojects\VideoTextExtractor\gui\dashboard.py', 'r', encoding='utf-8', errors='replace') as f:
    c = f.read()
idx = c.find('def _cc_parse_response')
print(c[idx:idx+6000])