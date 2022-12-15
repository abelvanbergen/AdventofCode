def manhatten_distance(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

sensors = set()
for line in open("input.txt").read().splitlines():
	tokens = line.split()
	sx, sy, bx = [int(tokens[i][2:-1]) for i in [2, 3, 8]]
	by = int(tokens[9][2:])
	mh_dis = manhatten_distance((sx, sy), (bx, by))
	sensors.add((sx, sy, mh_dis))

line_y= 2000000
line_x = set()
for sensor in sensors:
	distance_to_line = abs(sensor[1] - line_y)
	start = sensor[0] - (sensor[2] - distance_to_line)
	end = sensor[0] + (sensor[2] - distance_to_line)
	for x in range(start, end):
		line_x.add(x)
print(len(line_x))

	