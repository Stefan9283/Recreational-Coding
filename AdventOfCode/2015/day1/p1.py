
f = open("in")
floor = 0
for c in f.read().strip('\n'):
    if c == '(':
        floor += 1
    elif c == ")":
        floor -= 1
print(floor)