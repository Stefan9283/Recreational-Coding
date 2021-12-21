input = open('in').read().strip('\n')

def getCollapsedSize(s: list) -> int:
    found = 69
    while found:
        found = 0
        for i in range(len(s) - 2, -1, -1):
            if abs(ord(s[i]) - ord(s[i + 1])) == ord('a') - ord('A'):
                s.pop(i + 1)
                s.pop(i)
                found += 1
                break
    return len(s)

import string
import math

minLen = math.inf
for low, up in zip(string.ascii_uppercase, string.ascii_lowercase):
    if low in input or up in input:
        s = str(input)
        s = s.replace(low, '')
        s = s.replace(up, '')
        minLen = min(minLen, getCollapsedSize(list(s)))
        print('completed ', low)
print(minLen)