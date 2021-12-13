s = open('in').readline().strip('\n')

steps = 50

for step in range(0, steps):
    groups = [[0, s[0]]]
    i = 0
    s = list(s)
    for c in s:
        if c == groups[i][1]:
            groups[i][0] += 1
        else:
            groups.append([1, c])
            i += 1
    s = ''.join([''.join([str(g[0]), g[1]]) for g in groups])

print(len(s))
