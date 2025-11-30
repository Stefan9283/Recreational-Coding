
with open ('in') as f:
    nums = list(map(int, f.read().rstrip().split()))
    stones = {}
    for val in nums:
        if val not in stones.keys():
            stones[val] = 0
        stones[val] += 1
    
for i in range(75):
    new_stones = {}
    
    
    def add_stones(dict, key, val):
        if key not in dict.keys():
            dict[key] = val
        else:
            dict[key] += val
                    
    for k, v in stones.items():
        if k == 0:
            add_stones(new_stones, 1, v)
        elif len(str(k)) % 2 == 0:
            asstring = str(k)
            # print(asstring)
            half1, half2 = [
                int(asstring[:len(asstring)//2]),
                int(asstring[len(asstring)//2:])
            ]
            add_stones(new_stones, half1, v)
            add_stones(new_stones, half2, v)
        else:
            add_stones(new_stones, k * 2024, v)
    
    stones = new_stones

print(sum([v for _, v in stones.items()]))
    