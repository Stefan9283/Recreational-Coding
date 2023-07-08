
f = open('input', 'r')
lines = list(map(lambda x : x.rstrip(), f.readlines()))

# print(lines)

monkeys = {}

max_div = 1

while lines:
    monkey = int(lines.pop(0).split()[1][:-1])
    
    starting = lines.pop(0)[len('  Starting items: '):].split(', ')
    starting = list(map(lambda x: int(x), starting))
    
    operation = lines.pop(0)[len('  Operation: new = '):].split()
        
        
    test = int(lines.pop(0)[len('  Test: divisible by '):])
    iftrue = int(lines.pop(0)[len('    If true: throw to monkey ')])
    iffalse = int(lines.pop(0)[len('    If false: throw to monkey ')])
    lines.pop(0)
    
    max_div *= test
    
    # print(monkey, starting, operation, test, iftrue, iffalse)
    monkeys[monkey] = {
        'starting': starting,
        'operation': operation,
        'test': test,
        'iftrue': iftrue,
        'iffalse': iffalse
    }



from pprint import pprint


# pprint(monkeys)

counters = {}
for id in monkeys.keys():
    counters[id] = 0


for round_ in range(1, 10000 + 1):
    for id in monkeys.keys():
        monkey = monkeys[id]
        while monkey['starting']:
            item = monkey['starting'].pop(0)
            counters[id] += 1
            operation = monkey['operation']
            if operation[-1] != 'old':
                worry = {
                    '+': lambda x: x + int(operation[-1]),
                    '*': lambda x: x * int(operation[-1])
                }[operation[1]](item)
            else:
                worry = {
                    '+': lambda x: 2 * x,
                    '*': lambda x: x ** 2
                }[operation[1]](item)
            worry_after_boredom = worry % max_div
            test = worry_after_boredom % monkey['test'] == 0
            if test:
                monkeys[monkey['iftrue']]['starting'].append(worry_after_boredom)
            else:
                monkeys[monkey['iffalse']]['starting'].append(worry_after_boredom)
    
    # print(round_)
    if round_ in [1, 20, 1000, 2000]:
        print(round_, counters.values())
        pprint(monkeys)

a, b = sorted(counters.values())[-2:]
monkey_business = a * b
print(monkey_business)


# == After round 1 ==
# Monkey 0 inspected items 2 times.
# Monkey 1 inspected items 4 times.
# Monkey 2 inspected items 3 times.
# Monkey 3 inspected items 6 times.

# == After round 20 ==
# Monkey 0 inspected items 99 times.
# Monkey 1 inspected items 97 times.
# Monkey 2 inspected items 8 times.
# Monkey 3 inspected items 103 times.

# After round 2, the monkeys are holding items with these worry levels:
# Monkey 0: 695, 10, 71, 135, 350
# Monkey 1: 43, 49, 58, 55, 362
# Monkey 2: 
# Monkey 3: 

# After round 3, the monkeys are holding items with these worry levels:
# Monkey 0: 16, 18, 21, 20, 122
# Monkey 1: 1468, 22, 150, 286, 739
# Monkey 2: 
# Monkey 3: 

# After round 4, the monkeys are holding items with these worry levels:
# Monkey 0: 491, 9, 52, 97, 248, 34
# Monkey 1: 39, 45, 43, 258
# Monkey 2: 
# Monkey 3: 

# After round 5, the monkeys are holding items with these worry levels:
# Monkey 0: 15, 17, 16, 88, 1037
# Monkey 1: 20, 110, 205, 524, 72
# Monkey 2: 
# Monkey 3: 

# After round 6, the monkeys are holding items with these worry levels:
# Monkey 0: 8, 70, 176, 26, 34
# Monkey 1: 481, 32, 36, 186, 2190
# Monkey 2: 
# Monkey 3: 

# After round 7, the monkeys are holding items with these worry levels:
# Monkey 0: 162, 12, 14, 64, 732, 17
# Monkey 1: 148, 372, 55, 72
# Monkey 2: 
# Monkey 3: 

# After round 8, the monkeys are holding items with these worry levels:
# Monkey 0: 51, 126, 20, 26, 136
# Monkey 1: 343, 26, 30, 1546, 36
# Monkey 2: 
# Monkey 3: 

# After round 9, the monkeys are holding items with these worry levels:
# Monkey 0: 116, 10, 12, 517, 14
# Monkey 1: 108, 267, 43, 55, 288
# Monkey 2: 
# Monkey 3: 

# After round 10, the monkeys are holding items with these worry levels:
# Monkey 0: 91, 16, 20, 98
# Monkey 1: 481, 245, 22, 26, 1092, 30
# Monkey 2: 
# Monkey 3: 

# ...

# After round 15, the monkeys are holding items with these worry levels:
# Monkey 0: 83, 44, 8, 184, 9, 20, 26, 102
# Monkey 1: 110, 36
# Monkey 2: 
# Monkey 3: 

# ...

# After round 20, the monkeys are holding items with these worry levels:
# Monkey 0: 10, 12, 14, 26, 34
# Monkey 1: 245, 93, 53, 199, 115
# Monkey 2: 
# Monkey 3: 