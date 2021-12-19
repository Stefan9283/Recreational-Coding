import sys

# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...


def getNeighbors(pos):
    x, y = pos
    return [
        (x + 1, y    ),
        (x - 1, y    ),
        (x    , y + 1),
        (x    , y - 1),
        (x + 1, y + 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y - 1),
    ]
def getNeighSum(pos: list, values: dict):
    s = 0
    for n in getNeighbors(pos):
        if values.get(n):
            s += values[n]
    return s

def exit():
    global values
    global pos
    print(values[tuple(pos)], pos)
    sys.exit()

input = 325489


values = {(0, 0): 1}

sq = 3

pos = [0, 0]

while True:
    pos[0] += 1
    pos[1] -= 1
    for i in range(sq - 1):
        pos[1] += 1
        values[tuple(pos)] = getNeighSum(pos, values)
        if values[tuple(pos)] > input:
            exit()
    
    for i in range(sq - 1):
        pos[0] -= 1
        values[tuple(pos)] = getNeighSum(pos, values)
        if values[tuple(pos)] > input:
           exit() 
    
    for i in range(sq - 1):
        pos[1] -= 1
        values[tuple(pos)] = getNeighSum(pos, values)
        if values[tuple(pos)] > input:
            exit()
    
    for i in range(sq - 1):
        pos[0] += 1
        values[tuple(pos)] = getNeighSum(pos, values)
        if values[tuple(pos)] > input:
            exit()
    sq += 2


