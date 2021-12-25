count = 0

for line in open('in').readlines():
    tok = line.strip('\n').replace('-', ' ').replace(':', '').split()
    i1 = int(tok[0]) - 1
    i2 = int(tok[1]) - 1
    password = tok[3]
    c = tok[2]
    chars = [password[i1], password[i2]]
    if chars.count(c) == 1:
        count += 1    
        
print(count)
    
    