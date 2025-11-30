
CASE = [
    ('in0', 6, 6, 12),
    ('in', 70, 70, 1024)
]


FILE, H, W, FALL = CASE[1]
H += 1 ; W += 1

with open(FILE, 'r') as f:
    coords = list(map(lambda x: list(map(int, x.split(','))), f.readlines()))

MAP = [ [ '.' for _ in range(W) ] for _ in range(H) ]

for (i, j) in coords[:FALL]:
    MAP[j][i] = '#'

print('\n'.join(''.join(l) for l in MAP))

lowest_distance_to_coord = {}

TARGET = (H-1, W-1)
stack = [((0, 0), 0)]
while stack:
    coord, dist = stack.pop(0)

    if coord not in lowest_distance_to_coord.keys():
        lowest_distance_to_coord[coord] = dist
    elif lowest_distance_to_coord[coord] <= dist:
        continue

    print(coord, dist, len(stack))

    lowest_distance_to_coord[coord] = dist

    if coord == TARGET:
        continue
    
    # print(coord, dist, lowest_distance_to_coord[coord])

    i, j = coord
    if i != 0 and MAP[i-1][j] != '#': stack.append(((i-1, j), dist+1))
    if i != H-1 and MAP[i+1][j] != '#': stack.append(((i+1, j), dist+1))
    if j != 0 and MAP[i][j-1] != '#': stack.append(((i, j-1), dist+1))
    if j != W-1 and MAP[i][j+1] != '#': stack.append(((i, j+1), dist+1))



print(lowest_distance_to_coord)

print(lowest_distance_to_coord[(H-1, W-1)])

