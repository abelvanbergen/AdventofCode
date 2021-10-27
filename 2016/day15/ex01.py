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

def slots_aligned(time):
	for i, disc in enumerate(discs):
		if not ((disc[1] + time + i + 1) % disc[0] == 0):
			return (0)
	return(1)

info = open('input_02.txt')
discs = list()
for line in info:
	amount = get_number(2, line)
	pos = get_number(4, line)
	discs.append([amount, pos])
print(discs)

time = 0
while not slots_aligned(time):
	time += 1
print(time)


