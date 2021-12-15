
from typing import List
import math

def getNeighbours(x, y, mat) -> List[tuple[int, int]]:
    neigh = [
        (x + 1, y    ),
        (x    , y + 1),
        (x - 1, y    ),
        (x    , y - 1),
    ]
    neigh = [(x, y) for x, y in neigh if x in range(mat.__len__()) and y in range(mat[0].__len__())]
    return neigh

map = [[int(c) for c in line.strip('\n')] for line in open('in').readlines()]

heatmap = [[0 for _ in range(len(map[0]))] for _ in range(len(map))] # TODO remove


minDist = {}
for i in range(len(map)):
    for j in range(len(map[0])):
        minDist[(i,j)] = math.inf
target = (len(map) - 1, len(map[0]) - 1)

minDist[(0, 0)] = 0

visited = set()

stack = [(0, 0, 0)]

while stack:
    stack.sort(key=lambda x: minDist[(x[:2])])
    x, y, risk = stack[0]
    stack.pop(0)

    if (x,y) in visited: continue
    visited.add((x,y))

    heatmap[x][y] += 1

    neigh = getNeighbours(x, y, map)
    for (a, b) in neigh:
        minDist[(a,b)] = min(minDist[(a,b)], risk + map[a][b])
        stack.append((a, b, minDist[(a,b)]))


# for row in heatmap:
#     print(row)


Dists = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]
for x,y in minDist:
    Dists[x][y] = minDist[(x,y)]
for row in Dists:
    print(row) 
print(minDist[target])




