import sys
import re

with open('D:\GitHub\pythonprojects\VideoTextExtractor\gui\dashboard.py', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Find the _cc_parse_response function
idx = content.find('def _cc_parse_response(')
if idx < 0:
    print("Function not found")
    sys.exit(1)

# Get the function content
func_content = content[idx:]

# I need to add new elif clauses for the new sections.
# Let me find where to insert them - after the COMMENTARY SPOTS handler and before "return result"

# First, let me find the "return result" position
ret_pos = func_content.find("return result")
if ret_pos < 0:
    print("Could not find return result")
    sys.exit(1)

# Now let me find the COMMENTARY SPOTS handler end position
# I'll look for the pattern that ends the commentary spots handling
# The function has a structure like:
# if ...:
#     ...
# elif ...:
#     ...
# elif upper.startswith("COMMENTARY SPOTS") ...:
#     ... handler code ...
# (new elif clauses I will add)
# return result

# Let me find a good insertion point - just before "return result"
# I'll insert new elif clauses between the last existing handler and "return result"

# Let me look at what the last handler is and where it ends
# Search for "COMMENTARY SPOTS" in the function
com_spots_pos = func_content.find("COMMENTARY SPOTS")
if com_spots_pos < 0:
    com_spots_pos = func_content.find("COMMENTARY SPOTS")
print("COMMENTARY SPOTS at position:", com_spots_pos)

# Let me find the "SPOTS" handler too
spots_pos = func_content.find("upper.startswith")
print("SPOTS handler positions found")

# Actually, let me take a different approach - I'll just add the new elif clauses
# at the end of the elif chain, just before "return result"

# The new sections I need to handle from the prompt:
# - "ORIGINAL CLIENT AUDIO" 
# - "VIDEO EDITING INSTRUCTIONS"
# - "CTA" (already have hashtag_1/hashtag_2)

# I'll add them as new elif clauses after the existing ones

# Let me construct the new elif clauses
new_elif_clauses = """
            elif upper.startswith("ORIGINAL CLIENT AUDIO"):
                current_section = "original_audio"
                content = chunk.split("\\n", 1)
                if len(content) > 1:
                    raw = content[1].strip()
                    result["original_audio"] = raw

            elif upper.startswith("VIDEO EDITING INSTRUCTIONS"):
                current_section = "editing_instructions"
                content = chunk.split("\\n", 1)
                if len(content) > 1:
                    raw = content[1].strip()
                    result["editing_instructions"] = raw

            elif upper.startswith("CTA"):
                current_section = "cta"
                content = chunk.split("\\n", 1)
                if len(content) > 1:
                    raw = content[1].strip()
                    # CTA is max 12 words, but we'll just store the text
                    result["cta"] = raw

            elif upper.startswith("THUMBNAIL"):
                current_section = "thumbnail"
                # Existing thumbnail handling might be here
                # Or we can just store the text
                content = chunk.split("\\n", 1)
                if len(content) > 1:
                    raw = content[1].strip()
                    # Try to extract timestamp and text
                    # Format: THUMBNAIL: 00:00 | [catchy overlay text]
                    match = re.match(r'THUMBNAIL:\\s*([\\d:]+)\\s*[|\\|]\\s*(.+)', raw)
                    if match:
                        result["thumbnail_ts"] = match.group(1).strip()
                        result["thumbnail_text"] = match.group(2).strip()
                    else:
                        result["thumbnail_text"] = raw

"""

# Now I need to insert these new elif clauses into the function content
# I'll insert them just before "return result"

# Find the position of "return result" in the function
ret_pos = func_content.find("return result")
if ret_pos < 0:
    print("Could not find return result")
    sys.exit(1)

# Insert the new elif clauses before "return result"
new_func_content = func_content[:ret_pos] + new_elif_clauses + func_content[ret_pos:]

# Now replace this section in the full content
if new_elif_clauses in func_content:
    # Actually, I need to replace the whole func_content in content
    # But func_content is a substring of content starting at idx
    # Let me find the exact position in content
    content_idx = content.find("def _cc_parse_response(")
    if content_idx < 0:
        print("Could not find function in main content")
        sys.exit(1)
    
    # Replace the function in the main content
    new_content = content[:content_idx] + new_func_content + content[content_idx + len(func_content):]
    
    # Write the modified content
    with open('D:\GitHub\pythonprojects\VideoTextExtractor\gui\dashboard.py', 'w', encoding='utf-8', errors='replace') as f:
        f.write(new_content)
    
    print("New elif clauses added successfully")
    print("Added handlers for: ORIGINAL CLIENT AUDIO, VIDEO EDITING INSTRUCTIONS, CTA, THUMBNAIL")
else:
    print("Could not find the function content to modify")