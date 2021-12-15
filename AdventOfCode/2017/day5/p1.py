
jumps = [int(line.strip('\n')) for line in open('in').readlines()]

i = 0
steps = 0

while i < len(jumps):
    steps += 1
    oldi = i
    i += jumps[i]
    jumps[oldi] += 1
    
print(steps)