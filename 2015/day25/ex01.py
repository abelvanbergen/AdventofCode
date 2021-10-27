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

def get_number_id(row, column):
	number_id = 1
	add_nbr = 1
	for i in range(1, row):
		number_id += add_nbr
		add_nbr += 1
	add_nbr += 1
	for i in range(1, column):
		number_id += add_nbr
		add_nbr += 1
	return number_id

instruction = open('input.txt').read()
row = get_number(1, instruction)
column = get_number(2, instruction)
number_id = get_number_id(row, column)
answer = 20151125
for _ in range(1, number_id):
	answer = (answer * 252533) % 33554393
print(answer)

