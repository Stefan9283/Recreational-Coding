import math

import time

offset = 5
map = [[int(c) for c in line.strip('\n')] for line in open('in').readlines()]

def getNeighbours(coords: tuple[int]) -> list[tuple[int]]:
    x, y = coords
    neigh = [
        (x + 1, y    ),
        (x    , y + 1),
        (x - 1, y    ),
        (x    , y - 1),
    ]
    neigh = [(x, y) for x, y in neigh if x in range(map.__len__() * offset) and y in range(map[0].__len__() * offset)]
    return neigh
def getMapValue(coords: tuple[int]):
    i, j = coords
    val = (map[i % len(map)][j % len(map[0])] \
            + i // len(map) + j // len(map[0]))
    if val // 10:
        return val % 10 + 1
    return val

minDist = {}
for i in range(len(map) * offset):
    for j in range(len(map[0]) * offset):
        minDist[(i,j)] = math.inf
target = (len(map) * offset - 1, len(map[0]) * offset - 1)
visited = set()
stack = [(0, 0)]
minDist[(0, 0)] = 0

time1 = time.perf_counter()

# min dist gen
while stack:
    current = stack[0]
    stack.pop(0)
    if current in visited: continue
    visited.add(current)
    
    neigh = getNeighbours(current)
    for next in neigh:
        minDist[next] = min(minDist[next], minDist[current] + getMapValue(next))
        if next not in visited:
            stack.append(next)
    stack.sort(key=lambda x: minDist[x])


print((time.perf_counter() - time1)) # / 60)


print(minDist[target])
