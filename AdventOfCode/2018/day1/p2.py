
freq = 0
v = [freq]
found = False

while not found:
    for line in open('in').readlines():
        freq += int(line)
        if freq in v:
            found = True
            break
        v.append(freq)

print(freq)
