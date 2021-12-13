import sys

x, y = 0, 0
dir = 'N'

visited = [[0, 0]]

moves = {
            'N': ['W', 'E'],
            'S': ['E', 'W'],
            'E': ['N', 'S'],
            'W': ['S', 'N']
         }
dirs = {
            'N': [0,  1],
            'S': [0, -1],
            'E': [ 1, 0],
            'W': [-1, 0]
        }

def drawmatrix():
    minCor = [0, 0]
    maxCor = [0, 0]
    for i in range(0, len(visited)):
        if visited[i][0] < minCor[0]: minCor[0] = visited[i][0]
        if visited[i][0] > maxCor[0]: maxCor[0] = visited[i][0]
        if visited[i][1] < minCor[1]: minCor[1] = visited[i][1]
        if visited[i][1] > maxCor[1]: maxCor[1] = visited[i][1]
    size = [maxCor[0] - minCor[0] + 1, maxCor[1] - minCor[1] + 1]
    print(minCor, maxCor, size)
    mat = []
    for i in range(0, size[0]):
        row = []
        for j in range(0, size[1]): row.append(0)
        mat.append(row)
    
    for i in range(0, len(visited)):
        x, y = visited[i]
        print(x, y, [x - minCor[0]], [y - minCor[1]])
        mat[x - minCor[0]][y - minCor[1]] = i        
    
    o = open('mat', 'w+')
    for row in mat:
        for val in row:
            o.write('{:>3} '.format(val))
        o.write('\n')
    pass


for instr in open('in').readline().strip('\n').split(' '):
    cmd = [instr[0], int(instr.strip(',')[1:])]
    # print([x, y], dir, cmd, end="")
    if cmd[0] == 'L':
        dir = moves[dir][0]
    elif cmd[0] == 'R':
        dir = moves[dir][1]
    else:
        raise RuntimeError('wrong direction change')
    # print(' ->', dir)
    
    for _ in range(0, cmd[1]):
        x += dirs[dir][0]
        y += dirs[dir][1]
        
        if [x, y] in visited:
            print(abs(x) + abs(y))  
            sys.exit()
        visited.append([x, y])
