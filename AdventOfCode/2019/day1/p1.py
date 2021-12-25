from math import floor

fuel = 0
for line in open('in').readlines():
    line = line.strip('\n')
    mass = int(line)
    fuel += floor(mass / 3) - 2
print(fuel)
