from collections import defaultdict

n, m = map(int, input().split())
group_a = [input() for _ in range(n)]
group_b = [input() for _ in range(m)]

indices = defaultdict(list)

for i, word in enumerate(group_a, start=1):
    indices[word].append(i)

for word in group_b:
    if word in indices:
        print(' '.join(map(str, indices[word])))
    else:
        print(-1)
