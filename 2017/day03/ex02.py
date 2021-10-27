def sum_all_neighbors(y, x):
	ret = 0
	for dy in [-1, 0, 1]:
		for dx in [-1, 1, 0]:
			ret += grid[y + dy][x + dx]
	return ret

def get_coor(input_nb):
	size = 1
	while (size + 2)**2 < input_nb:
		size += 2
	quarter = (input_nb - size**2 - 1) // (size + 1)
	remainder = (input_nb - size**2) % (size + 1)
	if remainder == 0:
		remainder = (size + 1)
	if quarter == 0:
		x = (size + 2) // 2
		y = -((size + 2) // 2) + remainder
	elif quarter == 1:
		y = (size + 2) // 2
		x = (size + 2) // 2 - remainder
	elif quarter == 2:
		x = -((size + 2) // 2)
		y = (size + 2) // 2 - remainder
	else:
		y = -((size + 2) // 2)
		x = -((size + 2) // 2) + remainder
	return x, y

grid = list()
grid_size = 201
for i in range(grid_size):
	grid.append([0] * grid_size)
input_nb = 368078
grid[(grid_size // 2)][(grid_size // 2)] = 1
num = 2
result = 1
while result <= input_nb:
	x, y = get_coor(num)
	print(x, y)
	x, y = x + (grid_size // 2), y + (grid_size // 2)
	print(x, y)
	result = sum_all_neighbors(y, x)
	print(result)
	grid[y][x] = result
	num += 1
	print('')
print(result)


