f = open("in")

grid = [[0 for i in range(0, 1000)] for j in range(0, 1000)]


for line in f.readlines():
    line = line.strip('\n')
    tok = line.split(' ')
    
    if line.startswith('toggle'):
        x1, y1 = [int(num) for num in tok[1].split(',')]
        x2, y2 = [int(num) for num in tok[3].split(',')]
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] += 2
    elif line.startswith('turn'):
        x1, y1 = [int(num) for num in tok[2].split(',')]
        x2, y2 = [int(num) for num in tok[4].split(',')]
        add = -1
        if line.startswith('turn on'):
            add = 1
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] = max(0, grid[i][j] + add)    


print(sum([sum(line) for line in grid]))
    