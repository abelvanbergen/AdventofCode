grid = open("input.txt").read().splitlines()
grid_size = 100

def get_value(grid, x, y):
	if (x < 0 or x == grid_size):
		return (10)
	if (y < 0 or y == grid_size):
		return (10)
	return (int(grid[y][x]))
	

def is_lowest(grid, x, y):
	count = 0
	for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
		if int(grid[y][x]) < get_value(grid, x + dx, y + dy):
			count += 1
	if count == 4:
		return (True)
	return (False)

def get_size(grid, x, y):
	value = get_value(grid, x, y)
	if value >= 9:
		return (0)
	loc.add((x, y))
	return_value = 1
	for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
		if (x + dx, y + dy) not in loc:
			return_value += get_size(grid, x + dx, y + dy)
	return (return_value)

total = 0
lowest_points = set()
for y in range(grid_size):
	for x in range(grid_size):
		if is_lowest(grid, x, y) == True:
			lowest_points.add((x, y))

biggest_pools = []
for x, y in lowest_points:
	loc = set()
	biggest_pools.append(get_size(grid, x, y))
biggest_pools = sorted(biggest_pools)
print(biggest_pools)
res = 1
for i in biggest_pools[-3:]:
	res *= i
print(res)