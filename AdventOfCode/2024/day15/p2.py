
with open('in', 'r') as f:
    input = f.read()

MAP, CMDS = input.split('\n\n')
MAP = [ list(line.rstrip()) for line in MAP.split('\n') ]
CMDS = ''.join(CMDS.split('\n'))
print(MAP)


def transform_map():
    MAP_ = [ ]
    for line in MAP:
        line_ = []
        for c in line:
            if c == '#':
                line_.append('#')
                line_.append('#')
            if c == '.':
                line_.append('.')
                line_.append('.')
            if c == '@':
                line_.append('@')
                line_.append('.')
            if c == 'O':
                line_.append('[')
                line_.append(']')
        MAP_.append(line_)
    return MAP_

MAP = transform_map()

for i in range(len(MAP)):
    if '@' in MAP[i]:
        j = MAP[i].index('@')
        break

curr = (i, j)
    
print('\n'.join([''.join(line) for line in MAP]))
    
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
    print(curr, (i, j))
    
    
    if MAP[i][j] == '.':
        MAP[i][j] = '@'
        MAP[a][b] = '.'
        curr = (i, j)
        continue
    
    if MAP[i][j] == '#':
        continue
    
    if MAP[i][j] in '[]':
        tmp = (i, j)
        
        if cmd in '<>':
            while MAP[tmp[0]][tmp[1]] not in ['.', '#']:
                tmp = get_next(cmd, tmp)
                
            if MAP[tmp[0]][tmp[1]] == '#': continue
            
            reverse = '<' if cmd == '>' else '>'
            
            MAP[tmp[0]][tmp[1]] = '['
            prev = tmp
            while MAP[tmp[0]][tmp[1]] != '@':
                tmp = get_next(reverse, tmp)
                MAP[prev[0]][prev[1]] = MAP[tmp[0]][tmp[1]]
                prev=tmp
            MAP[a][b] = '.'
            curr = (i, j)
        
        else:
            next_to_check = []
            next_to_check.append((i, j))
            to_be_moved = {}
            
            can_move = True
            
            tmp = curr
            while next_to_check:
                tmp = next_to_check.pop()
                
                # print(next_to_check, tmp)
                
                if tmp in to_be_moved.keys(): continue
                x, y = tmp
                
                if MAP[x][y] == '#':
                    can_move = False
                    break
                
                if MAP[x][y] == '.':
                    continue
                
                if MAP[x][y] in '[]':
                    to_be_moved[(x, y)] = MAP[x][y]
                    
                    # print(' ', curr, MAP[x][y])
                    if MAP[x][y] == '[':
                        next_to_check.append((x, y+1))
                    elif MAP[x][y] == ']':
                        next_to_check.append((x, y-1))
                    next_pos = get_next(cmd, tmp)                    
                    next_to_check.append(next_pos)
            
            # print(to_be_moved)
            
            if not can_move: continue
            for pos, char in to_be_moved.items():
                MAP[pos[0]][pos[1]] = '.'
            for pos, char in to_be_moved.items():
                x, y = get_next(cmd, pos)
                MAP[x][y] = char
                # print('\n'.join([''.join(line) for line in MAP]))
            
            MAP[a][b] = '.'
            MAP[i][j] = '@'
            
            curr = (i, j)
    
print('\n'.join([''.join(line) for line in MAP]))
print()

    
sum = 0
for i in range(len(MAP)):
    for j in range(len(MAP[0])):
        if MAP[i][j] != '[': continue
        sum += i * 100 + j
print(sum)




