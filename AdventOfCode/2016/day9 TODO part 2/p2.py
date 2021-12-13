
line = open('in').readline().strip('\n')
print(line)

def getMatchingBraket(i: int, line: str):
    return line[i:].find(')') + i


def uncompressLine(line: str) -> str:
    uncompressed = []
    i = 0 
    for _ in range(len(line)):
        if line[i] == '(':
            next = getMatchingBraket(i, line)
            count, repeat = [int(x) for x in line[i+1:next].split('x')]
            chars = line[next + 1:next + 1 + count]
            for _ in range(repeat):
                uncompressed.append(chars)
            i = next + count + 1
        else: 
            uncompressed.append(line[i])
            i += 1
        if i >= len(line): break
    uncompressed = ''.join(uncompressed)
    return uncompressed


while line.find('(') != -1: 
    line = uncompressLine(line)
    print(len(line), line.count('('))
print(line, len(line))