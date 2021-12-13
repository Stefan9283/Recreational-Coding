
screen = [['.' for i in range(50)] for j in range(6)]

size = [len(screen), len(screen[0])]

def printmat(mat):
    for row in mat:
        print(row)
    print()

for line in open('in').readlines():
    line = line.strip('\n')
    tok = line.split()
    if tok[0] == 'rect':
        x, y = tok[1].split('x')
        for i in range(int(y)):
            for j in range(int(x)):
                screen[i][j] = '#'
    elif tok[1] == 'row':
        _, y = tok[2].split('=')
        y = int(y)
        by = int(tok[-1]) % size[1]
        row = list(screen[y])
        row = row[size[1] - by :] + row[: size[1] - by]
        for i in range(size[1]):
            screen[y][i] = row[i]
    else:
        _, x = tok[2].split('=')
        x = int(x)
        by = int(tok[-1]) % size[0]
        col = []
        for i in range(size[0]):
            col.append(screen[i][x])
        col = col[size[0] - by :] + col[: size[0] - by]
        for i in range(size[0]):
            screen[i][x] = col[i]
            
printmat(screen) # for part 2 just read the letters displayed

print(sum(
    [sum([1 for j in range(size[1]) if screen[i][j] == '#']) \
                                for i in range(size[0])]))
