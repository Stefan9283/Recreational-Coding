
f = open("in")
floor = 0
i = 1
for c in f.read().strip('\n'):
    if c == '(':
        floor += 1
    elif c == ")":
        floor -= 1
    if floor < 0:
        print(i)
        break
    i += 1