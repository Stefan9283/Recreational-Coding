scores = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}

pair = {
    ')':'(',
    ']':'[',
    '}':'{',
    '>':'<'
}

revpair = {pair[key]:key for key in pair }

all_scores = []
for line in open('in1').readlines():
    line = line.strip('\n')
    stack = []
    err = False
    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
        else:
            if stack[-1] != pair[c]:
                # print(line, scores[c])
                err = True
                break
            else:
                stack.pop()
    if err: continue
    needed = list(stack)
    needed.reverse()
    needed = [revpair[c] for c in needed]
    score = 0
    for bracket in needed:
        score *= 5
        score += scores[bracket]
    all_scores.append(score)
    
    # print(line, stack, needed)
all_scores.sort()
print(all_scores[len(all_scores) // 2])