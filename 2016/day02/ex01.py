instructions = open('input.txt').read().splitlines()
numpad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x, y = 1, 1
password = str()
for line in instructions:
	for char in line:
		if char == "U":
			y -= 1
		elif char == "D":
			y += 1
		elif char == "R":
			x += 1
		else:
			x -= 1
		if y > 2:
			y -= 1
		if y < 0:
			y += 1
		if x > 2:
			x -= 1
		if x < 0:
			x += 1
	password += str(numpad[y][x])
print(password)
