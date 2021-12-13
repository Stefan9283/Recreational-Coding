
dirs = {
    'U': [0, -1],
    'D': [0,  1],
    'R': [ 1, 0],
    'L': [-1, 0]
}
keys = [
    ['#','#', 1, '#','#'],
    ['#', 2,  3,  4, '#'],
    [ 5,  6,  7,  8,  9],
    ['#','A','B','C','#'],
    ['#','#','D','#','#'],
]

def isValidKey(x, y) -> bool:
    return all([coord >= 0 and coord <= 4 for coord in [x, y]]) and keys[x][y] != '#' 

    
keycode = []

x,y = 2,0
for line in open('in').readlines():
    for c in line.strip('\n'):
        difx, dify = dirs[c]
        newy = y + difx
        newx = x + dify
        if isValidKey(newx, newy):
            x, y = newx, newy
    keycode.append(str(keys[x][y]))
print(''.join(keycode))
