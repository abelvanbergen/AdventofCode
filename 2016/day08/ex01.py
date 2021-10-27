instructions = open('input.txt').read().splitlines()
x = 50
y = 6
grid = list()
for _ in range(y):
	grid.append(['.'] * x)
for instr in instructions:
	if "rect" in instr:
		dx, dy = [int(x) for x in instr.split(' ')[1].split('x')]
		for j in range(dy):
			for i in range(dx):
				grid[j][i] = '#'
	elif "row" in instr:
		token = instr.split(' ')
		row = int(token[2][2:])
		amount = int(token[4])
		grid_to_rot = [x[:] for x in grid]
		for i in range(x):
			grid[row][(i + amount) % x] = grid_to_rot[row][i]
	else:
		token = instr.split(' ')
		column = int(token[2][2:])
		amount = int(token[4])
		grid_to_rot = [x[:] for x in grid]
		for i in range(y):
			grid[(i + amount) % y][column] = grid_to_rot[i][column]
	for j in range(y):
		for i in range(x):
			print(grid[j][i], end='')
		print('')
count = 0
for i in grid:
	count += i.count('#')
for j in range(y):
	for i in range(x):
		print(grid[j][i], end='')
		if i % 5 == 4:
			print('|', end='')
	print('')
print(count)
efeykfrfij