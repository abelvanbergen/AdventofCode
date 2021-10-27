instructions = open('input.txt').read().splitlines()
i = 0
a, b = 1, 0
while i < len(instructions):
	if "inc" in instructions[i]:
		if "a" in instructions[i]:
			a += 1
		else:
			b += 1
		i += 1
	elif "hlf" in instructions[i]:
		if "a" in instructions[i]:
			a = a // 2
		else:
			b = b // 2
		i += 1
	elif "tpl" in instructions[i]:
		if "a" in instructions[i]:
			a *= 3
		else:
			b *= 3
		i += 1
	elif "jmp" in instructions[i]:
		i += int(instructions[i][instructions[i].index(' ') + 1:])
	elif "jie" in instructions[i]:
		if "a" in instructions[i]:
			if a % 2 == 0:
				i += int(instructions[i][instructions[i].index(',') + 2:])
			else:
				i += 1
		else:
			if b % 2 == 0:
				i += int(instructions[i][instructions[i].index(',') + 2:])
			else:
				i += 1
	elif "jio" in instructions[i]:
		if "a" in instructions[i]:
			if a == 1:
				i += int(instructions[i][instructions[i].index(',') + 2:])
			else:
				i += 1
		else:
			if b == 1:
				i += int(instructions[i][instructions[i].index(',') + 2:])
			else:
				i += 1
	else:
		print("could not find instruction:", instructions[i])
print("a:", a)
print("b:", b)