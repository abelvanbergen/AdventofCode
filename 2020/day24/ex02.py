data = open('input.txt', 'r').read().splitlines()
amount_of_turns = 101
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

def neighbours(x, y):
	yield(x - 0.5, y + 1)
	yield(x + 0.5, y + 1)
	yield(x - 1, y)
	yield(x + 1, y)
	yield(x - 0.5, y - 1)
	yield(x + 0.5, y - 1)

def count_neighbours(x, y):
	count = 0
	for s in neighbours(x, y):
		count += s in flipped_tiles
	return(count)

def calc_flipped_tiles():
	new_flipped_tiles = set()
	for tile in flipped_tiles:
		for spot in neighbours(*tile):
			if spot not in flipped_tiles and count_neighbours(*spot) == 2:
				new_flipped_tiles.add(spot)
		if count_neighbours(*tile) in (1, 2):
			new_flipped_tiles.add(tile)
	return new_flipped_tiles

for i in range(1, amount_of_turns):
	flipped_tiles = calc_flipped_tiles()
print("day", str(i) + ":", len(flipped_tiles))
