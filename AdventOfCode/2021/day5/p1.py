from typing import List, overload

file1 = open('in0', 'r')
Lines = file1.readlines()

lines = []
size = [0, 0]
for line in Lines:
    coords = line.split("->")
    xy1 = coords[0].split(',')
    xy2 = coords[1].split(',')
    xs = [int(xy1[0]), int(xy2[0])]
    ys = [int(xy1[1]), int(xy2[1])]
    if xs[0] > xs[1]:
        xs.reverse()
        ys.reverse()
    e = [xs, ys]
    lines.append(e)
    size[0] = max(xs[1] + 1, size[0])
    size[1] = max(ys[1] + 1, size[1])

'''
.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
'''

map = []
for i in range(size[0] + 1):
    row = []
    for j in range(size[1] + 1):
        row.append(0)
    map.append(row)

for line in lines:
    if line[0][0] == line[0][1]: # x0 cu x1
        for i in range(min(line[1]), max(line[1]) + 1):
            map[i][line[0][0]] += 1
    elif line[1][0] == line[1][1]: # y0 cu y1
        for i in range(min(line[0]), max(line[0]) + 1):
            map[line[1][1]][i] += 1
    else:
        if line[1][0] < line[1][1]:
            for i in range(0, line[0][1] - line[0][0] + 1):
                map[line[1][0] + i][line[0][0] + i] += 1
        else:
            for i in range(0, - line[1][1] + line[1][0] + 1):
                map[line[1][0] - i][line[0][0] + i] += 1

overlaps = 0
for row in map:
    for pos in row:
        if pos >= 2:
            overlaps += 1
print(overlaps)