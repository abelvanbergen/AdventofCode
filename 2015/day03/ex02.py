directions = open('input.txt').read()
houses = set()
x_s, y_s, x_r, y_r = 0, 0, 0, 0
houses.add((x_s, y_s))
for i, char in enumerate(directions):
	if i % 2 == 0:
		if char == "<":
			x_s -= 1
		elif char == ">":
			x_s += 1
		elif char == "^":
			y_s += 1
		else:
			y_s-= 1
		houses.add((x_s, y_s))
	else:
		if char == "<":
			x_r -= 1
		elif char == ">":
			x_r += 1
		elif char == "^":
			y_r += 1
		else:
			y_r-= 1
		houses.add((x_r, y_r))
print(len(houses))