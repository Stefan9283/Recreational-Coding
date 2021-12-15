
def getCharOccur(s):
    d = {}
    for c in s:
        if d.get(c) == None:
            d[c] = 0
        d[c] += 1
    tup = []
    for c in d:
        tup.append((c, d[c]))
    tup.sort(key=lambda x: x[0])
    return tuple(tup)

total = 0

for line in open('in').readlines():
    words = [getCharOccur(word) for word in line.strip('\n').split()]
    wordsSet = set(words)
    if len(words) - len(wordsSet) == 0:
        total += 1
print(total)    