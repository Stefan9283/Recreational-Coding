

with open('in', 'r') as f:
    lines = f.readlines()
    
ret = 0
    
for line in lines:
    res, terms = line.rstrip().split(': ')
    res = int(res)
    terms = list(map(int, terms.split()))
    # print(res, terms)
    for i in range(2 ** (len(terms) - 1)):
        res_ = terms[0]
        for j in range(len(terms) - 1):
            op = i & 2**j != 0
            # print(i, j, op)
            if op == 0:
                res_ += terms[j + 1]
            else:
                res_ *= terms[j + 1]
        if res_ == res:
            ret += res
            break     

print(ret)