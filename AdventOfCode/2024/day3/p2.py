

with open('in', 'r') as f:
    input = f.read().rstrip()
    

import re

sum = 0
for i in range(3):
    for j in range(3):
        do = True
        for found in re.findall('do\\(\\)|don\'t\\(\\)|mul\\([1-9][0-9]{' + str(i) + '},[1-9][0-9]{' + str(j) + '}\\)', input):
            if found == 'do()':
                do = True
            elif found == 'don\'t()':
                do = False
            elif do:
                a, b = found[4:-1].split(',')
                sum += int(a) * int(b)

print(sum)