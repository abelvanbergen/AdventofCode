instructions = open('input.txt').read().split(', ')
x = 0
y = 0
direction = 0
loc = set()
for i in instructions:
	if "R" in i:
		direction += 1
	else:
		direction -= 1
	if direction % 4 == 0:
		y += int(i[1:])
	elif direction % 4 == 1:
		x += int(i[1:])
	elif direction % 4 == 2:
		y -= int(i[1:])
	else:
		x -= int(i[1:])
if x < 0:
	x = -x
if y < 0:
	y = -y
print(x + y)