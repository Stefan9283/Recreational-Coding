import collections
import itertools

nums = []

for num in open('in').readlines():
    n = int(num.strip('\n'))
    nums.append(n)

for a,b,c in itertools.combinations(nums, 3):
    if a + b + c == 2020:
        print(a * b * c)
        break    
