
from math import sqrt


minPresents = 36000000

houseIndex = 1

while True:
    presents = 0

    i = 1
    while i * i < houseIndex:
        if houseIndex % i == 0:
            presents += i
            presents += houseIndex // i
        i += 1
    
    i = int(sqrt(houseIndex))         
    if i * i == houseIndex:
        presents += i

    presents *= 11
    
    if houseIndex % 20000 == 0:
        print(f"House {houseIndex} has {presents}, out of {minPresents}")

    if presents >= minPresents:
        print(f"House {houseIndex} has {presents}, so over {minPresents}")
        break
    houseIndex += 1
    
    
    