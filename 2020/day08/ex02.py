def is_valid_solution(lines, j):
	if lines[j][0:3] == "jmp":
		lines[j] = lines[j].replace("jmp", "nop")
	elif lines[j][0:3] == "nop":
		lines[j] = lines[j].replace("nop", "jmp")
	happend = [0] * len(lines)
	i = 0
	acc = 0
	while 1:
		if happend[i] == 1:
			return -1
		happend[i] = 1
		if lines[i][0:3] == "acc":
			acc += int(lines[i][4:])
			i += 1
		elif lines[i][0:3] == "jmp":
			i += int(lines[i][4:])
		elif lines[i][0:4] == "done":
			return acc
		else:
			i += 1

lines = open("input.txt", "r").read().split('\n')
lines.append("done")
for i in range(len(lines)):
	temp = lines[:]
	res = is_valid_solution(temp, i)
	if res >= 0:
		print(res)
		exit()
