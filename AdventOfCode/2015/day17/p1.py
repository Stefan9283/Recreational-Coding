
import itertools
from typing import Tuple

def doTheyFit(containers: Tuple[int], capacity: int) -> bool:
    return capacity - sum(containers) == 0

containers = []
for line in open('in').readlines():
    containers.append(int(line.strip('\n')))
print(containers)

comb_counter = 0
for size in range(1, len(containers) + 1):
    for cont in [tuple(comb) for comb in itertools.combinations(containers, size)]:
        if doTheyFit(cont, 150):
            comb_counter += 1
            print(cont)
print(comb_counter)