with open('in', 'r') as f:
    patterns = f.readline().rstrip().split(', ')
    patterns.sort(key=lambda x: len(x), reverse=True)
    f.readline() # empty line
    desired = list(map(lambda x: x.rstrip(), f.readlines()))

# TODO

def can_be_generated(target, patterns):
    
    # print(list(filter(lambda x: x[0] == target[len(current)], remaining)), remaining[len(current)])
    
    stack = ['']
    visited = set()
    
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        for choice in list(filter(lambda x: x[0] == target[len(current)], patterns)):
            current_ = current + choice
            if len(current_) > len(target):
                continue
            if len(current_) == len(target) and target == current_:
                return True
            # print(current, '+', rem, 'vs', target)
            if target[:len(current_)] == current_:
                stack.append(current_)
            
    return False
    
print(desired, len(patterns))
print(patterns)
    
ret = 0
for idx, line in enumerate(desired):
    print(idx, line)
    if can_be_generated(line, patterns):
        # print(line, 'can be generated')
        ret += 1
    
print(ret)