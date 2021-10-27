#yeah very very slow

import copy
#printing cubed
# def print_cubed(space, z_len, y_len):
# 	for z in range(z_len):
# 		for y in range(y_len):
# 			print(space[z][y])
# 		print('\n')

def	in_range(space, z, y, x):
	if z < 0 or z >= len(space):
		return(0)
	if y < 0 or y >= len(space[0]):
		return(0)
	if x < 0 or x >= len(space[0][0]):
		return(0)
	return(1)


def count_active_neighbors(space, z, y, x):
	count = 0
	for k in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			for i in [-1, 0, 1]:
				if in_range(space, z + k, y + j, x + i) == 1:
					if space[z + k][y + j][x + i] == 1:
						if not (k == 0 and j == 0 and i == 0):
							count += 1
	return(count)

# redaing inputs
data = open('input.txt', 'r').read().split('\n')

#calc data
amount_of_turns = 6
x_len = len(data[0]) + 2 * amount_of_turns
y_len = len(data) + 2 * amount_of_turns
z_len = 1 + 2 * amount_of_turns

#making cubed
space = [list() for i in range(z_len)]
for i in range(z_len):
	space[i] = [list() for j in range(y_len)]
	for j in range(y_len):
		space[i][j] = [0] * x_len

#settimng input in the cubed
for j in range(len(data)):
	for i in range(len(data[0])):
		if data[j][i] == '#':
			space[amount_of_turns][amount_of_turns + j][amount_of_turns + i] = 1

#walking trough the loop
for index in range(amount_of_turns):
	temp_space = copy.deepcopy(space)
	for z in range(z_len):
		for y in range(y_len):
			for x in range(x_len):
				if space[z][y][x] == 1:
					active_neigh = count_active_neighbors(space, z, y, x)
					if active_neigh != 2 and active_neigh != 3:
						temp_space[z][y][x] = 0
				if space[z][y][x] == 0:
					active_neigh = count_active_neighbors(space, z, y, x)
					if active_neigh == 3:
						temp_space[z][y][x] = 1
	space = copy.deepcopy(temp_space)

# counting cubed:
count = 0
for z in range(z_len):
	for y in range(y_len):
		for x in range(x_len):
			if space[z][y][x] == 1:
				count += 1
print(count)