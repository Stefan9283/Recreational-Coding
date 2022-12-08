input = open('input0').readlines()

for line in input:
    for idx, _ in enumerate(line):
        s = set(line[idx : idx+4])
        if s.__len__() == 4:
            print(idx + 4, s)
            break
    print()