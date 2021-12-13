
import itertools
from typing import Tuple

def doTheyFit(containers: Tuple[int], capacity: int) -> bool:
    return capacity - sum(containers) == 0

containers = []
for line in open('in').readlines():
    containers.append(int(line.strip('\n')))
print(containers)

comb_counter = 0
min_num_containers = len(containers) + 1
for size in range(1, len(containers) + 1):
    thisIsTheSmallestSize = False
    for cont in [tuple(comb) for comb in itertools.combinations(containers, size)]:
        if doTheyFit(cont, 150):
            if len(cont) < min_num_containers:
                thisIsTheSmallestSize = True
                min_num_containers = len(cont)
                comb_counter = 1
            elif len(cont) == min_num_containers: 
                comb_counter += 1
            print(cont, len(cont))
    if thisIsTheSmallestSize: break
print(comb_counter)