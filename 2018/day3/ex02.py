plans = open("input.txt", "r").read().replace(":", "").split('\n')
grid_size = 1000
grid = [[0] * grid_size for x in range(grid_size)]
for plan in plans:
	plan = plan.split(' ')
	x, y = [int(i) for i in plan[2].split(',')]
	width, length = [int(i) for i in plan[3].split('x')]
	for dy in range(length):
		for dx in range(width):
			grid[y + dy][x + dx] += 1
for plan in plans:
	plan = plan.split(' ')
	x, y = [int(i) for i in plan[2].split(',')]
	width, length = [int(i) for i in plan[3].split('x')]
	count = 0
	for dy in range(length):
		for dx in range(width):
			if grid[y + dy][x + dx] > 1:
				count = 1
	if count == 0:
		print(plan[0])