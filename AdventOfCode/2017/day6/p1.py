
def printList(l, i): 
    print(i, "| ", end='')
    for idx, e in enumerate(l):
        if idx == i:
            print('(' + str(e) + ')', end=' ')
        else:
            print(e, end=' ')
    print()

banks = [int(num) for num in open('in').read().split()]

states = set()
states.add(tuple(banks))

n = len(banks)

# print(banks)

seenAt = {tuple(banks): 0}

step = 0
while True:
    step += 1
    maxVal = max(banks)
    maxValIndex = banks.index(maxVal)
    # print(banks, 
    #         'max =', maxVal, 
    #         'found at', maxValIndex, 
    #         "step:", step)
    banks[maxValIndex] = 0

    i = maxValIndex + 1

    toBeDistributed = maxVal
    
    while toBeDistributed:
        i %= n
        
        banks[i] += 1
        toBeDistributed -= 1
        # printList(banks, i)
        i += 1 
    # print(banks, '\n')
    # print(banks, step)
    if tuple(banks) in states: 
        break
    seenAt[tuple(banks)] = step
    states.add(tuple(banks))
    
    
print(banks, 'repeated at step', step)
print(banks, 'loop size', step - seenAt[tuple(banks)])
