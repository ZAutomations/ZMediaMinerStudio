import sys
sys.stdout.reconfigure(encoding='utf-8')
content=open('D:\GitHub\pythonprojects\VideoTextExtractor\gui\dashboard.py').read()
idx=content.find("def _cc_parse_response(")
print("Found at:", idx)