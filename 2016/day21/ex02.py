scramble = ['f','b', 'g', 'd', 'c', 'e', 'a', 'h']
instructions = open('input.txt').read().splitlines()
for line in instructions[::-1]:
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
			scramble = scramble[rot:] + scramble[:rot]
		elif line[1] == "left":
			rot = int(line[2])
			scramble = scramble[-rot:] + scramble[:-rot]
		else:
			rot = scramble.index(line[6]) + 1
			rot_count = 0
			while rot != rot_count:
				print(scramble, rot, rot_count)
				scramble = scramble[1:] + scramble[:1]
				rot = scramble.index(line[6]) + 1
				if (rot >= 5):
					rot += 1
				rot_count += 1
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
		a = int(line[5])
		b = int(line[2])
		elem = scramble[a]
		scramble.remove(elem)
		scramble.insert(b, elem)
	print(''.join(scramble))
print(''.join(scramble))