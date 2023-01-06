grid, instructions_line = open("input.txt").read().split("\n\n")

open_space = set()
wall = set()
all_spots = set()
grid = grid.splitlines()
for y, line in enumerate(grid, 1):
	for x, char in enumerate(line, 1):
		if char == ".":
			all_spots.add((x, y))
			open_space.add((x, y))
		elif char == "#":
			all_spots.add((x, y))
			wall.add((x, y))

i = 0
instructions = []
instructions_line= instructions_line[:-1]
while (i < len(instructions_line)):
	j = 0
	while (instructions_line[i:i+j+1].isdigit() and i + j < len(instructions_line)):
		j += 1
	instructions.append(int(instructions_line[i:i+j]))
	if (i + j < len(instructions_line)):
		instructions.append(instructions_line[i+j])
	i += j + 1

def get_next_loc(x, y, dx, dy, distance):
	for _ in range(distance):
		if (x + dx, y + dy) in wall:
			break 
		if (x + dx, y + dy) not in open_space:
			next_x, next_y = x, y
			if dx > 0:
				next_x = min(i for i,j in all_spots if j == y)
			elif dx < 0:
				next_x = max(i for i,j in all_spots if j == y)
			elif dy > 0:
				next_y = min(j for i,j in all_spots if i == x)
			else:
				next_y = max(j for i,j in all_spots if i == x)
			if (next_x, next_y) in wall:
				return (x, y)
			else:
				x, y = next_x, next_y
		else:
			x += dx
			y += dy
	return (x, y)

x = min(x for x,y in open_space if y == 1)
y = 1
dx, dy = 1, 0
for instruction in instructions:
	if type(instruction) == int:
		x, y = get_next_loc(x, y, dx, dy, instruction)
	else:
		if instruction == "R":
			dx,dy = dy*-1,dx
		else:
			dx,dy = dy,dx*-1

points_for_dir = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}
print(y * 1000 + x * 4 + points_for_dir[(dx, dy)])



