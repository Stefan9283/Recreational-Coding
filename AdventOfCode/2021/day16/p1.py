mapping = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}

def parseType4(s: str) -> list[int]:
    num = []
    bitsRead = 6
    t = s[6:]
    for i in range(len(t) // 5):
        num.append(t[5*i + 1 : 5*(i + 1)])
        bitsRead += 5
        if t[5 * i] == '0': break
    return [int(''.join(num), 2), bitsRead]

versionSum = 0

def parsePacket(s: str):
    global versionSum
    version = int(s[:3], 2)
    versionSum += version
    packetTypeID = int(s[3:6], 2)
    lenTypeID = int(s[6], 2)
    if packetTypeID == 4:
        return parseType4(s)
    
    start = 0
    vals = []
    if lenTypeID == 0:
        L = int(s[7:7+15], 2)
        while start < L - 6:
            val, inc = parsePacket(s[7 + 15 + start:])
            start += inc
            vals.append(val)
        return [vals, 7 + 15 + start]
    elif lenTypeID == 1:
        L = int(s[7:7+11], 2)
        for _ in range(L):
            val, inc = parsePacket(s[7 + 11 + start:])
            start += inc
            vals.append(val)
        return [vals, 7 + 11 + start]

message = ''.join([mapping[c] for c in open('in').read().strip('\n')])
# print(message)
print(parsePacket(message))
print(versionSum)
