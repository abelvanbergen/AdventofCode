def not_unsigned(nbr):
	mask = 0b1111111111111111
	return(mask ^ nbr)

def isnbr(string):
	for char in string:
		if char < '0' or char > '9':
			return(0)
	return (1)

def all_instructions_are_known(instructions, curcuit):
	for token in instructions:
		if token not in curcuit.keys() and token not in ["RSHIFT", "LSHIFT", "OR", "AND", "NOT"] and isnbr(token) == 0:
			return(0)
	return(1)

instructions = [i.split(' ') for i in open('input_02.txt').read().splitlines()]
curcuit = dict()
while len(instructions) > 0:
	i = 0
	print(curcuit)
	while 1:
		if (isnbr(instructions[i][0]) and len(instructions[i]) == 3):
			curcuit[instructions[i][2]] = int(instructions[i][0])
			instructions.remove(instructions[i])
			break
		if all_instructions_are_known(instructions[i][:-2], curcuit):
			if len(instructions[i]) == 3:
				curcuit[instructions[i][2]] = curcuit[instructions[i][0]]
			elif "OR" in instructions[i]:
				curcuit[instructions[i][-1]] = curcuit[instructions[i][0]] | curcuit[instructions[i][2]]
			elif "AND" in instructions[i]:
				if isnbr(instructions[i][0]):
					a = int(instructions[i][0])
				else:
					a = curcuit[instructions[i][0]]
				if isnbr(instructions[i][2]):
					b = int(instructions[i][2])
				else:
					b = curcuit[instructions[i][2]]
				curcuit[instructions[i][-1]] = a & b
			elif "RSHIFT" in instructions[i]:
				curcuit[instructions[i][-1]] = curcuit[instructions[i][0]] >> int(instructions[i][2])
			elif "LSHIFT" in instructions[i]:
				curcuit[instructions[i][-1]] = curcuit[instructions[i][0]] << int(instructions[i][2])
			else:
				curcuit[instructions[i][-1]] = not_unsigned(curcuit[instructions[i][1]])
			instructions.remove(instructions[i])
			break
		i += 1
print('a', curcuit['a'])