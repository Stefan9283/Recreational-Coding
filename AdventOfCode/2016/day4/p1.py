import re

def checkchecksum(checksum: str, occur: dict) -> bool:
    if not all([occur.get(c) != None for c in checksum]): return False
    l = sorted(list(occur), key=lambda x: (1 / occur[x]['occur'], x))  
    return checksum == ''.join(l[:len(checksum)])

         
total = 0
for line in open('in').readlines():
    tok = re.split("-|\[|\]", line.strip('\n'))
    room = int(tok[-3])
    checksum = tok[-2]
    occur = {}
    for group in tok[:-3]:
        for c in group:
            if occur.get(c) == None:
                occur[c] = {'occur':0, 'order':len(occur)}
            occur[c]['occur'] += 1
        # print(group, end=" ")
    if checkchecksum(checksum, occur):
        total += room
    # print(occur, tok, '\n')
print(total)