
l1, l2 = [], []

occur = {}


with open('in', 'r') as f:
    for line in f.readlines():
        e1, e2 = line.rstrip().split()
        
        l1.append(int(e1))
        
        e2 = int(e2)
        if e2 not in occur.keys():
            occur[e2] = 1
        else:
            occur[e2] += 1
        

sim = 0

for e in l1:
    if e in occur.keys():
        sim += e * occur[e]

print(sim)