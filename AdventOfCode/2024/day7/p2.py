
import itertools

with open('in', 'r') as f:
    lines = f.readlines()
    
ret = 0
    
for idx, line in enumerate(lines):
    res, terms = line.rstrip().split(': ')
    res = int(res)
    terms = list(map(int, terms.split()))
    for i in list(itertools.product([0, 1, 2], repeat=len(terms)-1)):
        res_ = terms[0]
        for j in range(len(terms) - 1):
            op = i[j]
            if op == 0:
                res_ += terms[j + 1]
            elif op == 1:
                res_ *= terms[j + 1]
            else:
                res_ = int(str(res_) + str(terms[j + 1]))
        if res_ == res:
            ret += res
            break     

print(ret)

