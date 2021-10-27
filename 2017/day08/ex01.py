lines = open('input.txt').read().splitlines()
registers = dict()
for line in lines:
	line = line.split(' ')
	condition = False
	if line[0] not in registers.keys():
		registers[line[0]] = 0
	if line[4] not in registers.keys():
		registers[line[4]] = 0
	if line[5] == "<":
		if registers[line[4]] < int(line[6]):
			condition = True
	elif line[5] == ">":
		if registers[line[4]] > int(line[6]):
			condition = True
	elif line[5] == "<=":
		if registers[line[4]] <= int(line[6]):
			condition = True
	elif line[5] == ">=":
		if registers[line[4]] >= int(line[6]):
			condition = True
	elif line[5] == "==":
		if registers[line[4]] == int(line[6]):
			condition = True
	else:
		if registers[line[4]] != int(line[6]):
			condition = True
	if condition == True:
		if line[1] == "inc":
			registers[line[0]] += int(line[2])
		else:
			registers[line[0]] -= int(line[2])
for key in registers:
	print(key, registers[key])
print(max(registers.values()))