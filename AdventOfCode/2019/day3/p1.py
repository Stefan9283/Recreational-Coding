def readWire(s: str):
    wire = list(map(lambda x: (x[0], int(x[1:])),  s.strip('\n').split(',')))
    ini = [0, 0]
    wire1 = [ini]
    for dir, step in wire:
        fin = list(ini)
        if dir == 'R':
            fin[0] += step
        elif dir == 'U':
            fin[1] += step
        elif dir == 'L':
            fin[0] -= step
        elif dir == 'D':
            fin[1] -= step
        wire1.append(fin)
        ini = fin
    return wire1

with open('in') as f:
    w1 = readWire(f.readline())
    w2 = readWire(f.readline())

def ortho_cross(w1, w2):
    # w1 -> | si w2 -> -
    [x1, y1], [x2, y2] = w1
    [a1, b1], [a2, b2] = w2
    a1, a2 = sorted([a1, a2])
    y1, y2 = sorted([y1, y2])
    if x1 in range(a1, a2 + 1) and b1 in range(y1, y2 + 1):
        return (x1, b1)
    



cross = []
for i in range(len(w1) - 1):
    for j in range(len(w2) - 1):
        [x1, y1], [x2, y2] = w1[i], w1[i+1]
        [a1, b1], [a2, b2] = w2[j], w2[j+1]
        
        if x1 == x2 and b1 == b2:
            x = ortho_cross([w1[i], w1[i+1]], [w2[j], w2[j+1]])
            if x: 
                cross.append(x)
        elif y1 == y2 and a1 == a2:
            x = ortho_cross([w2[j], w2[j+1]], [w1[i], w1[i+1]])
            if x: 
                cross.append(x)
                
cross = set(cross)
if (0, 0) in cross:
    cross.remove((0, 0))
manhat = [abs(x[0]) + abs(x[1]) for x in cross]
print(manhat, min(manhat))


