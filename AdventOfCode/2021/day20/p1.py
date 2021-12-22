import copy

def printMatrix(matrix):
    matrixcopy = copy.deepcopy(matrix)[1:-1]
    for row in matrixcopy:
        print(''.join(row[1:-1]))
    print()
def extendMatrix(matrix: list[list[int]], padding: int = 1):
    newmatrix = copy.deepcopy(matrix)
    
    c = matrix[0][0]
    
    for i in range(len(newmatrix)):
        newmatrix[i] = [c for _ in range(padding)] + newmatrix[i] + [c for _ in range(padding)]
    for _ in range(padding):
        newmatrix.insert(0, [c for _ in range(len(newmatrix[0]))])
        newmatrix.append([c for _ in range(len(newmatrix[0]))])
    return newmatrix

def readInput():
    f = open('in')
    algorithm = f.readline()
    f.readline()
    matrix = []
    for line in f.readlines():
        matrix.append(list(line.strip('\n')))
    return matrix, algorithm

def inRange(n, matrix) -> bool:
    return n[1] in range(len(matrix[0])) and n[0] in range(len(matrix))
def getCells(x, y) -> list[tuple]:
    neigh = [
        (x - 1, y - 1),
        (x - 1, y    ),
        (x - 1, y + 1),
        (x    , y - 1),
        (x    , y    ),
        (x    , y + 1),
        (x + 1, y - 1),
        (x + 1, y    ),
        (x + 1, y + 1),
    ]
    return neigh

matrix, algorithm = readInput()

steps = 50

for step in range(steps):
    print(step)
    # printMatrix(matrix)
    matrix = extendMatrix(matrix, padding=2)
    matrixOld = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            neigh = getCells(i, j)
            index = []
            for n in neigh:
                if not inRange(n, matrixOld):
                    if algorithm[0] == '#':
                        if step % 2 == 0:
                            index.append('0')
                        else:
                            index.append('1')
                    else:
                            index.append('0')
                else:
                    x, y = n
                    if matrixOld[x][y] == '.':
                        index.append('0')
                    else:
                        index.append('1')
            index = ''.join(index)
            # print(i,j, index, int(index, 2))
            matrix[i][j] = algorithm[int(index, 2)]
        
printMatrix(matrix)    
        
lit = 0
matrix = matrix[1:-1]
for row in matrix:
    lit += row[1:-1].count('#')
    
print("lit in total", lit)
