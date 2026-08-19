with open('D:\\MyFinalAutomations\\VideoTextExtractor\\gui\\dashboard.py', 'r') as f:
    content = f.read()
old = 'if bool(self.cc_vertical_var.get()):\n                cc_slug = "case_commentary_longvideo"'
new = '''if bool(self.cc_vertical_var.get()):
                cc_slug = "case_commentary_longvideo"
            elif self.cc_niche_var.get().strip().lower() == "animal storytelling":
                cc_slug = "case_commentary_animal_story"'''
if old in content:
    content = content.replace(old, new)
    with open('D:\\MyFinalAutomations\\VideoTextExtractor\\gui\\dashboard.py', 'w') as f:
        f.write(content)
    print('Replaced successfully')
else:
    print('Pattern not found - showing surrounding lines:')
    # Show lines around the target
    idx = content.find('if bool(self.cc_vertical_var.get()):')
    if idx >= 0:
        print(repr(content[idx:idx+120]))