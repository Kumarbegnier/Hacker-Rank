# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s, k = input().split()
k = int(k)

for i in range(1, k+1):
    for combo in combinations(sorted(s), i):
        print(''.join(combo))
