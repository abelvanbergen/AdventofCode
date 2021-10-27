def is_active_neighbour(y, x):
	for dx in [-1, 1]:
		if x + dx < 0 or x + dx == size_x:
			continue
		if grid[y][x + dx] == '.' or grid[y][x + dx] == '#':
			continue
		if grid[y][x + dx] == length + 1:
			return 1
	for dy in [-1, 1]:
		if y + dy < 0 or y + dy == size_y:
			continue
		if grid[y + dy][x] == '.' or grid[y + dy][x] == '#':
			continue
		if grid[y + dy][x] == length + 1:
			return 1
	return 0

size_x = 52
size_y = 52
grid = []
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
grid[1][1] = 51

for length in range(50, 0, -1):
	for y in range(size_y):
		for x in range(size_x):
			if not grid[y][x] == '.':
				continue
			if is_active_neighbour(y, x):
				grid[y][x] = length
			
for y in range(size_y):
	for x in range(size_x):
		print('%3s' % str(grid[y][x]), end='')
	print('')
count = 0
for y in range(size_y):
	for x in range(size_x):
		if not (grid[y][x] == '.' or grid[y][x] == '#'):
			count += 1
print(count)