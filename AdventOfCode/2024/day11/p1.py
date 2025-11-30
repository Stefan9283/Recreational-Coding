
with open ('in') as f:
    nums = list(map(int, f.read().rstrip().split()))
    
for i in range(25):
    j = 0
    while j < len(nums):
        if nums[j] == 0:
            nums[j] = 1
            j+=1
        elif len(str(nums[j])) % 2 == 0:
            asstring = str(nums[j])
            half1, half2 = [
                int(asstring[:len(asstring)//2]),
                int(asstring[len(asstring)//2:])
            ]
            nums[j] = half1
            nums.insert(j+1, half2)
            j+=2
        else:
            nums[j] *= 2024
            j+=1
    
print(nums, len(nums))