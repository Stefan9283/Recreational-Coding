
_, _, x, y = open('in').read().strip('\n').split()
x1, x2 = x[2:-1].replace('.', ' ').split()
y1, y2 = y[2:].replace('.', ' ').split()
x1, x2, y1, y2 = [int(co) for co in [x1, x2, y1, y2]]
print([x1, y1, x2, y2])

S = (0, 0)

#  vx, vy > 0
#  p1 = (0,0) + (vx, vy)
#  p2 = (0,0) + (vx, vy) + (vx - 1, vy - 1)
#  p3 = (0,0) + (vx, vy) + (vx - 1, vy - 1) + (vx - 2, vy - 2)
#  ...
#  pn = (vx - s, vy - s) 
#      for  s = n (n - 1) / 2 if s >= 2 
#           s = 1 if s == 1
#  OR
#  
#  vx < 0 vy > 0
#  p1 = (0,0) + (vx, vy)
#  p2 = (0,0) + (vx, vy) + (vx + 1, vy - 1)
#  p3 = (0,0) + (vx, vy) + (vx + 1, vy - 1) + (vx + 2, vy - 2)
#  ...
#  pn = (vx + s, vy - s) 
#      for  s = n (n - 1) / 2 if s >= 2 
#           s = 1 if s == 1
#
#   OR
# 
#  vx = 0 
#  pn = (0, vy - s)

def testVelocity(vel: tuple[int], target: list[list[int]], pos: list[int] = [0, 0]):
    vx, vy = vel
    x, y = pos
    
    (minx, miny), (maxx, maxy) = target
    
    Y = pos[1]
    while True:
        x, y = (x + vx, y + vy)
        
        Y = max(Y, y)
        
        if vx < 0:
            vx += 1
        elif vx > 0:
            vx -= 1
        vy -= 1
        
        if x in range(minx, maxx + 1) \
            and y in range(miny, maxy + 1):
                return [True, Y]
            
        if y < min([miny, maxy]):
            return [False, None]


v = 1
while True:
    ok, Y = testVelocity([0, v], ((0, y1), (0, y2)))
    if ok: print(v, ok, Y)
    v += 1