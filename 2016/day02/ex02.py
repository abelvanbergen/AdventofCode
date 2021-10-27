instructions = open('input.txt').read().splitlines()
numpad_loc = {(0, 2), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (4, 2)}
numpad = [["0", "0", "1", "0", "0"], ["0", "2", "3", "4", "0"], ["5", "6", "7", "8", "9"], ["0", "A", "B", "C", "0"], ["0", "0", "D", "0", "0"]]
x, y = 0, 2
password = str()
for line in instructions:
	for char in line:
		if char == "U":
			if (x, y - 1) in numpad_loc:
				y -= 1
		elif char == "D":
			if (x, y + 1) in numpad_loc:
				y += 1
		elif char == "R":
			if (x + 1, y) in numpad_loc:
				x += 1
		else:
			if (x - 1, y) in numpad_loc:
				x -= 1
	password += numpad[y][x]
print(password)
