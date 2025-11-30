
from typing import Tuple


with open('in', 'r') as f:
    m = [list(line.rstrip()) for line in f.readlines()]

visited = [['_' for _ in range(len(m[0]))] for _ in range(len(m))]

print(m)

def get_island_perim_and_area(start: Tuple[int, int]):
    init = m[start[0]][start[1]]
    
    s = [start]
    
    A, P = 0, 0
    
    while s:
        i, j = s.pop()
        c = m[i][j]
        
        if c != init: continue
        if visited[i][j] != '_': continue
        visited[i][j] = c

        A += 1
        
        if i == 0 or (i != 0 and m[i-1][j] != c):
            P += 1
        if i == len(m) - 1 or (i != len(m) - 1 and m[i+1][j] != c):
            P += 1
        if j == 0 or (j != 0 and m[i][j-1] != c):
            P += 1
        if j == len(m[0]) - 1 or (j != len(m[0]) - 1 and m[i][j + 1] != c):
            P += 1
            
        if i != 0: s.append((i-1, j))
        if j != 0: s.append((i, j-1))
        if i != len(m)-1: s.append((i+1, j))
        if j != len(m[0])-1: s.append((i, j+1))

    return P, A


ret = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if visited[i][j] != '_': continue
        P, A = get_island_perim_and_area((i, j))
        ret += P * A 
        print(P, A)
        print('\n'.join([''.join(l) for l in visited]))
        
print(ret)
