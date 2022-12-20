class Formula:
	def __init__(self, a, coor, length):
		self.a = a
		self.b = -a*coor[0] + coor[1]
		self.coor = coor
		self.length = length

	def __str__(self):
		ret = f"Formula y = {self.a}x + {self.b}\n"
		ret += f"start = {self.coor}, length = {self.length}\n"
		return ret
	
	def y_of_x(self, x):
		return (self.a * x + self.b)

	def intersect(self, obj):
		if (self.a == obj.a):
			return (None)
		return ((self.b - obj.b) // 2)


def manhatten_distance(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

sensors = set()
for line in open("example.txt").read().splitlines():
	tokens = line.split()
	sx, sy, bx = [int(tokens[i][2:-1]) for i in [2, 3, 8]]
	by = int(tokens[9][2:])
	mh_dis = manhatten_distance((sx, sy), (bx, by))
	sensors.add((sx, sy, mh_dis))

# a = Formula(-1, (1, 3), 3)
# print(a)
# b = Formula(1, (1, -1), 3)
# print(b)
# x = a.intersect(b)
# print(x)
# sensors.add((0, 0, 1))
formula = set()
for sensor in sensors:
	f = Formula(1, (sensor[0], sensor[1] - sensor[2] - 1), sensor[2] + 1)
	formula.add(f)
	f = Formula(-1, (sensor[0] + 1, sensor[1] + sensor[2]), sensor[2] + 1)
	formula.add(f)

overlaps = dict()
for a in formula:
	for b in formula:
		x = a.intersect(b)
		if (x == None):
			continue
		if (x - a.coor[0] < a.length and x - a.coor[0] >= 0):
			y = a.y_of_x(x)
			if (x, y) in overlaps:
				overlaps[(x, y)] += 1
			else:
				overlaps[(x,y)] = 1
print([key for key, value in overlaps.items() if value >= 3])


