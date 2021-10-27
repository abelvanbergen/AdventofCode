mfcsam = dict()
for line in open('mfcsam.txt').read().splitlines():
	mfcsam[line[:line.index(':')]] = int(line[line.index(' ') + 1:])
aunts = open('input.txt').read().splitlines()
for aunt in aunts:
	properties = aunt[aunt.index(':') + 2:].split(', ')
	count = 0
	for prop in properties:
		if mfcsam[prop[:prop.index(':')]] == int(prop[prop.index(' ') + 1:]):
			count += 1
	if (count == len(properties)):
		print(aunt)
