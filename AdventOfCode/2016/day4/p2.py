import re

def checkchecksum(checksum: str, occur: dict) -> bool:
    if not all([occur.get(c) != None for c in checksum]): return False
    l = sorted(list(occur), key=lambda x: (1 / occur[x]['occur'], x))  
    return checksum == ''.join(l[:len(checksum)])
    
def shiftLetter(c: chr, by: int) -> chr:
    by %= 26
    # print(c, by)
    for _ in range(0,by):
        if c == 'z':
            c = 'a'
        else:
            c = chr(ord(c) + 1)
    return c
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
    if checkchecksum(checksum, occur):
        # decrypt name
        decrypt = ''.join([shiftLetter(c, room) for group in tok[:-3] for c in group])
        decrypt = []
        for group in tok[:-3]:
            decr = []
            for c in group:
                decr.append(shiftLetter(c, room))
            decrypt.append(''.join(decr))
        print('-'.join(decrypt), room)
        