
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
    
    
############################ part 2
import os, time, sys

def does_obstruction_cause_loop(lab_map):
    
    current = initial
    direction = (-1, 0)

    steps = set()

    crosses = []

    def write_to_file(xc, yc):
        map_copy = list(lab_map)
        
        for (x, y), (_, dy) in steps:
            if dy == 0:
                map_copy[x] = map_copy[x][:y] + '|' + map_copy[x][y+1:]
            else:
                map_copy[x] = map_copy[x][:y] + '-' + map_copy[x][y+1:]
            
            position_counter = 0
            for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if ((x, y), dir) in steps:
                    position_counter += 1
            if position_counter > 1:
                crosses.append((x, y))
            

        for x, y in crosses:
            map_copy[x] = map_copy[x][:y] + '+' + map_copy[x][y+1:]
        
        xi, yi = initial
        map_copy[xi] = map_copy[xi][:yi] + '^' + map_copy[xi][yi+1:]
        
        loop = '\n'.join(map_copy).replace('$', '.')
        
        with open(f'route_{xc}_{yc}.txt', 'w') as f:
            f.write(loop)
        

    while True:
        x, y = current

        nextx, nexty = (x + direction[0], y + direction[1])
        
        if nextx not in range(0, len(lab_map)) or nexty not in range(0, len(lab_map[0])):
            steps.add((current, direction))
            break 

        if lab_map[nextx][nexty] in '#O':
            direction = rotate(direction)
            crosses.append(current)
            continue

        if (current, direction) in steps:

            # write_to_file(x, y)
            
            return True
        
        steps.add((current, direction))

        current = (current[0] + direction[0], current[1] + direction[1])


    
    obstruction_coords = (-1, -1)
    for i in range(len(m)):
        if obstruction_coords != (-1, -1):
            break
        for j in range(len(m[i])):
            if m[i][j] == 'O':
                obstruction_coords = (i, j)
                break

    # write_to_file('bad_' + str(obstruction_coords[0]), obstruction_coords[1])

    return False
   
xi, yi = initial 
m[xi] = m[xi][:yi] + '?' + m[xi][yi+1:]

count = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == '$':
            m[i] = m[i][:j] + 'O' + m[i][j+1:]
            # print('\n'.join(m))
            # print('\n'.join(m).count('#'))
            if does_obstruction_cause_loop(m):
                count += 1
            m[i] = m[i][:j] + '.' + m[i][j+1:]

print(count)