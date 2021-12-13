import re

total = 0
for line in open('in').readlines():
    line = line.strip('\n')

    in_brackets = re.findall("\[[a-z]*\]", line)
    for s in in_brackets:
        line = line.replace(s, ' ')
    
    in_brackets = [s[1:-1] for s in in_brackets]
    out_brackets = line.split()
    
    # print(in_brackets, out_brackets)
    
    good_ip = True
    for s in in_brackets:
        ans = re.match("[a-z]*([a-z])([a-z])\\2\\1[a-z]*", s) != None
        if ans: 
            good_ip = False
            break
    if not good_ip: continue
    
    good_ip = False
    for s in out_brackets:
        for i in range(len(s) - 3):
            if s[i] != s[i+1] and s[i+2] == s[i+1] and s[i] == s[i+3]:
                good_ip = True
                break 
        if good_ip:
            break
        # ans = re.match("[a-z]*([a-z])(!\\1)\\2\\1[a-z]*", s) != None
        # print(s, ans)
        # if ans: 
        #     good_ip = True

    if good_ip: total += 1
print(total)