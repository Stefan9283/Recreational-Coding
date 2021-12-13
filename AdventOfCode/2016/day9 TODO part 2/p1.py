
line = open('in').readline().strip('\n')
print(line)

## snd try - it crashes
# def getMatchingBraket(i: int, line: str):
#     return (line[:i]).rfind('(')
# def uncompressLine(line: str) -> str:
#     while line.find('(') != -1:
#         uncompressed = []
#         i = len(line) - 1 
#         while True:
#             if line[i] == ')':
#                 prev = getMatchingBraket(i, line)
#                 count, repeat = [int(x) for x in line[prev + 1:i].split('x')]
#                 chars = line[i + 1 : i + 1 + count]
#                 for _ in range(count):
#                     uncompressed.pop()
#                 for _ in range(repeat):
#                     uncompressed.append(chars)
#                 uncompressed.append(line[:prev])
#                 i = -1
#             else: 
#                 uncompressed.append(line[i])
#                 i -= 1
#             if i <= 0: break
#         uncompressed.reverse()
#         line = ''.join(uncompressed)
#         print(line)
#     return line

## fst try
def getMatchingBraket(i: int, line: str):
    return (line[i:]).find(')') + i
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

line = uncompressLine(line)
print(line, len(line))