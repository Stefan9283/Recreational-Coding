
from math import sqrt

minPresents = 36000000

houseIndex = 1

start_elf = 1

while True:
    presents = 0
    i = start_elf
    while i * i < houseIndex:
        if houseIndex % i == 0:
            presents += i
            presents += houseIndex // i
        i += 1
    
    i = int(sqrt(houseIndex))         
    if i * i == houseIndex:
        presents += i

    presents *= 11
    
    if houseIndex % 100000 == 0:
        print(f"House {houseIndex} has {presents}, out of {minPresents} and first elf {start_elf}")

    if presents >= minPresents:
        print(f"House {houseIndex} has {presents}, so over {minPresents}")
        break
    
    if houseIndex % 50 == 0:
        start_elf += 1
    houseIndex += 1
    