#!/usr/bin/python3
import re, json
members_html = open('List1.html', 'r').read()
members_json = {'List1Members': []}
members = re.finditer(
    r'<li><b>\s*([А-ЯЁа-яё]+)\s*<\/b>\s+([А-ЯЁа-яё]+)\s+\(\s*([А-ЯЁа-яё\-]+)\s*\)(\s+\[\*\])?<\/li>',
    members_html
)
for member in members:
    members_json['List1Members'].append({
        "name": member.group(2) + " " + member.group(1),
        "location": member.group(3)
    })
with open('List1.json', 'w') as list1:
    list1.write(json.dumps(members_json))
    list1.close()
