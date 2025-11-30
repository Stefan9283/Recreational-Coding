
# A * a + B * c = e
# A * b + B * d = f
# 
# A = (e - B * c) / a
# A = (f - B * d) / b
# 
# (e - B * c) / a = (f - B * d) / b
# (e - B * c) * b = (f - B * d) * a
# B * (ad - bc) = (af - be) 
# B = (af - be) / (ad - bc)

with open('in') as f:
    input = f.read().replace('Button A: X+', '').replace('Button B: X+', '').replace('Prize: X=', '').replace(', Y+', ' ').replace(', Y=', ' ').split('\n\n')
    input = list(map(lambda x: list(map(lambda y: list(map(int, y.split(' '))), x.split('\n'))), input))

A_cost = 3
B_cost = 1

tokens = 0
for case in input:
    [[a, b], [c, d], [e, f]] = case
    
    e += 10000000000000
    f += 10000000000000
    
    B = (f * a - b * e) // (a * d - b * c)
    A = (e - B * c) // a
    if all([A * a + B * c == e, A * b + B * d == f]):
        tokens += A_cost * A + B * B_cost

print(tokens)

