from copy import deepcopy

def commen_divider(dx, dy) -> int:
	if 0 in [dx, dy]:
		divider = abs(dx) if dx != 0 else abs(dy)
		return dx//divider, dy//divider
	step = abs(dx) if abs(dx) < abs(dy) else abs(dy)
	for s in range(step, 0, -1):
		if dx % s == 0 and dy % s == 0:
			return dx//s, dy//s

def is_in_sight(grid, a, b):
	dx = b[0] - a[0]
	dy = b[1] - a[1]
	dx, dy = commen_divider(dx, dy)
	# print(dx, dy)
	while True:
		a[0] += dx
		a[1] += dy
		if a == b:
			return True
		if grid[a[1]][a[0]] == '#':
			return False

def get_in_sight(grid, c_x, c_y):
	count = 0
	amount = 0
	for n_y, row in enumerate(grid):
		for n_x, char in enumerate(row):
			if n_x == c_x and n_y == c_y:
				continue
			if char != '#':
				continue
			if is_in_sight(grid, [c_x, c_y], [n_x, n_y]):
				count += 1
			amount += 1
	return (count)

grid = open("input.txt").read().splitlines()

asteroids = dict()
for y, row in enumerate(grid):
	for x, char in enumerate(row):
		if char == '#':
			asteroids[(x, y)] = get_in_sight(grid, x, y)
for key, value in asteroids.items():
	print(key, "->", value)
print(max(asteroids.values()))
