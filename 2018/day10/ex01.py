lines = open("input.txt", "r").readlines()
data = list()
for line in lines:
	x_pos = int(line[line.find("<") + 1:line.find(",")])
	y_pos = int(line[line.find(",") + 1:line.find(">")])
	line = line[line.find(">") + 1:]
	x_dif = int(line[line.find("<") + 1:line.find(",")])
	y_dif = int(line[line.find(",") + 1:line.find(">")])
	data.append([x_pos, y_pos, x_dif, y_dif])
# for d in data:
# 	print(d)

min_x, max_x, min_y, max_y = 0, 0, 0, 0
for d in data:
	if d[0] < min_x:
		min_x = d[0]
	elif d[0] > max_x:
		max_x = d[0]	
	if d[1] < min_y:
		min_y = d[1]
	elif d[1] > max_y:
		max_y = d[1]

for i in range(10500, 11500):
	grid = [["."] * 30 for _ in range(30)]
	for d in data:
		if (0 <= d[1] + d[3] * i < 30) and (0 <= d[0] + d[2] * i < 30):
			grid[d[1] + d[3] * i][d[0] + d[2] * i] = "#"
	for line in grid:
		print(line)
	print("")

	