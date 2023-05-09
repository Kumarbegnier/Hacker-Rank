from itertools import permutations

s, k = input().split()
k = int(k)

perms = list(permutations(sorted(s), k))

for perm in perms:
    print(''.join(perm))
