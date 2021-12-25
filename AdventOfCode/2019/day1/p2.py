from math import floor

fuel = 0
for line in open('in').readlines():
    line = line.strip('\n')
    mass = int(line)
    current_fuel = floor(mass / 3) - 2
    while current_fuel > 0:
        fuel += current_fuel
        current_fuel = floor(current_fuel / 3) - 2
print(fuel)
