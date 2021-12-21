

f = open('in')
algorithm = f.readline()
f.readline()

matrix = []

for line in f.readlines():
    matrix.append(list(line.strip('\n')))

for row in matrix:
    print(row)
print()

def inRange(n) -> bool:
    return n[1] in range(len(matrix[0])) and n[0] in range(len(matrix))
def getCells(x, y) -> list[tuple]:
    neigh = [
        (x - 1, y - 1),
        (x - 1, y    ),
        (x - 1, y + 1),
        (x    , y - 1),
        (x, y),
        (x    , y + 1),
        (x + 1, y    ),
        (x + 1, y - 1),
        (x + 1, y + 1),
    ]
    return neigh

import copy
matrixOld = copy.deepcopy(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        neigh = getCells(i, j)
        index = []
        for n in neigh:
            if not inRange(n):
                index.append('0')
            else:
                x, y = n
                if matrix[x][y] == '.':
                    index.append('0')
                else:
                    index.append('1')
        index = ''.join(index)
        print(i,j, index, int(index, 2))
        matrix[i][j] = algorithm[int(index, 2)]
        
        
for row in matrix:
    print(row)
print()