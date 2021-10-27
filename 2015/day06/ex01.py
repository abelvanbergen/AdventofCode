instructions = open('input.txt').read().replace(' through ', ',').splitlines()
lights = set()
for i in instructions:
	if "on" in i:
		cor = [int(j) for j in i.split(' ')[-1].split(',')]
		for j in range(cor[0], cor[2] + 1):
			for k in range(cor[1], cor[3] + 1):
				lights.add((j, k))
	elif "off" in i:
		cor = [int(j) for j in i.split(' ')[-1].split(',')]
		for j in range(cor[0], cor[2] + 1):
			for k in range(cor[1], cor[3] + 1):
				if (j, k) in lights:
					lights.remove((j, k))
	else:
		cor = [int(j) for j in i.split(' ')[-1].split(',')]
		for j in range(cor[0], cor[2] + 1):
			for k in range(cor[1], cor[3] + 1):
				if (j, k) in lights:
					lights.remove((j, k))
				else:
					lights.add((j, k))
print(len(lights))
# print(lights)