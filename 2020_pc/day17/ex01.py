# reading inputs
data = open('input.txt', 'r').read().split('\n')
amount_of_turns = 6

space = set()
for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x] == '#':
			space.add((0, y, x))

def neighbours(z, y, x):
	for k in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			for i in [-1, 0, 1]:
				if k == j == i == 0:
					continue
				yield(z + k, y + j, x + i)

def count_neighbours(z, y, x):
	count = 0
	for s in neighbours(z, y, x):
		count += s in space
	return(count)


def step():
	new_space = set()
	for dot in space:
		for spot in neighbours(*dot):
			if spot not in space and count_neighbours(*spot) == 3:
				new_space.add(spot)
		if count_neighbours(*dot) in (2, 3):
			new_space.add(dot)
	return new_space

for index in range(amount_of_turns):
	space = step()
print(len(space))