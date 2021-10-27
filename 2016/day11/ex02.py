from collections import deque
from itertools import chain, combinations

def everything_at_floor_four(floor_grid):
	for combi in floor_grid[1:]:
		for i in [0, 1]:
			if combi[i] != 4:
				return(0)
	return(1)

def is_save(floor_grid):
	for combi in floor_grid:
		if combi[0] != combi[1]:
			for gen in floor_grid:
				if gen[0] == combi[1]:
					return(0)
	return(1)

#parcing
#make a list of all the different objects (floor_grid) sorted so that
#the the grif[_][0] is the generator and grid[_][1] the chip with the floorlevel
lines = [i.split(' ') for i in open('input.txt')]
floor_grid = [1]
generator_index = 1
floor_index = 1
generator_number = dict()
for line in lines:
	for i, token in enumerate(line):
		if "generator" in token:
			generator_number[line[i - 1]] = generator_index
			new = [floor_index]
			floor_grid.append(new)
			generator_index += 1
	floor_index += 1
floor_index = 1
for line in lines:
	for i, token in enumerate(line):
		if "-" in token:
			chip_id = token[:token.index('-')]
			gen_nbr = generator_number[chip_id]
			floor_grid[gen_nbr].append(floor_index)
	floor_index += 1

def solve():
	while pq:
		depth, node = pq.popleft()
		if node in visited:
			continue
		visited.add(node)
		if everything_at_floor_four(node):
			return depth
		for elevator_inc in [-1, 1]:
			if (node[0] + elevator_inc == 0 or node[0] + elevator_inc == 5):
				continue
			moves = [(i, j) for i, row in enumerate(node[1:]) for j, cell in enumerate(row) if cell == node[0]]
			for move in chain(combinations(moves, 1), combinations(moves, 2)):
				new_node = (node[0] + elevator_inc,) + tuple(sorted(tuple(cell if (i, j) not in move else cell + elevator_inc for j, cell in enumerate(row)) for i, row in enumerate(node[1:])))
				if is_save(new_node[1:]):
					pq.append((depth + 1, new_node))

floor_grid += [(1, 1), (1, 1)]
print(floor_grid)
visited = set()
floor_grid = tuple(tuple(x) if isinstance(x, list) else x for x in floor_grid)
pq = deque()
pq.append((0, floor_grid))
print(solve())
