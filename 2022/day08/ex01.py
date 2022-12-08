def is_visible(height, x, y):
	visible = 4
	for i in range(x):
		if (grid[y][i] >= height):
			visible -= 1
			break
	for i in range(x + 1, len(grid[0])):
		if (grid[y][i] >= height):
			visible -= 1
			break
	for i in range(y):
		if (grid[i][x] >= height):
			visible -= 1
			break
	for i in range(y + 1, len(grid)):
		if (grid[i][x] >= height):
			visible -= 1
			break
	return visible > 0

grid = [[int(x) for x in line] for line in open("input.txt").read().splitlines()]
count = 0
for y in range(len(grid)):
	for x in range(len(grid[0])):
		count += is_visible(grid[y][x], x, y)
print(count)
	