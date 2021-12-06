from typing import List, overload

file1 = open('in0', 'r')
Lines = file1.readlines()

def doIteration(L: List) -> List:
    n = len(L)
    for i in range(n):
        if L[i] != 0:
            L[i] -= 1
        else:
            L[i] = 6
            L.append(8)
    return L

L = [int(i) for i in Lines[0].split(',')]
print(L)

for i in range(80):
    L = doIteration(L)
    print(len(L), i)
