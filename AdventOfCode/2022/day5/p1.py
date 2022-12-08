input = open('input').readlines()

stacks = [] * 9

for line in input:
    line = line.rstrip()
    if line.startswith(' 1') or len(line) == 0:
        continue
    elif line.startswith('move'):
        tokens = line.split()
        count_, from_, to_ = int(tokens[1]), int(tokens[3]) - 1, int(tokens[5]) - 1
        for i in range(count_):
            stacks[to_] = [ stacks[from_][0] ] + stacks[to_]
            stacks[from_] = stacks[from_][1:]
    else:
        idx = 0
        for i in range(1, len(line), 4):
            c = line[i]
            if c != ' ':
                if len(stacks) <= idx:
                    for j in range(idx + 1 - len(stacks)):
                        stacks.append([])
                stacks[idx].append(c)
            idx += 1

print(''.join(list(map(lambda x : x[0], stacks))))
