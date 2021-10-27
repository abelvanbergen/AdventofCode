def find_lowest_coor(x, y, coor):
	min_dis = -1
	for c in coor:
		distance = abs(x - c[1]) + abs(y - c[2])
		if distance == min_dis:
			amount_min_dis += 1
		if distance < min_dis or min_dis == -1:
			amount_min_dis = 0
			min_dis = distance
			coor_id_min_distance = c[0]
	if amount_min_dis == 1:
		return (0)
	else:
		return (coor_id_min_distance)

lines = open("input.txt", "r").readlines()
coor = set()
x_max, y_max = 0, 0
coor_id = 1
for line in lines:
	x, y = [int(x) for x in line.split(", ")]
	if (x >= x_max):
		x_max = x + 1
	if (y >= y_max):
		y_max = y + 1
	coor.add((coor_id, x, y))
	coor_id += 1


grid = [[0] * x_max for _ in range(y_max)]
for y in range(y_max):
	for x in range(x_max):
		grid[y][x] = find_lowest_coor(x, y, coor)

all_coor_id = set()
for i in range(len(lines)):
	all_coor_id.add(i + 1)
for i in range(x_max):
	if grid[0][i] in all_coor_id:
		all_coor_id.remove(grid[0][i])
	if grid[y_max - 1][i] in all_coor_id:
		all_coor_id.remove(grid[y_max - 1][i])
for i in range(y_max):
	if grid[i][0] in all_coor_id:
		all_coor_id.remove(grid[i][0])
	if grid[i][x_max - 1] in  all_coor_id:
		all_coor_id.remove(grid[i][x_max - 1])
test_grid = [[0] * 10 for _ in range(10)]
highest = 0
for c_id in all_coor_id:
	count = 0
	for line in grid:
		count += line.count(c_id)
	if count > highest:
		highest = count
print(highest)


