def get_len_token(line):
	i = 1
	count = 1
	while count > 0:
		if (line[i] == '{'):
			count += 1
		if (line[i] == '}'):
			count -= 1
		i += 1
	return i

def get_len_nbr(line):
	i = 1
	while(i != len(line) and line[i] >= '0' and line[i] <= '9'):
		i += 1
	return i

def calc_answer(line):
	i = 0
	answer = 0
	while i < len(line):
		if (line[i] == '{'):
			len_token = get_len_token(line[i:])
			if "red" not in line[i + 1:i + len_token]:
				answer += calc_answer(line[i + 1:i + len_token])
			i += len_token
		elif (line[i] == '-' or (line[i] >= '0' and line[i] <= '9')):
			len_nbr = get_len_nbr(line[i:])
			answer += int(line[i:i + len_nbr])
			i += len_nbr
		i += 1
	return answer

line = open('input.txt').read()
print(calc_answer(line[1:-1]))