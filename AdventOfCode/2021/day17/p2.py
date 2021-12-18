
import itertools

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

def testVelocity(vel: list[int], target: list[list[int]], drag: list[bool] = [True, True],  pos: list[int] = [0, 0]):
    vx, vy = vel
    x, y = pos
    
    (minx, miny), (maxx, maxy) = target
    
    prev = []
    
    Y = pos[1]
    while True:
        prev.append((x, y))
        x, y = (x + vx, y + vy)
        
        if not drag[1] and (x, y) in prev: 
            return [False, None]
        Y = max(Y, y)
        
        if drag[0]:
            if vx < 0: vx += 1
            elif vx > 0: vx -= 1
        if drag[1]:
            vy -= 1
            
        if x in range(minx, maxx + 1) \
            and y in range(miny, maxy + 1):
                return [True, Y]
            
        if y < min([miny, maxy]):
            return [False, None]


v = 1
xs = set()
ys = set()

# print([x1, y1, x2, y2])

for v in range(max(abs(y1), abs(y2)) + 1):
    ok, Y = testVelocity([0, v], [[0, y1], [0, y2]], [True, True])
    if ok: ys.add(v)
    ok, Y = testVelocity([0, -v], [[0, y1], [0, y2]], [True, True])
    if ok: ys.add(-v)
        
INF = 9999999999999999999
        
for v in range(max(abs(x1), abs(x2)) + 1):
    ok, _ = testVelocity([v, 0], ((x1, -9999999999999999999), (x2, 9999999999999999999)), [True, False])
    if ok: xs.add(v)
    ok, _ = testVelocity([-v, 0], ((x1, -9999999999999999999), (x2, 9999999999999999999)), [True, False])
    if ok: xs.add(-v)


vels = 0


for comb in list(itertools.product(xs, ys)):
    ok, _ = testVelocity(comb, ((x1,y1), (x2,y2)))
    if ok: 
        vels += 1
print(vels)
