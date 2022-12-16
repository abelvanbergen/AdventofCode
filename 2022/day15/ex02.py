def manhatten_distance(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

sensors = set()
for line in open("example.txt").read().splitlines():
	tokens = line.split()
	sx, sy, bx = [int(tokens[i][2:-1]) for i in [2, 3, 8]]
	by = int(tokens[9][2:])
	mh_dis = manhatten_distance((sx, sy), (bx, by))
	sensors.add((sx, sy, mh_dis))

new_coor = set()
for ax, ay, am in sensors:
	for bx, by, bm in sensors:
		if manhatten_distance((ax, ay), (bx, by)) == am + bm + 2:
			new_coor.add((ax, ay, am))
			new_coor.add((bx, by, bm))
print(new_coor)

overlap = dict()
for sensor in new_coor:
	for dy in range(-sensor[2], sensor[2] + 1):
		for dx in range(-sensor[2], sensor[2] + 1):
			if (manhatten_distance((sensor[0] + dx, sensor[1] + dy), (sensor[0], sensor[1])) <= sensor[2] + 1):
				if (sensor[0] + dx, sensor[1] + dy) in overlap:
					overlap[(sensor[0] + dx, sensor[1] + dy)] += 1
				else:
					overlap[(sensor[0] + dx, sensor[1] + dy)] = 1
for key in overlap.keys():
	print(key)
	overlap = False
	for sensor in sensors:
		if manhatten_distance(key, (sensor[0], sensor[1])) <= sensor[2]:
			overlap = True
	if not overlap:
		print(key)
		break