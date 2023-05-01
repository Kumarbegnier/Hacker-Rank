from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = sorted(product(A, B))

for pair in result:
    print(pair, end=' ')
