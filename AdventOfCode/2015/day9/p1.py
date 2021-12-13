from typing import List

infinity = 99999999999999999999

graph = {}

def shortestPath(current: str, visited: List[str], current_dist: int) -> int:
    if len(graph) == len(visited): return 0
    
    global ind
    
    visitedNew = list(visited)
    visitedNew.append(current)
    
    shortest = infinity
    
    for next, dist in graph[current]:
        if next in visited: continue
        nextlen = shortestPath(next, visitedNew, dist)
        shortest = min(shortest, nextlen)
        
    if shortest == infinity:
        shortest = 0
    return current_dist + shortest


# build graph
for line in open('in').readlines():
    loc1, _, loc2, _, dist = line.split()
    if graph.get(loc1) == None: graph[loc1] = []
    if graph.get(loc2) == None: graph[loc2] = []
    graph[loc1].append([loc2, int(dist)])
    graph[loc2].append([loc1, int(dist)])

# print graph
for loc in graph:
    print(loc, graph[loc])

# find shortest path
shortest = infinity
for loc in graph:
    shortest = min(shortest, shortestPath(loc, [], 0))
print(shortest)

