def get_number(pos, line):
	i = 0
	count = 1
	while 1:
		while line[i] < '0'  or line[i] > '9':
			i += 1
		if count == pos:
			break
		count += 1
		while line[i] >= '0' and line[i] <= '9':
			i += 1
	j = 0
	while i + j != len(line) and (line[i + j] >= '0' and line[i + j] <= '9'):
		j += 1
	return (int(line[i:i + j]))

numbers = open('input.txt').read().splitlines()
triangles = []
for nb in numbers:
	new = []
	new.append(get_number(1, nb))
	new.append(get_number(2, nb))
	new.append(get_number(3, nb))
	triangles.append(sorted(new))
count = 0
for nb in triangles:
	if nb[0] + nb[1] > nb[2]:
		count += 1
print(count)
