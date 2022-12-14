lines = open("example.txt").read().splitlines()
rock = set()
for line in lines:
	coor = [[int(x) for x in c.split(",")] for c in line.split("->")]
	for i in range(len(coor) - 1):
		x1, y1, x2, y2 = [*coor[i], *coor[i+1]]
		sx, ex = [x1, x2] if x1 < x2 else [x2, x1]
		sy, ey = [y1, y2] if y1 < y2 else [y2, y1]
		for x in range(sx, ex + 1):
			for y in range(sy, ey + 1):
				rock.add((x, y))
print(rock)