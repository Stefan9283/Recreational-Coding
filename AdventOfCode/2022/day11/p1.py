
f = open('input', 'r')
lines = list(map(lambda x : x.rstrip(), f.readlines()))

# print(lines)

monkeys = {}
while lines:
    monkey = int(lines.pop(0).split()[1][:-1])
    
    starting = lines.pop(0)[len('  Starting items: '):].split(', ')
    starting = list(map(lambda x: int(x), starting))
    
    operation = lines.pop(0)[len('  Operation: new = '):].split()
    
        
        
        
    test = int(lines.pop(0)[len('  Test: divisible by '):])
    iftrue = int(lines.pop(0)[len('    If true: throw to monkey ')])
    iffalse = int(lines.pop(0)[len('    If false: throw to monkey ')])
    lines.pop(0)
    
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


for round_ in range(1, 21):
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
            worry_after_boredom = int(worry / 3)
            test = worry_after_boredom % monkey['test'] == 0
            if test:
                monkeys[monkey['iftrue']]['starting'].append(worry_after_boredom)
            else:
                monkeys[monkey['iffalse']]['starting'].append(worry_after_boredom)
    
    print(round_)
    pprint(monkeys)

a, b = sorted(counters.values())[-2:]
monkey_business = a * b
print(monkey_business)