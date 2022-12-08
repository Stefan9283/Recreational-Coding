score = 0

for line in open('input').readlines():
    line = line.rstrip()
    comp1, comp2 = line[: line.__len__() // 2], line[line.__len__() // 2 : ]
    comp1 = set(comp1)
    comp2 = set(comp2)
    for val in comp1.intersection(comp2):
        if val.lower() == val:
            score0 = ord(val) - ord('a') + 1
        else:
            score0 = ord(val) - ord('A') + 26 + 1
        score += score0
print(score)