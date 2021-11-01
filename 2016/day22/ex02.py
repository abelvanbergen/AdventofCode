from math import sqrt

def coorExits(x, y) -> bool:
	return x >= 0 and x < size_map and y >= 0 and y < size_map

class StorageNode:
	def __init__(self, data):
		elem = data[0].split('-')
		self.x = int(elem[1][1:])
		self.y = int(elem[2][1:])
		self.size = int(data[1][:-1])
		self.used = int(data[2][:-1])
		self.avail = int(data[3][:-1])

	def printobj(self):
		print("x-y = ", self.x, "-", self.y)
		print("size= ", self.size)
		print("used= ", self.used)
		print("avail= ", self.avail)
	
	def fitsIn(self, dest) -> bool:
		return self.used <= dest.avail

	def move(self, srcs):
		self.used += srcs.used
		self.avail -= srcs.used
		srcs.used = 0
		srcs.avail = srcs.size

	def empty(self) -> bool:
		return self.used == 0
    
	def getAllOptions(self) -> list:
		options = list()
		for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
			if coorExits(self.x + dx, self.y + dy):
				options.add((self.x + dx, self.y + dy))
		return options

data = open("input.txt", "r").read().splitlines()
nodes = dict()
for d in data[2:]:
	node = StorageNode(d.split())
	nodes[(node.x, node.y)] = node

for key in nodes:
	if nodes[key].empty() == True:
		print(nodes[key].x, nodes[key].y)

# ret = 0
# print(nPuzzle())
