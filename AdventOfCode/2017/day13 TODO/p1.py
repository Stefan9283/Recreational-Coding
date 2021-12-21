import json

firewall = {}

def getStep(step):
    for d in firewall:
        if firewall[d][1] == firewall[]

max_depth = 0
for line in open('in').readlines():
    Depth, Range = map(int, line.strip('\n').split(': '))
    firewall[Depth] = [Range, 0]
    max_depth = max(max_depth, Depth)

for i in range(max_depth + 1):
    doStep()
