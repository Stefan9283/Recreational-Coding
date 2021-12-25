import collections

firewall = {}

max_depth = 0
for line in open('in').readlines():
    Depth, Range = map(int, line.strip('\n').split(': '))
    firewall[Depth] = Range
    max_depth = max(max_depth, Depth)

severity = 0
for step in firewall:
    i = step % (2 * firewall[step] - 2)
    if i >= firewall[step]:
        isAt = firewall[step] - (i - firewall[step] + 2)
    else:
        isAt = i
    if isAt == 0:
        severity += step * firewall[step]
print(severity)