class Node:
	def __init__(self, mat: list[str], id: int):
		self.map = list(mat)
		self.neigh = [[None for _ in range(3)]for _ in range(3)]
import os

print(os.getcwd())

nodes = []
for line in open('in').readlines():
	if line.startswith('Tile'):
		map = []
		id = int(line.strip('\n').replace(':', ' ').split()[-1])
	if len(line) == 1:
		nodes.append(Node(map, id))
print(len(nodes))