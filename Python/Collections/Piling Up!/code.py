from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    cubes = list(map(int, input().split()))
    
    tower = deque()
    if cubes[0] >= cubes[-1]:
        tower.append(cubes[0])
        last_cube = cubes[0]
        cubes.pop(0)
    else:
        tower.append(cubes[-1])
        last_cube = cubes[-1]
        cubes.pop()
    
    while cubes:
        if cubes[0] >= cubes[-1] and cubes[0] <= last_cube:
            tower.appendleft(cubes[0])
            last_cube = cubes[0]
            cubes.pop(0)
        elif cubes[-1] > cubes[0] and cubes[-1] <= last_cube:
            tower.append(cubes[-1])
            last_cube = cubes[-1]
            cubes.pop()
        else:
            print("No")
            break
    else:
        print("Yes")
