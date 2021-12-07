from typing import Dict

file1 = open('in1', 'r')
Lines = file1.readlines()

L = [int(i) for i in Lines[0].split(',')]
L.sort()
median = L[len(L) // 2]
moves = 0
for i in L:
    moves += abs(i - median)
print(L, moves)

