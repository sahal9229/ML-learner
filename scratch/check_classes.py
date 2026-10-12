import re
with open('js/demos.js', 'r', encoding='utf-8') as f:
    d = f.read()
classes = set(re.findall(r'class="([^"]+)"', d))
for c in sorted(classes):
    print(c)
