import sys
import re

with open('D:\GitHub\pythonprojects\VideoTextExtractor\gui\dashboard.py', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# The parser function starts at position 185598
# I need to add new elif clauses after the existing ones

# Let me find a good insertion point - after the COMMENTARY SPOTS handler
# and before the "return result" statement

# First, let me find the exact structure around the existing handlers
# Look for the COMMENTARY SPOTS handler end and return result

# Search for the pattern that ends the commentary spots handling
# and leads to return result

# Actually, let me look at the full function structure by finding
# where each section handler ends

# I'll search for patterns that indicate section handlers end
# Typically they end with a blank line or the next elif

# Let me find where the COMMENTARY SPOTS handler's relevant code ends
# by searching for patterns after it

# Get the function content
func_start = 185598
func_content = content[func_start:]

# Find "return result" in the function
ret_pos = func_content.find("return result")
print("return result at position:", ret_pos)

# Now, let me look at what comes before return result
# I need to add new elif clauses BEFORE the return result

# Let me print the last 2000 characters of the function
print("Last 2000 chars of function:")
print(func_content[-2000:])