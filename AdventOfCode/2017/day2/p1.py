
total = 0

for line in open('in').readlines():
    line = [int(num) for num in line.strip('\n').split()]
    total += max(line) - min(line)
print(total)    