
x, y = 0, 0
dir = 'N'
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
for cmd in [[dir[0], int(dir.strip(',')[1:])] \
             for dir in open('in').readline().strip('\n').split(' ')]:
    if cmd[0] == 'L':
        dir = moves[dir][0]
    else:
        dir = moves[dir][1]
    x += dirs[dir][0] * cmd[1]
    y += dirs[dir][1] * cmd[1]
print(abs(x) + abs(y))