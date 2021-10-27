data = open('input.txt', 'r').read().splitlines()
flipped_tiles = set()
for line in data:
	x, y, i = 0.0, 0, 0
	while i < len(line):
		if line[i] == 'e':
			x += 1
		elif line[i] == 'w':
			x -= 1
		elif line[i: i + 2:] == "ne":
			x += 0.5
			y += 1
			i+= 1
		elif line[i: i + 2:] == "nw":
			x -= 0.5
			y += 1
			i+= 1
		elif line[i: i + 2:] == "se":
			x += 0.5
			y -= 1
			i+= 1
		elif line[i: i + 2:] == "sw":
			x -= 0.5
			y -= 1
			i+= 1
		i+= 1
	elem = (x, y)
	if elem in flipped_tiles:
		flipped_tiles.remove(elem)
	else:
		flipped_tiles.add(elem)
print(len(flipped_tiles))