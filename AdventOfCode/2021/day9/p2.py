from functools import reduce
from typing import List

file1 = open('in1', 'r')
Lines = file1.readlines()

grid = [[int(c) for c in l.strip('\n')] for l in Lines]
visited = [[0 for _ in l.strip('\n')] for l in Lines]
values = sorted([[grid[i][j], [i, j]] \
                 for i in range(0, len(grid)) \
                 for j in range(0, len(grid[i]))])

visitedVal = 1

s = 0

def getNeighbours(i: int, j: int) -> List[int]:
    neigh = []
    if i != 0: neigh.append([i - 1, j])
    if i != len(grid) - 1: neigh.append([i + 1, j])
    if j != 0: neigh.append([i, j - 1])
    if j != len(grid[i]) - 1: neigh.append([i, j + 1])
    return neigh
def getLowestPoint(values) -> List:
    return values[0]
def markAsVisited(i, j):
    values.remove([grid[i][j], [i, j]])
    visited[i][j] = visitedVal
    
def visit(i, j):
    markAsVisited(i, j)
    if grid[i][j] == 9: return 0
    basinSize = 1 + sum(visit(x, y)  \
                    for x, y in getNeighbours(i, j) \
                                    if visited[x][y] == 0)
    return basinSize

sizes = []

while values:
    val, [x, y] = getLowestPoint(values)
    if val == 9: 
        markAsVisited(x, y)
        continue
    sizes.append(visit(x, y))
    visitedVal += 1

sizes.sort()
print(reduce(lambda x, y: x * y, sizes[-3:]))
