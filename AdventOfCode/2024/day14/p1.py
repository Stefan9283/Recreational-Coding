
# read input

with open('in', 'r') as f:
    robots = []
    for line in f.readlines():
        p,v = line.rstrip().replace('v=', '').replace('p=', '').split(' ')
        p = list(map(int, p.split(',')))
        v = list(map(int, v.split(',')))
        # print(p, v)
        robots.append([p, v])
        
w, h = 101, 103
# w, h = 11, 7

# solve 

for it in range(100):
    # print('iteration', it)
    for i, robot in enumerate(robots):
        p, v = robot
        p[0] += v[0]
        p[1] += v[1]
        if p[0] < 0: p[0] += w
        if p[1] < 0: p[1] += h
        if p[0] >= w: p[0] -= w
        if p[1] >= h: p[1] -= h
        # print(p, v)

# display map

MAP = [['.' for _ in range(w)] for _ in range(h)]

for robot in robots:
    p, _ = robot
    if MAP[p[1]][p[0]] == '.':
        MAP[p[1]][p[0]] = 0
    MAP[p[1]][p[0]] += 1

print('\n'.join([''.join(map(str, x)) for x in MAP]))



safety_factor = 1

tmp1, tmp2 = 0, 0
for i in range(h//2):
    # tmp2.append(MAP[i][h//2+1:])
    print(MAP[i][:w//2], MAP[i][w//2+1:])
    
    tmp1 += sum(filter(lambda x: x != '.', MAP[i][:w//2]))
    tmp2 += sum(filter(lambda x: x != '.', MAP[i][w//2+1:]))
print(tmp1, tmp2)
safety_factor *= tmp1 * tmp2
    
print()
tmp1, tmp2 = 0, 0
for i in range(h//2+1, h):
#     tmp1.append(MAP[i][:h//2])
#     tmp2.append(MAP[i][h//2+1:])
    print(MAP[i][:w//2], MAP[i][w//2+1:])
    tmp1 += sum(filter(lambda x: x != '.', MAP[i][:w//2]))
    tmp2 += sum(filter(lambda x: x != '.', MAP[i][w//2+1:]))
print(tmp1, tmp2)
safety_factor *= tmp1 * tmp2

print(safety_factor)