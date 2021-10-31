from math import sqrt

class Tile:
	def __init__(self, data):
		self.id = int(data[0][5:9:])
		self.grid = [list(x) for x in data[1:]]
		self.north = self.grid[0]
		self.south = self.grid[-1][::-1]
		self.west = list()
		for i in range(len(self.grid)):
			self.west.append(self.grid[i][0])
		self.east = list()
		for i in range(len(self.grid) - 1, -1, -1):
			self.east.append(self.grid[i][-1])
		self.northConnects = 0
		self.southConnects = 0
		self.westConnects = 0
		self.eastConnects = 0
	
	def printobj(self):
		print("Tile.ID =", self.id)
		for line in self.grid:
			print(line)
		print("north = ", self.north)
		print("south = ", self.south)
		print("west = ", self.west)
		print("east = ", self.east)
		print("northConnects = ", self.northConnects)
		print("southConnects = ", self.southConnects)
		print("westConnects = ", self.westConnects)
		print("eastConnects = ", self.eastConnects)
		print()
	
	def removeSides(self):
		newGrid = [self.grid[x][1:-1:] for x in range(1, len(self.grid) - 1)]	
		self.grid = newGrid

	def rotateRight(self):
		newGrid = list()
		for i in range(len(self.grid)):
			newLine = [self.grid[j][i] for j in range(len(self.grid) - 1, -1, -1)]
			newGrid.append(newLine)
		self.grid = newGrid
		temp = self.north
		self.north = self.west
		self.west = self.south
		self.south = self.east
		self.east = temp
		temp = self.northConnects
		self.northConnects = self.westConnects
		self.westConnects = self.southConnects
		self.southConnects = self.eastConnects
		self.eastConnects = temp

	def flipNS(self):
		self.grid = self.grid[::-1]
		temp = self.north
		self.north = self.south
		self.south = temp
		temp = self.northConnects
		self.northConnects = self.southConnects
		self.southConnects = temp
		self.east = self.east[::-1]
		self.west = self.west[::-1]

	def flipWE(self):
		self.grid = [x[::-1] for x in self.grid]
		temp = self.west
		self.west = self.east
		self.east = temp
		temp = self.westConnects
		self.westConnects = self.eastConnects
		self.eastConnects = temp
		self.north = self.north[::-1]
		self.south = self.south[::-1]

	def rotateTill(self, northSide, westSide, corner):
		while self.northConnects != northSide:
			self.rotateRight()
		if corner == False:
			if self.westConnects != westSide:
				self.flipWE()
			if self.westConnects != westSide:
				self.rotateRight()
		else:
			if self.westConnects != westSide and self.westConnects != 0:
				self.flipWE()
			if self.westConnects != westSide:
				self.rotateRight()

def count_seamonsters(totalMap, j, i):
	seamonster = [(0, 18), (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19), (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)]
	for y, x in seamonster:
		if totalMap[j + y][i + x] != '#':
			return (0)
	return (1)

def is_rightrotaion(totalMap):
	total_seamonsters = 0
	for j in range(len(totalMap) - 2):
		for i in range(len(totalMap) - 19):
			total_seamonsters += count_seamonsters(totalMap, j, i)
	return total_seamonsters

def rotateTotalMap(totalMap):
	newGrid = list()
	for i in range(len(totalMap)):
		newLine = [totalMap[j][i] for j in range(len(totalMap) - 1, -1, -1)]
		newGrid.append(newLine)
	return newGrid
		
def flipTotalMap(totalMap):
	return totalMap[::-1]

size_tile = 8

data = open("input.txt", 'r').read().split('\n\n')
tiles = list()
for d in data:
	tiles.append(Tile(d.split('\n')))


corners = dict()
sides = dict()
midle = dict()
for tile in tiles:
	amount = 0
	for toCompare in tiles:
		if tile.id == toCompare.id:
			continue
		toCompareSides = [toCompare.north, toCompare.east, toCompare.south, toCompare.west]
		if tile.north in toCompareSides or tile.north[::-1] in toCompareSides:
			amount += 1
			tile.northConnects = toCompare.id
		if tile.south in toCompareSides or tile.south[::-1] in toCompareSides:
			amount += 1
			tile.southConnects = toCompare.id
		if tile.east in toCompareSides or tile.east[::-1] in toCompareSides:
			amount += 1
			tile.eastConnects = toCompare.id
		if tile.west in toCompareSides or tile.west[::-1] in toCompareSides:
			amount += 1
			tile.westConnects = toCompare.id
	if amount == 2:
		corners[tile.id] = tile
	elif amount == 3:
		sides[tile.id] = tile
	else:
		midle[tile.id] = tile

all_tiles = dict()
for key in corners:
	all_tiles[key] = corners[key]
	all_tiles[key].removeSides()
for key in midle:
	all_tiles[key] = midle[key]
	all_tiles[key].removeSides()
for key in sides:
	all_tiles[key] = sides[key]
	all_tiles[key].removeSides()

size_map = int(sqrt(len(all_tiles)))

newGrid = [[0] * (size_map + 2) for _ in range(size_map + 2)]
for key in corners:
	newGrid[1][1] = key
	break
all_tiles[newGrid[1][1]].rotateTill(0, 0, False)
for j in range(1, size_map + 1):
	for i in range(1, size_map + 1):
		if j == 1 and i == 1:
			continue
		if i == 1:
			newGrid[j][i] = all_tiles[newGrid[j - 1][i]].southConnects
		else:
			newGrid[j][i] = all_tiles[newGrid[j][i - 1]].eastConnects
		# if (j == 2 and i == 12):
			# print("north: ", newGrid[j - 1][i])
			# print("east: ", newGrid[j][i - 1])
			# all_tiles[newGrid[j][i]].printobj()
		all_tiles[newGrid[j][i]].rotateTill(newGrid[j - 1][i], newGrid[j][i - 1], (j, i) == (1, size_map))
		# if (j == 2 and i == 12):
		# 	all_tiles[newGrid[j][i]].printobj()

totalMap = [[] for _ in range(size_map * size_tile)]
for j in range(1, size_map + 1):
	for i in range(1, size_map + 1):
		for k in range(size_tile):
			totalMap[size_tile * (j - 1) + k] += all_tiles[newGrid[j][i]].grid[k]
total_hashes = 0
for line in totalMap:
	total_hashes += line.count('#')

for _ in range(4):
	ret = is_rightrotaion(totalMap)
	if ret > 0:
		print(total_hashes - (ret * 15))
	totalMap = rotateTotalMap(totalMap)
totalMap = flipTotalMap(totalMap)
for _ in range(4):
	ret = is_rightrotaion(totalMap)
	if ret > 0:
		print(total_hashes - (ret * 15))
	totalMap = rotateTotalMap(totalMap)



		

		




