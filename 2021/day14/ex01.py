poly, instructions_lines = open("input.txt").read().split("\n\n")

instructions = dict()
for instruct in instructions_lines.splitlines():
	key, value = instruct.split(' -> ')
	instructions[key] = value

for step in range(10):
	new_poly = ""
	for i in range(len(poly) - 1):
		new_poly += poly[i]
		if poly[i:i+2] in instructions.keys():
			new_poly += instructions[poly[i:i+2]]
	
	new_poly += poly[-1]
	poly = new_poly
	# print(step)
	print(poly)
 
total = dict()
for char in set(poly):
	total[char] = poly.count(char)
print(max(total.values()) - min(total.values()))
