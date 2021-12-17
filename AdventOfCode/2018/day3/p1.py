
import sys

grid = [[[] for _ in range(2000)] for _ in range(2000)]

claims = []

for line in open('in').readlines():
    claim, x, y, w, h = [int(tok) for tok in line[1:].strip('\n').replace('@', ' ').replace(',', ' ').replace(':', ' ').replace('x', ' ').split()]
    # print(x,y,w,h)
    claims.append([x, y, w, h, claim])
    for i in range(w):
        for j in range(h):
            grid[x + i][y + j].append(claim)
        
overlaps = 0
for i in range(2000):
    for j in range(2000):
        if grid[i][j].__len__() >= 2:
            overlaps += 1

print(overlaps)
  
for x, y, w, h, claim in claims:
    overlap = False
    for i in range(w):
        for j in range(h):
            if grid[x + i][y + j].__len__() >= 2:
                overlap = True
    if not overlap:
        print(claim)
        sys.exit()
    

   
   