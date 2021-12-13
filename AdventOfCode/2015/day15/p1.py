import itertools
from typing import List

recipie = {}

def getScore(names: List[str], teaspoons: List[int]) -> int:
    score = 1
    for i in range(4):
        property_score = 0
        for name, teaspoon in zip(names, teaspoons):
            property_score += recipie[name][i] * teaspoon
        score *= max(0, property_score)
    # print(names, teaspoons, score)
    return score

    

for line in open('in').readlines():
    line = line.strip('\n')
    # name, _, cap, _, dur, _, flav, _, text, _, cals  
    tok = line.replace(',', ' ').replace(':', ' ').split()
    recipie[tok[0]] = [int(tok[i + 1]) for i in range(len(tok) - 1) if i % 2 == 1] 



def getSums(remaining: int, step: int, lastStep: int, untilNow: List[int]):
    if step == lastStep:
        untilNow.append(remaining)
        sums.append(untilNow)
        return        
    
    
    for i in range(remaining):
        getSums(remaining - i, step + 1, lastStep, untilNow + [i])
    pass


max_score = 0
for ingr_count in range(1, len(recipie) + 1):
    names = [list(L) for L in itertools.combinations(recipie, ingr_count)]
    print(names)
    sums = []
    getSums(100, 1, ingr_count, [])
    for namelist in names:
        for teasps in sums:
            max_score = max(max_score, getScore(namelist, teasps))
print(max_score)



# print(getScore(['Butterscotch', 'Cinnamon'], [44, 56]))