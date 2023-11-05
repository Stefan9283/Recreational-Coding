import numpy as np
from numpy.core.defchararray import rpartition

players = {}

init = []
reboot = []

with open('in') as f:
    for line in f.readlines():
        tok = line.strip('\n').replace('=', ' ')\
            .replace('.', ' ').replace(',', ' ').split()
        
        x1 = int(tok[2]) + 50
        x2 = int(tok[3]) + 50
            
        y1 = int(tok[5]) + 50
        y2 = int(tok[6]) + 50
        
        z1 = int(tok[8]) + 50
        z2 = int(tok[9]) + 50

        val = 1
        if tok[0] == 'off': val = 0
        
        if all([coord in range(0, 101) for coord in [x1,x2,y1,y2,z1,z2]]):
            init.append((val, [x1,x2],[y1,y2],[z1,z2]))
        else:
            reboot.append((val, [x1,x2],[y1,y2],[z1,z2]))

xMin = min(min(init, key=lambda x: min(x[1]))[1])
yMin = min(min(init, key=lambda x: min(x[2]))[2])
zMin = min(min(init, key=lambda x: min(x[3]))[3])
xMax = max(max(init, key=lambda x: max(x[1]))[1])
yMax = max(max(init, key=lambda x: max(x[2]))[2])
zMax = max(max(init, key=lambda x: max(x[3]))[3])


grid = np.zeros((100, 100, 100), dtype=int)
for ini in init:
    print(ini)
    for x in range(ini[1][0], ini[1][1] + 1):
        for y in range(ini[2][0], ini[2][1] + 1):
            for z in range(ini[3][0], ini[3][1] + 1):
                grid[x][y][z] = ini[0]

count = 0

for x in range(100):
    for y in range(100):
        for z in range(100):        
            count += grid[x][y][z]

print(count)