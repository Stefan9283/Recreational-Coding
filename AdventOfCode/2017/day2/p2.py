total = 0

for line in open('in').readlines():
    line = [int(num) for num in line.strip('\n').split()]
    line.sort()
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            if line[j] % line[i] == 0:
                total += line[j] // line[i]
print(total)    