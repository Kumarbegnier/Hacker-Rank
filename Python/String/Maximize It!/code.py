import itertools

# Read input
K, M = map(int, input().split())
lists = [list(map(int, input().split()[1:])) for _ in range(K)]

# Compute maximum value
max_sum = -1
for xs in itertools.product(*lists):
    s = sum(x*x for x in xs) % M
    if s > max_sum:
        max_sum = s

# Print result
print(max_sum)
