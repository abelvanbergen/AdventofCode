instructions = open('input.txt').read().replace(' through ', ',').splitlines()
lights = dict()
for y in range(1000):
	for x in range(1000):
		lights[(x, y)] = 0
for i in instructions:
	xs, ys, xe, ye = [int(j) for j in i.split(' ')[-1].split(',')]
	if "on" in i:
		for j in range(xs, xe + 1):
			for k in range(ys, ye + 1):
				lights[(j, k)] += 1
	elif "off" in i:
		for j in range(xs, xe + 1):
			for k in range(ys, ye + 1):
				if (lights[(j, k)] > 0):
					lights[(j, k)] -= 1
	else:
		for j in range(xs, xe + 1):
			for k in range(ys, ye + 1):
				lights[(j, k)] += 2
print(sum(lights.values()))