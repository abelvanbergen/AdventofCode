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
i = 0
while i < len(numbers):
	new = [[], [], []]
	for j in range(3):
		new[j].append(get_number(j + 1, numbers[i]))
		new[j].append(get_number(j + 1, numbers[i + 1]))
		new[j].append(get_number(j + 1, numbers[i + 2]))
	for j in range(3):
		triangles.append(sorted(new[j]))
	i += 3
count = 0
for nb in triangles:
	if nb[0] + nb[1] > nb[2]:
		count += 1
print(count)
