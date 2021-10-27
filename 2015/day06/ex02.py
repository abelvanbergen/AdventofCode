instructions = open('input.txt').read().replace(' through ', ',').splitlines()
lights = dict()
for y in range(1000):
	for x in range(1000):
		lights[str(y) + "-" + str(x)] = 0
for i in instructions:
	if "on" in i:
		cor = [int(j) for j in i.split(' ')[-1].split(',')]
		for j in range(cor[0], cor[2] + 1):
			for k in range(cor[1], cor[3] + 1):
				lights[str(y) + "-" + str(x)] += 1
	elif "off" in i:
		cor = [int(j) for j in i.split(' ')[-1].split(',')]
		for j in range(cor[0], cor[2] + 1):
			for k in range(cor[1], cor[3] + 1):
				if (lights[str(y) + "-" + str(x)] > 0):
					lights[str(y) + "-" + str(x)] -= 1
	else:
		cor = [int(j) for j in i.split(' ')[-1].split(',')]
		for j in range(cor[0], cor[2] + 1):
			for k in range(cor[1], cor[3] + 1):
				lights[str(y) + "-" + str(x)] += 2
print(sum(lights.values()))