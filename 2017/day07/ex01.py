lines = [i.split(' -> ') for i in open('input.txt').read().splitlines()]
stick = set()
for line in lines:
	if len(line) == 2:
		nodes = line[1].split(', ')
		for node in nodes:
			stick.add(node)
for line in lines:
	if line[0][:line[0].index(' ')] not in stick:
		print(line[0][:line[0].index(' ')])
		quit()