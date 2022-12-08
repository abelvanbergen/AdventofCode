def get_scenic_score(height, x, y):
	score = 1
	i = 1
	count = 0
	while (x + i < len(grid[0])):
		count += 1
		if (grid[y][x + i] >= height):
			break
		i += 1
	score *= count
	i = 1
	count = 0
	while (x - i >= 0):
		count += 1
		if (grid[y][x - i] >= height):
			break
		i += 1
	score *= count
	i = 1
	count = 0
	while (y + i < len(grid)):
		count += 1
		if (grid[y + i][x] >= height):
			break
		i += 1
	score *= count
	i = 1
	count = 0
	while (y - i >= 0):
		count += 1
		if (grid[y - i][x] >= height):
			break
		i += 1
	score *= count
	return score

grid = [[int(x) for x in line] for line in open("input.txt").read().splitlines()]
scores = []
for y in range(len(grid)):
	for x in range(len(grid[0])):
		scores.append(get_scenic_score(grid[y][x], x, y))
print(max(scores))
	