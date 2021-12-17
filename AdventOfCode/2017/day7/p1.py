from functools import reduce
import sys

class TreeNode:
    def __init__(self, name, weight):
        self.name: str = name
        self.weight: int = weight
        self.children: list[str] = []
    def add(self, child):
        self.children.append(child) 
    def hasChild(self, child) -> bool:
        return child in self.children
    def __str__(self) -> str:
        return self.name + " (" + str(self.weight) + ") " + str(self.children) 
  
def checkNode(node: TreeNode) -> int:
    childrenWeights : list[(str, int)] = []
    for c in node.children:
        childrenWeights.append((c, checkNode(nodes[c])))  
    if not all([w[1] == childrenWeights[0][1] for w in childrenWeights]):
        print(node, childrenWeights)
        childrenWeights.sort()
        # median = childrenWeights[len(childrenWeights) // 2]
        # minSteps = sum([abs(num - median) for num in childrenWeights])
        # print(nodes['obxrn'].weight - minSteps)
        # return median * len(childrenWeights) + node.weight
        sys.exit()
    return node.weight + reduce(lambda s, x: s + x[1], childrenWeights, 0)

nodes = {}
for line in open('in').readlines():
    tok = line.replace('(', '').replace(')', '') \
            .replace(',', '').strip('\n').split()
    node = TreeNode(tok[0], int(tok[1]))
    for name in tok[3:]:
        node.add(name)
    nodes[node.name] = node

for child in nodes:
    hasParent = False
    for parent in nodes:
        if nodes[parent].hasChild(nodes[child].name):
            hasParent = True
            break
    if not hasParent:
        print('root', child)
        break

root = child

checkNode(nodes[root])
