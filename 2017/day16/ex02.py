def lets_dance(programs):
	for ins in instructions:
		if "x" in ins:
			a = int(ins[1:ins.index('/')])
			b = int(ins[ins.index('/') + 1:])
			temp = programs[a]
			programs[a] = programs[b]
			programs[b] = temp
		elif "p" in ins:
			for i in range(len(programs)):
				if programs[i] == ins[1]:
					programs[i] = ins[3]
				elif programs[i] == ins[3]:
					programs[i] = ins[1]
		else:
			length = int(ins[1:])
			end = programs[-length:]
			start = programs[:-length]
			programs = end + start
	return (programs)

instructions = open('input.txt').read().split(',')
programs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
i = 1
programs = lets_dance(programs)
while programs != ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]:
	programs = lets_dance(programs)
	i += 1
remainder = 1000000000 % i
print(remainder)
for i in range(remainder):
	programs = lets_dance(programs)
print(''.join(programs))