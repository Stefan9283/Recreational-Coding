
def hasIncreasingSeq(s: str) -> bool:
    for i in range(len(s) - 2):
        if ord(s[i+1]) - ord(s[i]) == 1 and ord(s[i+2]) - ord(s[i+1]) == 1:
            return True
    return False
def hasValidChars(s: str) -> bool:
    invalid_chars = ['i', 'o', 'l']
    return all([c not in s for c in invalid_chars])
def has2orMorePairs(s: str) -> bool:
    count = 0
    i = 0
    while i < len(s) - 1 and count < 2:
        if s[i] == s[i + 1]:
            count += 1
            i = i + 2
        else: 
            i += 1
            
    return count == 2
def isPasswordValid(s: str) -> bool:
    return hasValidChars(s) and \
            has2orMorePairs(s) and \
            hasIncreasingSeq(s)

def incrementString(s: str) -> str:
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'z':
            s = list(s)
            s[i] = 'a'
            s = ''.join(s)
        else:
            s = list(s)
            s[i] = chr(ord(s[i]) + 1)
            s = ''.join(s)
            break
    return s

password = incrementString(open("in").read().strip('\n'))

# for the first password
while not isPasswordValid(password):
    password = incrementString(password)
print(password)

# for the second password
password = incrementString(password)
while not isPasswordValid(password):
    password = incrementString(password)
print(password)


