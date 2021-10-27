instructions = [i.split(' ') for i in open('input.txt').read().splitlines()]
registers = dict()
registers['a'] = 0
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
		if instructions[i][1] in "abcd":
			registers[instructions[i][2]] = registers[instructions[i][1]]
		else:
			registers[instructions[i][2]] = int(instructions[i][1])
		i += 1
	else:
		if instructions[i][1][0] in "abcd":
			if registers[instructions[i][1]] != 0:
				i += int(instructions[i][2])
			else:
				i += 1
		else:
			if int(instructions[i][1]) != 0:
				i += int(instructions[i][2])
			else:
				i += 1
print(registers["a"])
	