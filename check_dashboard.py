import re

with open('D:\GitHub\pythonprojects\VideoTextExtractor\gui\dashboard.py', 'r', encoding='utf-8', errors='replace') as f:
    c = f.read()

idx = c.find('_cc_parse_response')
if idx >= 0:
    print('Found _cc_parse_response at position', idx)
    print('Context:')
    print(c[max(0,idx-100):idx+1500])
else:
    print('_cc_parse_response not found in dashboard.py')