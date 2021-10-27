def count_amount_of_neighbors(grid, i, j):
	count = 0
	for dy in [-1, 0, 1]:
		for dx in [-1, 0, 1]:
			if not (j + dy < 0 or j + dy >= len(grid) or i + dx < 0 or i + dx >= len(grid) or (dx == 0 and dy == 0)):
				if (grid[j + dy][i + dx] == 1):
					count += 1
	return count

def get_new_grid():
	new_grid = list()
	for j in range(len(grid)):
		new_row = []
		for i in range(len(grid[0])):
			amount_of_neighbors = count_amount_of_neighbors(grid, i, j)
			if grid[j][i] == 1:
				if ((j, i) in [(0,0), (len(grid) -1, 0), (0, len(grid[0]) - 1), (len(grid) -1, len(grid[0]) -1)]):
					new_row.append(1)
				elif (amount_of_neighbors in [2,3]):
					new_row.append(1)
				else:
					new_row.append(0)
			else:
				if (amount_of_neighbors == 3):
					new_row.append(1)
				else:
					new_row.append(0)	
		new_grid.append(new_row)
	return new_grid

grid = [[int(x) for x in i] for i in open('input_02.txt').read().replace('#', '1').replace('.', '0').splitlines()]
for i in range(100):
	grid = get_new_grid()
answer = 0
for i in grid:
	answer += sum(i)
print(answer)
