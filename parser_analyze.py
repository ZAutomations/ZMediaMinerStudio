import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('D:\GitHub\pythonprojects\VideoTextExtractor\gui\dashboard.py', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Find the _cc_parse_response function
idx = content.find('def _cc_parse_response')
if idx < 0:
    print("Function not found")
    sys.exit(1)

# Print the function for analysis
func_content = content[idx:]
print("Function found, length:", len(func_content))

# Now let's look at the end of the function to add new handlers
# Find where the function ends
# Look for the last "return result" or similar
end_marker = "return result"
end_idx = content.find(end_marker, idx)
if end_idx < 0:
    print("Could not find end marker")
    sys.exit(1)

# Print the last part of the function
print("Function end section:")
print(content[end_idx:end_idx+2000])
PYEOF