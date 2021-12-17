import sys
import math

vars = {}

def getVal(n: str) -> int:
    if n.isdecimal() or n.lstrip('-').isdecimal():
        return int(n)
    if vars.get(n) == None:
        vars[n] = 0
    return vars[n]

def compare(x, comp, y) -> bool:
    x = getVal(x)
    y = getVal(y)
    res = False
    if '!=' in comp:
        res = res or x != y
    else: 
        if '=' in comp:
            res = res or x == y
        if '>' in comp:
            res = res or x > y 
        if '<' in comp:
            res = res or x < y 
    return res
    
def doOp(x, op, y):
    getVal(x)
    if op == 'inc':
        vars[x] += getVal(y)
    elif op == 'dec':
        vars[x] -= getVal(y)
    else:
        print('bruh', op)

maxValueEver = -math.inf

for line in open('in').readlines():
    a, op, b, _, c, comp, d = line.strip('\n').split()
    if compare(c, comp, d):
        doOp(a, op, b)
        maxValueEver = max(maxValueEver, vars[max(vars, key=lambda x: vars[x])])
print(vars)

print('max value =', vars[max(vars, key=lambda x: vars[x])])
print('max value ever =', maxValueEver)
