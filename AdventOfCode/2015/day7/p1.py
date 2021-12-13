import numpy as np

variables = {}
computed = {}

def getValue(s: str) -> int:
    if computed.get(s) != None:
        return computed[s]
    
    if s.isnumeric(): return np.uint16(int(s))
    f, terms = variables[s]['func'], variables[s]['terms']
    # print(s, f, terms, type(terms))
    
    if type(terms) == tuple:
        res = f(terms[0], terms[1])
    else: 
        res = f(terms)
        
    computed[s] = res
    return res
for line in open('in').readlines():
    tok = line.strip('\n').split()
    
    if tok[0] == 'NOT':
        variables[tok[-1]] = { 'func':(lambda x: ~getValue(x)), 'terms': tok[1]}
    elif tok[1] == 'AND':        
        variables[tok[-1]] = { 'func':(lambda x, y: getValue(x) & getValue(y)), 'terms': (tok[0], tok[2])}
    elif tok[1] == 'OR':        
        variables[tok[-1]] = { 'func':(lambda x, y: getValue(x) | getValue(y)), 'terms': (tok[0], tok[2])}
    elif tok[1] == 'LSHIFT':        
        variables[tok[-1]] = { 'func':(lambda x, y: getValue(x) << getValue(y)), 'terms': (tok[0], tok[2])}
    elif tok[1] == 'RSHIFT':
        variables[tok[-1]] = { 'func':(lambda x, y: getValue(x) >> getValue(y)), 'terms': (tok[0], tok[2])}
    else:     
        variables[tok[-1]] = { 'func':(lambda x: getValue(x)), 'terms': tok[0]}

a = getValue('a')
print('fst a',  a)
variables['b'] = { 'func':(lambda x: getValue(x)), 'terms': str(a)}
computed = {}
print('snd a',  getValue('a'))
