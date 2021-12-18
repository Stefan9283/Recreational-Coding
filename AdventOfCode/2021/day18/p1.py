import json
import math

def parse(s: str) -> list:
    return json.loads(s)

def passValue(L: list, val: int, atIndex: int) -> list:
    if type(L) == int:
        return L + val
    if type(L[atIndex]) == int:
        L[atIndex] += val
    else:
        L[atIndex] = passValue(L[atIndex], val, atIndex)
    return L

def reduce(L: list, depth: int = 0) -> list:
    if depth >= 4 and len(L) == 2:
        return L[0], L[1], 0, True
    l, r = None, None
    fnd = False
    for i in range(len(L)):
        if type(L[i]) == list:
            l, r, Li, fnd = reduce(L[i], depth + 1)

            L[i] = Li

            if not fnd: continue

        if fnd == True:
            break

    if l and i - 1 in range(len(L)):
        L[i - 1] = passValue(L[i - 1], l, -1)
        l = None
    if r and i + 1 in range(len(L)):
        L[i + 1] = passValue(L[i + 1], r, 0)
        r = None

    return l, r, L, fnd

def magnitude(l: list) -> int:
    if type(l) == int: return l
    return magnitude(l[0]) * 3 + magnitude(l[1]) * 2

def split(L: list) -> list:
    fnd = False
    for i in range(len(L)):
        if type(L[i]) == int:
            if L[i] >= 10:
                # TODO
                L[i] = [math.floor(L[i] / 2), math.ceil(L[i] / 2)]
                fnd = True
                break
        else:
            L[i], fnd = split(L[i])
            if fnd: break
    return L, fnd

sum = []
for line in open('in').readlines():
    toBeAdded = parse(line.strip('\n'))
    if sum == []:
        sum = toBeAdded
    else:
        sum = [sum, toBeAdded]
    fnd = True
    while fnd:
        _, _, sum, fnd = reduce(sum)
        if fnd: continue
        sum, fnd = split(sum)
print(sum)
print(magnitude(sum))
