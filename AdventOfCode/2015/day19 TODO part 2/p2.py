
# vezi https://en.wikipedia.org/wiki/CYK_algorithm

from cProfile import Profile
import copy
from pstats import SortKey, Stats

with Profile() as profile:
    from random import shuffle


    lines = open('in').readlines()

    replacements = []
    for line in lines[:-2]:
        replacements.append(line.rstrip().split(' => '))

    shuffle(replacements)    
    
    
    molecule = lines[-1].rstrip()

    stack = [(molecule, 0)]
    hit = 1
    miss = 1

    visited = set()
    
    while stack:
        molec, depth = stack.pop()

        # if molec in visited:
        #     continue
        # visited.add(molec)
        
        new = copy.deepcopy(molec)
        for repl in replacements:
            if new.find(repl[1]) != -1:
                new = new.replace(repl[1], repl[0], 1)
        if molec != new:
            stack.append((new, depth + 1))
        # print(replacements)
        print(depth, molec)

    # (
    #     Stats(profile)
    #     .strip_dirs()
    #     .sort_stats(SortKey.TIME)
    #     .print_stats()
    # )