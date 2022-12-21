def find_intersection(points1, points2):
	point1_1, point1_2 = points1
	point2_1, point2_2 = points2
	# Calculate slopes of the lines through the points
	m1 = (point1_2[1] - point1_1[1]) / (point1_2[0] - point1_1[0])
	m2 = (point2_2[1] - point2_1[1]) / (point2_2[0] - point2_1[0])
	# Calculate y-intercepts of the lines
	b1 = point1_1[1] - m1 * point1_1[0]
	b2 = point2_1[1] - m2 * point2_1[0]
	# Check if the lines are parallel
	if m1 == m2:
		return None
	# Calculate x-coordinate of the intersection point
	x = (b2 - b1) / (m1 - m2)
	if not (point1_1[0] <= x <= point1_2[0] or point1_2[0] <= x <= point1_1[0]):
		return None
	# Calculate y-coordinate of the intersection point
	y = m1 * x + b1
	return (x, y)

def manhatten_distance(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

sensors = set()
for line in open("input.txt").read().splitlines():
	tokens = line.split()
	sx, sy, bx = [int(tokens[i][2:-1]) for i in [2, 3, 8]]
	by = int(tokens[9][2:])
	mh_dis = manhatten_distance((sx, sy), (bx, by))
	sensors.add((sx, sy, mh_dis))

all_lines = list()
for sensor in sensors:
	point_1 = (sensor[0] - (sensor[2] + 1), sensor[1])
	point_2 = (sensor[0] - 1, sensor[1] + sensor[2])
	all_lines.append((point_1, point_2))
	point_1 = (sensor[0], sensor[1] - (sensor[2] + 1))
	point_2 = (sensor[0] - sensor[2], sensor[1] - 1)
	all_lines.append((point_1, point_2))

overlap = set()
for j in range(len(all_lines)):
	for i in range(len(all_lines)):
		if (j == i):
			continue
		b = all_lines[i]
		a = all_lines[j]
		coor = find_intersection(a, b)
		if coor == None:
			continue
		if not (coor[0].is_integer() and coor[1].is_integer()):
			continue
		x, y = int(coor[0]), int(coor[1])
		if not (0 <= x < 4_000_000 and 0 <= y < 4_000_000):
			continue
		if (x, y) not in overlap:
			overlap.add((x, y))
for key in overlap:
	if any(manhatten_distance(key, (x,y)) <= m for x,y,m in sensors):
		continue
	print(key[0] * 4_000_000 + key[1])
