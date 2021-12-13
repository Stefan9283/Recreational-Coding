
dirs = {
    'U': [0, -1],
    'D': [0,  1],
    'R': [ 1, 0],
    'L': [-1, 0]
}

keys = [[1,2,3],
        [4,5,6],
        [7,8,9]]

keycode = []

x,y = 1,1
for line in open('in').readlines():
    for c in line.strip('\n'):
        difx, dify = dirs[c]
        y += difx
        x += dify
        x = max(0, min(2, x))
        y = max(0, min(2, y))
    keycode.append(str(keys[x][y]))
    
print(''.join(keycode))