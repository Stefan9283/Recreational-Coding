f = open("in")

x, y = 0, 0
visited = [(x, y)]
for c in f.read():
    if c == '<':
        x -= 1
    elif c == '>':
        x += 1
    elif c == 'v':
        y -= 1
    elif c == '^':
        y += 1
    if (x, y) not in visited:
        visited.append((x, y))
print(len(visited))