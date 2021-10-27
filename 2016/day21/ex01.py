scramble = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
instructions = open('input.txt').read().splitlines()
for line in instructions:
	print(line)
	line = line.split(' ')
	if line[0] == "swap":
		if line[1] == "position":
			a = int(line[2])
			b = int(line[5])
			temp = scramble[a]
			scramble[a] = scramble[b]
			scramble[b] = temp
		else:
			a = scramble.index(line[2])
			b = scramble.index(line[5])
			temp = scramble[a]
			scramble[a] = scramble[b]
			scramble[b] = temp
	elif line[0] == "rotate":
		if line[1] == "right":
			rot = int(line[2])
			scramble = scramble[-rot:] + scramble[:-rot]
		elif line[1] == "left":
			rot = int(line[2])
			scramble = scramble[rot:] + scramble[:rot]
		else:
			rot = scramble.index(line[6]) + 1
			if (rot >= 5):
				rot += 1
			rot = rot % len(scramble)
			scramble = scramble[-rot:] + scramble[:-rot]
	elif line[0] == "reverse":
		a = int(line[2])
		b = int(line[4])
		if b == len(scramble) - 1:
			temp = scramble[a:]
			scramble = scramble[:a] + temp[::-1]
		else:
			temp= scramble[a:b + 1]
			scramble = scramble[:a] + temp[::-1] + scramble[b + 1:]
	else:
		a = int(line[2])
		b = int(line[5])
		elem = scramble[a]
		scramble.remove(elem)
		scramble.insert(b, elem)
	print(scramble)
print(''.join(scramble))
	