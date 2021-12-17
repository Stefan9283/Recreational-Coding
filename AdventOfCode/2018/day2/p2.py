import itertools

def compare(s1: str, s2: str) -> list[int]:
    diff = []
    for idx, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            diff .append(idx)
    return diff


s = set()

for line in open('in').readlines():
    s.add(line.strip('\n'))

for s1, s2 in itertools.combinations(s, 2):
    diff = compare(s1, s2) 
    if len(diff) == 1:
        print(s1[:diff[0]] + s1[diff[0] + 1:])
        break


