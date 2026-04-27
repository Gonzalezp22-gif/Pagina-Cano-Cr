import re
import json

html = open('index.html', encoding='utf-8').read()

# Find all href links
links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', html)
wa_links = [l for l in links if 'wa.me' in l.lower() or 'whatsapp' in l.lower()]
print("WhatsApp links in href:", json.dumps(wa_links, indent=2))

# Find phone numbers in text (basic regex)
# let's look for numbers we previously had: 5539580291, 5215546865327, 11305122142
for num in ["5539580291", "5215546865327", "11305122142"]:
    if num in html:
        print(f"WARNING: Old number {num} found in html!")
    else:
        print(f"Good: Old number {num} NOT found.")

# Look for the new number
print("Occurrences of new number:", html.count("525661452038"))

# Look for 'joinchat' configuration (the whatsapp plugin)
joinchat_match = re.search(r'data-settings=\'([^\']+)\'', html)
if joinchat_match:
    print("Joinchat settings:", joinchat_match.group(1))

