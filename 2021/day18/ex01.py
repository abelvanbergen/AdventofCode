digits = "0123456789"

def snail_add(line1, line2):
	return ("[" + line1 + "," + line2 + "]")

def has_to_explode(line):
	c = 0
	for char in line:
		if char == "[":
			c += 1
		elif char == "]":
			c -= 1
		if c >= 5:
			return True
	return False

def snail_explode(line):
	c = 0
	i = 0
	while c < 5:
		if line[i] == "[":
			c += 1
		elif line[i] == "]":
			c -= 1
		i += 1 
	i -= 1
	j = i
	while line[j] != ']':
		j += 1
	nb_left, nb_right = [int(x) for x in line[i + 1:j].split(',')]
	line = line[:i] + "0" + line[j + 1:]
	j = i + 1
	while j < len(line):
		if line[j] in digits:
			k = j
			while line[k] in digits:
				k += 1
			line = line[:j] + str(int(line[j:k]) + nb_right) + line[k:]
			break
		j += 1
	i -= 1
	while i >= 0:
		if line[i] in digits:
			k = i
			while line[k] in digits:
				k -= 1
			line = line[:k + 1] + str(int(line[k+1:i+1]) + nb_left) + line[i+1:]
			break
		i -= 1
	return line

def has_to_split(line):
	for i in range(len(line) - 1):
		if line[i] in digits and line[i + 1] in digits:
			return True
	return False

def snail_split(line):
	for i in range(len(line) - 1):
		if line[i] in digits and line[i + 1] in digits:
			j = i
			while line[j] in digits:
				j += 1
			nb = int(line[i:j])
			if nb % 2 == 0:
				pair_to_replace = "[" + str(nb // 2) + "," + str(nb // 2) + "]"
			else: 
				pair_to_replace = "[" + str(nb // 2) + "," + str(nb // 2 + 1) + "]"
			return line[:i] + pair_to_replace + line[j:]

def is_pair(line, i):
	if line[i] != '[':
		return False
	i += 1
	if line[i] not in digits:
		return False
	while line[i] in digits:
		i += 1
	if line[i] != ',':
		return False
	i += 1
	if line[i] not in digits:
		return False
	while line[i] in digits:
		i += 1
	if line[i] != ']':
		return False
	return True

def calc_magnitude(line):
	i = 0
	while i < len(line):
		if is_pair(line, i):
			j = i
			while line[j] != ']':
				j += 1
			nb_left, nb_right = [int(x) for x in line[i + 1:j].split(',')]
			nb = 3 * nb_left + 2 * nb_right
			line = line[:i] + str(nb) + line[j+1:]
			i = 0
			continue
		i += 1
	return(int(line))

lines = open("input.txt").read().splitlines()
res = lines[0]
for line in lines[1:]:
	res = snail_add(res, line)
	while True:
		if has_to_explode(res):
			res = snail_explode(res)
			continue
		if has_to_split(res):
			res = snail_split(res)
			continue
		break
print(calc_magnitude(res))
