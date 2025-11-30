
l1, l2 = [], []

with open('in', 'r') as f:
    for line in f.readlines():
        e1, e2 = line.rstrip().split()
        l1.append(int(e1))
        l2.append(int(e2))

l1.sort()
l2.sort()

diffs = 0

for a,b in zip(l1, l2):
    diffs += abs(a - b)

print(diffs)