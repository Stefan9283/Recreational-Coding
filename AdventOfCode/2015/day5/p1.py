f = open("in")

nice = 0

for line in f.readlines():
    line = line.strip('\n')
    
    vowels = len(list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'], line)))
    if vowels < 3:
        continue
    
    twiceInARow = False
    for i in range(0, len(line) - 1):
        if line[i] == line[i + 1]:
            twiceInARow = True
            break
    if not twiceInARow:
        continue
    
    if not any([line.find(string) != -1 for string in ['ab', 'cd', 'pq', 'xy']]):
        nice += 1
        
print(nice)    
    