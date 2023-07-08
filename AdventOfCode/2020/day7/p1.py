

import pprint


d = {}


for line in open('input').readlines():
    line = line.replace(' bags', '').replace(' bag', '').replace('.', '').rstrip()
    parent, children = line.split(' contain ')
    children = children.split(', ')

    if d.get(parent) == None:
        d[parent] = {'children' : {}, 'parents': set()}

    for child in children:
        if child == 'no other':
            break
        tmp = child.split()
        count = int(tmp[0])
        color = ' '.join(tmp[1:])
        
        d[parent]['children'][color] = count
        if d.get(color) == None:
            d[color] = {'children' : {}, 'parents': set()}
        d[color]['parents'].add(parent)



to_visit = [ 'shiny gold' ]
found = set()
found.add('shiny gold')

while to_visit:
    last = to_visit.pop()
    
    for color in d[last]['parents']:
        if color not in found:
            found.add(color)
            to_visit.append(color)
    

print(len(found) - 1)

    

