from typing import List

graph = {}

foundPaths = set()

def generatePaths(current: str, visited: List[str]):
    if current.islower() and current in visited: return
    if current == 'end': 
        visited.append('end')
        foundPaths.add(tuple(visited))
    
    visited.append(current)
    
    for next in graph[current]:
        if next.islower() and next in visited: continue
        generatePaths(next, list(visited))


for line in open('in').readlines():
    line = line.strip('\n')
    source, dest = line.split('-')
    if graph.get(source) == None: graph[source] = []
    if graph.get(dest) == None: graph[dest] = []
    graph[source].append(dest)
    graph[dest].append(source)

print(graph)
generatePaths('start', [])
        
for path in foundPaths:
    print(path)
print(len(foundPaths))
