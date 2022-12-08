input = open('input').readlines()

for line in input:
    for idx, _ in enumerate(line):
        s = set(line[idx : idx+14])
        if s.__len__() == 14:
            print(idx + 14, s)
            break
    print()