import re

n = int(input())
html = ''
for i in range(n):
    html += input()

# Remove comments from the HTML code
html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

# Find all tags, attributes, and attribute values
tags = re.findall(r'<([a-zA-Z0-9]+)[^>]*>', html)
attrs = re.findall(r'<[a-zA-Z0-9]+([^>]*)>', html)
values = re.findall(r'([a-zA-Z0-9-]+)="([^"]*)"', html)

# Print the tags, attributes, and attribute values in the required format
for i, tag in enumerate(tags):
    print(tag)
    for j, attr in enumerate(re.findall(r'([a-zA-Z0-9-]+)="([^"]*)"', attrs[i])):
        print('-> ' + attr[0] + ' > ' + attr[1], end='')
        if j < len(re.findall(r'([a-zA-Z0-9-]+)="([^"]*)"', attrs[i])) - 1:
            print('', end='')
        print()
