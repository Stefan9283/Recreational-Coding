count = 0

for line in open('in').readlines():
    tok = line.strip('\n').replace('-', ' ').replace(':', '').split()
    if tok[3].count(tok[2]) in range(int(tok[0]), int(tok[1]) + 1):
        count += 1
        
print(count)
    
    