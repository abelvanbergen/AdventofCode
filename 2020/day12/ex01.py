instructions = open("input.txt", "r").read().split('\n')
x = 0
y = 0
direction = 1
for i in instructions:
	if "R" in i:
		direction += int(i[1:]) / 90
	elif "L" in i:
		direction -= int(i[1:]) / 90
	elif "N" in i or ("F" in i and direction % 4 == 0):
		y += int(i[1:])
	elif "E" in i or ("F" in i and direction % 4 == 1):
		x += int(i[1:])
	elif "S" in i or ("F" in i and direction % 4 == 2):
		y -= int(i[1:])
	elif "W" in i or ("F" in i and direction % 4 == 3):
		x -= int(i[1:])
print(abs(x) + abs(y))