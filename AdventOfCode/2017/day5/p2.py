
jumps = [int(line.strip('\n')) for line in open('in').readlines()]

i = 0
steps = 0

while i < len(jumps):
    steps += 1
    oldi = i
    i += jumps[i]
    if jumps[oldi] >= 3:
        jumps[oldi] -= 1
    else: jumps[oldi] += 1
print(steps)