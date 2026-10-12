import re
with open('js/catalog.js', 'r', encoding='utf-8') as f:
    d = f.read()
ms = set(re.findall(r'"module":\s*"([^"]+)"', d))
for m in sorted(ms):
    print(m)
