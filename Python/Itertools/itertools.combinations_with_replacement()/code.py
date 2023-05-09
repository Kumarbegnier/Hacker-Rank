# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)

# Get the combinations with replacements
combs = combinations_with_replacement(sorted(s), k)

# Print the combinations in lexicographic order
for c in combs:
    print(''.join(c))
