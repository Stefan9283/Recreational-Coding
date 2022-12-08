score = 0

def doOverlap(range1, range2):
    return (range1[0] <= range2[0] and range2[0] <= range1[1]) \
        or (range1[0] <= range2[1] and range2[1] <= range1[1])
        
overlapping = 0

for line in open('input').readlines():
    line = line.rstrip()
    elf1, elf2 = line.split(',')
    elf1 = list(map(int, elf1.split('-')))
    elf2 = list(map(int, elf2.split('-')))
    if doOverlap(elf1, elf2) or doOverlap(elf2, elf1):
        overlapping += 1

print(overlapping)