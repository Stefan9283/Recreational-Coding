
from typing import Tuple


with open('in', 'r') as f:
    m = [list(line.rstrip()) for line in f.readlines()]
    # enhance
    m_ = []
    for l in m:
        l_ = []
        for c in l:
            l_.append(c)
            l_.append(c)
            l_.append(c)
        m_.append(list(l_))
        m_.append(list(l_))
        m_.append(list(l_))
    m = m_            
    print('\n'.join([''.join(l) for l in m]))

visited = [['.' for _ in range(len(m[0]))] for _ in range(len(m))]


def get_island_perim_and_area(start: Tuple[int, int]):
    init = m[start[0]][start[1]]
    
    stack = [start]
    
    A = 0
    perimeter = set()
    
    while stack:
        i, j = stack.pop()
        c = m[i][j]
        
        if c != init: continue
        if visited[i][j] != '.': continue
        visited[i][j] = c

        A += 1

        if i == 0 or (i != 0 and m[i-1][j] != c):
            perimeter.add((i, j))
        if i == len(m) - 1 or (i != len(m) - 1 and m[i+1][j] != c):
            perimeter.add((i, j))
        if j == 0 or (j != 0 and m[i][j-1] != c):
            perimeter.add((i, j))
        if j == len(m[0]) - 1 or (j != len(m[0]) - 1 and m[i][j + 1] != c):
            perimeter.add((i, j))
        # diagonals
        # left top
        if i != 0 and j != 0 and m[i-1][j-1] != c:
            perimeter.add((i, j))
        # left bottom
        if i != len(m) - 1 and j != 0 and m[i+1][j-1] != c:
            perimeter.add((i, j))
        # right top
        if i != 0 and j != len(m[0]) - 1 and m[i-1][j+1] != c:
            perimeter.add((i, j))
        # right bottom
        if i != len(m) - 1 and j != len(m[0]) - 1 and m[i+1][j+1] != c:
            perimeter.add((i, j))
        
        if i != 0: stack.append((i-1, j))
        if j != 0: stack.append((i, j-1))
        if i != len(m)-1: stack.append((i+1, j))
        if j != len(m[0])-1: stack.append((i, j+1))

    
    def draw_perimeter(perim):
        m_ = [ [ '.' for _ in range(len(m[0])) ] for _ in range(len(m)) ]
        for (i, j) in perim:
            m_[i][j] = '#'
        print('\n'.join([''.join(x) for x in m_]))

    # draw_perimeter(perimeter)
    
    # 8,5
    notused = list(perimeter)
    notused.remove(start)
    perimeter = [start]

    while notused:
        # print(notused, end=' ')
        lastx, lasty = perimeter[-1]

        notused.sort(key=lambda x: (lastx - x[0])**2 + (lasty - x[1])**2)
        
        # print((lastx, lasty), notused[0])
        next = notused.pop(0)
        
        perimeter.append(next)
        
    # print('perimeter', perimeter)
    fst, snd = perimeter[0], perimeter[1]
    edge_direction = (snd[0] - fst[0], snd[1] - fst[1])
    direction_change_counter = 1
    for i in range(1, len(perimeter) - 2):
        fst, snd, trd = perimeter[i], perimeter[i+1], perimeter[i+2]
        if (fst[0] + edge_direction[0], fst[1] + edge_direction[1]) == snd:
            # print(fst, snd, edge_direction)
            continue
        direction_change_counter += 1
        # print(fst, snd, edge_direction, 'switch')
        edge_direction = (trd[0] - snd[0], trd[1] - snd[1])
        
    # print(direction_change_counter)
    
    # print(init, perimeter)        

    # print(perimeter, len(perimeter))
    
    draw_perimeter(perimeter)
   
    if direction_change_counter % 2 == 1:
        direction_change_counter += 1
        
    # print(direction_change_counter)

    return direction_change_counter, A // 9


ret = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if visited[i][j] != '.': continue
        print("new shape", m[i][j])
        P, A = get_island_perim_and_area((i, j))
        ret += P * A 
        print('values', P, A)
        # print('\n'.join([''.join(l) for l in visited]))
print(ret)
