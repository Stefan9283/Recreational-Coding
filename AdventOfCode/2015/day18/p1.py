from typing import List

def printMat(mat):
    for row in mat:    
        print(row)
    print()

def copyMatrix(mat):
    mat2 = []
    for row in mat:
        mat2.append(list(row))
    return mat2

def getNeighbours(x, y, mat) -> List[tuple[int, int]]:
    neigh = [
        (x + 1, y    ),
        (x - 1, y    ),
        (x   , y + 1),
        (x   , y - 1),
        (x + 1, y + 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y - 1),
    ]
    neigh = [(x, y) for x, y in neigh if x in range(mat.__len__()) and y in range(mat[0].__len__())]
    return neigh

def countLitNeighbours(i, j, mat) -> int:
    neigh = getNeighbours(i, j, mat)
    count = 0
    for x, y in neigh:
        if mat[x][y] == '#':
            count += 1
    return count

steps = 100

mat = []

for line in open('in').readlines():
    mat.append([c for c in line.strip('\n')])


for _ in range(steps):
    old = copyMatrix(mat)
    x, y = len(mat), len(mat[0])
    for i in range(x):        
        for j in range(y):
            lit = countLitNeighbours(i, j, old)
            if old[i][j] == '.':
                if lit == 3:
                    mat[i][j] = '#'
            else:
                if lit not in [2, 3]:
                    mat[i][j] = '.'
    # for the 2nd part uncomment the following 4 lines
    # mat[0][0]  = '#'
    # mat[0][y - 1]  = '#'
    # mat[x - 1][0]  = '#'
    # mat[x - 1][y - 1]  = '#'
                
print(sum([row.count('#') for row in mat]))