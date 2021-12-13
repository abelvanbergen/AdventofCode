def flip_coor(coor, char, foldline):
	x, y = coor
	if char == "x" and x > foldline:
		x = 2*foldline - x
	elif char == "y" and y > foldline:
		y = 2*foldline - y
	return (x, y)

coor, folds = open("input.txt").read().split("\n\n")
coors = {(int(l.split(',')[0]), int(l.split(',')[1])) for l in coor.split()}
for f in folds.split('\n'):
	new_coor = set()
	foldline = int(f[f.index('=') + 1:])
	fold_dir = f[f.index('=') - 1]
	for c in coors:
		new_coor.add(flip_coor(c, fold_dir, foldline))
	coors = new_coor
	print(len(coors))
	quit()