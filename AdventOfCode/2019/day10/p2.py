import math


def getOnLine(x1, y1, x2, y2):
    pos = [x1, y1]
    
    for i in range(1, 100):
        if x1 == x2:
            if y1 < y2:
                pos[1] += 1
            else:
                pos[1] -= 1
        elif y1 == y2:
            if x1 < x2:
                pos[0] += 1
            else:
                pos[0] -= 1
        else:
            # m = (y2 - y1) / (x2 - x1)
            pos = ??????

def removeFirstOnLine(x1, y1, x2, y2):
    on_line = getOnLine(x1, y1, x2, y2)
    if on_line != None:
        x, y = on_line
        map[x][y] = '-'

map = []

with open('in') as f:
    for line in f.readlines():
        line = line.rstrip()
        map.append(line)
    
    
x_station, y_station = 16, 8

h, w = len(map),len(map[0])
lookat = [w / 2, 0]

for iter in range(100):
    # do a 360 degrees rotation
    while lookat[0] < w:
        removeFirstOnLine(x_station, y_station, lookat[0], lookat[1])
        lookat[0] += 1
    lookat[0] -= 1
    while lookat[1] < h:
        removeFirstOnLine(x_station, y_station, lookat[0], lookat[1])
        lookat[1] += 1
    lookat[1] -= 1
    while lookat[0] >= 0:
        removeFirstOnLine(x_station, y_station, lookat[0], lookat[1])
        lookat[0] -= 1
    lookat[0] += 1
    while lookat[1] >= 0:
        removeFirstOnLine(x_station, y_station, lookat[0], lookat[1])
        lookat[1] -= 1
    lookat[1] += 1

