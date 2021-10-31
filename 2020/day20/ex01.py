class Tile:
	def __init__(self, data):
		self.id = int(data[0][5:9:])
		self.grid = [list(x) for x in data[1:]]
		self.north = self.grid[0]
		self.south = self.grid[-1]
		self.west = list()
		for i in range(len(self.grid)):
			self.west.append(self.grid[i][0])
		self.east = list()
		for i in range(len(self.grid)):
			self.east.append(self.grid[i][-1])
	
	def printobj(self):
		print("Tile.ID =", self.id)
		for line in self.grid:
			print(line)
		print("north = ", self.north)
		print("south = ", self.south)
		print("west = ", self.west)
		print("east = ", self.east)



data = open("input.txt", 'r').read().split('\n\n')
tiles = list()
for d in data:
	tiles.append(Tile(d.split('\n')))

corners = set()
sides = set()
midle = set()
for tile in tiles:
	amount = 0
	for toCompare in tiles:
		if tile.id == toCompare.id:
			continue
		for tileSide in [tile.north, tile.east, tile.south, tile.west]:
			toCompareSides = [toCompare.north, toCompare.east, toCompare.south, toCompare.west]
			if tileSide in toCompareSides or tileSide[::-1] in toCompareSides:
				amount += 1
				break
	if amount == 2:
		corners.add(tile)
	elif amount == 3:
		sides.add(tile)
	else:
		midle.add(tile)
res = 1
for tile in corners:
	res *= tile.id
print(res)

