import sys
import re

with open('D:\GitHub\pythonprojects\VideoTextExtractor\gui\dashboard.py', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Find the _cc_parse_response function
idx = content.find('def _cc_parse_response(')
if idx < 0:
    print("Function not found")
    sys.exit(1)

# Print the function's structure to understand where to add new handlers
# Get the full function
func_start = idx
# Find the end of the function - look for the next major function or class
# For now, let me just identify where to insert new elif clauses

# Search for the pattern after COMMENTARY SPOTS handler
# The function has a series of elif clauses, I need to add new ones before "return result"

# Let me find "return result" position in the function
# The function starts at idx, so search from idx
search_for = "return result"
search_pos = content.find(search_for, idx)
print("return result at position:", search_pos)

# Now let me look at what's just before "return result"
# I need to add new elif clauses just before this

# Let me look at the structure - I need to find a good place to insert
# Look for the end of the COMMENTARY SPOTS handler and add new handlers after it

# Let me print a section to understand the structure
# Print from 800 chars before return result to return result
ret_start = max(idx, search_pos - 800)
print(content[ret_start:search_pos+100])