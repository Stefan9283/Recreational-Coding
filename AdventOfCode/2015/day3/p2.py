f = open("in")

x1, y1 = 0, 0
x2, y2 = 0, 0
visited = [(0, 0)]

turn = 0

for c in f.read():
    diff = [0, 0]
    if c == '<':
        diff[0] = -1
    elif c == '>':
        diff[0] = 1
    elif c == 'v':
        diff[1] = -1
    elif c == '^':
        diff[1] = 1
    if turn:
        x1 += diff[0]
        y1 += diff[1]
        current = (x1, y1)
    else:
        x2 += diff[0]
        y2 += diff[1]
        current = (x2, y2)
    if current not in visited:
        visited.append(current)
    turn = 1 - turn
print(len(visited))