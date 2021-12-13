coor, folds = open("input.txt").read().split("\n\n")
coors = {(int(l.split(',')[0]), int(l.split(',')[1])) for l in coor.split()}
for f in folds.split('\n')[:-1]:
	new_coor = set()
	foldline = int(f[f.index('=') + 1:])
	if "x" in f:
		for c in coors:
			x, y = c
			if (x > foldline):
				x = foldline - (x - foldline)
			new_coor.add((x, y))
	else:
		for c in coors:
			x, y = c
			if (y > foldline):
				y = foldline - (y - foldline)
			new_coor.add((x, y))
	coors = new_coor
grid = []
for _ in range(7):
	grid.append(["."] * 40)
for x, y in coors:
	grid[y][x] = "#"
for line in grid:
	print("".join(line))