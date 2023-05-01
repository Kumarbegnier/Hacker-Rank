from collections import deque

d = deque()

n = int(input())

for i in range(n):
    op = input().split()
    if op[0] == 'append':
        d.append(op[1])
    elif op[0] == 'appendleft':
        d.appendleft(op[1])
    elif op[0] == 'pop':
        d.pop()
    elif op[0] == 'popleft':
        d.popleft()

print(' '.join(d))
