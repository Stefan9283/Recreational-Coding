
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

def display_map():
    MAP = [['.' for _ in range(w)] for _ in range(h)]

    for robot in robots:
        p, _ = robot
        MAP[p[1]][p[0]] = '#'

    print('\n'.join([''.join(map(str, x)) for x in MAP]))


it = 0
for it in range(8149):
    it += 1
    for i, robot in enumerate(robots):
        p, v = robot
        p[0] += v[0]
        p[1] += v[1]
        if p[0] < 0: p[0] += w
        if p[1] < 0: p[1] += h
        if p[0] >= w: p[0] -= w
        if p[1] >= h: p[1] -= h
display_map()


