import itertools

f = open('in0')
s = f.readlines()

m = {"abcefg":0, "cf":1, "acdeg":2, "acdfg":3, "bcdf":4, 
     "abdfg":5, "abdefg":6, "acf":7, "abcdefg":8, "abcdfg":9 }

res = 0
for line in s:
    sig, num = line.strip().strip('\n').split(" | ")
    sig = sig.split(" ")
    num = num.split(" ")
    for perm in itertools.permutations("abcdefg"):
        charMap = {a:b for a,b in zip(perm,"abcdefg")}
        signew = ["".join(charMap[c] for c in line) for line in sig]
        numnew = ["".join(charMap[c] for c in line) for line in num]
        if all("".join(sorted(an)) in m for an in signew):
            numnew = ["".join(sorted(digit)) for digit in numnew]
            res += int("".join([str(m[digit]) for digit in numnew]))
print(res)
