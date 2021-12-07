lines = open("input.txt", "r").read().replace(" -> ", ",").splitlines()
coor = dict()
for line in lines:
	x1, y1, x2, y2 = [int(x) for x in line.split(',')]
	if (x2 < x1):
		x1, x2 = x2, x1
	if (y2 < y1)
		y1, y2 = y2, y1
	for y in range(y1, y2 + 1):
		for x in range(x1, x2 + 1):
			if (x, y) in coor.keys():
				coor[(x, y)] += 1
			else:
				coor[(x, y)] = 1
print(sum(coor[key]>1 for key in coor.keys()))