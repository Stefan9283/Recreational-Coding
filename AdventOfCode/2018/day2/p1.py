
two = 0
three = 0

def atLeast2or3(s: str) -> list[int]:
    found = [False, False]
    for c in s:
        n = s.count(c)
        found[0] = found[0] or n == 2
        found[1] = found[1] or n == 3
    return found

for line in open('in').readlines():
    two_word, three_word = atLeast2or3(line)
    two += two_word
    three += three_word
print(two * three)