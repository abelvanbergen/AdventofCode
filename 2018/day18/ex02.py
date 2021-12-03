
def neighbours(y, x):
	for j in [-1, 0, 1]:
		for i in [-1, 0, 1]:
			if j == i == 0:
				continue
			yield(y + j, x + i)

def countStateNeighbors(acres, y, x):
	open_acre, trees, lumberyard = 0, 0, 0
	for y, x in neighbours(y, x):
		if (1, y, x) in acres:
			open_acre += 1
		elif (2, y, x) in acres:
			trees += 1
		elif (3, y, x) in acres:
			lumberyard += 1
	return open_acre, trees, lumberyard

max_time = 1000
acres = set()
for j, line in enumerate(open("input.txt", "r").read().splitlines()):
	for i, char in enumerate(line):
		if char == '.':
			acres.add((1, j, i))
		elif char == '|':
			acres.add((2, j, i))
		else:
			acres.add((3, j, i))

states = dict()
for time in range(max_time):
	new_acres = set()
	for typeAcres, y, x in acres:
		open_acre, trees, lumberyard = countStateNeighbors(acres, y, x)
		if typeAcres == 1:
			if trees >= 3:
				new_acres.add((2, y, x))
			else:
				new_acres.add((1, y, x))
		elif typeAcres == 2:
			if lumberyard >= 3:
				new_acres.add((3, y, x))
			else:
				new_acres.add((2, y, x))
		else:
			if lumberyard >= 1 and trees >= 1:
				new_acres.add((3, y, x))
			else:
				new_acres.add((1, y, x))
	acres = new_acres
	lstAcres = str(acres)
	if lstAcres in states:
		print(states[lstAcres])
		quit()
	states[lstAcres] = time

print("hij vind geen repetition")
trees, lumberyard = 0, 0
for acre in acres:
	if acre[0] == 2:
		trees += 1
	elif acre[0] == 3:
		lumberyard += 1
print(trees, "*", lumberyard, "=", trees * lumberyard)