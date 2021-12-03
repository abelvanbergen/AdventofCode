#for exercixe 1 the max_time = 10
#for exercise 2 the max_time = 10000000

def neighbours(y, x):
	for j in [-1, 0, 1]:
		for i in [-1, 0, 1]:
			if j == i == 0:
				continue
			if y + j < 0 or y + j >= grid_size:
				continue
			if x + i < 0 or x + i >= grid_size:
				continue
			yield(y + j, x + i)

def countStateNeighbors(grid, y, x):
	open_acre, trees, lumberyard = 0, 0, 0
	for y, x in neighbours(y, x):
		if grid[y][x] == '.':
			open_acre += 1
		elif grid[y][x] == '|':
			trees += 1
		else:
			lumberyard += 1
	return open_acre, trees, lumberyard

def getResult(grid):
	trees, lumberyard = 0, 0
	for line in grid:
		trees += line.count('|')
		lumberyard += line.count('#')
	return (trees * lumberyard)

grid = [list(x) for x in open("input.txt", "r").read().splitlines()]
originalGird = [list(x) for x in grid]
max_time = 5000
grid_size = len(grid)
for time in range(max_time):
	new_grid = [['_'] * grid_size for _ in range(grid_size)]
	for j in range(grid_size):
		for i in range(grid_size):
			open_acre, trees, lumberyard = countStateNeighbors(grid, j, i)
			if grid[j][i] == '.':
				if trees >= 3:
					new_grid[j][i] = '|'
				else:
					new_grid[j][i] = '.'
			elif grid[j][i] == '|':
				if lumberyard >= 3:
					new_grid[j][i] = '#'
				else:
					new_grid[j][i] = '|'
			else:
				if lumberyard >= 1 and trees >= 1:
					new_grid[j][i] = '#'
				else:
					new_grid[j][i] = '.'
	grid = new_grid
	if grid == originalGird:
		print(time)
		quit()
