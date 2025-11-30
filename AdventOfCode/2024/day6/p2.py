
with open('in', 'r') as f:
    m = list(map(lambda x: x.rstrip(), f.readlines()))

for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == '^':
            initial = (i, j)

direction = (-1, 0)

current = initial

def rotate(dir):
    return {
        ( 1,  0): ( 0, -1),
        ( 0,  1): ( 1,  0),
        (-1,  0): ( 0,  1),
        ( 0, -1): (-1,  0),
    }[dir]

while True:
    x, y = current

    m[x] = m[x][:y] + '$' + m[x][y+1:]
    
    nextx, nexty = (x + direction[0], y + direction[1])
    
    if nextx not in range(0, len(m)) or nexty not in range(0, len(m[0])):
        break 
    
    if m[nextx][nexty] == '#':
        direction = rotate(direction)
    
    current = (current[0] + direction[0], current[1] + direction[1])
    
    
print('\n'.join(m).count('$'))
    
############################ part 2

def does_obstruction_cause_loop(lab_map):
    
    steps_no = 0
    
    current = initial
    direction = (-1, 0)
    
    steps = set()
    
    while True:
        x, y = current

        nextx, nexty = (x + direction[0], y + direction[1])
        
        if nextx not in range(0, len(lab_map)) or nexty not in range(0, len(lab_map[0])):
            break 
        
        steps_no += 1
        
        if lab_map[nextx][nexty] == '#':
            direction = rotate(direction)
        
        current = (current[0] + direction[0], current[1] + direction[1])

        if (current, direction) in steps:
            return True

        steps.add((current, direction))

    return False
    
count = 0

for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == '$':
            m[i] = m[i][:j] + '#' + m[i][j+1:]
            
            # print('\n'.join(m))
            # print('\n'.join(m).count('#'))
            
            if does_obstruction_cause_loop(m):
                count += 1
            m[i] = m[i][:j] + '.' + m[i][j+1:]
            
print(count)