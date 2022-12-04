def get_next_loc(c, dy, dx):
	new_y = c[0] + dy if c[0] + dy < max_y else 0
	new_x = c[1] + dx if c[1] + dx < max_x else 0
	return new_y, new_x

def move_sea(right, down):
	total_moved = 0
	new_group = set()
	for c in right:
		new_y, new_x = get_next_loc(c, 0, 1)
		if (new_y, new_x) in right or (new_y, new_x) in down:
			new_group.add(c)
		else:
			new_group.add((new_y, new_x))
			total_moved += 1
	right = new_group
	new_group = set()
	for c in down:
		new_y, new_x = get_next_loc(c, 1, 0)
		if (new_y, new_x) in right or (new_y, new_x) in down:
			new_group.add(c)
		else:
			new_group.add((new_y, new_x))
			total_moved += 1
	down = new_group
	return (total_moved > 0), right, down

lines = open("input.txt").read().splitlines()
right = set()
down = set()
max_y = len(lines)
max_x = len(lines[0])
for y, line in enumerate(lines):
	for x, char in enumerate(line):
		if char == ">":
			right.add((y, x))
		elif char == "v":
			down.add((y, x))
step = 0
while True:
	step += 1
	has_moved, right, down = move_sea(right, down)
	if not has_moved:
		break
print(step)