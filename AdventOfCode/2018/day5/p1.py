input = list(open('in').read().strip('\n'))

def getCollapsedSize(s: str) -> int:
    found = 69
    while found:
        found = 0
        for i in range(len(s) - 2, -1, -1):
            if abs(ord(s[i]) - ord(s[i + 1])) == ord('a') - ord('A'):
                s.pop(i + 1)
                s.pop(i)
                found += 1
                break
    return len(s)

print(getCollapsedSize(input))