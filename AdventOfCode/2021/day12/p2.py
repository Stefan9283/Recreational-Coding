from typing import List

graph = {}
foundPaths = set()

def atLeastTwoCanBeFoundTwice(arr: List[str]) -> bool:
    lower = [s for s in arr if s.islower()]
    lowerset = set(lower)
    return lower.__len__() - lowerset.__len__() >= 2

def generatePaths(current: str, visited: List[str]):
    if atLeastTwoCanBeFoundTwice(visited): return
    visited.append(current)
    if current == 'end': 
        foundPaths.add(tuple(visited))
        return
  
    for next in graph[current]:
        if next == 'start': continue
        if visited.count(next) == 2 and next.islower(): continue
        generatePaths(next, list(visited))

for line in open('in').readlines():
    line = line.strip('\n')
    source, dest = line.split('-')
    if graph.get(source) == None: graph[source] = []
    if graph.get(dest) == None: graph[dest] = []
    graph[source].append(dest)
    graph[dest].append(source)

generatePaths('start', [])
        
print(len(foundPaths))
