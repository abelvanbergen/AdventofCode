class Train:
	def __init__(self, char, y, x):
		direction = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
		self.y = y
		self.x = x
		self.dy, self.dx = direction[char]
		self.intersectionCounter = 0

	def printobj(self):
		print("train-=-=-=-")
		print("y=", self.y, "x=", self.x)
		print("dy=", self.dy, "dx=", self.dx)
		print()

	def move_forward(self):
		self.y += self.dy
		self.x += self.dx

	def turn_left(self):
		temp = self.dy
		self.dy = self.dx * -1
		self.dx = temp

	def turn_right(self):
		temp = self.dy
		self.dy = self.dx
		self.dx = temp * -1
	
	def isCrashedWith(self, train) -> bool:
		return self.y == train.y and self.x == train.x

	def move(self, traintrack) -> bool:
		track = traintrack[self.y][self.x]
		if track == '+':
			if self.intersectionCounter % 3 == 0:
				self.turn_left()
			elif self.intersectionCounter % 3 == 2:
				self.turn_right()
			self.intersectionCounter += 1
		elif track == '/':
			temp = self.dy
			self.dy = self.dx * -1
			self.dx = temp * -1
		elif track == '\\':
			temp = self.dy
			self.dy = self.dx
			self.dx = temp
		self.move_forward()




traintrack = [list(x) for x in open("input.txt","r").read().splitlines()]
trains = []
for j, line in enumerate(traintrack):
	for i, char in enumerate(line):
		if char in ['^', '>', 'v', '<']:
			trainToTrack = {'^': '|', '>': '-', 'v': '|', '<': '-'}
			trains.append(Train(char, j, i))
			traintrack[j][i] = trainToTrack[char]

def trainComp(train):
	return (train.y, train.x)

while(True):
	trains = sorted(trains, key=trainComp)
	i = 0
	while (i < len(trains)):
		train = trains[i]
		train.move(traintrack)
		for toCrash, trainToCrash in enumerate(trains):
			if i != toCrash and train.isCrashedWith(trainToCrash):
				print("removing trains..")
				trains.remove(train)
				trains.remove(trainToCrash)
				if toCrash < i:
					i -= 2
				else:
					i -= 1
				break
		i += 1
	if (len(trains) == 1):
		print(str(trains[0].x) + "," + str(trains[0].y))
		quit()

