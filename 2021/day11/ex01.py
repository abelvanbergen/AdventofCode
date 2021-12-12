grid = [[int(x) for x in l] for l in open("input.txt").read().splitlines()]

def increase_neighbors(grid, x, y):
	for dy in [-1, 0, 1]:
		for dx in [-1, 0, 1]:
			if dx + x < 0 or dx + x >= len(grid[0]):
				continue
			if dy + y < 0 or dy + y >= len(grid):
				continue
			grid[y + dy][x + dx] += 1

flashes = 0
for step in range(100):
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			grid[y][x] += 1
	old_flash = None
	while (flashes != old_flash):
		old_flash = flashes
		for y in range(len(grid)):
			for x in range(len(grid[0])):
				if grid[y][x] > 9 and grid[y][x] < 1000:
					flashes += 1
					grid[y][x] = 1000
					increase_neighbors(grid, x, y)
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] > 9:
				grid[y][x] = 0
print(flashes)