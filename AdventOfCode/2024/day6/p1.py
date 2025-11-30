
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
    
    


