
points = []
for line in open('in').readlines():
    line = line.rstrip()                    \
                .replace('position=<', '')  \
                .replace('velocity=<', '')  \
                .replace('>', '')           \
                .replace(',', '')           \
                .split(' ')
                # .replace('  ', ' ')\
    nums = []
    for tok in line:
        if tok.__len__() != 0:
            nums.append(int(tok))
    points.append(nums)


def print_grid(points):
    x = list(map(lambda x: x[0], points))
    y = list(map(lambda x: x[1], points))
    minmax = [min(x), min(y), max(x), max(y)]
    
    coords = list(map(lambda x: (x[0], x[1]), points))
    
    shiftx, shifty = minmax[0], minmax[1]

    # print(x, minmax)
    for i in range((abs(minmax[1]) + 1 + abs(minmax[3]))):
        for j in range((abs(minmax[0]) + 1 + abs(minmax[2]))):
            if (i + shiftx, j + shifty) in coords:
                print('#', end='')
            else:
                print('.', end='')
        print()
        


for second in range(40000):
    for i in range(points.__len__()):
        x, y, vx, vy = points[i]
        x += vx
        y += vy
        points[i] = [x, y, vx, vy]
    print(f'SECOND {second + 1}')
    if second > 10000:
        print_grid(points=points)







