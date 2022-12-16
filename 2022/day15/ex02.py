class Formula:
	def __init__(self, a, coor, length):
		self.a = a
		self.b = coor[1] - coor[1] * a
		self.coor = coor
		self.length = length
	
	def y_of_x(self, x):
		return (self.a * x + self.b)

	def intersect(self, obj)
		if (self.a == obj.a):
			return (None)
		return ((-self.b + obj.b) // 32)


def manhatten_distance(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

sensors = set()
for line in open("input.txt").read().splitlines():
	tokens = line.split()
	sx, sy, bx = [int(tokens[i][2:-1]) for i in [2, 3, 8]]
	by = int(tokens[9][2:])
	mh_dis = manhatten_distance((sx, sy), (bx, by))
	sensors.add((sx, sy, mh_dis))

formula = set()
for sensor in sensors

for i in range(4_000_000):
	print(i)
	line_x = set()
	for sensor in sensors:
		distance_to_line = abs(sensor[1] - i)
		start = sensor[0] - (sensor[2] - distance_to_line)
		if start < 0:
			start = 0
		end = sensor[0] + (sensor[2] - distance_to_line)
		if end > 4_000_000:
			end = 4_000_000
		for x in range(start, end):
			line_x.add(x)
	if (len(line_x) < 4_000_000):
		print(i)
		quit()
