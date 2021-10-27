mfcsam = dict()
for line in open('mfcsam.txt').read().splitlines():
	mfcsam[line[:line.index(':')]] = int(line[line.index(' ') + 1:])
aunts = open('input.txt').read().splitlines()
for aunt in aunts:
	properties = aunt[aunt.index(':') + 2:].split(', ')
	count = 0
	for prop in properties:
		token = prop[:prop.index(':')]
		if token == "cats" or token == "trees":
			if mfcsam[token] < int(prop[prop.index(' ') + 1:]):
				count += 1
		elif token == "pomeranians" or token == "goldfish":
			if mfcsam[token] > int(prop[prop.index(' ') + 1:]):
				count += 1
		else:
			if mfcsam[token] == int(prop[prop.index(' ') + 1:]):
				count += 1
	if (count == len(properties)):
		print(aunt)