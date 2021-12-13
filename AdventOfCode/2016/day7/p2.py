import re

total = 0
for line in open('in').readlines():
    line = line.strip('\n')
    
    in_brackets = re.findall("\[[a-z]*\]", line)
    for s in in_brackets:
        line = line.replace(s, ' ')
    
    in_brackets = [s[1:-1] for s in in_brackets]
    
    BABs = set()
    for s in in_brackets:
        for i in range(len(s) - 2):
            if s[i] != s[i+1] and s[i] == s[i+2]:
                BAB = ''.join([s[i+1], s[i], s[i+1]])
                BABs.add(BAB)

    good_ip = False    
    for BAB in BABs:
        if re.match("[a-z ]*("+BAB+")[a-z ]*", line):
            good_ip = True
            break
    if good_ip: 
        total += 1
print(total)