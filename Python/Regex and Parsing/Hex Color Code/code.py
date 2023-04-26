import re

n = int(input())
for i in range(n):
    line = input().strip()
    # Ignore lines that are not property lines
    if ':' not in line:
        continue
    # Find all the HEX color codes in the line
    color_codes = re.findall(r'#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b', line)
    # Print the color codes with '#' symbol
    for code in color_codes:
        print('#' + code)
