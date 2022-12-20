lines = open("input.txt").read().splitlines()
lava = set()
for line in lines:
	x, y, z = [int(i) for i in line.split(',')]
	lava.add((x, y, z))

total_sides = 6 * len(lava)
for x,y,z in lava:
	for d in [-1, 1]:
		if (x + d, y, z) in lava:
			total_sides -= 1
		if (x, y + d, z) in lava:
			total_sides -= 1
		if (x, y, z + d) in lava:
			total_sides -= 1
print(total_sides)