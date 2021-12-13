
scores = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}

pair = {
    ')':'(',
    ']':'[',
    '}':'{',
    '>':'<'
}
revpair = {pair[key]:key for key in pair }

score = 0
for line in open('in1').readlines():
    line = line.strip('\n')
    stack = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
        else:
            if stack[-1] != pair[c]:
                # print(line, scores[c])
                score += scores[c]
                break
            else:
                stack.pop()
print(score)