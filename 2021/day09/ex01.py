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

total = 0
for y in range(grid_size):
	for x in range(grid_size):
		if is_lowest(grid, x, y) == True:
			total += int(grid[y][x]) + 1
print(total)

