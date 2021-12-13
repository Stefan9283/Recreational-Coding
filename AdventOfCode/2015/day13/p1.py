import itertools
from typing import Tuple


relationships = {}

def computeHappines(seatting: Tuple[str]) -> int:
    happines = 0
    for i in range(1, len(seatting) - 1):
        happines += relationships[seatting[i]][seatting[i+1]]
        happines += relationships[seatting[i]][seatting[i-1]]
    return happines

for line in open('in').readlines():
    tok = line.strip('.\n').split()
    
    if relationships.get(tok[0]) == None:
        relationships[tok[0]] = {}
    
    val = int(tok[3])
    if tok[2] == 'lose':
        val = -val

    relationships[tok[0]][tok[-1]] = val

maxHappines = 0
for perm in itertools.permutations(relationships):
    perm = perm.__add__((perm[0], )).__add__((perm[1], ))
    maxHappines = max(maxHappines, computeHappines(perm))

print(maxHappines)    
