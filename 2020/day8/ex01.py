def calc_acc():
	lines = open("input.txt", "r").read().split('\n')
	happend = [0] * len(lines)
	i = 0
	acc = 0
	while 1:
		if happend[i] == 1:
			return acc
		happend[i] = 1
		if lines[i][0:3] == "acc":
			acc += int(lines[i][4:])
			i += 1
		elif lines[i][0:3] == "jmp":
			i += int(lines[i][4:])
		else:
			i += 1

print(calc_acc())