from hashlib import md5

key = 'abbhdwsy'
num = 0

newpass = []
for _ in range(0, 8):
    hash = ''
    while not hash.startswith('00000'):
        hash = md5((key + str(num)).encode()).hexdigest()
        num += 1
    newpass.append(hash[5])
print(''.join(newpass))