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

message = ''.join([mapping[c] for c in open('in').read().strip('\n')])

print(message)

def parseType4(s: str) -> list[int]:
    num = []
    t = s[6:]
    bitsRead = 6
    for i in range(len(s) // 5):
        num.append(t[5*i + 1:5*(i + 1)])
        bitsRead += 5
        if t[5 * i] == '0':
            break
    while bitsRead % 4:
        bitsRead += 1
    # print('\t' * indent, num)
    return [int(''.join(num), 2), bitsRead]

indent = 0

versionSum = 0

def parsePacket(s: str) -> list[int]:
    global indent
    global versionSum 
    version = int(s[:3], 2)
    packetTypeID = int(s[3:6], 2)

    versionSum += version
    print(versionSum)
    indent += 1

    print('\t' * indent, (version, packetTypeID), s, end=' ')

    if packetTypeID == 4:
        print('literal')
        indent -= 1
        return parseType4(s)
    else:
        lenTypeID = int(s[6])
        print('lenType', lenTypeID, end=' ')
        if lenTypeID == 0:
            bitsRead = 7 + 15
            L = int(s[7:bitsRead], 2)
            print('15bit', L)
            start = 0
            vals = []
            while start < L - 6:
                val, aux = parsePacket(s[22 + start:])
                vals.append(val)
                newstart = start + aux - 1
                print('\t' * (indent + 1), (val, aux), 22 + start, 'XV', 22 + newstart)
                start = newstart
                bitsRead += aux
            while bitsRead % 4:
                bitsRead += 1
            indent -= 1
            return [vals, bitsRead]
        else:
            bitsRead = 7 + 11
            L = int(s[7:bitsRead], 2)
            print('11bit', L)
            start = 0
            vals = []
            for _ in range(L):
                val, aux = parsePacket(s[18 + start:])
                vals.append(val)
                newstart = start + aux - 1
                print('\t' * (indent + 1), (val, aux), 18 + start, 'XI', 18 + newstart)
                start = newstart
                bitsRead += aux
            while bitsRead % 4:
                bitsRead += 1
            indent -= 1
            return [vals, bitsRead]

print(parsePacket(message))
print(versionSum)


# 0110001 00000000010 
    # 0000000 000000000010110
        # 000100 01010 
        # 101100 01011
    # 0010001 00000000010 
        # 000100 01100
        # 011100 01101
    # 00


# 01100010000000001000000000000000000101100001000101010110001011001000100000000010000100011000111000110100
# 0110001000000000100000000000000000010110 00010001010101100010110 01000100000000010000100011000111000110100

# 11
# 011 000 1 00000000010 

    # 15
    # 000 000 0 000000000010110 
        # 000 100 01010 
        # 101 100 01011 

    # 11
    # 001 000 1 00000000010 
        # 000 100 01100 
        # 011 100 01101 00
        
# 1010000 000000001011011 L = 27 XV
# 0010001 00000000001 L = 1 XI 
# 0110001 00000000101 L = 5 XI
# 111100 00110 
# 110100 00110 
# 101100 01100
# 010100 01111
# 010100 01111
# 0000000
