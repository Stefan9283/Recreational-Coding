from typing import Dict

file1 = open('in0', 'r')
Lines = file1.readlines()

def doIteration(D: Dict) -> Dict:
    D1 = {}
    for key, value in zip(D.keys(), D.values()):
        if key == 0:
            if D1.get(6) == None:
                D1[6] = value
            else:
                D1[6] += value
            if D1.get(8) == None:
                D1[8] = value
            else:
                D1[8] += value
        else:
            if D1.get(key - 1) == None:
                D1[key - 1] = value
            else:
                D1[key - 1] += value
    return D1

L = [int(i) for i in Lines[0].split(',')]

D = {}
for i in L:
    if D.get(i) == None:
        D[i] = 1
    else:
        D[i] += 1
print(D)

for i in range(256):
    D = doIteration(D)
    print(sum(D.values()))
