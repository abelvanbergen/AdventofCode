import copy

def find_path(grid, x, y, length):
	grid[y][x] = 'O'
	new_grid = copy.deepcopy(grid)
	global lowest_path
	if x == 31 and y == 39:
		if length < lowest_path or lowest_path == 0:
			lowest_path = length
	elif length > lowest_path and lowest_path != 0:
		return
	else:
		for dx in [-1, 1]:
			if not (x + dx == 0 or x + dx == size_x):
				if grid[y][x + dx] == '.':
					find_path(new_grid, x + dx, y, length + 1)
		for dy in [-1, 1]:
			if not (y + dy == 0 or y + dy == size_y):
				if grid[y + dy][x] == '.':
					find_path(new_grid, x, y + dy, length + 1)


grid = []
size_x = 100
size_y = 100
for y in range(size_y):
	lst = []
	for x in range(size_x):
		ans = x * x + 3 * x + 2 * x * y + y + y * y + 1350
		bin_num = bin(ans)
		if bin_num.count("1") % 2 == 1:
			lst.append("#")
		else:
			lst.append(".")
	grid.append(lst)
# for y in range(7):
# 	for x in range(10):
# 		print(grid[y][x], end='')
# 	print('')
lowest_path = 0
find_path(grid, 1, 1, 0)
print(lowest_path)


