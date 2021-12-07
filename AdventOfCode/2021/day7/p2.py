from typing import Dict

file1 = open('in0', 'r')
Lines = file1.readlines()

L = [int(i) for i in Lines[0].split(',')]
L.sort()

# for given example in in0 just remove - 1
mid = round(sum(L) / len(L)) - 1
moves = 0
for i in L:
    n = abs(i - mid)
    moves += (n * (n + 1)) // 2
print(mid, moves)