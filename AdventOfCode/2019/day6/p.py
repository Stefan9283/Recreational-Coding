
graph = {}

for line in open('in').readlines():
    orbited, orbitee = line.rstrip().split(')')
    
    if not graph.__contains__(orbited):
        graph[orbited] = {'children': [], 'parent': None} 
    
    if not graph.__contains__(orbitee):
        graph[orbitee] = {'children': [], 'parent': None}
    
    graph[orbited]['children'].append(orbitee)
    graph[orbitee]['parent'] = orbited

# PART1
def get_depth_sum(node, depth = 0):
    sum_ = depth
    for child in graph[node]['children']:
        sum_ += get_depth_sum(child, depth + 1)
    return sum_

print('PART1', get_depth_sum('COM'))

# PART2
depths = {}
def get_depths(node, depth = 0):
    depths[node] = depth
    for child in graph[node]['children']:
        get_depths(child, depth + 1)

def get_ancestors(node):
    parents = []
    tmp = node
    while tmp != None:
        parents.append(tmp)
        tmp = graph[tmp]['parent']
    return parents


def get_common_ancestor(node1, node2):
    parents1 = get_ancestors(node1)
    parents2 = get_ancestors(node2)
    parents1.reverse()
    parents2.reverse()
    last = None
    for (p1, p2) in zip(parents1, parents2):
        if p1 == p2:
            last = p1
        else:
            break
    return last


get_depths('COM')
print('PART2', depths)
you = depths['YOU']
san = depths['SAN']
com = depths[get_common_ancestor('YOU', 'SAN')]

print(you + san - com * 2 - 2)
