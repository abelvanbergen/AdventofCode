serial_id = 7139

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
for y in range(298):
	for x in range(298):
		sqaure = sum(grid[y][x:x + 3:]) + sum(grid[y + 1][x:x + 3:]) + sum(grid[y + 2][x:x + 3:])
		if sqaure > highest:
			highest = sqaure
			coor = (x, y)
print(highest)
print(coor)