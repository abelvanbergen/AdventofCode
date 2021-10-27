def get_len_nbr(line):
	i = 1
	while(line[i] >= '0' and line[i] <= '9'):
		i += 1
	return i

line = open('input.txt').read()
i = 0
answer = 0
while i < len(line):
	if (line[i] == '-' or (line[i] >= '0' and line[i] <= '9')):
		len_nbr = get_len_nbr(line[i:])
		answer += int(line[i:i + len_nbr])
		i += len_nbr
	i += 1
print(answer)