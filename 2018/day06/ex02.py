def total_distance(x, y, coor):
	dis = 0
	for c in coor:
		dis += abs(x - c[0]) + abs(y - c[1])
	return (dis)


max_distance = 10000

lines = open("input.txt", "r").readlines()
coor = set()
x_max, y_max = 0, 0
for line in lines:
	x, y = [int(x) for x in line.split(", ")]
	if (x >= x_max):
		x_max = x + 1
	if (y >= y_max):
		y_max = y + 1
	coor.add((x, y))

result = 0
for y in range(y_max):
	for x in range(x_max):
		if (total_distance(x, y, coor) < max_distance):
			result += 1
print(result)
