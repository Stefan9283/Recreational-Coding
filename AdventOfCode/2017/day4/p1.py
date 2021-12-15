
total = 0

for line in open('in').readlines():
    words = [word for word in line.strip('\n').split()]
    wordsSet = set(words)
    if len(words) - len(wordsSet) == 0:
        total += 1
print(total)    