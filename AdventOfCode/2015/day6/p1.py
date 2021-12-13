f = open("in")

grid = [[0 for i in range(0, 1000)] for j in range(0, 1000)]


for line in f.readlines():
    line = line.strip('\n')
    tok = line.split(' ')
    # print(tok)
    
    if line.startswith('toggle'):
        x1, y1 = [int(num) for num in tok[1].split(',')]
        x2, y2 = [int(num) for num in tok[3].split(',')]
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] = 1 - grid[i][j]
    elif line.startswith('turn'):
        x1, y1 = [int(num) for num in tok[2].split(',')]
        x2, y2 = [int(num) for num in tok[4].split(',')]
        setTo = 0
        if line.startswith('turn on'):
            setTo = 1
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] = setTo    


print(sum([line.count(1) for line in grid]))
    