

with open('in', 'r') as f:
    input = f.read().rstrip()
    

import re

sum = 0
for i in range(3):
    for j in range(3):
        for found in re.findall('mul\\([1-9][0-9]{' + str(i) + '},[1-9][0-9]{' + str(j) + '}\\)', input):
            a, b = found[4:-1].split(',')
            sum += int(a) * int(b)

print(sum)