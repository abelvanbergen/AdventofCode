#register a starts with 7
#register a starts with 12

instructions = [i.split(' ') for i in open('input.txt').read().splitlines()]
registers = dict()
registers['a'] = 12
registers['b'] = 0
registers['c'] = 0
registers['d'] = 0
i = 0
while i < len(instructions):
	if instructions[i][0] == "inc":
		registers[instructions[i][1]] += 1
		i += 1
	elif instructions[i][0] == "dec":
		registers[instructions[i][1]] -= 1
		i += 1
	elif instructions[i][0] == "cpy":
		if instructions[i][2] in "abcd":
			if instructions[i][1] in "abcd":
				registers[instructions[i][2]] = registers[instructions[i][1]]
			else:
				registers[instructions[i][2]] = int(instructions[i][1])
		i += 1
	elif instructions[i][0] == "jnz":
		if instructions[i][1] in "abcd":
			if registers[instructions[i][1]] != 0:
				if instructions[i][2] in "abcd":
					i += registers[instructions[i][2]]
				else:
					i += int(instructions[i][2])
			else:
				i += 1
		else:
			if int(instructions[i][1]) != 0:
				if instructions[i][2] in "abcd":
					i += registers[instructions[i][2]]
				else:
					i += int(instructions[i][2])
			else:
				i += 1
	else:
		pos = registers[instructions[i][1][0]]
		if (i + pos < len(instructions)) and (0 < i + pos):
			if instructions[i + pos][0] == "inc":
				instructions[i + pos][0] = "dec"
			elif instructions[i + pos][0] == "jnz":
				instructions[i + pos][0] = "cpy"
			elif instructions[i + pos][0] == "cpy":
				instructions[i + pos][0] = "jnz"
			else:
				instructions[i + pos][0] = "inc"
		i += 1
print(registers["a"])