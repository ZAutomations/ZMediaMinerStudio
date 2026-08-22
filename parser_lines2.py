import sys
sys.stdout.reconfigure(encoding='utf-8')
content=open('D:\GitHub\pythonprojects\VideoTextExtractor\gui\dashboard.py','r',encoding='utf-8',errors='replace').read()
idx=content.find("def _cc_parse_response(")
ret_pos=content.find("return result", idx)
lines=content.split('\n')
for i in range(ret_pos-60, ret_pos+20):
    if i < len(lines):
        print(f'{i}: {lines[i][:80]}')