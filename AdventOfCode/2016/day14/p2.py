import hashlib
import re
  
def md5(salt, i):
    hash = str(hashlib.md5((salt + str(i)).encode()).hexdigest())
    for _ in range(2016):
        hash = str(hashlib.md5(hash.encode()).hexdigest())
    return hash

salt = 'ahsbgdzn'

hashes = []
consec5 = []

rx3 = re.compile(r'(.)\1{2,}')
rx5 = re.compile(r'(.)\1{4,}')

for i in range(1000):
    result = md5(salt, i)
    hashes.append(result)
    
    c5 = rx5.findall(result)
    if c5 != []:
        consec5.append(c5[0])
    else:
        consec5.append('')


max_found = 64
nth = max_found


i = 0
while nth > 0:
    # consec5 = consec5[1:]
    result = md5(salt, i + 1000)
    hashes.append(result)
    
    c5 = rx5.findall(result)
    if c5 != []:
        consec5.append(c5[0])
    else:
        consec5.append('')
        
    
    c3 = rx3.findall(hashes[i])
    for c in c3:
        if c in consec5[i+1 :]:
            print(c, end='| ')
            print(max_found - nth + 1, i, hashes[i])
            nth -= 1
        break
    i += 1

    
