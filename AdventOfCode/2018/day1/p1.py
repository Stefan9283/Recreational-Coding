
freq = 0

for line in open('in').readlines():
    freq += int(line)
print(freq)