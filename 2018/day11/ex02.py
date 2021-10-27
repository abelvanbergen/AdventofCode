serial_id = 7139

def calc_sum_square(x, y, grid, grid_size):
	res = 0
	for j in range(grid_size):
		for i in range(grid_size):
			res += grid[y + j][x + i]
	return res

grid = [[0] * 300 for _ in range(300)]
for y in range(300):
	for x in range(300):
		rack_id = x + 10
		power_level = rack_id * y
		power_level += serial_id
		power_level *= rack_id
		power_level = int((power_level / 100)) % 10
		power_level -= 5
		grid[y][x] = power_level

highest = 0
for grid_size in range(20):
	for y in range(300 - grid_size + 1):
		for x in range(300 - grid_size + 1):
			sqaure = calc_sum_square(x, y, grid, grid_size)
			if sqaure > highest:
				highest = sqaure
				coor = (x, y, grid_size)
print(highest)
print(coor)