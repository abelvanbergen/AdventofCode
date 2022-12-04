instructions = open("e").read().splitlines()
reactor = set()
for line in instructions:
	status, coors = line.split()
	x_s, y_s, z_s = coors.split(',')
	x_min, x_max = [int(nb) for nb in x_s[2:].split("..")]
	y_min, y_max = [int(nb) for nb in y_s[2:].split("..")]
	z_min, z_max = [int(nb) for nb in z_s[2:].split("..")]
	if x_min < -50:
		x_min = -50
	if x_max > 50:
		x_max = 50
	if y_min < -50:
		y_min = 50
	if y_max > 50:
		y_max = 50
	if z_min < -50:
		z_min = 50
	if z_max > 50:
		z_max = 50
	for z in range(z_min, z_max + 1):
		for y in range(y_min, y_max + 1):
			for x in range(x_min, x_max + 1):

				if status == "on":
					reactor.add((x, y, z))
				else:
					if (x, y, z) in reactor:
						reactor.remove((x, y, z))
print(len(reactor))