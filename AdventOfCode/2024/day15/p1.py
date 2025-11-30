

with open('in', 'r') as f:
    input = f.read()

MAP, CMDS = input.split('\n\n')
MAP = [ list(line.rstrip()) for line in MAP.split('\n') ]
CMDS = ''.join(CMDS.split('\n'))
print(MAP)

for i in range(len(MAP)):
    if '@' in MAP[i]:
        j = MAP[i].index('@')
        break

curr = (i, j)
    
def get_next(cmd, base):
    if cmd == '<':
        return (base[0], base[1] - 1)
    if cmd == '>':
        return (base[0], base[1] + 1)
    if cmd == '^':
        return (base[0] - 1, base[1])
    if cmd == 'v':
        return (base[0] + 1, base[1])

# print(curr)
for iter, cmd in enumerate(CMDS):
    a, b = curr
    i, j = get_next(cmd, curr)
    
    print('\n'.join([''.join(line) for line in MAP]))
    print()

    # print(a-i, b-j)
    # print(a, i, b, j)
    
    print(f'{iter} Move {cmd}:')
    
    
    if MAP[i][j] == '.':
        MAP[i][j] = '@'
        MAP[a][b] = '.'
        curr = (i, j)
        continue
    
    if MAP[i][j] == '#':
        continue
    
    if MAP[i][j] == 'O':
        print(i, j)
        tmp = (i, j)
        while MAP[tmp[0]][tmp[1]] not in ['.', '#']:
            tmp = get_next(cmd, tmp)
            
        if MAP[tmp[0]][tmp[1]] == '#': continue
        
        MAP[tmp[0]][tmp[1]] = 'O'
        MAP[i][j] = '@'
        MAP[a][b] = '.'
        curr = (i, j)
        
        
        # raise Exception('AAAAAA')
    
sum = 0
for i in range(len(MAP)):
    for j in range(len(MAP[0])):
        if MAP[i][j] != 'O': continue
        sum += i * 100 + j
print(sum)