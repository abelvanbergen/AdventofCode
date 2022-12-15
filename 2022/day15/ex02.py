def manhatten_distance(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

sensors = set()
for line in open("input.txt").read().splitlines():
	tokens = line.split()
	sx, sy, bx = [int(tokens[i][2:-1]) for i in [2, 3, 8]]
	by = int(tokens[9][2:])
	mh_dis = manhatten_distance((sx, sy), (bx, by))
	sensors.add((sx, sy, mh_dis))

i = 0	
for x in range(4_000):
	for y in range(4_000_000):
		i +=1
print(i)
