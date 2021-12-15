poly, instructions_lines = open("input.txt").read().split("\n\n")
instructions = dict()
for instruct in instructions_lines.splitlines():
	key, value = instruct.split(' -> ')
	instructions[key] = value

polymore = dict()
for i in range(len(poly) - 1):
	if poly[i:i + 2] not in polymore.keys():
		polymore[poly[i:i + 2]] = 0
	polymore[poly[i:i + 2]] += 1

# print(polymore)

for step in range(400000):
	new_polymore = dict()
	for key in polymore:
		if key in instructions.keys():
			key_a = key[0] + instructions[key]
			key_b = instructions[key] + key[1]
			if key_a not in new_polymore.keys():
				new_polymore[key_a] = 0
			if key_b not in new_polymore.keys():
				new_polymore[key_b] = 0
			new_polymore[key_a] += polymore[key]
			new_polymore[key_b] += polymore[key]
		else:
			if key not in new_polymore.keys():
				new_polymore[key] = 0
			new_polymore[key] += polymore[key]
	polymore = new_polymore
	# print(step, polymore)
total = dict()
for key in polymore:
	if key[0] not in total:
		total[key[0]] = 0
	total[key[0]] += polymore[key]
total[poly[-1]] += 1
print(sum(total.values()))
print(len(str(sum(total.values()))))
print(max(total.values()) - min(total.values()))