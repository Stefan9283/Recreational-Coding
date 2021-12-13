
def matpri(mat):
    for row in mat:
        print(row)
    print()
def getNeigh(x: int, y: int):
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

mat = []

for line in open('in').readlines():
    line = line.strip('\n')
    row = []
    for c in line:
        row.append(int(c))
    mat.append(row)

matpri(mat)

idx = 1
while True:
    flashed = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = mat[i][j] + 1
    
    while True:   
        totalFlashed =  0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] > 9 and not flashed[i][j]:
                    flashed[i][j] = 1
                    totalFlashed += 1
                    for x, y in getNeigh(i, j):
                        mat[x][y] = mat[x][y] + 1
        if totalFlashed == 0: break

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if flashed[i][j]:
                mat[i][j] = 0
    if sum([sum(row) for row in flashed]) == len(mat) * len(mat[0]):
        print('step', idx)
        break
    idx += 1
