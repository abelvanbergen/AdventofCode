lines = open('input.txt').read().splitlines()
total_length = sum(map(len, lines))
stripped_length = 0
for line in lines:
	line = line[1:-1]
	i = 0
	while i < len(line):
		if line[i] == '\\' and line[i + 1] == '\\':
			i += 1
		elif line[i] == '\\' and line[i + 1] == '\"':
			i += 1
		elif line[i] == '\\' and line[i + 1] == 'x':
			i += 3
		stripped_length += 1
		i += 1
print(total_length, "-", stripped_length, "=", total_length - stripped_length)
