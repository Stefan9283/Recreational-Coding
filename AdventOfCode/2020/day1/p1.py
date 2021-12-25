
nums = {}

for num in open('in').readlines():
    n = int(num.strip('\n'))
    if nums.get(2020 - n) != None:
        print((2020 - n) * n)
        break
    nums[n] = 1
    
    