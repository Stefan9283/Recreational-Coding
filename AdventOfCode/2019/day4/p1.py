

def isPassword(val: int) -> bool:
    if len(str(val)) != 6: 
        return False
    digits = list(map(int, str(val)))
    if sorted(digits) != digits:
        return False

    adj_same = False
    for i in range(5):
        if digits[i] == digits[i + 1]:
            adj_same = True

    return adj_same

vals = list(map(int, open('in').readline().split('-')))

count = 0

for password in range(vals[0], vals[1] + 1):
    if isPassword(password):
        count += 1
print(count)