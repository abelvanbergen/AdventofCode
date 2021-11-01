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

	def empty(self) -> bool:
		return self.used == 0

data = open("input.txt", "r").read().splitlines()
nodes = dict()
for d in data[2:]:
	node = StorageNode(d.split())
	nodes[(node.x, node.y)] = node

res = 0
for key_1 in nodes:
	node_1 = nodes[key_1]
	for key_2 in nodes:
		node_2 = nodes[key_2]
		if key_1 != key_2 and node_1.used == False and node_1.fitsIn(node_2):
			res += 1
print(res)