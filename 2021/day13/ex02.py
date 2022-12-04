def flip_coor(coor, char, foldline):
	x, y = coor
	if char == "x" and x > foldline:
		x = 2*foldline - x
	elif char == "y" and y > foldline:
		y = 2*foldline - y
	return (x, y)

coor, folds = open("big_input.txt").read().split("\n\n")
coors = {(int(l.split(',')[0]), int(l.split(',')[1])) for l in coor.split()}
for f in folds.splitlines():
	new_coor = set()
	foldline = int(f[f.index('=') + 1:])
	fold_dir = f[f.index('=') - 1]
	for c in coors:
		new_coor.add(flip_coor(c, fold_dir, foldline))
	coors = new_coor

max_x = max(c[0] for c in coors)
max_y = max(c[1] for c in coors)
for y in range(max_y + 1):
	print("".join("#" if (x, y) in coors else " " for x in range(max_x + 1)))