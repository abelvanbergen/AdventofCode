directions = open('input.txt').read()
houses = set()
x, y = 0, 0
houses.add((x, y))
for char in directions:
	if char == "<":
		x -= 1
	elif char == ">":
		x += 1
	elif char == "^":
		y += 1
	else:
		y -= 1
	houses.add((x, y))
print(len(houses))