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

data = open('input.txt').read().splitlines()
data = data[2:]
storage = dict()
for line in data:
	storage[line[15:line.index(' ')]] = (get_number(3, line), get_number(4, line), get_number(5, line))
count = 0
for key_b in storage:
	_, _, avail_b = storage[key_b]
	for key_a in storage:
		_, used_a, _ = storage[key_a]
		if used_a != 0 and key_a != key_b and used_a <= avail_b:
			count += 1
print(count)
			