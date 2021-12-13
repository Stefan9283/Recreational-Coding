from hashlib import md5

key = 'abbhdwsy'
num = 0

newpass = ['_' for _ in range(0, 8)]
while newpass.count('_'):
    hash = ''
    while not hash.startswith('00000'):
        hash = md5((key + str(num)).encode()).hexdigest()
        num += 1
    if str(hash[5]).isdigit() and int(hash[5]) < 8:
        i = int(hash[5])
        if newpass[i] == '_':
            newpass[i] = hash[6]
            print(hash, i, newpass)
print(''.join(newpass[0:8]))