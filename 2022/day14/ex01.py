def get_lowest_rock(rocks):
	return (max(y for _, y in rocks))

def get_pos_new_item(items, lowest_rock):
	x, y = 500, 0
	while (True):
		if y > lowest_rock:
			return None
		has_to_move = True
		for dx in [0, -1, 1]:
			if (x + dx, y + 1) not in items:
				x += dx
				y += 1
				has_to_move = False
				break
		if (has_to_move):
			return (x, y)

def let_sand_fall(items):
	lowest_rock = get_lowest_rock(items)
	count = 0
	while (True):
		pos = get_pos_new_item(items, lowest_rock)
		if (pos == None):
			return (count)
		items.add(pos)
		count += 1

lines = open("input.txt").read().splitlines()
rocks = set()
for line in lines:
	coor = [[int(x) for x in c.split(",")] for c in line.split("->")]
	for i in range(len(coor) - 1):
		x1, y1, x2, y2 = [*coor[i], *coor[i+1]]
		sx, ex = [x1, x2] if x1 < x2 else [x2, x1]
		sy, ey = [y1, y2] if y1 < y2 else [y2, y1]
		for x in range(sx, ex + 1):
			for y in range(sy, ey + 1):
				rocks.add((x, y))

print(let_sand_fall(rocks))