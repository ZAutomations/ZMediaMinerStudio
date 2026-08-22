import sys
import re

# Read the file
with open('D:\\GitHub\\pythonprojects\\VideoTextExtractor\\gui\\dashboard.py', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Find the _cc_parse_response function
idx = content.find('def _cc_parse_response')
print("Function at position:", idx)

# Print the last 500 characters of the function to see its structure
# Find "return result" near the end
search_for = "return result"
search_pos = content.find(search_for, idx)
if search_pos >= 0:
    # Print from search_pos to search_pos + 500
    print(content[search_pos:search_pos+2000])
else:
    print("Could not find return result")