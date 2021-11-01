class NormalTrack:
	def __init__(self, trainTrack, y, x):
		self.y, self.x = y, x
		if (trainTrack[y][x] == '|'):
			neighbors = [(y - 1, x), (y + 1, x)]
		elif (trainTrack[y][x] == '-'):
			neighbors = [(y, x - 1), (y, x + 1)]
		elif (trainTrack[y][x] == '/'):
			if y >=0 and  trainTrack[y - 1][x] in ['|', '+']:
				neighbors = [(y - 1, x), (y, x - 1)]
			else:
				neighbors = [(y + 1, x), (y, x + 1)]
		else:
			if y >=0 and  trainTrack[y - 1][x] in ['|', '+']:
				neighbors = [(y - 1, x), (y, x + 1)]
			else:
				neighbors = [(y + 1, x), (y, x - 1)]
		
class Intersection:
	def __init__(self, y, x):
		self.y, self.x = y, x

class Train:
	def __init__(self, t, y, x):
		self.y, self.x = y, x
		if t == '^':
			self.y_old, self.x_old = y - 1, x
		elif t == '>':
			self.y_old, self.x_old = y, x - 1
		elif t == 'v':
			self.y_old, self.x_old = y + 1, x
		else:
			self.y_old, self.x_old = y, x + 1
		self.intersectionCounter = 0

	def isAt(self, y, x) -> bool:
		return self.y == y and self.x == x

	def move(self, track):
		if type(track) == Intersection:
			direction = (track.y - self.y, track.x - self.x)
			ways = [(0, -1), (-1, 0), (0, 1), (1, 0)]
			i_ways = ways.find(direction)
			new_way = 
		else:
			nb_1, nb_2 = track.neighbors
			if (self.y_old == nb_1[0] and self.x_old == nb_1[1]):
				self.y_old, self.x_old = self.y, self.x_old
				self.y, self.x = nb_2[0], nb_2[1]
			else:
				self.y_old, self.x_old = self.y, self.x_old
				self.y, self.x = nb_2[0], nb_2[1]




trainTrack = [list(x) for x in open("example.txt", "r").read().splitlines()]
trains = []
normalTrack = dict()
intersections = dict()
for j in range(len(trainTrack)):
	for i in range(len(trainTrack[0])):
		if trainTrack[j][i] in ['^', '>', 'v', '<']:
			trains.append(Train(trainTrack[j][i], j, i))
			if trainTrack[j][i] in ['^', 'v',]:
				trainTrack[j][i] = '|'
			else:
				trainTrack[j][i] = '-'
			normalTrack[(j, i)] = NormalTrack(trainTrack, j, i)
		elif trainTrack[j][i] == '+':
			intersections[(j, i)] = Intersection(j, i)
		else:
			normalTrack[(j, i)] = NormalTrack(trainTrack, j, i)

# tick = 0
# while(True):
# 	for t in sorted(trains.keys()):
# 		tra
