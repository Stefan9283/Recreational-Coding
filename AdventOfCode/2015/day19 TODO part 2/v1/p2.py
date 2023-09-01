import re
import sys

def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString
    
import math

replacements = {}

indent = 0

visited = set()

def findNumSteps(s: str):
    if s == 'e': return 0
    if s.find('e') != -1 and s.__len__() != 1: return math.inf
    if s in visited: return math.inf
    visited.add(s)
    global indent
    minSteps = math.inf
    # print(''.join(['\t' for _ in range(indent)]), s)
    for To in replacements:
        for From in replacements[To]:
            for i in range(s.count(To)):
                indent += 1
                minSteps = min(minSteps, 1 + findNumSteps(replacenth(s, To, From, i)))
                indent -= 1
    return minSteps

lines = open('in').readlines()

startMolecule = lines[-1]


for rep in lines[:-2]:
    fst, _, snd = rep.strip('\n').split()
    if replacements.get(snd) == None: replacements[snd] = []
    replacements[snd].append(fst)

print(findNumSteps(startMolecule))
