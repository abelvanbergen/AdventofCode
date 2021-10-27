instructions = [i.split(' ') for i in open('input.txt').read().splitlines()]
i = 0
register = dict()
while 1:
	if instructions[i][1] not in register.keys():
		register[instructions[i][1]] = 0
	if instructions[i][0] == "set":
		if instructions[i][2][0] in "-0123456789":
			register[instructions[i][1]] = int(instructions[i][2])
		else:
			register[instructions[i][1]] = register[instructions[i][2]]
		i += 1
	elif instructions[i][0] == "add":
		if instructions[i][2][0] in "-0123456789":
			register[instructions[i][1]] += int(instructions[i][2])
		else:
			register[instructions[i][1]] += register[instructions[i][2]]
		i += 1
	elif instructions[i][0] == "mul":
		if instructions[i][2][0] in "-0123456789":
			register[instructions[i][1]] *= int(instructions[i][2])
		else:
			register[instructions[i][1]] *= register[instructions[i][2]]
		i += 1
	elif instructions[i][0] == "mod":
		if instructions[i][2][0] in "-0123456789":
			register[instructions[i][1]] = register[instructions[i][1]] % int(instructions[i][2])
		else:
			register[instructions[i][1]] = register[instructions[i][1]] % register[instructions[i][2]]
		i += 1
	elif instructions[i][0] == "snd":
		last_sound_played = register[instructions[i][1]]
		i += 1
	elif instructions[i][0] == "jgz":
		if register[instructions[i][1]] > 0:
			if instructions[i][2][0] in "-0123456789":
				i += int(instructions[i][2])
			else:
				i += register[instructions[i][2]]
		else:
			i += 1
	else:
		if last_sound_played != 0:
			print(last_sound_played)
			quit()
		i += 1
	print(i)
		