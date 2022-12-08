score = 0

def toInt(val):
    if val.lower() == val:
        score0 = ord(val) - ord('a') + 1
    else:
        score0 = ord(val) - ord('A') + 26 + 1
    return score0

with open('input') as f:
    for _ in range(0, open('input').readlines().__len__(), 3):
        back1 = set(f.readline().rstrip())
        back2 = set(f.readline().rstrip())
        back3 = set(f.readline().rstrip())
        for val in back1.intersection(back2).intersection(back3):
            score += toInt(val)
        
print(score)