

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



to_visit = [ ('shiny gold', 1) ]
total = 0
while to_visit:
    color, count = to_visit.pop()
    total += count
    print(count)
    for child in d[color]['children']:
        to_visit.append((child, count * d[color]['children'][child]))
      
    
print(total - 1)
