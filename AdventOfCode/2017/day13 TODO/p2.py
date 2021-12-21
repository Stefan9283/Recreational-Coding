import json

nodes = {}

def visitComponent(current: int, visited: list[int]): 
    visited.append(current)
    for next in nodes[current]:
        if next in visited: continue
        visitComponent(next, visited)
        
for line in open('in').readlines():
    node, next = line.strip('\n').split(' <-> ')
    nodes[int(node)] = json.loads('[' + next + ']')

visited = []
count = 0

for i in nodes:
    if i not in visited:
        count += 1
        component = []
        visitComponent(i, component)
        visited += component
        
print(count)


